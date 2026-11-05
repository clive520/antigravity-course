// ============================================================================
// LabEngine.js - 實驗室核心渲染與事件分發引擎
// 負責 60 FPS 渲染循環、Canvas 高清適應、事件分發與幽靈游標繪製
// ============================================================================

export class LabEngine {
  constructor(canvasElement, realtimeSync, labRegistry) {
    this.canvas = canvasElement;
    this.ctx = this.canvas.getContext("2d");
    this.sync = realtimeSync;
    this.registry = labRegistry;

    this.currentExp = null;
    this.isRunning = false;
    this.lastTime = performance.now();

    // 游標廣播節流
    this.lastCursorBroadcast = 0;

    // 視窗寬高
    this.width = 0;
    this.height = 0;
    this.dpr = window.devicePixelRatio || 1;

    // 綁定事件監聽
    this.initCanvasSize();
    this.bindEvents();
    this.bindSync();

    // 啟動循環
    this.start();
  }

  initCanvasSize() {
    const rect = this.canvas.parentElement.getBoundingClientRect();
    this.width = rect.width;
    this.height = rect.height;

    this.canvas.width = this.width * this.dpr;
    this.canvas.height = this.height * this.dpr;
    this.canvas.style.width = `${this.width}px`;
    this.canvas.style.height = `${this.height}px`;

    this.ctx.scale(this.dpr, this.dpr);

    if (this.currentExp && this.currentExp.onResize) {
      this.currentExp.onResize(this.width, this.height);
    }
  }

  bindEvents() {
    window.addEventListener("resize", () => {
      this.initCanvasSize();
    });

    // 滑鼠移動與游標廣播
    const handlePointerMove = (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      const normX = Math.max(0, Math.min(1, x / this.width));
      const normY = Math.max(0, Math.min(1, y / this.height));

      // 節流廣播游標給其他學員 (約 30 FPS 發送一次，極省流量)
      const now = performance.now();
      if (now - this.lastCursorBroadcast > 33) {
        this.sync.broadcastCursor(normX, normY);
        this.lastCursorBroadcast = now;
      }

      if (this.currentExp && this.currentExp.onPointerMove) {
        this.currentExp.onPointerMove(x, y, e);
      }
    };

    this.canvas.addEventListener("mousemove", handlePointerMove);
    this.canvas.addEventListener("touchmove", (e) => {
      if (e.touches.length > 0) {
        handlePointerMove(e.touches[0]);
      }
    }, { passive: false });

    // 滑鼠按壓
    const handlePointerDown = (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      if (this.currentExp && this.currentExp.onPointerDown) {
        this.currentExp.onPointerDown(x, y, e);
      }
    };
    this.canvas.addEventListener("mousedown", handlePointerDown);
    this.canvas.addEventListener("touchstart", (e) => {
      if (e.touches.length > 0) {
        handlePointerDown(e.touches[0]);
      }
    }, { passive: false });

    // 滑鼠釋放
    const handlePointerUp = (e) => {
      const rect = this.canvas.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      if (this.currentExp && this.currentExp.onPointerUp) {
        this.currentExp.onPointerUp(x, y, e);
      }
    };
    this.canvas.addEventListener("mouseup", handlePointerUp);
    this.canvas.addEventListener("touchend", (e) => {
      if (e.changedTouches.length > 0) {
        handlePointerUp(e.changedTouches[0]);
      }
    }, { passive: false });
  }

  bindSync() {
    // 收到遠端夥伴的自定義實驗動作
    this.sync.onAction((actionType, payload, meta) => {
      if (this.currentExp && this.currentExp.onRemoteAction) {
        this.currentExp.onRemoteAction(actionType, payload, meta);
      }
    });
  }

  /**
   * 載入指定實驗模組
   * @param {string} expId 
   */
  loadExperiment(expId) {
    const exp = this.registry.get(expId);
    if (!exp) {
      console.error(`[LabEngine] 找不到實驗模組: ${expId}`);
      return false;
    }

    if (this.currentExp && this.currentExp.destroy) {
      this.currentExp.destroy();
    }

    this.currentExp = exp;
    if (this.currentExp.init) {
      this.currentExp.init(this.canvas, this.sync, this.width, this.height);
    }
    console.log(`[LabEngine] 已掛載實驗室: ${exp.name}`);
    return true;
  }

  start() {
    if (this.isRunning) return;
    this.isRunning = true;
    this.lastTime = performance.now();
    this.loop();
  }

  stop() {
    this.isRunning = false;
  }

  loop() {
    if (!this.isRunning) return;

    const now = performance.now();
    const dt = Math.min((now - this.lastTime) / 1000, 0.1); // 秒為單位，防止卡頓過大步進
    this.lastTime = now;

    // 1. 更新遠端幽靈游標位置 (LERP 插值)
    this.sync.updateRemoteCursors();

    // 2. 清除背景
    this.ctx.clearRect(0, 0, this.width, this.height);

    // 3. 執行當前實驗室的物理步進與繪製
    if (this.currentExp) {
      if (this.currentExp.update) {
        this.currentExp.update(dt);
      }
      if (this.currentExp.render) {
        this.currentExp.render(this.ctx, this.width, this.height);
      }
    } else {
      this.renderEmptyState();
    }

    // 4. 在最上層渲染遠端協同夥伴的幽靈游標 (Ghost Cursors)
    this.renderRemoteCursors();

    requestAnimationFrame(() => this.loop());
  }

  renderEmptyState() {
    this.ctx.fillStyle = "#94a3b8";
    this.ctx.font = "16px sans-serif";
    this.ctx.textAlign = "center";
    this.ctx.fillText("請自左側或選單選擇一個物理/化學實驗室開始體驗", this.width / 2, this.height / 2);
  }

  /**
   * 繪製遠端夥伴的幽靈游標與發光名字標籤
   */
  renderRemoteCursors() {
    for (const peer of this.sync.peers.values()) {
      const px = peer.x * this.width;
      const py = peer.y * this.height;

      this.ctx.save();
      this.ctx.translate(px, py);

      // 1. 繪製精緻的指針箭頭
      this.ctx.shadowColor = peer.color;
      this.ctx.shadowBlur = 8;
      this.ctx.fillStyle = peer.color;
      this.ctx.beginPath();
      this.ctx.moveTo(0, 0);
      this.ctx.lineTo(0, 15);
      this.ctx.lineTo(4, 11);
      this.ctx.lineTo(10, 11);
      this.ctx.closePath();
      this.ctx.fill();

      // 2. 繪製名字標籤膠囊
      const label = peer.userName || "夥伴";
      this.ctx.font = "bold 11px sans-serif";
      const textWidth = this.ctx.measureText(label).width;

      this.ctx.shadowBlur = 0;
      this.ctx.fillStyle = "rgba(15, 23, 42, 0.88)";
      this.ctx.strokeStyle = peer.color;
      this.ctx.lineWidth = 1;

      const badgeX = 12;
      const badgeY = 6;
      const badgeW = textWidth + 14;
      const badgeH = 20;
      const radius = 6;

      this.ctx.beginPath();
      this.ctx.roundRect(badgeX, badgeY, badgeW, badgeH, radius);
      this.ctx.fill();
      this.ctx.stroke();

      // 標籤文字
      this.ctx.fillStyle = "#ffffff";
      this.ctx.textAlign = "left";
      this.ctx.textBaseline = "middle";
      this.ctx.fillText(label, badgeX + 7, badgeY + badgeH / 2);

      this.ctx.restore();
    }
  }
}
