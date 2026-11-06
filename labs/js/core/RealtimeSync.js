// ============================================================================
// RealtimeSync.js - 多人即時同步核心層 (跨網雙層傳輸升級版)
// 支援：
// 1. 公網雲端 WebSocket (MQTT Broker: EMQX / HiveMQ) ➔ 實現跨帳號、跨瀏覽器、跨電腦/手機連線！
// 2. 本地記憶體 BroadcastChannel ➔ 本機同源快速備援與離線可用
// 負責幽靈游標 (Ghost Cursors)、在線人員感知 (Presence) 與實驗動作同步 (Action Sync)
// ============================================================================

const DEFAULT_NAMES = [
  "愛因斯坦", "居禮夫人", "牛頓", "費曼", "波耳", 
  "拉瓦節", "門得列夫", "霍金", "法拉第", "特斯拉",
  "達爾文", "伽利略", "克卜勒", "笛卡兒", "圖靈"
];

const CURSOR_COLORS = [
  "#38bdf8", // 天藍
  "#a855f7", // 紫羅蘭
  "#fbbf24", // 琥珀金
  "#34d399", // 翠綠
  "#f43f5e", // 玫瑰紅
  "#fb923c", // 暖橘
  "#ec4899", // 洋紅
  "#22d3ee"  // 亮青
];

// 公共穩定 WebSocket MQTT Brokers (免 key、全球開源公共端點)
const CLOUD_BROKERS = [
  "wss://broker.emqx.io:8084/mqtt",
  "wss://broker.hivemq.com:8884/mqtt"
];

export class RealtimeSync {
  constructor(roomId = "room-alpha") {
    this.roomId = roomId.toLowerCase().trim();
    this.userId = "usr_" + Math.random().toString(36).substr(2, 8);
    
    // 讀取或隨機分配科學家名字與游標顏色
    const storedName = localStorage.getItem("omni_lab_user_name");
    this.userName = storedName || (DEFAULT_NAMES[Math.floor(Math.random() * DEFAULT_NAMES.length)] + "_" + this.userId.substr(-3));
    this.userColor = CURSOR_COLORS[Math.floor(Math.random() * CURSOR_COLORS.length)];

    // 遠端游標與在線成員列表 Map(userId -> peerData)
    this.peers = new Map();
    
    // 事件回呼
    this.actionCallbacks = [];
    this.presenceCallbacks = [];
    this.statusCallbacks = [];

    // 連線狀態: "connecting" | "cloud" | "local" | "offline"
    this.connectionMode = "connecting";

    // 1. 初始化本機 BroadcastChannel (同源保底通道)
    this.initBroadcastChannel();

    // 2. 初始化公網雲端 MQTT WebSocket (跨帳號、跨電腦核心通道)
    this.initCloudTransport();

    // 3. 啟動在線心跳
    this.startHeartbeat();

    console.log(`[RealtimeSync] 啟動多人同步引擎，房間: ${this.roomId}，用戶: ${this.userName} (${this.userColor})`);
  }

  setUserName(newName) {
    if (!newName || !newName.trim()) return;
    this.userName = newName.trim();
    localStorage.setItem("omni_lab_user_name", this.userName);
    this.sendHeartbeat();
    this.notifyPresence();
  }

  setConnectionMode(mode) {
    this.connectionMode = mode;
    this.statusCallbacks.forEach(fn => fn(mode));
  }

  onStatusChange(callback) {
    this.statusCallbacks.push(callback);
    callback(this.connectionMode);
  }

  // --------------------------------------------------------------------------
  // 通道 1: 本地 BroadcastChannel
  // --------------------------------------------------------------------------
  initBroadcastChannel() {
    try {
      this.channel = new BroadcastChannel(`omni_lab_${this.roomId}`);
      this.channel.onmessage = (event) => this.handleIncomingMessage(event.data, "local");
    } catch (e) {
      console.warn("[RealtimeSync] 本地 BroadcastChannel 初始化失敗", e);
    }
  }

  // --------------------------------------------------------------------------
  // 通道 2: 公網雲端 MQTT over WSS (實現真正跨帳號/跨裝置連線)
  // --------------------------------------------------------------------------
  async initCloudTransport() {
    // 檢查是否已有全域 mqtt 客戶端庫
    if (!window.mqtt) {
      try {
        await this.loadScript("https://unpkg.com/mqtt@5.3.5/dist/mqtt.min.js");
      } catch (e) {
        console.warn("[RealtimeSync] 無法載入 MQTT 雲端連線庫，降級為本機模式", e);
        this.setConnectionMode("local");
        return;
      }
    }

    if (!window.mqtt) {
      this.setConnectionMode("local");
      return;
    }

    this.connectMqttBroker(0);
  }

