# 📚 Antigravity 實戰學院：教學圖表製作與呈現標準作業程序（SOP）

> **版本**：v1.0.0  
> **制定日期**：2026-10-13  
> **適用範圍**：本專案所有章節（第 1 章至第 8 章及未來延伸教材）之架構圖、流程圖、介面導覽與解說圖表。  
> **核心準則**：**「框架容器向量化 ＋ 文字真實打字嵌入（SVG Vector Typography）＋ 框選互動放大」**。

---

## 一、 核心哲學：為什麼採用此模式？

在技術教學教材中，文字與圖表扮演著傳遞精準概念的關鍵角色。傳統製作方式與本 SOP 模式的對比如下：

| 評估維度 | 傳統點陣圖（JPG / PNG 死圖） | 本 SOP 標準：SVG 向量打字 ＋ 互動燈箱 |
| :--- | :--- | :--- |
| **文字清晰度** | 縮放時產生鋸齒、邊緣模糊、壓縮偽影。 | **100% 視網膜極致清晰**，由瀏覽器向量引擎原生渲染，放大千倍無損。 |
| **字型與符號相容性** | 易因系統缺字產生「豆腐方塊亂碼（□）」。 | 依靠現代瀏覽器完備的中英文字型 Fallback，**零缺字、零亂碼**。 |
| **檔案大小與載入速度** | 2K 點陣圖每張需 250KB～500KB。 | 純 SVG 向量代碼每張僅 **5KB～10KB**，載入極快。 |
| **教學展示與課堂互動** | 只能整體放大縮小，無法局部聚焦。 | **支援「按住滑鼠框選任意區塊立即放大至全螢幕」**，講到哪框到哪！ |
| **復原體驗** | 放大後難以抓回原本視角。 | 提供 **「🔄 一鍵還原全圖」**，平滑切換適應視窗。 |

---

## 二、 圖表製作規格標準（SVG 規範）

所有教學圖表一律產出為標準 `.svg` 格式，存放於專案 `PIC/` 目錄中。

### 1. 檔案命名規範
```text
PIC/ch{章節編號}_{功能或內容簡稱}.svg
```
*範例：*
- `PIC/ch1_ide_layout.svg`（第 1 章：介面三大架構導覽）
- `PIC/ch1_workspace_boundary.svg`（第 1 章：工作區安全邊界）
- `PIC/ch2_landing_page_anatomy.svg`（第 2 章：網頁 5 大核心區塊）
- `PIC/ch2_interview_flow.svg`（第 2 章：反向訪談三步驟）

---

### 2. SVG 畫布與防呆設定（關鍵規範）

#### ⚠️ 關鍵防呆：宣告絕對像素寬高，防止尺寸塌陷
SVG 的 `<svg>` 根節點**必須同時宣告 `viewBox` 與固有像素單位的 `width`、`height`**！
若僅寫 `width="100%" height="100%"`，瀏覽器在燈箱以 `width: auto` 彈出時，會因無法計算固有尺寸而將圖片塌陷為 `0px × 0px`（導致圖片隱形看不見）。

```xml
<!-- 正確範例：宣告絕對像素寬高與 viewBox -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 940" width="1600" height="940">
```

#### 標準畫布尺寸推薦：
- **三大區塊橫向對比 / 複雜介面**：`1600 x 940` 或 `1600 x 1000`
- **雙欄對照圖（如安全 vs 禁止、模式 A vs 模式 B）**：`1600 x 820`
- **水平三步驟流程圖（Step 1 ➔ Step 2 ➔ Step 3）**：`1600 x 780`

---

### 3. 字型與文字排版規範

#### （1）字型宣告（Font Stack）
在 SVG `<style>` 區塊中宣告高相容性的原生字型族群：
```css
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif;
```

