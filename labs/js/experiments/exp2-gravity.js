// ============================================================================
// exp2-gravity.js - 首發物理實驗室：萬有引力與克卜勒軌道星系沙盒
// 實現牛頓萬有引力數值積分、克卜勒軌跡即時預覽、黑洞吞噬與多人同屏星系投放
// ============================================================================

import { LabRegistry } from "../core/LabRegistry.js";

const GravityLab = {
  id: "gravity",
  name: "萬有引力與天體軌道沙盒",
  category: "物理",
  icon: "🌌",
  description: "拖曳發射行星、即時預覽克卜勒公轉軌跡，體驗三體混沌引力與黑洞吞噬！",

  init(canvas, syncEngine, width, height) {
    this.canvas = canvas;
    this.sync = syncEngine;
    this.width = width;
    this.height = height;

    // 物理常數
    this.G = 800; // 重力常數
    this.timeScale = 1.0;
    this.isPaused = false;

    // 天體陣列
    this.bodies = [];
    this.particles = []; // 碰撞爆炸星雲粒子

    // 當前欲發射的天體型別: "planet" | "star" | "moon" | "blackhole"
    this.spawnType = "planet";

    // 滑鼠拖曳發射狀態
    this.isAiming = false;
    this.aimStart = { x: 0, y: 0 };
    this.aimCurrent = { x: 0, y: 0 };

    // 遠端夥伴的拖曳發射預覽 Map(userId -> { start, current, color, name })
    this.remoteAims = new Map();

    // 預設載入經典太陽系
    this.loadPreset("solar");
  },

  loadPreset(presetName) {
    this.bodies = [];
    this.particles = [];
    const cx = this.width / 2;
    const cy = this.height / 2;

    if (presetName === "solar") {
      // 1. 中央太陽
      this.bodies.push({
        id: "sun",
        x: cx, y: cy, vx: 0, vy: 0,
        mass: 3000, radius: 24,
        color: "#fbbf24", glowColor: "rgba(251, 191, 36, 0.4)",
        type: "star", isFixed: false,
        trail: []
      });

      // 2. 地球 (逆時針圓形公轉)
      const r1 = 180;
      const v1 = Math.sqrt((this.G * 3000) / r1);
      this.bodies.push({
        id: "earth",
        x: cx + r1, y: cy, vx: 0, vy: -v1,
        mass: 12, radius: 8,
        color: "#38bdf8", glowColor: "rgba(56, 189, 248, 0.4)",
        type: "planet", isFixed: false,
        trail: []
      });

      // 3. 火星 (更遠的外側橢圓軌道)
      const r2 = 280;
      const v2 = Math.sqrt((this.G * 3000) / r2) * 1.05;
      this.bodies.push({
        id: "mars",
        x: cx - r2, y: cy, vx: 0, vy: v2,
        mass: 8, radius: 6,
        color: "#f87171", glowColor: "rgba(248, 113, 113, 0.4)",
        type: "planet", isFixed: false,
        trail: []
      });
    } else if (presetName === "binary") {
      // 雙星互繞系統
      const dist = 120;
      const v = Math.sqrt((this.G * 1500) / (dist * 2));
      this.bodies.push({
        id: "star1",
        x: cx - dist, y: cy, vx: 0, vy: v,
        mass: 1800, radius: 18,
        color: "#fbbf24", glowColor: "rgba(251, 191, 36, 0.4)",
        type: "star", isFixed: false, trail: []
      });
      this.bodies.push({
        id: "star2",
        x: cx + dist, y: cy, vx: 0, vy: -v,
        mass: 1800, radius: 18,
        color: "#a855f7", glowColor: "rgba(168, 85, 247, 0.4)",
        type: "star", isFixed: false, trail: []
      });
    } else if (presetName === "threeBody") {
      // 三體混沌運動模型
      const r = 160;
      for (let i = 0; i < 3; i++) {
        const ang = (i * 2 * Math.PI) / 3;
        const x = cx + Math.cos(ang) * r;
        const y = cy + Math.sin(ang) * r;
        const vx = -Math.sin(ang) * 65;
        const vy = Math.cos(ang) * 65;
        const colors = ["#fbbf24", "#38bdf8", "#34d399"];
        this.bodies.push({
          id: `three_${i}`,
          x, y, vx, vy,
          mass: 1200, radius: 14,
          color: colors[i], glowColor: colors[i],
          type: "star", isFixed: false, trail: []
        });
      }
    }
  },

  /**
   * 物理更新循環
   */
  update(dt) {
    if (this.isPaused) return;

    const effDt = dt * this.timeScale;
    const subSteps = 4; // 子步長提升數值精度
    const subDt = effDt / subSteps;

    for (let step = 0; step < subSteps; step++) {
      this.physicsSubStep(subDt);
    }

    // 更新爆炸星雲粒子
    for (let i = this.particles.length - 1; i >= 0; i--) {
      const p = this.particles[i];
      p.x += p.vx * effDt;
      p.y += p.vy * effDt;
      p.life -= effDt * 1.5;
      if (p.life <= 0) {
        this.particles.splice(i, 1);
      }
    }
  },

  physicsSubStep(dt) {
    const N = this.bodies.length;
    const softening = 8; // 軟化長度避免分母除以零

    // 1. 計算兩兩引力加速度
    for (let i = 0; i < N; i++) {
      const b1 = this.bodies[i];
      if (b1.isFixed) continue;

      let ax = 0;
      let ay = 0;

      for (let j = 0; j < N; j++) {
        if (i === j) continue;
        const b2 = this.bodies[j];

        const dx = b2.x - b1.x;
        const dy = b2.y - b1.y;
        const distSq = dx * dx + dy * dy + softening * softening;
        const dist = Math.sqrt(distSq);

        // 黑洞強引力加權
        let forceScale = 1.0;
        if (b2.type === "blackhole") forceScale = 2.5;

        const f = (this.G * b2.mass * forceScale) / distSq;
        ax += (dx / dist) * f;
        ay += (dy / dist) * f;

        // 碰撞與吞噬檢查 (僅在整步長檢查一次)
        if (dist < b1.radius + b2.radius) {
          this.handleCollision(i, j);
          return; // 陣列結構改變，提前跳出該子步長
        }
      }

      b1.vx += ax * dt;
      b1.vy += ay * dt;
      b1.x += b1.vx * dt;
      b1.y += b1.vy * dt;
    }

    // 2. 記錄平滑軌跡尾跡 (每隔數步記錄)
    this.bodies.forEach(b => {
      b.trail.push({ x: b.x, y: b.y });
      if (b.trail.length > 50) {
        b.trail.shift();
      }
    });
  },

  handleCollision(i, j) {
    const b1 = this.bodies[i];
    const b2 = this.bodies[j];
    if (!b1 || !b2) return;

    // 較大者吞噬較小者
    const bigger = b1.mass >= b2.mass ? b1 : b2;
    const smaller = b1.mass >= b2.mass ? b2 : b1;

    // 動量守恆
    const totalMass = bigger.mass + smaller.mass;
    bigger.vx = (bigger.vx * bigger.mass + smaller.vx * smaller.mass) / totalMass;
    bigger.vy = (bigger.vy * bigger.mass + smaller.vy * smaller.mass) / totalMass;
    bigger.mass = totalMass;
    bigger.radius = Math.min(40, Math.sqrt(bigger.radius * bigger.radius + smaller.radius * smaller.radius));

    // 噴發星雲碎片粒子
    for (let p = 0; p < 16; p++) {
      const angle = Math.random() * Math.PI * 2;
      const speed = 40 + Math.random() * 120;
      this.particles.push({
        x: smaller.x,
        y: smaller.y,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        color: smaller.color,
        life: 1.0
      });
    }

    // 移除較小者
    const removeIdx = this.bodies.indexOf(smaller);
    if (removeIdx !== -1) {
      this.bodies.splice(removeIdx, 1);
    }
  },

  /**
   * 計算初速度並即時預覽未來克卜勒軌道虛線
   */
  simulateTrajectory(startX, startY, vx, vy, steps = 120) {
    const points = [];
    let curX = startX;
    let curY = startY;
    let curVx = vx;
    let curVy = vy;
    const simDt = 0.08;

    for (let s = 0; s < steps; s++) {
      let ax = 0;
      let ay = 0;

      for (const b of this.bodies) {
        const dx = b.x - curX;
        const dy = b.y - curY;
        const distSq = dx * dx + dy * dy + 64;
        const dist = Math.sqrt(distSq);
        const f = (this.G * b.mass) / distSq;
        ax += (dx / dist) * f;
        ay += (dy / dist) * f;

        // 若撞入天體則中斷預覽
        if (dist < b.radius) {
          points.push({ x: curX, y: curY });
          return points;
        }
      }

      curVx += ax * simDt;
      curVy += ay * simDt;
      curX += curVx * simDt;
      curY += curVy * simDt;

      points.push({ x: curX, y: curY });
    }
    return points;
  },

  onPointerDown(x, y, e) {
    this.isAiming = true;
    this.aimStart = { x, y };
    this.aimCurrent = { x, y };
  },

  onPointerMove(x, y, e) {
    if (this.isAiming) {
      this.aimCurrent = { x, y };
      // 廣播給其他學員看我的發射預覽虛線
      this.sync.broadcastAction("AIM_MOVE", {
        start: this.aimStart,
        current: this.aimCurrent,
        spawnType: this.spawnType
      });
    }
  },

  onPointerUp(x, y, e) {
    if (!this.isAiming) return;
    this.isAiming = false;

    // 初速度由拉伸向量決定 (反向拉射彈弓感)
    const dx = this.aimStart.x - x;
    const dy = this.aimStart.y - y;
    const velocityScale = 0.65;
    const vx = dx * velocityScale;
    const vy = dy * velocityScale;

    // 生成並發射天體
    this.spawnBody(this.aimStart.x, this.aimStart.y, vx, vy, this.spawnType);

    // 廣播給其他學員同步生成
    this.sync.broadcastAction("SPAWN_BODY", {
      x: this.aimStart.x,
      y: this.aimStart.y,
      vx, vy,
      spawnType: this.spawnType
    });

    // 清除發射預覽
    this.sync.broadcastAction("AIM_CANCEL");
  },

  spawnBody(x, y, vx, vy, type) {
    let mass = 12;
    let radius = 8;
    let color = "#38bdf8";
    let glow = "rgba(56, 189, 248, 0.4)";

    if (type === "star") {
      mass = 2000;
      radius = 20;
      color = "#fbbf24";
      glow = "rgba(251, 191, 36, 0.5)";
    } else if (type === "moon") {
      mass = 2;
      radius = 4;
      color = "#e2e8f0";
      glow = "rgba(226, 232, 240, 0.3)";
    } else if (type === "blackhole") {
      mass = 6000;
      radius = 16;
      color = "#000000";
      glow = "#c084fc"; // 霓虹引力透鏡光環
    }

    this.bodies.push({
      id: "body_" + Math.random().toString(36).substr(2, 6),
      x, y, vx, vy,
      mass, radius, color,
      glowColor: glow,
      type,
      isFixed: false,
      trail: []
    });
  },

  onRemoteAction(actionType, payload, meta) {
    switch (actionType) {
      case "AIM_MOVE":
        this.remoteAims.set(meta.userId, {
          start: payload.start,
          current: payload.current,
          color: meta.color || "#c084fc",
          userName: meta.userName || "夥伴"
        });
        break;
      case "AIM_CANCEL":
        this.remoteAims.delete(meta.userId);
        break;
      case "SPAWN_BODY":
        this.remoteAims.delete(meta.userId);
        this.spawnBody(payload.x, payload.y, payload.vx, payload.vy, payload.spawnType);
        break;
      case "SET_PRESET":
        this.loadPreset(payload.presetName);
        break;
      case "CLEAR_ALL":
        this.bodies = [];
        this.particles = [];
        break;
    }
  },

  render(ctx, width, height) {
    this.width = width;
    this.height = height;

    // 1. 深邃星空背景與星塵
    ctx.fillStyle = "#050814";
    ctx.fillRect(0, 0, width, height);

    // 2. 繪製所有天體的軌道尾跡 (Trails)
    this.bodies.forEach(b => {
      if (b.trail.length > 2) {
        ctx.strokeStyle = b.glowColor;
        ctx.lineWidth = Math.max(1, b.radius * 0.35);
        ctx.beginPath();
        b.trail.forEach((p, idx) => {
          if (idx === 0) ctx.moveTo(p.x, p.y);
          else ctx.lineTo(p.x, p.y);
        });
        ctx.stroke();
      }
    });

    // 3. 繪製爆炸星雲碎片
    this.particles.forEach(p => {
      ctx.fillStyle = p.color;
      ctx.globalAlpha = p.life;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 2.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.globalAlpha = 1.0;
    });

    // 4. 繪製天體本體
    this.bodies.forEach(b => {
      ctx.save();
      if (b.type === "blackhole") {
        // 黑洞吸積盤光環
        ctx.strokeStyle = "#a855f7";
        ctx.shadowColor = "#c084fc";
        ctx.shadowBlur = 18;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(b.x, b.y, b.radius + 5, 0, Math.PI * 2);
        ctx.stroke();

        ctx.fillStyle = "#000000";
        ctx.shadowBlur = 0;
        ctx.beginPath();
        ctx.arc(b.x, b.y, b.radius, 0, Math.PI * 2);
        ctx.fill();
      } else {
        // 一般發光恆星與行星
        ctx.fillStyle = b.color;
        ctx.shadowColor = b.glowColor;
        ctx.shadowBlur = b.type === "star" ? 24 : 8;
        ctx.beginPath();
        ctx.arc(b.x, b.y, b.radius, 0, Math.PI * 2);
        ctx.fill();
      }
      ctx.restore();
    });

    // 5. 繪製自己當前瞄準的初速度向量與克卜勒軌道預覽 (Aiming)
    if (this.isAiming) {
      this.renderAimTrajectory(ctx, this.aimStart, this.aimCurrent, "#38bdf8", "你");
    }

    // 6. 繪製其他遠端學員的發射預覽線 (Remote Aiming)
    for (const remoteAim of this.remoteAims.values()) {
      this.renderAimTrajectory(ctx, remoteAim.start, remoteAim.current, remoteAim.color, remoteAim.userName);
    }

    // 7. 左側控制說明提示
    this.renderHUD(ctx);
  },

  renderAimTrajectory(ctx, start, current, color, label) {
    const dx = start.x - current.x;
    const dy = start.y - current.y;
    const vx = dx * 0.65;
    const vy = dy * 0.65;

    // 拉伸彈力線
    ctx.strokeStyle = color;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(start.x, start.y);
    ctx.lineTo(current.x, current.y);
    ctx.stroke();

    // 未來克卜勒軌道預覽虛線
    const trajectory = this.simulateTrajectory(start.x, start.y, vx, vy, 120);
    if (trajectory.length > 1) {
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      trajectory.forEach((pt, idx) => {
        if (idx === 0) ctx.moveTo(pt.x, pt.y);
        else ctx.lineTo(pt.x, pt.y);
      });
      ctx.stroke();
      ctx.setLineDash([]);
    }

    // 標籤提示
    ctx.fillStyle = color;
    ctx.font = "bold 11px sans-serif";
    ctx.fillText(`${label} 正在計算軌道...`, start.x + 12, start.y - 12);
  },

  renderHUD(ctx) {
    const w = 270;
    const h = 130;
    ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
    ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.roundRect(24, 24, w, h, 10);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px sans-serif";
    ctx.fillText("🌌 萬有引力天體沙盒", 38, 48);

    ctx.fillStyle = "#cbd5e1";
    ctx.font = "12px sans-serif";
    ctx.fillText(`• 當前投放型別: ${this.getTypeLabel()}`, 38, 72);
    ctx.fillText("• 操作方式：按住拖曳拉射，自動預覽軌道！", 38, 94);
    ctx.fillText("• 多人連線：同屏放行星、黑洞互搶衛星！", 38, 116);
  },

  getTypeLabel() {
    if (this.spawnType === "planet") return "藍色行星 (Earth)";
    if (this.spawnType === "star") return "金色恆星 (Sun)";
    if (this.spawnType === "moon") return "小型衛星 (Moon)";
    return "超重黑洞 (Black Hole)";
  },

  destroy() {
    this.bodies = [];
    this.particles = [];
    this.remoteAims.clear();
  }
};

// 註冊進外掛模組表
LabRegistry.register(GravityLab);
export default GravityLab;
