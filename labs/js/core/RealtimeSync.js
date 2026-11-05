// ============================================================================
// RealtimeSync.js - 多人即時同步核心層
// 支援原生 BroadcastChannel (本地零門檻) 與事件廣播
// 負責幽靈游標 (Ghost Cursors)、在線人員感知 (Presence) 與實驗動作同步 (Action Sync)
// ============================================================================

const DEFAULT_NAMES = [
  "愛因斯坦", "居禮夫人", "牛頓", "費曼", "波耳", 
  "拉瓦節", "門得列夫", "霍金", "法拉第", "特斯拉"
];

const CURSOR_COLORS = [
  "#38bdf8", // 天藍
  "#a855f7", // 紫羅蘭
  "#fbbf24", // 琥珀金
  "#34d399", // 翠綠
  "#f43f5e", // 玫瑰紅
  "#fb923c", // 暖橘
  "#ec4899"  // 洋紅
];

export class RealtimeSync {
  constructor(roomId = "omni-lab-room-alpha") {
    this.roomId = roomId;
    this.userId = "usr_" + Math.random().toString(36).substr(2, 8);
    
    // 隨機分配科學家名字與游標顏色
    const storedName = sessionStorage.getItem("omni_lab_user_name");
    this.userName = storedName || (DEFAULT_NAMES[Math.floor(Math.random() * DEFAULT_NAMES.length)] + "_" + this.userId.substr(-3));
    this.userColor = CURSOR_COLORS[Math.floor(Math.random() * CURSOR_COLORS.length)];

    // 遠端游標與在線成員列表
    this.peers = new Map(); // userId -> { userName, color, x, y, targetX, targetY, lastSeen }
    
    // 事件回呼
    this.actionCallbacks = [];
    this.presenceCallbacks = [];

    // 初始化廣播通道 (BroadcastChannel)
    this.initChannel();

    // 啟動在線心跳
    this.startHeartbeat();

    console.log(`[RealtimeSync] 已加入房間: ${this.roomId}，身分: ${this.userName} (${this.userColor})`);
  }

  initChannel() {
    try {
      this.channel = new BroadcastChannel(`omni_lab_${this.roomId}`);
      this.channel.onmessage = (event) => this.handleMessage(event.data);
    } catch (e) {
      console.warn("[RealtimeSync] 瀏覽器不支援 BroadcastChannel，啟用單機模擬模式", e);
    }
  }

  /**
   * 切換房間
   */
  joinRoom(newRoomId) {
    if (this.channel) {
      this.broadcastMessage({ type: "LEAVE", userId: this.userId });
      this.channel.close();
    }
    this.roomId = newRoomId;
    this.peers.clear();
    this.initChannel();
    this.sendHeartbeat();
    this.notifyPresence();
  }

  /**
   * 廣播訊息核心
   */
  broadcastMessage(msg) {
    if (!this.channel) return;
    try {
      this.channel.postMessage({
        ...msg,
        senderId: this.userId,
        timestamp: Date.now()
      });
    } catch (e) {
      console.error("[RealtimeSync] 發送訊息失敗", e);
    }
  }

  /**
   * 廣播滑鼠游標移動 (座標為 0~1 的相對比例)
   */
  broadcastCursor(normX, normY) {
    this.broadcastMessage({
      type: "CURSOR",
      userId: this.userId,
      userName: this.userName,
      color: this.userColor,
      x: normX,
      y: normY
    });
  }

  /**
   * 廣播實驗室專屬動作 (如：加試劑、點擊開關、發射星球)
   */
  broadcastAction(actionType, payload = {}) {
    this.broadcastMessage({
      type: "ACTION",
      userId: this.userId,
      userName: this.userName,
      actionType,
      payload
    });
  }

  /**
   * 接收處理來自其他分頁/學員的訊息
   */
  handleMessage(data) {
    if (!data || data.senderId === this.userId) return;

    const now = Date.now();

    switch (data.type) {
      case "HEARTBEAT":
      case "CURSOR": {
        let peer = this.peers.get(data.userId);
        if (!peer) {
          peer = {
            userId: data.userId,
            userName: data.userName,
            color: data.color,
            x: data.x || 0.5,
            y: data.y || 0.5,
            targetX: data.x || 0.5,
            targetY: data.y || 0.5,
            lastSeen: now
          };
          this.peers.set(data.userId, peer);
          this.notifyPresence();
        } else {
          peer.lastSeen = now;
          peer.userName = data.userName || peer.userName;
          peer.color = data.color || peer.color;
          if (typeof data.x === "number") peer.targetX = data.x;
          if (typeof data.y === "number") peer.targetY = data.y;
        }
        break;
      }

      case "ACTION": {
        // 觸發實驗室動作回呼
        this.actionCallbacks.forEach(fn => fn(data.actionType, data.payload, data));
        break;
      }

      case "LEAVE": {
        if (this.peers.has(data.userId)) {
          this.peers.delete(data.userId);
          this.notifyPresence();
        }
        break;
      }
    }
  }

  /**
   * 心跳循環：定期宣示存在並清除離線學員 (超過 5 秒未活動視為離線)
   */
  startHeartbeat() {
    // 立即發送一次
    this.sendHeartbeat();

    this.heartbeatTimer = setInterval(() => {
      this.sendHeartbeat();
      
      // 清除過期離線夥伴
      const now = Date.now();
      let changed = false;
      for (const [id, peer] of this.peers.entries()) {
        if (now - peer.lastSeen > 5000) {
          this.peers.delete(id);
          changed = true;
        }
      }
      if (changed) {
        this.notifyPresence();
      }
    }, 2000);
  }

  sendHeartbeat() {
    this.broadcastMessage({
      type: "HEARTBEAT",
      userId: this.userId,
      userName: this.userName,
      color: this.userColor
    });
  }

  /**
   * 平滑插值更新所有遠端游標位置 (在 60 FPS 渲染循環中呼叫)
   */
  updateRemoteCursors() {
    for (const peer of this.peers.values()) {
      // 簡單的線性插值平滑過渡 (LERP)
      peer.x += (peer.targetX - peer.x) * 0.25;
      peer.y += (peer.targetY - peer.y) * 0.25;
    }
  }

  /**
   * 取得當前所有在線夥伴清單 (包含自己)
   */
  getOnlineUsers() {
    const list = [
      { userId: this.userId, userName: this.userName, color: this.userColor, isMe: true }
    ];
    for (const peer of this.peers.values()) {
      list.push({ ...peer, isMe: false });
    }
    return list;
  }

  onAction(callback) {
    this.actionCallbacks.push(callback);
  }

  onPresence(callback) {
    this.presenceCallbacks.push(callback);
  }

  notifyPresence() {
    const users = this.getOnlineUsers();
    this.presenceCallbacks.forEach(fn => fn(users));
  }

  destroy() {
    if (this.heartbeatTimer) clearInterval(this.heartbeatTimer);
    if (this.channel) {
      this.broadcastMessage({ type: "LEAVE", userId: this.userId });
      this.channel.close();
    }
  }
}
