// ============================================================================
// LabRegistry.js - 實驗室模組註冊管理器
// 支援外掛式即插即用（Plug-and-Play），新增實驗室無須改動核心代碼
// ============================================================================

class LabRegistryClass {
  constructor() {
    this.modules = new Map();
    this.listeners = [];
  }

  /**
   * 註冊一個新實驗室模組
   * @param {Object} module 實驗室規範物件
   */
  register(module) {
    if (!module.id || !module.name) {
      console.error("[LabRegistry] 註冊失敗：模組必須具備 id 與 name 屬性", module);
      return;
    }
    this.modules.set(module.id, module);
    console.log(`[LabRegistry] 成功註冊實驗室: [${module.category || '未分類'}] ${module.name} (id: ${module.id})`);
    
    // 通知所有監聽器
    this.listeners.forEach(fn => fn(module));
  }

  /**
   * 取得特定實驗室
   * @param {string} id 
   */
  get(id) {
    return this.modules.get(id);
  }

  /**
   * 取得所有已註冊的實驗室清單
   */
  getAll() {
    return Array.from(this.modules.values());
  }

  /**
   * 註冊模組加入時的事件回呼
   * @param {Function} callback 
   */
  onRegister(callback) {
    this.listeners.push(callback);
  }
}

export const LabRegistry = new LabRegistryClass();