#### （2）階層字級標準
- **頂部主標題（Title）**：`32px`，字重 800（Extra Bold），顏色 `#f8fafc`
- **頂部副標題（Subtitle）**：`17px`，字重 500，顏色 `#94a3b8`
- **區塊/卡片標題（Card Title）**：`20px～24px`，字重 700，顏色 `#ffffff`
- **項目主標籤（Item Title）**：`16px～18px`，字重 700，顏色 `#f8fafc` 或 主題色
- **內文解說（Item Desc）**：`14px～15px`，字重 400，顏色 `#cbd5e1`

#### （3）符號與文字避免殘缺原則
- **避免在文字標籤內夾雜特殊 Unicode 字符或未支援的私用區 Emoji**（如自訂箭頭或特殊圖示）。
- 流程引導箭頭一律使用 SVG 幾何圖形繪製（例如 `<polygon points="535,410 565,430 535,450" fill="#38bdf8"/>`）。
- 狀態指示統一使用標準中括號結構標籤，如 `[允許]`、`[禁止]`、`[新對話]`、`[步驟 1]`。

---

### 4. 視覺風格與色彩規範（科技感深色模式）

| 角色 | 色碼 (HEX) | 用途說明 |
| :--- | :--- | :--- |
| **畫布底色 (Canvas BG)** | `#0b0f19` | 深黑藍底色，專業沈穩。 |
| **頂部 Banner 底色** | `#0f172a` | 區隔標題列。 |
| **卡片背景色 (Card BG)** | `#151b2b` / `#1e293b` | 獨立內容容器。 |
| **安全 / 正向 / 成果色** | `#10b981` (Emerald) | 安全沙盒、完成步驟、第 3 區塊。 |
| **核心 / 焦點 / 連結色** | `#0ea5e9` / `#38bdf8` (Sky) | 正中央對話框、操作焦點、第 2 區塊。 |
| **導覽 / 系統 / 初始色** | `#6366f1` / `#818cf8` (Indigo) | 左側導覽列、第 1 區塊、初始化。 |
| **高效 / 微調 / 注意色** | `#f59e0b` / `#d97706` (Amber) | 自動同意模式、微調指令。 |
| **危險 / 禁止 / 限制色** | `#f43f5e` / `#e11d48` (Rose) | 系統防護隔離區、禁止事項。 |
| **輔助線與分隔線** | `#334155` / `#475569` | 輕量邊界，保持畫面整齊。 |

---

## 三、 前端 HTML 課文嵌入標準

在各章節 HTML 內容中引用圖表時，遵循以下統一結構：

```html
<div style="margin: 1.75rem 0; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 12px; padding: 1rem; text-align: center;">
  <!-- SVG 圖片標籤：自適應寬度，最大限制 820px -->
  <img src="../PIC/chX_diagram_name.svg" 
       alt="圖表完整中文標題說明" 
       style="width: 100%; max-width: 820px; border-radius: 8px; border: 1px solid var(--border-color); display: block; margin: 0 auto 0.75rem;">
  
  <!-- 下方中文圖說 -->
  <div style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">
    <strong>▲ 圖 X-Y：圖表中文標題</strong><br>
    此處撰寫 1～2 行精煉的導讀說明，引導學生觀看圖中焦點。
  </div>
</div>
```

---

## 四、 前端互動檢視系統（互動式燈箱 Lightbox）

所有教學圖表點擊後均自動掛載專業互動燈箱，提供課堂講解必備的操控能力。

### 1. 核心操控功能一覽

1. **🔲 框選局部放大（Marquee / Box Zoom）**
   - 游標預設為十字準心（`crosshair`）。
   - 按住滑鼠左鍵拖曳拉出半透明藍色框線，**放開滑鼠時立即將圈選區域平滑放大至全螢幕中央**。
2. **🔄 一鍵還原全圖（Reset Zoom）**
   - 點擊工具列「`🔄 還原全圖`」，圖片立即順暢復原至 100% 原始適應比例。
3. **✋ 拖曳平移（Pan）**
   - 放大狀態下，切換「拖曳平移」模式（或直接按住滑鼠右鍵/滾輪中鍵拖曳），自由游覽圖表各個角落。
