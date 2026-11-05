// ============================================================================
// exp-template.js - 新實驗室外掛擴充模板 (10 分鐘快速起步)
// 只要複製此檔案、填寫以下 6 個標準生命週期方法，即可自動註冊進實驗室大廳！
// ============================================================================

import { LabRegistry } from "../core/LabRegistry.js";

const TemplateLab = {
  // 1. 唯一識別碼與基本資訊
  id: "custom-lab",             // 英文小寫唯一 ID
  name: "自訂新實驗室名稱",     // 顯示名稱 (如：串並聯電路實驗室)
  category: "物理",             // 分類: "物理" | "化學" | "生物" | "地球科學"
  icon: "⚡",                   // 代表 Emoji
  description: "簡短一句話介紹這個實驗室能探索什麼現象！",

  /**
   * 2. 初始化生命週期 (掛載時執行一次)
   * @param {HTMLCanvasElement} canvas 繪圖畫布
   * @param {RealtimeSync} syncEngine 多人即時同步引擎
   * @param {number} width 畫布寬度
   * @param {number} height 畫布高度
   */
  init(canvas, syncEngine, width, height) {
    this.canvas = canvas;
    this.sync = syncEngine;
    this.width = width;
    this.height = height;

    // TODO: 在此初始化你的物理/化學變數 (如電壓、電阻、分子清單)
  },

  /**
   * 3. 物理運算循環 (以約 60 FPS 頻率每幀呼叫)
   * @param {number} dt 兩幀之間的時間差 (秒，例如 0.016 秒)
   */
  update(dt) {
    // TODO: 在此更新質點位置、速度、溫度、化學反應速率等
  },

  /**
   * 4. 畫面渲染方法 (每幀繪製)
   * @param {CanvasRenderingContext2D} ctx 2D 畫布畫筆
   * @param {number} width 
   * @param {number} height 
   */
  render(ctx, width, height) {
    // TODO: 在此使用 ctx 繪製你的虛擬儀器、圖表與流體效果
  },

  /**
   * 5. 處理來自遠端其他學員的操作廣播
   * @param {string} actionType 動作名稱
   * @param {Object} payload 附帶資料
   * @param {Object} meta 包含發送者 ID, 姓名與游標顏色
   */
  onRemoteAction(actionType, payload, meta) {
    // TODO: 當其他學員按下開關或調整旋鈕時，在此同步你的畫面狀態
    // 例如: if (actionType === "TOGGLE_SWITCH") this.isOpen = payload.isOpen;
  },

  /**
   * 6. 視窗尺寸改變時的回呼 (選填)
   */
  onResize(width, height) {
    this.width = width;
    this.height = height;
  },

  /**
   * 7. 切換離開實驗室時的記憶體清理
   */
  destroy() {
    // TODO: 清空陣列與計時器，避免記憶體洩漏
  }
};

// 立即向外掛註冊表登記 (取消註解即可啟用)
// LabRegistry.register(TemplateLab);
export default TemplateLab;
