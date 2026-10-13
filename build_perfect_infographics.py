import os
from PIL import Image, ImageDraw, ImageFont

font_bold = r'C:\Windows\Fonts\msjhbd.ttc'
font_reg = r'C:\Windows\Fonts\msjh.ttc'

def fb(sz): return ImageFont.truetype(font_bold, sz)
def fr(sz): return ImageFont.truetype(font_reg, sz)

pic_dir = r'c:\Antigravity\Antigravity教學\PIC'

def draw_header(d, W, title, subtitle):
    d.rectangle([0, 0, W, 130], fill=(15, 23, 42))
    d.line([0, 130, W, 130], fill=(51, 65, 85), width=3)
    d.text((W // 2, 50), title, font=fb(46), fill=(248, 250, 252), anchor='mm')
    d.text((W // 2, 98), subtitle, font=fb(23), fill=(148, 163, 184), anchor='mm')

def draw_arrow(d, cx, cy, col=(148, 163, 184), size=24):
    # Right-pointing clean polygon arrow
    d.polygon([(cx - size, cy - size), (cx + size, cy), (cx - size, cy + size)], fill=col)

def draw_badge(d, x, y, text, bg, fg, sz=22, pad_x=16, pad_y=6):
    font = fb(sz)
    bbox = d.textbbox((x, y), text, font=font, anchor='mm')
    bx1 = bbox[0] - pad_x
    by1 = bbox[1] - pad_y
    bx2 = bbox[2] + pad_x
    by2 = bbox[3] + pad_y
    d.rounded_rectangle([bx1, by1, bx2, by2], radius=8, fill=bg)
    d.text((x, y), text, font=font, fill=fg, anchor='mm')

# ==============================================================================
# 1. ch1_ide_layout.png (2200 x 1150)
# ==============================================================================
print("1. Generating ch1_ide_layout.png...")
W, H = 2200, 1200
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "Google Antigravity 2.0 介面架構導覽", 
    "以 AI 代理為核心的全新對話指揮中心：三大核心功能區塊配置圖")

card_y1, card_y2 = 165, 1140

# --- Card 1: Left Sidebar ---
c1_x1, c1_x2 = 60, 680
d.rounded_rectangle([c1_x1, card_y1, c1_x2, card_y2], radius=20, fill=(21, 27, 43), outline=(99, 102, 241), width=4)

d.rounded_rectangle([c1_x1+20, card_y1+20, c1_x2-20, card_y1+85], radius=12, fill=(99, 102, 241))
d.text(((c1_x1 + c1_x2) // 2, card_y1+52), "[區塊 1] 左側功能導覽欄 (Left Sidebar)", font=fb(26), fill=(255, 255, 255), anchor='mm')
d.text(((c1_x1 + c1_x2) // 2, card_y1+115), "專案管理與全域設定切換中心", font=fb(22), fill=(165, 180, 252), anchor='mm')

items_c1 = [
    ("[新對話] New Conversation", "開啟全新獨立對話視窗", (79, 70, 229)),
    ("[專案管理] Projects", "綁定與管理本地資料夾工作區", (30, 58, 138)),
    ("[設定與權限] Settings", "切換手動審查 / 自動同意權限", (30, 41, 59)),
    ("[外掛技能] Skills & Plugins", "管理自訂提示詞技能與 MCP 工具", (30, 41, 59)),
    ("[排程任務] Scheduled Tasks", "管理定時背景任務與自動化排程", (30, 41, 59)),
]

y_curr = card_y1 + 150
for title, desc, bg in items_c1:
    d.rounded_rectangle([c1_x1+25, y_curr, c1_x2-25, y_curr+108], radius=12, fill=bg, outline=(71, 85, 105), width=2)
    d.text((c1_x1+45, y_curr+34), title, font=fb(24), fill=(248, 250, 252), anchor='lm')
    d.text((c1_x1+45, y_curr+74), desc, font=fb(21), fill=(203, 213, 225), anchor='lm')
    y_curr += 128

d.rounded_rectangle([c1_x1+25, card_y2-135, c1_x2-25, card_y2-25], radius=12, fill=(15, 23, 42), outline=(99, 102, 241), width=2)
d.text(((c1_x1 + c1_x2) // 2, card_y2-95), "提示：左上角圖示可隨時收合此欄", font=fb(22), fill=(165, 180, 252), anchor='mm')
d.text(((c1_x1 + c1_x2) // 2, card_y2-55), "介面不再是傳統擁擠複雜的程式碼檔案樹", font=fb(20), fill=(148, 163, 184), anchor='mm')


# --- Card 2: Center Chat Canvas ---
c2_x1, c2_x2 = 720, 1540
d.rounded_rectangle([c2_x1, card_y1, c2_x2, card_y2], radius=20, fill=(15, 23, 42), outline=(14, 165, 233), width=5)

d.rounded_rectangle([c2_x1+20, card_y1+20, c2_x2-20, card_y1+85], radius=12, fill=(2, 132, 199))
d.text(((c2_x1 + c2_x2) // 2, card_y1+52), "[區塊 2] 正中央：對話主畫布 (Chat Canvas) ★ 核心", font=fb(26), fill=(255, 255, 255), anchor='mm')
d.text(((c2_x1 + c2_x2) // 2, card_y1+115), "核心操作區：直接在視窗正中央指揮 AI 代理", font=fb(22), fill=(56, 189, 248), anchor='mm')

# Mockup center message
d.rounded_rectangle([c2_x1+30, card_y1+155, c2_x2-30, card_y1+380], radius=16, fill=(30, 41, 59), outline=(56, 189, 248), width=2)
d.text((c2_x1+55, card_y1+195), "使用者提問示範（自然語言輸入）：", font=fb(23), fill=(125, 211, 252), anchor='lm')
d.text((c2_x1+55, card_y1+245), "「請幫我建立一個耳機銷售網站 index.html，", font=fb(26), fill=(248, 250, 252), anchor='lm')
d.text((c2_x1+55, card_y1+295), "  使用專案 PIC 資料夾照片，並支援手機版 RWD！」", font=fb(26), fill=(248, 250, 252), anchor='lm')
d.text((c2_x1+55, card_y1+345), "-> AI 代理即刻自主建檔、撰寫代碼並回報進度", font=fb(22), fill=(52, 211, 153), anchor='lm')

# Central Input Box
in_y1, in_y2 = card_y1+410, card_y1+645
d.rounded_rectangle([c2_x1+30, in_y1, c2_x2-30, in_y2], radius=16, fill=(24, 30, 44), outline=(14, 165, 233), width=3)
d.text((c2_x1+55, in_y1+42), "中央輸入框：Ask anything, @ to mention, / for actions", font=fb(24), fill=(226, 232, 240), anchor='lm')
d.line([c2_x1+30, in_y1+85, c2_x2-30, in_y1+85], fill=(51, 65, 85), width=2)

pills = [
    ("[語音輸入 Ctrl+M]", (16, 185, 129)),
    ("[+ 附加檔案]", (99, 102, 241)),
    ("[/ 斜線指令]", (245, 158, 11)),
    ("[@ 提及檔案]", (236, 72, 153))
]
px = c2_x1 + 60
for ptext, pcol in pills:
    draw_badge(d, px + 80, in_y1+145, ptext, pcol, (255, 255, 255), sz=20, pad_x=14, pad_y=8)
    px += 190

# Bottom notes
d.rounded_rectangle([c2_x1+30, card_y1+675, c2_x2-30, card_y2-25], radius=16, fill=(21, 27, 43), outline=(51, 65, 85), width=2)
d.text((c2_x1+55, card_y1+720), "新版 Antigravity 2.0 重大特點：", font=fb(25), fill=(56, 189, 248), anchor='lm')
c2_notes = [
    "* 擺脫傳統兩側夾縫對話框：對話佔據畫面主角！",
    "* 支援一鍵麥克風語音輸入：動口就能叫 AI 改網頁",
    "* 內建反向訪談：不知如何下提示詞時 AI 會反問你 (/grill-me)",
]
ny = card_y1 + 770
for note in c2_notes:
    d.text((c2_x1+55, ny), note, font=fb(23), fill=(203, 213, 225), anchor='lm')
    ny += 48


# --- Card 3: Right Auxiliary Pane ---
c3_x1, c3_x2 = 1580, 2140
d.rounded_rectangle([c3_x1, card_y1, c3_x2, card_y2], radius=20, fill=(21, 27, 43), outline=(16, 185, 129), width=4)

d.rounded_rectangle([c3_x1+20, card_y1+20, c3_x2-20, card_y1+85], radius=12, fill=(16, 185, 129))
d.text(((c3_x1 + c3_x2) // 2, card_y1+52), "[區塊 3] 右側輔助面板 (Auxiliary Pane)", font=fb(26), fill=(255, 255, 255), anchor='mm')
d.text(((c3_x1 + c3_x2) // 2, card_y1+115), "執行成果與程式碼變更審查面板", font=fb(22), fill=(110, 231, 183), anchor='mm')

items_c3 = [
    ("[成果產出] Artifacts", "檢視 AI 產出的實作計畫、架構文件與生成圖片", (6, 78, 59)),
    ("[程式碼變更] Files Changed", "即時比對與審查被建立/修改的檔案代碼差異", (30, 41, 59)),
    ("[系統終端機] Terminal", "檢視底層命令執行日誌（快速鍵 Ctrl + `）", (30, 41, 59)),
    ("[背景子代理] Subagents", "監看並行子代理任務與瀏覽器自動化測試狀態", (30, 41, 59)),
]
y_curr = card_y1 + 155
for title, desc, bg in items_c3:
    d.rounded_rectangle([c3_x1+25, y_curr, c3_x2-25, y_curr+140], radius=12, fill=bg, outline=(71, 85, 105), width=2)
    d.text((c3_x1+45, y_curr+40), title, font=fb(24), fill=(248, 250, 252), anchor='lm')
    d.text((c3_x1+45, y_curr+88), desc, font=fb(21), fill=(203, 213, 225), anchor='lm')
    y_curr += 165

d.rounded_rectangle([c3_x1+25, card_y2-135, c3_x2-25, card_y2-25], radius=12, fill=(15, 23, 42), outline=(16, 185, 129), width=2)
d.text(((c3_x1 + c3_x2) // 2, card_y2-95), "提示：執行時自動展開，平時彈性收合", font=fb(22), fill=(110, 231, 183), anchor='mm')
d.text(((c3_x1 + c3_x2) // 2, card_y2-55), "不干擾中央主對話，讓思路保持清晰", font=fb(20), fill=(148, 163, 184), anchor='mm')

img.save(os.path.join(pic_dir, 'ch1_ide_layout.png'), quality=95)
print("ch1_ide_layout.png successfully rendered!")


# ==============================================================================
# 2. ch1_workspace_boundary.png (2000 x 950)
# ==============================================================================
print("2. Generating ch1_workspace_boundary.png...")
W, H = 2000, 950
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "Project 專案工作區安全邊界示意圖", 
    "Antigravity 具備「環境隔離沙盒」：只在授權資料夾內操作，保護個人電腦安全")

card_y1, card_y2 = 165, 900

# Left Card: Authorized Sandbox (Green)
l_x1, l_x2 = 70, 970
d.rounded_rectangle([l_x1, card_y1, l_x2, card_y2], radius=20, fill=(16, 40, 32), outline=(16, 185, 129), width=4)

d.rounded_rectangle([l_x1+25, card_y1+25, l_x2-25, card_y1+95], radius=12, fill=(16, 185, 129))
d.text(((l_x1 + l_x2) // 2, card_y1+60), "[安全沙盒] AI 獲授權操作工作區", font=fb(30), fill=(255, 255, 255), anchor='mm')

d.rounded_rectangle([l_x1+30, card_y1+125, l_x2-30, card_y1+215], radius=12, fill=(6, 78, 59), outline=(52, 211, 153), width=2)
d.text(((l_x1 + l_x2) // 2, card_y1+170), "專案資料夾路徑：C:\\Antigravity\\web-demo\\", font=fb(25), fill=(248, 250, 252), anchor='mm')

l_items = [
    ("[允許] 建立與修改網頁檔案", "自由新增 index.html、style.css、main.js 等專案代碼"),
    ("[允許] 讀取專案圖片素材", "讀寫本資料夾內的 PIC/ 照片庫，快速插入網頁版面"),
    ("[允許] 執行專案終端機命令", "執行 git 初始化、GitHub CLI 發布網頁等專案建置指令"),
]
y_curr = card_y1 + 245
for title, desc in l_items:
    d.rounded_rectangle([l_x1+30, y_curr, l_x2-30, y_curr+110], radius=12, fill=(20, 54, 42), outline=(52, 211, 153), width=1)
    d.text((l_x1+55, y_curr+38), title, font=fb(25), fill=(52, 211, 153), anchor='lm')
    d.text((l_x1+55, y_curr+80), desc, font=fb(22), fill=(226, 232, 240), anchor='lm')
    y_curr += 130

d.rounded_rectangle([l_x1+30, card_y2-110, l_x2-30, card_y2-25], radius=12, fill=(6, 95, 70))
d.text(((l_x1 + l_x2) // 2, card_y2-68), "安全保證：AI 所有寫入操作嚴格受限於此資料夾內", font=fb(23), fill=(255, 255, 255), anchor='mm')


# Right Card: Protected System (Red)
r_x1, r_x2 = 1030, 1930
d.rounded_rectangle([r_x1, card_y1, r_x2, card_y2], radius=20, fill=(45, 18, 24), outline=(244, 63, 94), width=4)

d.rounded_rectangle([r_x1+25, card_y1+25, r_x2-25, card_y1+95], radius=12, fill=(225, 29, 72))
d.text(((r_x1 + r_x2) // 2, card_y1+60), "[系統保護] 未授權禁止存取區域", font=fb(30), fill=(255, 255, 255), anchor='mm')

d.rounded_rectangle([r_x1+30, card_y1+125, r_x2-30, card_y1+215], radius=12, fill=(76, 29, 44), outline=(251, 113, 133), width=2)
d.text(((r_x1 + r_x2) // 2, card_y1+170), "外部磁碟與目錄：桌面 / C 槽根目錄 / 個人相片", font=fb(25), fill=(254, 205, 211), anchor='mm')

r_items = [
    ("[禁止] 個人桌面與我的文件", "AI 預設無法越界存取電腦桌面、下載資料夾與私人物件"),
    ("[禁止] 作業系統核心根目錄", "C:\\Windows 及系統開機檔案受到作業系統與沙盒雙重隔離"),
    ("[禁止] 私人密碼與個人隱私", "未經授權禁止讀取外圍個人文件，避免個人資訊外洩"),
]
y_curr = card_y1 + 245
for title, desc in r_items:
    d.rounded_rectangle([r_x1+30, y_curr, r_x2-30, y_curr+110], radius=12, fill=(60, 25, 35), outline=(251, 113, 133), width=1)
    d.text((r_x1+55, y_curr+38), title, font=fb(25), fill=(251, 113, 133), anchor='lm')
    d.text((r_x1+55, y_curr+80), desc, font=fb(22), fill=(226, 232, 240), anchor='lm')
    y_curr += 130

d.rounded_rectangle([r_x1+30, card_y2-110, r_x2-30, card_y2-25], radius=12, fill=(159, 18, 57))
d.text(((r_x1 + r_x2) // 2, card_y2-68), "新手守則：切勿將整個桌面或 C 槽設為專案資料夾！", font=fb(23), fill=(255, 255, 255), anchor='mm')

img.save(os.path.join(pic_dir, 'ch1_workspace_boundary.png'), quality=95)
print("ch1_workspace_boundary.png successfully rendered!")


# ==============================================================================
# 3. ch1_permission_modes.png (2000 x 1020)
# ==============================================================================
print("3. Generating ch1_permission_modes.png...")
W, H = 2000, 1020
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "Antigravity 權限管理模式對照圖", 
    "在中央對話輸入框的 Permissions 選單中隨時切換：「逐步審查」或「極速放行」")

card_y1, card_y2 = 165, 970

# Left: Request Review (Default)
l_x1, l_x2 = 70, 970
d.rounded_rectangle([l_x1, card_y1, l_x2, card_y2], radius=20, fill=(15, 30, 48), outline=(56, 189, 248), width=4)
d.rounded_rectangle([l_x1+25, card_y1+25, l_x2-25, card_y1+95], radius=12, fill=(2, 132, 199))
d.text(((l_x1 + l_x2) // 2, card_y1+60), "[預設模式] 手動審查模式 (Default / Request Review)", font=fb(27), fill=(255, 255, 255), anchor='mm')

d.rounded_rectangle([l_x1+30, card_y1+125, l_x2-30, card_y1+250], radius=14, fill=(24, 45, 70), outline=(56, 189, 248), width=2)
d.text(((l_x1 + l_x2) // 2, card_y1+160), "【運作流程】", font=fb(23), fill=(125, 211, 252), anchor='mm')
d.text(((l_x1 + l_x2) // 2, card_y1+210), "提出指令  ->  彈出確認視窗 [Approve / Reject]  ->  點擊執行", font=fb(23), fill=(248, 250, 252), anchor='mm')

p_items_l = [
    ("[核心特徵]", "AI 在執行任何系統終端機命令前，必須等待你點擊 Approve 授權"),
    ("[適合對象]", "初學者、第一次接觸命令行、或正在處理公司重要專案"),
    ("[使用體驗]", "安全感 100%！但每一步都需要手動點擊同意，操作節奏較緊湊"),
]
y_curr = card_y1 + 280
for title, desc in p_items_l:
    d.rounded_rectangle([l_x1+30, y_curr, l_x2-30, y_curr+110], radius=12, fill=(20, 38, 60), outline=(71, 85, 105), width=1)
    d.text((l_x1+55, y_curr+38), title, font=fb(25), fill=(56, 189, 248), anchor='lm')
    d.text((l_x1+55, y_curr+80), desc, font=fb(22), fill=(226, 232, 240), anchor='lm')
    y_curr += 130

d.rounded_rectangle([l_x1+30, card_y2-100, l_x2-30, card_y2-25], radius=12, fill=(3, 105, 161))
d.text(((l_x1 + l_x2) // 2, card_y2-62), "學習建議：初次安裝時維持此預設模式最安心！", font=fb(23), fill=(255, 255, 255), anchor='mm')


# Right: Always Proceed (Auto)
r_x1, r_x2 = 1030, 1930
d.rounded_rectangle([r_x1, card_y1, r_x2, card_y2], radius=20, fill=(45, 30, 15), outline=(245, 158, 11), width=4)
d.rounded_rectangle([r_x1+25, card_y1+25, r_x2-25, card_y1+95], radius=12, fill=(217, 119, 6))
d.text(((r_x1 + r_x2) // 2, card_y1+60), "[高效模式] 自動同意模式 (Always Proceed / Auto)", font=fb(27), fill=(255, 255, 255), anchor='mm')

d.rounded_rectangle([r_x1+30, card_y1+125, r_x2-30, card_y1+250], radius=14, fill=(70, 48, 22), outline=(245, 158, 11), width=2)
d.text(((r_x1 + r_x2) // 2, card_y1+160), "【運作流程】", font=fb(23), fill=(253, 230, 138), anchor='mm')
d.text(((r_x1 + r_x2) // 2, card_y1+210), "提出指令  ->  AI 連續自主執行 (建檔 + 改碼 + 終端機)  ->  完工", font=fb(23), fill=(248, 250, 252), anchor='mm')

p_items_r = [
    ("[核心特徵]", "AI 連續執行讀取、寫檔、修復與部署命令，完全不打斷思維"),
    ("[適合對象]", "練習獨立網頁、原型快速開發、想體驗 Agentic 全自動流程"),
    ("[使用體驗]", "開發速度極快！建議在乾淨獨立的練習專案資料夾中使用"),
]
y_curr = card_y1 + 280
for title, desc in p_items_r:
    d.rounded_rectangle([r_x1+30, y_curr, r_x2-30, y_curr+110], radius=12, fill=(60, 40, 20), outline=(71, 85, 105), width=1)
    d.text((r_x1+55, y_curr+38), title, font=fb(25), fill=(245, 158, 11), anchor='lm')
    d.text((r_x1+55, y_curr+80), desc, font=fb(22), fill=(226, 232, 240), anchor='lm')
    y_curr += 130

d.rounded_rectangle([r_x1+30, card_y2-100, r_x2-30, card_y2-25], radius=12, fill=(180, 83, 9))
d.text(((r_x1 + r_x2) // 2, card_y2-62), "本課程推薦：製作耳機網頁與發布時切換此模式最省時！", font=fb(23), fill=(255, 255, 255), anchor='mm')

img.save(os.path.join(pic_dir, 'ch1_permission_modes.png'), quality=95)
print("ch1_permission_modes.png successfully rendered!")


# ==============================================================================
# 4. ch2_landing_page_anatomy.png (2000 x 1050)
# ==============================================================================
print("4. Generating ch2_landing_page_anatomy.png...")
W, H = 2000, 1050
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "商業產品介紹頁（Landing Page）5 大核心架構解剖", 
    "在向 AI 下達提示詞前，先掌握現代高轉換率產品網頁的骨架架構")

# Browser frame
fx1, fy1, fx2, fy2 = 80, 160, 1920, 1000
d.rounded_rectangle([fx1, fy1, fx2, fy2], radius=18, fill=(15, 23, 42), outline=(71, 85, 105), width=3)
d.rounded_rectangle([fx1, fy1, fx2, fy1+50], radius=18, fill=(30, 41, 59))
d.rectangle([fx1, fy1+30, fx2, fy1+50], fill=(30, 41, 59))
for idx, col in enumerate([(239, 68, 68), (245, 158, 11), (16, 185, 129)]):
    d.ellipse([fx1+25+idx*24-6, fy1+25-6, fx1+25+idx*24+6, fy1+25+6], fill=col)
d.text(((fx1+fx2)//2, fy1+25), "https://yoursite.github.io/product-demo.html", font=fb(20), fill=(148, 163, 184), anchor='mm')

blocks = [
    ("[區塊 1] 頂部導覽列 (Navbar)", "SmartSound Pro 品牌 Logo  ＋  特點選單導航  ＋  [立即預購] 快速行動按鈕", (99, 102, 241)),
    ("[區塊 2] 主視覺區 (Hero Section)", "超吸睛主標題  ＋  痛點副標題  ＋  耳機高畫質主圖  ＋  [搶先預購] 主要行動呼籲 (CTA)", (2, 132, 199)),
    ("[區塊 3] 核心賣點 (Features 3 大特色)", "[頂級主動降噪]  ｜  [40 小時超長續航]  ｜  [人體工學極致舒適耳罩]", (16, 185, 129)),
    ("[區塊 4] 多角度圖鑑與定價 (Gallery & Pricing)", "多視角照片展示（正面/側面/情境） ＋  [標準版 $3,990] 與 [旗艦版 $5,990] 比較表", (245, 158, 11)),
    ("[區塊 5] 預購表單與頁尾 (Form & Footer)", "姓名/Email/電話線上表單輸入框  ＋  隱私保護政策  ＋  版權聲明與社群連結", (100, 116, 139)),
]

by = fy1 + 75
for title, desc, bg_title in blocks:
    d.rounded_rectangle([fx1+30, by, fx2-30, by+135], radius=14, fill=(24, 32, 48), outline=bg_title, width=2)
    d.rounded_rectangle([fx1+50, by+15, fx1+520, by+65], radius=8, fill=bg_title)
    d.text((fx1+285, by+40), title, font=fb(23), fill=(255, 255, 255), anchor='mm')
    d.text((fx1+60, by+98), desc, font=fb(24), fill=(248, 250, 252), anchor='lm')
    by += 155

img.save(os.path.join(pic_dir, 'ch2_landing_page_anatomy.png'), quality=95)
print("ch2_landing_page_anatomy.png successfully rendered!")


# ==============================================================================
# 5. ch2_interview_flow.png (2000 x 900)
# ==============================================================================
print("5. Generating ch2_interview_flow.png...")
W, H = 2000, 900
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "「先問答、後動工」反向訪談法三部曲", 
    "提示詞不用一次想破頭！請 AI 扮演顧問主動提問，像做選擇題一樣輕鬆敲定需求")

step_w = 560
step_y1, step_y2 = 165, 840

steps = [
    (70, "步驟 1：啟動反向訪談", "叫 AI 先別急著寫程式！", 
     (99, 102, 241), (25, 30, 52),
     [
         ("使用者輸入開場白提示詞：", (165, 180, 252)),
         ("「我想做耳機銷售網頁，請先不要寫程式！", (248, 250, 252)),
         ("  請扮演顧問，向我提出 4 個關鍵問題並給選項。」", (248, 250, 252)),
         ("", (0, 0, 0)),
         ("快捷秘訣：直接輸入 /grill-me 斜線指令", (245, 158, 11)),
     ]),

    (720, "步驟 2：像做選擇題回答", "快速挑選符合預期的選項", 
     (2, 132, 199), (18, 38, 62),
     [
         ("AI 顧問逐一列出問題讓你選：", (125, 211, 252)),
         ("1. 配色風格：(A) 曜石黑  (B) 純白  (C) 霓虹？", (241, 245, 249)),
         ("2. 核心賣點：主動降噪、超長續航、人體工學？", (241, 245, 249)),
         ("3. 價格方案：單一售價 vs 雙版本？", (241, 245, 249)),
         ("", (0, 0, 0)),
         ("你只需回覆：1 選 A、2 強調降噪、3 分兩版", (52, 211, 153)),
     ]),

    (1370, "步驟 3：精準生成成果", "100% 貼合心中想像與期待", 
     (16, 185, 129), (16, 42, 34),
     [
         ("AI 彙整規格確認書後一鍵動工：", (110, 231, 183)),
         ("* 自動建立完整架構 index.html", (241, 245, 249)),
         ("* 精準套用專案 PIC 資料夾耳機照片", (241, 245, 249)),
         ("* 一次到位！產出完全不偏離預期", (241, 245, 249)),
         ("", (0, 0, 0)),
         ("成果：省下 80% 來回除錯與重做時間！", (245, 158, 11)),
     ]),
]

for sx, title, subtitle, col_main, col_bg, text_list in steps:
    d.rounded_rectangle([sx, step_y1, sx+step_w, step_y2], radius=18, fill=col_bg, outline=col_main, width=4)
    d.rounded_rectangle([sx+20, step_y1+20, sx+step_w-20, step_y1+85], radius=12, fill=col_main)
    d.text((sx+step_w//2, step_y1+52), title, font=fb(26), fill=(255, 255, 255), anchor='mm')
    d.text((sx+step_w//2, step_y1+115), subtitle, font=fb(21), fill=(203, 213, 225), anchor='mm')
    
    d.rounded_rectangle([sx+20, step_y1+150, sx+step_w-20, step_y2-25], radius=14, fill=(15, 23, 42), outline=(71, 85, 105), width=2)
    
    ly = step_y1 + 185
    for line, color in text_list:
        if line == "":
            ly += 16
        else:
            d.text((sx+40, ly), line, font=fb(21), fill=color, anchor='lm')
            ly += 42

# Draw clean vector arrows
draw_arrow(d, 675, 480, col=(203, 213, 225), size=20)
draw_arrow(d, 1325, 480, col=(203, 213, 225), size=20)

img.save(os.path.join(pic_dir, 'ch2_interview_flow.png'), quality=95)
print("ch2_interview_flow.png successfully rendered!")


# ==============================================================================
# 6. ch2_iterative_tuning.png (2000 x 900)
# ==============================================================================
print("6. Generating ch2_iterative_tuning.png...")
W, H = 2000, 900
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "對話式迭代微調（Iterative Tuning）進化路徑", 
    "生成第一版後不用自己改程式！動口說一句，AI 自動精準進行局部增量修復")

col_w = 560
col_y1, col_y2 = 165, 840

# Col 1: V1 Prototype
c1_x = 70
d.rounded_rectangle([c1_x, col_y1, c1_x+col_w, col_y2], radius=18, fill=(30, 41, 59), outline=(100, 116, 139), width=3)
d.rounded_rectangle([c1_x+20, col_y1+20, c1_x+col_w-20, col_y1+85], radius=12, fill=(71, 85, 105))
d.text((c1_x+col_w//2, col_y1+52), "階段 1：初版網頁 (V1 原型)", font=fb(25), fill=(255, 255, 255), anchor='mm')
d.text((c1_x+col_w//2, col_y1+115), "基本骨架建立，待細緻打磨", font=fb(21), fill=(203, 213, 225), anchor='mm')

v1_items = [
    ("[骨架完成]", "已建立標題、耳機圖片與預購表單"),
    ("[細節不足]", "Hero 標題不夠突出、按鈕顏色略暗"),
    ("[區塊待補]", "缺少顧客好評推薦與多視角耳機圖"),
    ("[當前評估]", "基本骨架正確，但缺乏商業轉單吸引力"),
]
vy = col_y1 + 150
for t, dsc in v1_items:
    d.rounded_rectangle([c1_x+25, vy, c1_x+col_w-25, vy+110], radius=12, fill=(15, 23, 42), outline=(71, 85, 105), width=1)
    d.text((c1_x+45, vy+36), t, font=fb(23), fill=(203, 213, 225), anchor='lm')
    d.text((c1_x+45, vy+78), dsc, font=fb(21), fill=(148, 163, 184), anchor='lm')
    vy += 130


# Col 2: Tuning Prompts
c2_x = 720
d.rounded_rectangle([c2_x, col_y1, c2_x+col_w, col_y2], radius=18, fill=(45, 35, 15), outline=(245, 158, 11), width=4)
d.rounded_rectangle([c2_x+20, col_y1+20, c2_x+col_w-20, col_y1+85], radius=12, fill=(217, 119, 6))
d.text((c2_x+col_w//2, col_y1+52), "階段 2：對話微調 (自然語言指令)", font=fb(25), fill=(255, 255, 255), anchor='mm')
d.text((c2_x+col_w//2, col_y1+115), "動口不動手：針對細節下達微調指令", font=fb(21), fill=(253, 230, 138), anchor='mm')

prompts_tuning = [
    ("[指令 1：視覺強化]", "「請把 Hero 標題字體加大，並把按鈕改成亮橘色漸層按鈕！」"),
    ("[指令 2：擴充區塊]", "「請在產品特色後面加上 3 位顧客的五星好評推薦卡片！」"),
    ("[指令 3：互動體驗]", "「點擊預購按鈕時平滑捲動到表單，送出後跳出感謝訊息！」"),
]
py = col_y1 + 150
for t, dsc in prompts_tuning:
    d.rounded_rectangle([c2_x+25, py, c2_x+col_w-25, py+145], radius=12, fill=(24, 30, 44), outline=(245, 158, 11), width=2)
    d.text((c2_x+45, py+36), t, font=fb(23), fill=(245, 158, 11), anchor='lm')
    # Split text into two lines nicely
    split_pt = len(dsc) // 2 + 1
    d.text((c2_x+45, py+78), dsc[:split_pt], font=fb(20), fill=(248, 250, 252), anchor='lm')
    d.text((c2_x+45, py+112), dsc[split_pt:], font=fb(20), fill=(248, 250, 252), anchor='lm')
    py += 165


# Col 3: V2 Final
c3_x = 1370
d.rounded_rectangle([c3_x, col_y1, c3_x+col_w, col_y2], radius=18, fill=(16, 42, 34), outline=(16, 185, 129), width=4)
d.rounded_rectangle([c3_x+20, col_y1+20, c3_x+col_w-20, col_y1+85], radius=12, fill=(16, 185, 129))
d.text((c3_x+col_w//2, col_y1+52), "階段 3：最終成品 (V2 商業旗艦版)", font=fb(25), fill=(255, 255, 255), anchor='mm')
d.text((c3_x+col_w//2, col_y1+115), "視覺精緻、高信任感與轉換率", font=fb(21), fill=(110, 231, 183), anchor='mm')

v2_items = [
    ("[視覺層次豐富]", "亮橘色發光 CTA 按鈕 ＋ 大器科技感排版"),
    ("[完整信任背書]", "五星好評評價卡片 ＋ 雙版本價格方案比較表"),
    ("[流暢互動體驗]", "平滑錨點捲動 ＋ 表單填寫即時驗證視窗"),
    ("[自適應 RWD]", "電腦大螢幕與手機窄螢幕皆具備自適應版面"),
]
vy = col_y1 + 150
for t, dsc in v2_items:
    d.rounded_rectangle([c3_x+25, vy, c3_x+col_w-25, vy+110], radius=12, fill=(15, 23, 42), outline=(16, 185, 129), width=1)
    d.text((c3_x+45, vy+36), t, font=fb(23), fill=(52, 211, 153), anchor='lm')
    d.text((c3_x+45, vy+78), dsc, font=fb(21), fill=(248, 250, 252), anchor='lm')
    vy += 130

# Connecting arrows
draw_arrow(d, 675, 480, col=(245, 158, 11), size=20)
draw_arrow(d, 1325, 480, col=(16, 185, 129), size=20)

img.save(os.path.join(pic_dir, 'ch2_iterative_tuning.png'), quality=95)
print("ch2_iterative_tuning.png successfully rendered!")

print("ALL 6 INFOGRAPHIC DIAGRAMS RE-RENDERED WITH ZERO GLITCHES!")