  connectMqttBroker(brokerIdx = 0) {
    if (brokerIdx >= CLOUD_BROKERS.length) {
      console.warn("[RealtimeSync] 所有雲端 Broker 皆連線超時，使用本機 BroadcastChannel 保底");
      this.setConnectionMode("local");
      return;
    }

    const brokerUrl = CLOUD_BROKERS[brokerIdx];
    const clientId = `omnilab_${this.userId}_${Math.random().toString(16).substr(2, 6)}`;
    const topic = `antigravity/omnilab/room_${this.roomId}`;

    console.log(`[RealtimeSync] 正在連線公網 Broker: ${brokerUrl} ...`);

    try {
      const client = window.mqtt.connect(brokerUrl, {
        clientId,
        clean: true,
        connectTimeout: 5000,
        reconnectPeriod: 6000
      });

      client.on("connect", () => {
        console.log(`[RealtimeSync] 🟢 雲端 Broker 已連線！已加入頻道: ${topic}`);
        this.mqttClient = client;
        this.mqttTopic = topic;
        this.setConnectionMode("cloud");

        // 訂閱房間 Topic
        client.subscribe(topic, { qos: 0 }, (err) => {
          if (!err) {
            // 發送首次心跳上線通知
            this.sendHeartbeat();
          }
        });
      });

      client.on("message", (recvTopic, payload) => {
        if (recvTopic !== this.mqttTopic) return;
        try {
          const msg = JSON.parse(payload.toString());
          this.handleIncomingMessage(msg, "cloud");
        } catch (e) {
          // ignore invalid json
        }
      });

      client.on("error", (err) => {
        console.warn("[RealtimeSync] MQTT 連線錯誤", err);
      });

      client.on("close", () => {
        if (this.connectionMode === "cloud") {
          this.setConnectionMode("local");
        }
      });

    } catch (e) {
      console.warn(`[RealtimeSync] 連線 Broker ${brokerUrl} 異常，嘗試下一個備用伺服器`, e);
      this.connectMqttBroker(brokerIdx + 1);
    }
  }

  loadScript(src) {
    return new Promise((resolve, reject) => {
      const s = document.createElement("script");
      s.src = src;
      s.onload = () => resolve();
      s.onerror = (err) => reject(err);
      document.head.appendChild(s);
    });
  }

  // --------------------------------------------------------------------------
  // 雙通道統一生產與分發 (雙管齊下)
  // --------------------------------------------------------------------------
  broadcastMessage(msg) {
    const packet = {
      ...msg,
      senderId: this.userId,
      timestamp: Date.now()
    };
    const jsonStr = JSON.stringify(packet);

    // 1. 本地 BroadcastChannel 廣播
    if (this.channel) {
      try {
        this.channel.postMessage(packet);
      } catch (e) {}
    }

    // 2. 雲端 MQTT 廣播 (跨帳號、跨電腦)
    if (this.mqttClient && this.mqttClient.connected) {
      try {
        this.mqttClient.publish(this.mqttTopic, jsonStr, { qos: 0 });
      } catch (e) {}
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
   * 接收處理來自其他分頁/學員的訊息 (具備訊息去重)
   */
  handleIncomingMessage(data, source) {
    if (!data || data.senderId === this.userId) return;

    // 防止同一個訊息被 Local 和 Cloud 重複處理
    const msgId = `${data.senderId}_${data.timestamp}_${data.type}`;
    if (this.lastMsgId === msgId) return;
    this.lastMsgId = msgId;

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
   * 切換房間
   */
  joinRoom(newRoomId) {
    if (!newRoomId) return;
    const cleanId = newRoomId.toLowerCase().trim();
    if (cleanId === this.roomId) return;

    // 離開舊房
    this.broadcastMessage({ type: "LEAVE", userId: this.userId });
    if (this.channel) this.channel.close();
    if (this.mqttClient && this.mqttClient.connected) {
      this.mqttClient.unsubscribe(this.mqttTopic);
    }

    this.roomId = cleanId;
    this.peers.clear();

    // 重新初始化
    this.initBroadcastChannel();
    if (this.mqttClient && this.mqttClient.connected) {
      this.mqttTopic = `antigravity/omnilab/room_${this.roomId}`;
      this.mqttClient.subscribe(this.mqttTopic, { qos: 0 });
    } else {
      this.initCloudTransport();
    }

    this.sendHeartbeat();
    this.notifyPresence();
  }

  /**
   * 心跳循環：定期宣示存在並清除離線夥伴 (超過 6 秒未活動視為離線)
   */
  startHeartbeat() {
    this.sendHeartbeat();

    this.heartbeatTimer = setInterval(() => {
      this.sendHeartbeat();
      
      const now = Date.now();
      let changed = false;
      for (const [id, peer] of this.peers.entries()) {
        if (now - peer.lastSeen > 6000) {
          this.peers.delete(id);
          changed = true;
        }
      }
      if (changed) {
        this.notifyPresence();
      }
    }, 2500);
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
      peer.x += (peer.targetX - peer.x) * 0.25;
      peer.y += (peer.targetY - peer.y) * 0.25;
    }
  }

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
    this.broadcastMessage({ type: "LEAVE", userId: this.userId });
    if (this.channel) this.channel.close();
    if (this.mqttClient) this.mqttClient.end();
  }
}