4. **🖱️ 滑鼠滾輪無段縮放（Mouse Wheel Zoom）**
   - 游標停留在圖片任一部位滾動滾輪，自動以游標焦點為核心進行平滑放大或縮小（支援 75%～1600%）。
5. **快捷控制按鈕**
   - 提供 `➕`、`➖` 及即時倍率顯示（例如 `100%`、`280%`、`520%`）。
   - 按下鍵盤 `ESC` 或點擊右上角 `✕ 關閉` 隨時退出燈箱。

---

### 2. 框選放大核心數學演算原理

當使用者在燈箱舞台上框選區域時，系統執行以下座標換算並計算變換矩陣：

```javascript
// 1. 取得圈選框相對於舞台的中心座標
const boxCenterX = boxLeft + boxWidth / 2;
const boxCenterY = boxTop + boxHeight / 2;
const stageCenterX = stageRect.width / 2;
const stageCenterY = stageRect.height / 2;

// 2. 換算回原始內容未縮放時的相對座標點
const x_content = (boxCenterX - stageCenterX - translateX) / scale;
const y_content = (boxCenterY - stageCenterY - translateY) / scale;

// 3. 計算使選取框剛好填滿舞台所需之新縮放倍率（預留 6% 安全內距）
const zoomRatio = Math.min(stageRect.width / boxWidth, stageRect.height / boxHeight) * 0.94;
const newScale = Math.min(Math.max(scale * zoomRatio, 1), 16);

// 4. 將該目標內容點精準平移至舞台中心
translateX = - x_content * newScale;
translateY = - y_content * newScale;
scale = newScale;

// 5. 套用 GPU 硬體加速 CSS Transform 動畫
imgWrapper.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
```

---

## 五、 自動化腳本模板（Python SVG 生成器）

專案內備有標準生成腳本 [`generate_svg_diagrams.py`](file:///c:/Antigravity/Antigravity教學/generate_svg_diagrams.py)，未來新增章節圖表時，可直接複製該模板結構擴充：

```python
import os

pic_dir = r"c:\Antigravity\Antigravity教學\PIC"
os.makedirs(pic_dir, exist_ok=True)

def svg_wrap(width, height, content):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 800; font-size: 32px; fill: #f8fafc; text-anchor: middle; }}
      .subtitle {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 500; font-size: 17px; fill: #94a3b8; text-anchor: middle; }}
      .card-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 700; font-size: 20px; fill: #ffffff; text-anchor: middle; }}
      .item-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 700; font-size: 17px; fill: #f8fafc; }}
      .item-desc {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 400; font-size: 14.5px; fill: #cbd5e1; }}
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <rect width="{width}" height="{height}" fill="#0b0f19"/>
{content}
</svg>"""
```

---

## 六、 後續章節製圖自我查核清單（Checklist）

在完成新章節並準備發布時，請依據此清單逐一確認：

- [ ] 圖檔格式是否為 `.svg`？
- [ ] `<svg>` 標籤是否同時宣告了 `viewBox` 與具體像素 `width`、`height`（禁止只寫 100%）？
- [ ] 字型族群是否優先指定微軟正黑體與系統無襯線字型？
- [ ] 圖面上是否有任何未支援字元或豆腐方塊（□）？
- [ ] 流程箭頭是否由向量多邊形（`<polygon>` / `<path>`）繪製？
- [ ] HTML 課文中的 `<img>` 路徑是否正確指向 `.svg` 檔案？
- [ ] 在瀏覽器中點擊圖片，燈箱能否正常彈出且完整置中？
- [ ] 測試在燈箱中用滑鼠框選局部區域，能否立即平滑放大至全螢幕？
- [ ] 測試「🔄 還原全圖」按鈕，能否順暢復原為 100% 原始比例？
- [ ] 測試滑鼠滾輪與「✋ 拖曳平移」，確認導覽流暢無卡頓？

---

> **維護備註**：任何關於圖表呈現架構或燈箱互動腳本之更新，請同步修訂本文件，確保教材風格與教學體驗的高度統一。
