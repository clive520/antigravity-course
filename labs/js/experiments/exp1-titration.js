// ============================================================================
// exp1-titration.js - 首發化學實驗室：多彩指示劑與酸鹼滴定突躍實驗室
// 實現真實 pH 算式、流體動態顏色突躍、磁力攪拌漩渦與即時 S 型滴定曲線
// ============================================================================

import { LabRegistry } from "../core/LabRegistry.js";

const TitrationLab = {
  id: "titration",
  name: "酸鹼滴定與多彩突躍實驗室",
  category: "化學",
  icon: "🧪",
  description: "精準控制滴定管旋塞，觀察 pH 突躍臨界點與多彩指示劑的分子變色瞬間！",

  init(canvas, syncEngine, width, height) {
    this.canvas = canvas;
    this.sync = syncEngine;
    this.width = width;
    this.height = height;

    // 化學系統參數
    this.resetExperiment();

    // 粒子系統：落下液滴與泛起漣漪
    this.drops = [];
    this.ripples = [];

    // 攪拌子旋轉角度
    this.stirAngle = 0;
    this.isStirring = true;

    // 滴定管旋塞模式: 0: 停止, 1: 慢滴 (每秒 1 滴), 2: 快滴 (每秒 5 滴)
    this.flowMode = 0;
    this.dropInterval = 0;
    this.lastDropTime = 0;

    // 評分狀態
    this.evaluated = false;
    this.scoreText = "";
  },

  resetExperiment() {
    this.acidConc = 0.10;      // 0.10 M HCl
    this.acidVol = 25.0;       // 25.0 mL
    this.baseConc = 0.10;      // 0.10 M NaOH
    this.baseVol = 0.0;        // 已滴入體積 (mL)
    this.indicator = "phenolphthalein"; // "phenolphthalein" | "universal" | "methylOrange"
    
    // 歷史曲線數據點 [ { v: baseVol, ph: currentPh } ]
    this.curvePoints = [];
    this.flowMode = 0;
    this.evaluated = false;
    this.scoreText = "";

    this.recomputeChemistry();
  },

  /**
   * 計算即時化學平衡 pH 值
   */
  recomputeChemistry() {
    const Va = this.acidVol; // mL
    const Vb = this.baseVol; // mL
    const Ca = this.acidConc;
    const Cb = this.baseConc;

    const totalVol = Va + Vb;
    const molH = (Va * Ca) / 1000;
    const molOH = (Vb * Cb) / 1000;

    let ph = 7.0;

    if (molH > molOH + 1e-9) {
      // 過量酸
      const remMolH = molH - molOH;
      const concH = remMolH / (totalVol / 1000);
      ph = -Math.log10(concH);
    } else if (molOH > molH + 1e-9) {
      // 過量鹼
      const remMolOH = molOH - molH;
      const concOH = remMolOH / (totalVol / 1000);
      const poh = -Math.log10(concOH);
      ph = 14.0 - poh;
    } else {
      // 當量點 (強酸強鹼 = 7.0)
      ph = 7.0;
    }

    this.currentPh = Math.max(0, Math.min(14, ph));

    // 記錄曲線 (取樣稀疏避免重複過密)
    const lastP = this.curvePoints[this.curvePoints.length - 1];
    if (!lastP || Math.abs(lastP.v - this.baseVol) >= 0.15 || this.curvePoints.length < 2) {
      this.curvePoints.push({ v: this.baseVol, ph: this.currentPh });
    }

    // 評估是否精準抓到當量點
    if (this.baseVol >= 24.8 && this.baseVol <= 25.2 && this.flowMode === 0 && !this.evaluated) {
      const err = Math.abs(this.baseVol - 25.0).toFixed(2);
      this.evaluated = true;
      if (err <= 0.05) {
        this.scoreText = `🏆 完美的化學神手！誤差僅 ${err} mL (100分)`;
      } else {
        this.scoreText = `🎉 成功捕獲當量點！誤差 ${err} mL (優秀)`;
      }
    }
  },

  /**
   * 取得溶液當前渲染顏色 (RGBA)
   */
  getSolutionColor() {
    const ph = this.currentPh;

    if (this.indicator === "phenolphthalein") {
      // 酚酞：pH < 8.2 無色微灰透明，pH 8.2~10 突變粉紅，pH > 10 洋紅
      if (ph < 8.2) {
        return "rgba(241, 245, 249, 0.25)";
      } else if (ph < 10.0) {
        const ratio = (ph - 8.2) / (10.0 - 8.2);
        return `rgba(244, 114, 182, ${0.35 + ratio * 0.45})`;
      } else {
        return "rgba(225, 29, 72, 0.85)";
      }
    } else if (this.indicator === "universal") {
      // 廣用指示劑：彩虹光譜紅(1) ➔ 橙黃(4) ➔ 綠(7) ➔ 藍(9) ➔ 紫(12)
      if (ph < 3) return "rgba(239, 68, 68, 0.75)";     // 紅
      if (ph < 6) return "rgba(245, 158, 11, 0.75)";    // 橙黃
      if (ph < 8) return "rgba(16, 185, 129, 0.75)";    // 翠綠
      if (ph < 10) return "rgba(59, 130, 246, 0.75)";   // 藍
      return "rgba(147, 51, 234, 0.8)";                 // 紫
    } else if (this.indicator === "methylOrange") {
      // 甲基橙：pH < 3.1 紅，3.1~4.4 橙，> 4.4 黃
      if (ph < 3.1) return "rgba(239, 68, 68, 0.75)";
      if (ph < 4.4) return "rgba(249, 115, 22, 0.75)";
      return "rgba(234, 179, 8, 0.75)";
    }
    return "rgba(241, 245, 249, 0.3)";
  },

  /**
   * 每幀物理步進
   */
  update(dt) {
    // 磁力攪拌旋轉
    if (this.isStirring) {
      this.stirAngle += dt * 15;
    }

    // 處理自動滴定流速
    if (this.flowMode > 0) {
      const rate = this.flowMode === 1 ? 1 : 6; // 每秒滴數
      this.dropInterval += dt;
      if (this.dropInterval >= 1 / rate) {
        this.dropInterval = 0;
        this.addDrop();
      }
    }

    // 更新滴落水滴
    for (let i = this.drops.length - 1; i >= 0; i--) {
      const drop = this.drops[i];
      drop.y += drop.vy * dt;
      drop.vy += 980 * dt; // 重力加速度

      // 落入燒杯液面
      if (drop.y >= drop.targetY) {
        this.drops.splice(i, 1);
        this.ripples.push({ x: drop.x, y: drop.targetY, r: 2, alpha: 0.8 });
        // 增加體積
        this.baseVol = parseFloat((this.baseVol + 0.05).toFixed(2));
        this.recomputeChemistry();
      }
    }

    // 更新漣漪
    for (let i = this.ripples.length - 1; i >= 0; i--) {
      const rip = this.ripples[i];
      rip.r += 60 * dt;
      rip.alpha -= 1.5 * dt;
      if (rip.alpha <= 0) {
        this.ripples.splice(i, 1);
      }
    }
  },

  addDrop() {
    if (this.baseVol >= 50.0) return; // 滴定管用盡

    // 滴定管尖端座標
    const tipX = this.width * 0.35;
    const tipY = this.height * 0.52;
    const beakerLiquidY = this.height * 0.72;

    this.drops.push({
      x: tipX,
      y: tipY,
      vy: 120,
      targetY: beakerLiquidY
    });
  },

  singleDrop() {
    this.addDrop();
    // 廣播給其他學員
    this.sync.broadcastAction("SINGLE_DROP");
  },

  setFlowMode(mode) {
    this.flowMode = mode;
    this.sync.broadcastAction("SET_FLOW_MODE", { mode });
  },

  setIndicator(name) {
    this.indicator = name;
    this.sync.broadcastAction("SET_INDICATOR", { indicator: name });
  },

  resetAll() {
    this.resetExperiment();
    this.sync.broadcastAction("RESET_EXP");
  },

  /**
   * 收到遠端其他學員的操作同步
   */
  onRemoteAction(actionType, payload, meta) {
    switch (actionType) {
      case "SINGLE_DROP":
        this.addDrop();
        break;
      case "SET_FLOW_MODE":
        this.flowMode = payload.mode;
        break;
      case "SET_INDICATOR":
        this.indicator = payload.indicator;
        break;
      case "RESET_EXP":
        this.resetExperiment();
        break;
    }
  },

  /**
   * 繪製主畫面
   */
  render(ctx, width, height) {
    this.width = width;
    this.height = height;

    // 1. 實驗台背景與陰影
    this.renderWorkbench(ctx);

    // 2. 磁力攪拌器基座
    this.renderStirrer(ctx);

    // 3. 錐形反應燒杯與液體
    this.renderBeakerAndLiquid(ctx);

    // 4. 滴定管 (Buret) 與鐵架台
    this.renderBuretAndStand(ctx);

    // 5. 水滴與漣漪特效
    this.renderDropsAndRipples(ctx);

    // 6. 右側即時 HUD：數位 pH 計與 S 型突躍曲線圖表
    this.renderCurveHUD(ctx);

    // 7. 左側控制開關提示
    this.renderControlHints(ctx);
  },

  renderWorkbench(ctx) {
    // 科技感深邃實驗台背景
    const grad = ctx.createLinearGradient(0, 0, 0, this.height);
    grad.addColorStop(0, "#080c18");
    grad.addColorStop(0.6, "#0f172a");
    grad.addColorStop(1, "#0a0f1d");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, this.width, this.height);

    // 桌面橫線
    const tableY = this.height * 0.85;
    ctx.strokeStyle = "rgba(51, 65, 85, 0.6)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(0, tableY);
    ctx.lineTo(this.width, tableY);
    ctx.stroke();

    // 桌面科技反光
    const deskGrad = ctx.createLinearGradient(0, tableY, 0, this.height);
    deskGrad.addColorStop(0, "rgba(30, 41, 59, 0.4)");
    deskGrad.addColorStop(1, "rgba(15, 23, 42, 0.9)");
    ctx.fillStyle = deskGrad;
    ctx.fillRect(0, tableY, this.width, this.height - tableY);
  },

  renderStirrer(ctx) {
    const cx = this.width * 0.35;
    const cy = this.height * 0.83;
    const w = 180;
    const h = 30;

    // 攪拌器底座
    ctx.fillStyle = "#1e293b";
    ctx.strokeStyle = "#475569";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.roundRect(cx - w / 2, cy, w, h, [6, 6, 2, 2]);
    ctx.fill();
    ctx.stroke();

    // 運轉呼吸綠燈
    ctx.fillStyle = this.isStirring ? "#10b981" : "#64748b";
    ctx.shadowColor = this.isStirring ? "#10b981" : "transparent";
    ctx.shadowBlur = this.isStirring ? 8 : 0;
    ctx.beginPath();
    ctx.arc(cx - 65, cy + 15, 4, 0, Math.PI * 2);
    ctx.fill();
    ctx.shadowBlur = 0;

    // 銘牌
    ctx.fillStyle = "#94a3b8";
    ctx.font = "bold 10px sans-serif";
    ctx.textAlign = "center";
    ctx.fillText("MAGNETIC STIRRER", cx, cy + 18);
  },

  renderBeakerAndLiquid(ctx) {
    const cx = this.width * 0.35;
    const bottomY = this.height * 0.83;
    const beakerW = 120;
    const beakerH = 130;
    const beakerTopY = bottomY - beakerH;

    // 燒杯內溶液高度 (隨已滴入體積微幅上升)
    const liquidH = Math.min(85, 40 + (this.acidVol + this.baseVol) * 0.7);
    const liquidTopY = bottomY - liquidH;

    // 1. 繪製燒杯溶液
    ctx.save();
    ctx.fillStyle = this.getSolutionColor();
    ctx.beginPath();
    ctx.moveTo(cx - beakerW / 2 + 6, bottomY - 4);
    ctx.lineTo(cx + beakerW / 2 - 6, bottomY - 4);
    ctx.lineTo(cx + beakerW / 2 - 10, liquidTopY);
    ctx.lineTo(cx - beakerW / 2 + 10, liquidTopY);
    ctx.closePath();
    ctx.fill();

    // 2. 磁力攪拌漩渦效果
    if (this.isStirring) {
      ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.ellipse(cx, liquidTopY + 4, 25, 4, 0, 0, Math.PI * 2);
      ctx.stroke();

      // 旋轉的白色磁力攪拌子
      ctx.save();
      ctx.translate(cx, bottomY - 10);
      ctx.rotate(this.stirAngle);
      ctx.fillStyle = "#ffffff";
      ctx.shadowColor = "#38bdf8";
      ctx.shadowBlur = 6;
      ctx.beginPath();
      ctx.roundRect(-12, -4, 24, 8, 4);
      ctx.fill();
      ctx.restore();
    }
    ctx.restore();

    // 3. 繪製玻璃燒杯外框 (帶高光厚度)
    ctx.strokeStyle = "rgba(255, 255, 255, 0.65)";
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.moveTo(cx - beakerW / 2, beakerTopY);
    ctx.lineTo(cx - beakerW / 2 + 6, bottomY);
    ctx.lineTo(cx + beakerW / 2 - 6, bottomY);
    ctx.lineTo(cx + beakerW / 2, beakerTopY);
    ctx.stroke();

    // 燒杯刻度線
    ctx.strokeStyle = "rgba(255, 255, 255, 0.35)";
    ctx.lineWidth = 1;
    for (let i = 1; i <= 3; i++) {
      const markY = bottomY - i * 28;
      ctx.beginPath();
      ctx.moveTo(cx + beakerW / 2 - 8, markY);
      ctx.lineTo(cx + beakerW / 2 - 20, markY);
      ctx.stroke();
    }
  },

  renderBuretAndStand(ctx) {
    const cx = this.width * 0.35;
    const tipY = this.height * 0.52;
    const buretTopY = this.height * 0.12;
    const buretW = 18;

    // 1. 鐵架台直柱與夾子
    const standX = cx + 80;
    ctx.fillStyle = "#334155";
    ctx.fillRect(standX - 5, this.height * 0.08, 10, this.height * 0.76); // 立柱
    ctx.fillRect(standX - 40, this.height * 0.83, 100, 10); // 底座

    // 雙夾固定器
    ctx.fillStyle = "#64748b";
    ctx.fillRect(cx - 2, this.height * 0.32, standX - cx + 4, 8);

    // 2. 滴定管本體 (玻璃圓柱)
    ctx.strokeStyle = "rgba(255, 255, 255, 0.7)";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(cx - buretW / 2, buretTopY);
    ctx.lineTo(cx - buretW / 2, tipY - 24);
    // 錐形尖嘴
    ctx.lineTo(cx - 2, tipY);
    ctx.lineTo(cx + 2, tipY);
    ctx.lineTo(cx + buretW / 2, tipY - 24);
    ctx.lineTo(cx + buretW / 2, buretTopY);
    ctx.stroke();

    // 3. 滴定管內鹼液液面 (NaOH，隨消耗體積下降)
    const maxCapacity = 50.0;
    const consumedRatio = Math.min(1, this.baseVol / maxCapacity);
    const totalTubeH = (tipY - 24) - buretTopY;
    const currentLiquidTopY = buretTopY + totalTubeH * consumedRatio;

    if (currentLiquidTopY < tipY - 24) {
      ctx.fillStyle = "rgba(56, 189, 248, 0.45)"; // 澄清透明微青藍
      ctx.fillRect(cx - buretW / 2 + 2, currentLiquidTopY, buretW - 4, (tipY - 24) - currentLiquidTopY);
    }

    // 4. 滴定管旋塞 (Stopcock)
    const stopcockY = tipY - 16;
    ctx.fillStyle = this.flowMode > 0 ? "#10b981" : "#f43f5e";
    ctx.shadowColor = this.flowMode > 0 ? "#10b981" : "#f43f5e";
    ctx.shadowBlur = 8;
    ctx.beginPath();
    ctx.roundRect(cx - 16, stopcockY - 5, 32, 10, 3);
    ctx.fill();
    ctx.shadowBlur = 0;

    // 滴定管精細刻度線
    ctx.strokeStyle = "rgba(255, 255, 255, 0.4)";
    ctx.lineWidth = 1;
    for (let v = 0; v <= 50; v += 5) {
      const y = buretTopY + (totalTubeH * (v / 50));
      ctx.beginPath();
      ctx.moveTo(cx - buretW / 2 + 2, y);
      ctx.lineTo(cx - buretW / 2 + 8, y);
      ctx.stroke();
    }
  },

  renderDropsAndRipples(ctx) {
    // 水滴
    ctx.fillStyle = "rgba(56, 189, 248, 0.9)";
    ctx.shadowColor = "#38bdf8";
    ctx.shadowBlur = 6;
    for (const drop of this.drops) {
      ctx.beginPath();
      ctx.arc(drop.x, drop.y, 3, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.shadowBlur = 0;

    // 漣漪
    for (const rip of this.ripples) {
      ctx.strokeStyle = `rgba(255, 255, 255, ${rip.alpha})`;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.ellipse(rip.x, rip.y, rip.r, rip.r * 0.35, 0, 0, Math.PI * 2);
      ctx.stroke();
    }
  },

  renderCurveHUD(ctx) {
    const hudW = Math.min(380, this.width * 0.38);
    const hudH = 290;
    const hudX = this.width - hudW - 24;
    const hudY = 24;

    // 1. HUD 半透明科技面板底框
    ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
    ctx.strokeStyle = "rgba(56, 189, 248, 0.4)";
    ctx.lineWidth = 1.5;
    ctx.shadowColor = "rgba(0,0,0,0.5)";
    ctx.shadowBlur = 15;
    ctx.beginPath();
    ctx.roundRect(hudX, hudY, hudW, hudH, 12);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // 2. 標題與數位 pH 讀數計
    ctx.fillStyle = "#38bdf8";
    ctx.font = "bold 13px sans-serif";
    ctx.textAlign = "left";
    ctx.fillText("📊 滴定突躍 S 型曲線儀表板", hudX + 16, hudY + 26);

    // 數位大字 pH 儀表
    ctx.fillStyle = this.getSolutionColor();
    ctx.font = "900 24px 'JetBrains Mono', monospace";
    ctx.textAlign = "right";
    ctx.fillText(`pH ${this.currentPh.toFixed(2)}`, hudX + hudW - 16, hudY + 30);

    // 體積指示
    ctx.fillStyle = "#94a3b8";
    ctx.font = "11px sans-serif";
    ctx.fillText(`已加 NaOH: ${this.baseVol.toFixed(2)} mL / 25.00 mL (當量點)`, hudX + hudW - 16, hudY + 48);

    // 3. 繪製坐標系 (X 軸: 0 ~ 40 mL, Y 軸: pH 0 ~ 14)
    const plotX = hudX + 38;
    const plotY = hudY + 65;
    const plotW = hudW - 54;
    const plotH = 180;

    // 坐標底網格
    ctx.strokeStyle = "rgba(51, 65, 85, 0.5)";
    ctx.lineWidth = 1;
    ctx.strokeRect(plotX, plotY, plotW, plotH);

    // 突躍基準線 (pH 7.0)
    const midY = plotY + plotH * (1 - 7 / 14);
    ctx.strokeStyle = "rgba(251, 191, 36, 0.35)";
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(plotX, midY);
    ctx.lineTo(plotX + plotW, midY);
    ctx.stroke();

    // 當量點基準線 (25.0 mL)
    const eqX = plotX + plotW * (25.0 / 40.0);
    ctx.strokeStyle = "rgba(244, 63, 94, 0.35)";
    ctx.beginPath();
    ctx.moveTo(eqX, plotY);
    ctx.lineTo(eqX, plotY + plotH);
    ctx.stroke();
    ctx.setLineDash([]);

    // 軸刻度文字
    ctx.fillStyle = "#64748b";
    ctx.font = "10px monospace";
    ctx.textAlign = "right";
    ctx.fillText("14", plotX - 4, plotY + 8);
    ctx.fillText("7", plotX - 4, midY + 4);
    ctx.fillText("0", plotX - 4, plotY + plotH);
    ctx.textAlign = "center";
    ctx.fillText("0mL", plotX, plotY + plotH + 14);
    ctx.fillText("25mL", eqX, plotY + plotH + 14);
    ctx.fillText("40mL", plotX + plotW, plotY + plotH + 14);

    // 4. 動態繪製歷史曲線點
    if (this.curvePoints.length > 1) {
      ctx.strokeStyle = "#38bdf8";
      ctx.lineWidth = 2.5;
      ctx.shadowColor = "#38bdf8";
      ctx.shadowBlur = 6;
      ctx.beginPath();

      this.curvePoints.forEach((pt, idx) => {
        const cx = plotX + plotW * Math.min(1, pt.v / 40.0);
        const cy = plotY + plotH * (1 - pt.ph / 14.0);
        if (idx === 0) ctx.moveTo(cx, cy);
        else ctx.lineTo(cx, cy);
      });
      ctx.stroke();
      ctx.shadowBlur = 0;
    }

    // 評分與成就顯示
    if (this.scoreText) {
      ctx.fillStyle = "#fbbf24";
      ctx.font = "bold 11px sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(this.scoreText, hudX + hudW / 2, hudY + hudH - 12);
    }
  },

  renderControlHints(ctx) {
    const hintW = Math.min(300, this.width * 0.3);
    const hintX = 24;
    const hintY = 24;

    ctx.fillStyle = "rgba(15, 23, 42, 0.85)";
    ctx.strokeStyle = "rgba(51, 65, 85, 0.6)";
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.roundRect(hintX, hintY, hintW, 160, 10);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = "#f8fafc";
    ctx.font = "bold 13px sans-serif";
    ctx.textAlign = "left";
    ctx.fillText("🧪 滴定協同操作面板", hintX + 14, hintY + 24);

    ctx.font = "12px sans-serif";
    ctx.fillStyle = "#cbd5e1";
    ctx.fillText(`• 當前指示劑: ${this.getIndicatorName()}`, hintX + 14, hintY + 50);
    ctx.fillText(`• 旋塞狀態: ${this.getFlowModeName()}`, hintX + 14, hintY + 74);
    ctx.fillText("• 提示：雙分頁可同時滴定與切換指示劑！", hintX + 14, hintY + 98);
    ctx.fillText("• 目標：精準停在 25.00 mL 當量點！", hintX + 14, hintY + 122);
    ctx.fillText("• 下方控制列可直接一鍵切換與微調 ⬇", hintX + 14, hintY + 144);
  },

  getIndicatorName() {
    if (this.indicator === "phenolphthalein") return "酚酞 (無色 ➔ 粉紅)";
    if (this.indicator === "universal") return "廣用 (紅橙黃綠藍靛紫)";
    return "甲基橙 (紅 ➔ 橙黃)";
  },

  getFlowModeName() {
    if (this.flowMode === 0) return "已關閉 (停止)";
    if (this.flowMode === 1) return "慢速滴定 (每秒 1 滴)";
    return "快速連續滴定 (每秒 6 滴)";
  },

  onPointerDown(x, y, e) {
    // 點擊旋塞區域直接切換流速
    const tipX = this.width * 0.35;
    const stopcockY = this.height * 0.52 - 16;
    if (Math.hypot(x - tipX, y - stopcockY) < 30) {
      const nextMode = (this.flowMode + 1) % 3;
      this.setFlowMode(nextMode);
    }
  },

  destroy() {
    this.drops = [];
    this.ripples = [];
    this.curvePoints = [];
  }
};

// 註冊進外掛模組表
LabRegistry.register(TitrationLab);
export default TitrationLab;
