import os
from PIL import Image, ImageDraw, ImageFont

font_bold = r'C:\Windows\Fonts\msjhbd.ttc'
font_reg = r'C:\Windows\Fonts\msjh.ttc'

def fb(sz): return ImageFont.truetype(font_bold, sz)
def fr(sz): return ImageFont.truetype(font_reg, sz)

pic_dir = r'c:\Antigravity\Antigravity教學\PIC'

# ==============================================================================
# Helper functions
# ==============================================================================
def draw_header(d, W, title, subtitle):
    # Top banner background
    d.rectangle([0, 0, W, 130], fill=(15, 23, 42))
    d.line([0, 130, W, 130], fill=(51, 65, 85), width=3)
    d.text((W // 2, 50), title, font=fb(48), fill=(248, 250, 252), anchor='mm')
    d.text((W // 2, 98), subtitle, font=fb(24), fill=(148, 163, 184), anchor='mm')

def draw_pill(d, x, y, text, bg, fg, sz=22, pad_x=20, pad_y=8):
    font = fb(sz)
    bbox = d.textbbox((x, y), text, font=font, anchor='mm')
    bx1 = bbox[0] - pad_x
    by1 = bbox[1] - pad_y
    bx2 = bbox[2] + pad_x
    by2 = bbox[3] + pad_y
    d.rounded_rectangle([bx1, by1, bx2, by2], radius=(by2 - by1) // 2, fill=bg)
    d.text((x, y), text, font=font, fill=fg, anchor='mm')

# ==============================================================================
# 1. ch1_ide_layout.png (2200 x 1150)
# ==============================================================================
print("1. Generating ch1_ide_layout.png...")
W, H = 2200, 1150
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "Google Antigravity 2.0 介面架構導覽", 
    "以 AI 代理為核心的全新對話指揮中心：三大核心功能區塊配置圖")

# 3 Big Columns: Left Sidebar, Center Canvas, Right Auxiliary
card_y1, card_y2 = 170, 1070

# --- Card 1: Left Sidebar ---
c1_x1, c1_x2 = 60, 680
d.rounded_rectangle([c1_x1, card_y1, c1_x2, card_y2], radius=20, fill=(21, 27, 43), outline=(99, 102, 241), width=4)
# Header
d.rounded_rectangle([c1_x1+20, card_y1+25, c1_x2-20, card_y1+95], radius=14, fill=(99, 102, 241))
d.text(((c1_x1 + c1_x2) // 2, card_y1+60), "① 左側功能導覽欄 (Left Sidebar)", font=fb(28), fill=(255, 255, 255), anchor='mm')
d.text(((c1_x1 + c1_x2) // 2, card_y1+125), "【專案與功能切換中心】", font=fb(24), fill=(165, 180, 252), anchor='mm')

items_c1 = [
    ("➕ New Chat", "開啟全新對話視窗", (79, 70, 229)),
    ("📁 Projects (專案)", "綁定與管理本地資料夾工作區", (30, 58, 138)),
    ("⚙️ Settings (設定)", "切換手動審查 / 自動同意權限", (30, 41, 59)),
    ("🧩 Skills & Plugins", "擴充外掛工具、規則與自訂技能", (30, 41, 59)),
    ("⏱️ Scheduled Tasks", "管理排程自動化與背景定時任務", (30, 41, 59)),
]

y_curr = card_y1 + 175
for title, desc, bg in items_c1:
    d.rounded_rectangle([c1_x1+25, y_curr, c1_x2-25, y_curr+120], radius=14, fill=bg, outline=(71, 85, 105), width=2)
    d.text((c1_x1+45, y_curr+38), title, font=fb(26), fill=(248, 250, 252), anchor='lm')
    d.text((c1_x1+45, y_curr+82), desc, font=fb(22), fill=(203, 213, 225), anchor='lm')
    y_curr += 140

d.rounded_rectangle([c1_x1+25, card_y2-130, c1_x2-25, card_y2-30], radius=14, fill=(15, 23, 42), outline=(99, 102, 241), width=2)
d.text(((c1_x1 + c1_x2) // 2, card_y2-95), "💡 介面特色：左上角圖示可一鍵收合", font=fb(22), fill=(165, 180, 252), anchor='mm')
d.text(((c1_x1 + c1_x2) // 2, card_y2-60), "專案已不再是傳統混亂的檔案樹！", font=fb(20), fill=(148, 163, 184), anchor='mm')


# --- Card 2: Center Chat Canvas ---
c2_x1, c2_x2 = 720, 1540
d.rounded_rectangle([c2_x1, card_y1, c2_x2, card_y2], radius=20, fill=(15, 23, 42), outline=(14, 165, 233), width=5)
# Header
d.rounded_rectangle([c2_x1+20, card_y1+25, c2_x2-20, card_y1+95], radius=14, fill=(2, 132, 199))
d.text(((c2_x1 + c2_x2) // 2, card_y1+60), "② 正中央：對話主畫布 (Chat Canvas) ★", font=fb(28), fill=(255, 255, 255), anchor='mm')
d.text(((c2_x1 + c2_x2) // 2, card_y1+125), "【核心操作區：直接在中央向 AI 下達指令】", font=fb(24), fill=(56, 189, 248), anchor='mm')

# Mockup center message
d.rounded_rectangle([c2_x1+30, card_y1+170, c2_x2-30, card_y1+390], radius=16, fill=(30, 41, 59), outline=(56, 189, 248), width=2)
d.text((c2_x1+55, card_y1+215), "👤 你的自然語言提示詞：", font=fb(24), fill=(125, 211, 252), anchor='lm')
d.text((c2_x1+55, card_y1+270), "「請幫我建立一個耳機銷售網站 index.html，", font=fb(26), fill=(248, 250, 252), anchor='lm')
d.text((c2_x1+55, card_y1+320), "  使用 PIC 資料夾的照片，並支援手機版 RWD！」", font=fb(26), fill=(248, 250, 252), anchor='lm')
d.text((c2_x1+55, card_y1+365), "🤖 AI 即刻自主寫碼、建立檔案並回報成果", font=fb(22), fill=(16, 185, 129), anchor='lm')

# Central Input Box
in_y1, in_y2 = card_y1+430, card_y1+640
d.rounded_rectangle([c2_x1+30, in_y1, c2_x2-30, in_y2], radius=16, fill=(24, 30, 44), outline=(14, 165, 233), width=3)
d.text((c2_x1+55, in_y1+45), "中央輸入框：Ask anything, @ to mention, / for actions", font=fb(24), fill=(226, 232, 240), anchor='lm')
d.line([c2_x1+30, in_y1+90, c2_x2-30, in_y1+90], fill=(51, 65, 85), width=2)

pills = [
    ("🎙️ 語音輸入 (Ctrl + M)", (16, 185, 129)),
    ("📎 + 附件上傳", (99, 102, 241)),
    ("/ 斜線指令 (/grill-me)", (245, 158, 11)),
    ("@ 提及檔案", (236, 72, 153))
]
px = c2_x1 + 140
for ptext, pcol in pills:
    draw_pill(d, px, in_y1+150, ptext, pcol, (255, 255, 255), sz=22, pad_x=18, pad_y=10)
    px += 185

# Bottom notes
d.rounded_rectangle([c2_x1+30, card_y1+680, c2_x2-30, card_y2-30], radius=16, fill=(21, 27, 43), outline=(51, 65, 85), width=2)
d.text((c2_x1+55, card_y1+725), "🔥 新版 2.0 重大升級特點：", font=fb(26), fill=(56, 189, 248), anchor='lm')
c2_notes = [
    "• 擺脫傳統兩側夾縫對話框：對話佔據畫面主角！",
    "• 支援一鍵麥克風語音輸入：動口就能叫 AI 改網頁",
    "• 內建對話式需求訪談：不知如何下提示詞時 AI 會反問你",
]
ny = card_y1 + 775
for note in c2_notes:
    d.text((c2_x1+55, ny), note, font=fb(24), fill=(203, 213, 225), anchor='lm')
    ny += 45


# --- Card 3: Right Auxiliary Pane ---
c3_x1, c3_x2 = 1580, 2140
d.rounded_rectangle([c3_x1, card_y1, c3_x2, card_y2], radius=20, fill=(21, 27, 43), outline=(16, 185, 129), width=4)
# Header
d.rounded_rectangle([c3_x1+20, card_y1+25, c3_x2-20, card_y1+95], radius=14, fill=(16, 185, 129))
d.text(((c3_x1 + c3_x2) // 2, card_y1+60), "③ 右側輔助面板 (Auxiliary Pane)", font=fb(28), fill=(255, 255, 255), anchor='mm')
d.text(((c3_x1 + c3_x2) // 2, card_y1+125), "【執行成果與檔案變更檢視】", font=fb(24), fill=(110, 231, 183), anchor='mm')

items_c3 = [
    ("📦 Artifacts (成果物)", "檢視 AI 寫出的完整計畫、架構報告與生成圖片", (6, 78, 59)),
    ("📝 Files Changed (變更)", "即時比對被建立與修改的程式碼（VCS 版本差異）", (30, 41, 59)),
    ("💻 Terminal (終端機)", "檢視系統指令執行日誌（快速鍵 Ctrl + `）", (30, 41, 59)),
    ("🤖 Subagents (子代理)", "背景任務、並行工作排程與瀏覽器測試狀態", (30, 41, 59)),
]
y_curr = card_y1 + 175
for title, desc, bg in items_c3:
    d.rounded_rectangle([c3_x1+25, y_curr, c3_x2-25, y_curr+145], radius=14, fill=bg, outline=(71, 85, 105), width=2)
    d.text((c3_x1+45, y_curr+42), title, font=fb(26), fill=(248, 250, 252), anchor='lm')
    d.text((c3_x1+45, y_curr+92), desc, font=fb(22), fill=(203, 213, 225), anchor='lm')
    y_curr += 175

d.rounded_rectangle([c3_x1+25, card_y2-130, c3_x2-25, card_y2-30], radius=14, fill=(15, 23, 42), outline=(16, 185, 129), width=2)
d.text(((c3_x1 + c3_x2) // 2, card_y2-95), "💡 預設彈性收合，工作時自動展開", font=fb(22), fill=(110, 231, 183), anchor='mm')
d.text(((c3_x1 + c3_x2) // 2, card_y2-60), "不搶佔中央視覺，乾淨專注！", font=fb(20), fill=(148, 163, 184), anchor='mm')

img.save(os.path.join(pic_dir, 'ch1_ide_layout.png'), quality=95)
print("ch1_ide_layout.png done!")


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

card_y1, card_y2 = 170, 890

# Left Card: Authorized Sandbox (Green)
l_x1, l_x2 = 70, 970
d.rounded_rectangle([l_x1, card_y1, l_x2, card_y2], radius=20, fill=(16, 40, 32), outline=(16, 185, 129), width=4)
# Header
d.rounded_rectangle([l_x1+25, card_y1+25, l_x2-25, card_y1+100], radius=14, fill=(16, 185, 129))
d.text(((l_x1 + l_x2) // 2, card_y1+62), "✅ AI 授權操作工作區 (安全沙盒)", font=fb(32), fill=(255, 255, 255), anchor='mm')

# Path block
d.rounded_rectangle([l_x1+30, card_y1+130, l_x2-30, card_y1+220], radius=12, fill=(6, 78, 59), outline=(52, 211, 153), width=2)
d.text(((l_x1 + l_x2) // 2, card_y1+175), "📁 專案資料夾路徑：C:\\Antigravity\\web-demo\\", font=fb(26), fill=(248, 250, 252), anchor='mm')

l_items = [
    ("✔ 建立與修改網頁檔案", "自由新增 index.html、style.css、main.js 等專案代碼"),
    ("✔ 讀取專案圖片素材", "讀寫本資料夾內的 PIC/ 照片庫，快速插入網頁版面"),
    ("✔ 執行專案終端機命令", "執行 git 初始化、GitHub CLI 發布網頁等專案建置指令"),
]
y_curr = card_y1 + 250
for title, desc in l_items:
    d.rounded_rectangle([l_x1+30, y_curr, l_x2-30, y_curr+105], radius=12, fill=(20, 54, 42), outline=(52, 211, 153), width=1)
    d.text((l_x1+55, y_curr+36), title, font=fb(26), fill=(52, 211, 153), anchor='lm')
    d.text((l_x1+55, y_curr+76), desc, font=fb(22), fill=(226, 232, 240), anchor='lm')
    y_curr += 125

d.rounded_rectangle([l_x1+30, card_y2-110, l_x2-30, card_y2-30], radius=12, fill=(6, 95, 70))
d.text(((l_x1 + l_x2) // 2, card_y2-70), "🛡️ 安全保證：AI 所有寫入操作嚴格受限於此資料夾內", font=fb(24), fill=(255, 255, 255), anchor='mm')


# Right Card: Protected System (Red)
r_x1, r_x2 = 1030, 1930
d.rounded_rectangle([r_x1, card_y1, r_x2, card_y2], radius=20, fill=(45, 18, 24), outline=(244, 63, 94), width=4)
# Header
d.rounded_rectangle([r_x1+25, card_y1+25, r_x2-25, card_y1+100], radius=14, fill=(225, 29, 72))
d.text(((r_x1 + r_x2) // 2, card_y1+62), "🔒 本機受保護區域 (未授權禁止存取)", font=fb(32), fill=(255, 255, 255), anchor='mm')

# Path block
d.rounded_rectangle([r_x1+30, card_y1+130, r_x2-30, card_y1+220], radius=12, fill=(76, 29, 44), outline=(251, 113, 133), width=2)
d.text(((r_x1 + r_x2) // 2, card_y1+175), "🚫 外部磁碟與目錄：桌面 / C 槽根目錄 / 個人相片", font=fb(26), fill=(254, 205, 211), anchor='mm')

r_items = [
    ("🚫 個人桌面與我的文件", "AI 預設無法越界存取電腦桌面、下載資料夾與私人物件"),
    ("🚫 作業系統核心根目錄", "C:\\Windows 及系統開機檔案受到作業系統與沙盒雙重隔離"),
    ("🚫 私人密碼與個人隱私", "未經授權禁止讀取外圍個人文件，避免個人資訊外洩"),
]
y_curr = card_y1 + 250
for title, desc in r_items:
    d.rounded_rectangle([r_x1+30, y_curr, r_x2-30, y_curr+105], radius=12, fill=(60, 25, 35), outline=(251, 113, 133), width=1)
    d.text((r_x1+55, y_curr+36), title, font=fb(26), fill=(251, 113, 133), anchor='lm')
    d.text((r_x1+55, y_curr+76), desc, font=fb(22), fill=(226, 232, 240), anchor='lm')
    y_curr += 125

d.rounded_rectangle([r_x1+30, card_y2-110, r_x2-30, card_y2-30], radius=12, fill=(159, 18, 57))
d.text(((r_x1 + r_x2) // 2, card_y2-70), "⚠️ 新手守則：切勿將整個桌面或 C:\\ 槽設為專案資料夾！", font=fb(24), fill=(255, 255, 255), anchor='mm')

img.save(os.path.join(pic_dir, 'ch1_workspace_boundary.png'), quality=95)
print("ch1_workspace_boundary.png done!")


# ==============================================================================
# 3. ch1_permission_modes.png (2000 x 950)
# ==============================================================================
print("3. Generating ch1_permission_modes.png...")
W, H = 2000, 950
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "Antigravity 權限管理模式對照圖", 
    "在中央對話輸入框的 Permissions 選單中隨時切換：「逐步審查」或「極速放行」")

card_y1, card_y2 = 170, 890

# Left: Request Review (Default)
l_x1, l_x2 = 70, 970
d.rounded_rectangle([l_x1, card_y1, l_x2, card_y2], radius=20, fill=(15, 30, 48), outline=(56, 189, 248), width=4)
d.rounded_rectangle([l_x1+25, card_y1+25, l_x2-25, card_y1+100], radius=14, fill=(2, 132, 199))
d.text(((l_x1 + l_x2) // 2, card_y1+62), "🛡️ 手動審查模式 (Default / Request Review)", font=fb(30), fill=(255, 255, 255), anchor='mm')

# Flow box
d.rounded_rectangle([l_x1+30, card_y1+130, l_x2-30, card_y1+270], radius=14, fill=(24, 45, 70), outline=(56, 189, 248), width=2)
d.text(((l_x1 + l_x2) // 2, card_y1+170), "【運作流程】", font=fb(24), fill=(125, 211, 252), anchor='mm')
d.text(((l_x1 + l_x2) // 2, card_y1+225), "提出需求 ➔ 彈出確認視窗 [Approve / Reject] ➔ 點擊後執行", font=fb(25), fill=(248, 250, 252), anchor='mm')

p_items_l = [
    ("📌 核心特徵", "AI 在執行任何系統命令前，必須等待你點擊「Approve」授權"),
    ("🎯 適合對象", "初學者、第一次接觸命令行、或正在處理公司正式生產專案"),
    ("💡 優缺點", "安全感 100%！但每動都需點擊同意，操作節奏較為緊湊"),
]
y_curr = card_y1 + 300
for title, desc in p_items_l:
    d.rounded_rectangle([l_x1+30, y_curr, l_x2-30, y_curr+105], radius=12, fill=(20, 38, 60), outline=(71, 85, 105), width=1)
    d.text((l_x1+55, y_curr+36), title, font=fb(26), fill=(56, 189, 248), anchor='lm')
    d.text((l_x1+55, y_curr+76), desc, font=fb(22), fill=(226, 232, 240), anchor='lm')
    y_curr += 125

d.rounded_rectangle([l_x1+30, card_y2-110, l_x2-30, card_y2-30], radius=12, fill=(3, 105, 161))
d.text(((l_x1 + l_x2) // 2, card_y2-70), "推薦：剛開始學習時維持此預設模式最安心！", font=fb(24), fill=(255, 255, 255), anchor='mm')


# Right: Always Proceed (Auto)
r_x1, r_x2 = 1030, 1930
d.rounded_rectangle([r_x1, card_y1, r_x2, card_y2], radius=20, fill=(45, 30, 15), outline=(245, 158, 11), width=4)
d.rounded_rectangle([r_x1+25, card_y1+25, r_x2-25, card_y1+100], radius=14, fill=(217, 119, 6))
d.text(((r_x1 + r_x2) // 2, card_y1+62), "⚡ 自動同意模式 (Always Proceed / Auto)", font=fb(30), fill=(255, 255, 255), anchor='mm')

# Flow box
d.rounded_rectangle([r_x1+30, card_y1+130, r_x2-30, card_y1+270], radius=14, fill=(70, 48, 22), outline=(245, 158, 11), width=2)
d.text(((r_x1 + r_x2) // 2, card_y1+170), "【運作流程】", font=fb(24), fill=(253, 230, 138), anchor='mm')
d.text(((r_x1 + r_x2) // 2, card_y1+225), "提出需求 ➔ AI 連續自主執行（建檔 + 改碼 + 終端機）➔ 直接完工", font=fb(25), fill=(248, 250, 252), anchor='mm')

p_items_r = [
    ("📌 核心特徵", "AI 連續執行讀取、寫檔、建檔與指令，完全不打斷使用者思考"),
    ("🎯 適合對象", "練習獨立網頁、原型快速開發、想體驗 Agentic 全自動流程"),
    ("💡 優缺點", "開發效率極高！但建議在乾淨的獨立練習專案資料夾中使用"),
]
y_curr = card_y1 + 300
for title, desc in p_items_r:
    d.rounded_rectangle([r_x1+30, y_curr, r_x2-30, y_curr+105], radius=12, fill=(60, 40, 20), outline=(71, 85, 105), width=1)
    d.text((r_x1+55, y_curr+36), title, font=fb(26), fill=(245, 158, 11), anchor='lm')
    d.text((r_x1+55, y_curr+76), desc, font=fb(22), fill=(226, 232, 240), anchor='lm')
    y_curr += 125

d.rounded_rectangle([r_x1+30, card_y2-110, r_x2-30, card_y2-30], radius=12, fill=(180, 83, 9))
d.text(((r_x1 + r_x2) // 2, card_y2-70), "本課程推薦：製作耳機網頁與發布時切換此模式最省時！", font=fb(24), fill=(255, 255, 255), anchor='mm')

img.save(os.path.join(pic_dir, 'ch1_permission_modes.png'), quality=95)
print("ch1_permission_modes.png done!")


# ==============================================================================
# 4. ch2_landing_page_anatomy.png (2000 x 1050)
# ==============================================================================
print("4. Generating ch2_landing_page_anatomy.png...")
W, H = 2000, 1050
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "商業產品介紹頁（Landing Page）5 大核心架構解剖", 
    "在向 AI 下達提示詞前，先掌握高轉換率網站的黃金五部曲結構")

# Browser frame
fx1, fy1, fx2, fy2 = 80, 160, 1920, 1000
d.rounded_rectangle([fx1, fy1, fx2, fy2], radius=18, fill=(15, 23, 42), outline=(71, 85, 105), width=3)
# Window bar
d.rounded_rectangle([fx1, fy1, fx2, fy1+50], radius=18, fill=(30, 41, 59))
d.rectangle([fx1, fy1+30, fx2, fy1+50], fill=(30, 41, 59))
for idx, col in enumerate([(239, 68, 68), (245, 158, 11), (16, 185, 129)]):
    d.ellipse([fx1+25+idx*24-6, fy1+25-6, fx1+25+idx*24+6, fy1+25+6], fill=col)
d.text(((fx1+fx2)//2, fy1+25), "https://yoursite.github.io/product-demo.html", font=fb(20), fill=(148, 163, 184), anchor='mm')

# 5 Big Horizontal Blocks
blocks = [
    ("① 頂部導覽列 (Navbar)", "SmartSound Pro 品牌 Logo ＋ 功能導覽連結 ＋ 【立即預購】快速行動按鈕", (99, 102, 241), (79, 70, 229)),
    ("② 主視覺區 (Hero Section)", "超吸睛主標題 ＋ 痛點副標 ＋ 耳機高畫質主圖 ＋ 【搶先預購】主要行動呼籲按鈕 (CTA)", (2, 132, 199), (3, 105, 161)),
    ("③ 核心賣點 (Features 3 大特色)", "【🎧 頂級主動降噪】 ｜ 【🔋 40小時超長續航】 ｜ 【☁️ 人體工學極致舒適耳罩】", (16, 185, 129), (5, 150, 105)),
    ("④ 多角度圖鑑與定價 (Gallery & Pricing)", "多維度照片展示（正面/側面/情境） ＋ 【標準版 $3,990】 與 【旗艦版 $5,990】 方案比較表", (245, 158, 11), (217, 119, 6)),
    ("⑤ 預購表單與頁尾 (Form & Footer)", "姓名/Email/電話線上表單輸入框 ＋ 隱私政策 ＋ 版權聲明與社群連結", (100, 116, 139), (71, 85, 105)),
]

by = fy1 + 75
for title, desc, bg_title, bg_card in blocks:
    d.rounded_rectangle([fx1+30, by, fx2-30, by+135], radius=14, fill=(24, 32, 48), outline=bg_title, width=2)
    # Title badge
    d.rounded_rectangle([fx1+50, by+15, fx1+460, by+65], radius=8, fill=bg_title)
    d.text((fx1+255, by+40), title, font=fb(24), fill=(255, 255, 255), anchor='mm')
    # Content
    d.text((fx1+60, by+98), desc, font=fb(25), fill=(248, 250, 252), anchor='lm')
    by += 155

img.save(os.path.join(pic_dir, 'ch2_landing_page_anatomy.png'), quality=95)
print("ch2_landing_page_anatomy.png done!")


# ==============================================================================
# 5. ch2_interview_flow.png (2000 x 900)
# ==============================================================================
print("5. Generating ch2_interview_flow.png...")
W, H = 2000, 900
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "「先問答、後動工」反向訪談法三部曲", 
    "提示詞不用一次想破頭！請 AI 當顧問反向提問，像做選擇題一樣輕鬆敲定需求")

# 3 Horizontal Step Cards
step_w = 560
step_y1, step_y2 = 170, 830

steps = [
    (70, "步驟 1：啟動反向訪談", "叫 AI 先別急著寫程式！", 
     (99, 102, 241), (25, 30, 52),
     "💬 你輸入的開場白提示詞：\n\n「我想做耳機銷售網頁，請先不要寫程式！請扮演顧問，向我提出 4 個關鍵問題（附選項）。」\n\n⚡ 快捷鍵：直接輸入 /grill-me 指令"),

    (720, "步驟 2：像做選擇題回答", "快速挑選滿意選項", 
     (2, 132, 199), (18, 38, 62),
     "🤖 AI 逐一列出問題讓你選：\n\n1. 配色：(A)曜石黑 (B)純白 (C)霓虹？\n2. 賣點：降噪、續航、人體工學？\n3. 方案：標準版 vs 旗艦版？\n\n👤 你只需回覆：1選A、2強調降噪、3分兩版"),

    (1370, "步驟 3：精準生成成果", "100% 貼合心中想像", 
     (16, 185, 129), (16, 42, 34),
     "🎉 AI 彙整規格後一鍵動工：\n\n• 自動建立完整結構 index.html\n• 精準套用 PIC 資料夾耳機照片\n• 一次到位！完全不偏離預期規格\n• 省下 80% 來回除錯重做的時間！"),
]

for sx, title, subtitle, col_main, col_bg, body in steps:
    d.rounded_rectangle([sx, step_y1, sx+step_w, step_y2], radius=18, fill=col_bg, outline=col_main, width=4)
    # Header badge
    d.rounded_rectangle([sx+20, step_y1+25, sx+step_w-20, step_y1+95], radius=12, fill=col_main)
    d.text((sx+step_w//2, step_y1+60), title, font=fb(28), fill=(255, 255, 255), anchor='mm')
    d.text((sx+step_w//2, step_y1+125), subtitle, font=fb(22), fill=(203, 213, 225), anchor='mm')
    
    # Body
    d.rounded_rectangle([sx+20, step_y1+160, sx+step_w-20, step_y2-25], radius=14, fill=(15, 23, 42), outline=(71, 85, 105), width=2)
    
    lines = body.split('\n')
    ly = step_y1 + 195
    for line in lines:
        if line.startswith("💬") or line.startswith("🤖") or line.startswith("🎉"):
            d.text((sx+40, ly), line, font=fb(24), fill=col_main, anchor='lm')
            ly += 38
        elif line.startswith("⚡"):
            d.text((sx+40, ly), line, font=fb(22), fill=(245, 158, 11), anchor='lm')
            ly += 34
        elif line == "":
            ly += 14
        else:
            d.text((sx+40, ly), line, font=fb(22), fill=(241, 245, 249), anchor='lm')
            ly += 34

# Connecting arrows between steps
d.text((675, 480), "➔", font=fb(52), fill=(148, 163, 184), anchor='mm')
d.text((1325, 480), "➔", font=fb(52), fill=(148, 163, 184), anchor='mm')

img.save(os.path.join(pic_dir, 'ch2_interview_flow.png'), quality=95)
print("ch2_interview_flow.png done!")


# ==============================================================================
# 6. ch2_iterative_tuning.png (2000 x 900)
# ==============================================================================
print("6. Generating ch2_iterative_tuning.png...")
W, H = 2000, 900
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img)

draw_header(d, W, 
    "對話式迭代微調（Iterative Tuning）進化路徑", 
    "生成第一版後不用自己改程式！動口說一句，AI 自動精準進行增量修復")

# 3 Big Columns: V1 -> Prompt Command -> V2 Perfect
col_w = 560
col_y1, col_y2 = 170, 830

# Col 1: V1 Prototype
c1_x = 70
d.rounded_rectangle([c1_x, col_y1, c1_x+col_w, col_y2], radius=18, fill=(30, 41, 59), outline=(100, 116, 139), width=3)
d.rounded_rectangle([c1_x+20, col_y1+25, c1_x+col_w-20, col_y1+95], radius=12, fill=(71, 85, 105))
d.text((c1_x+col_w//2, col_y1+60), "階段 1：初版網頁 (V1 原型)", font=fb(26), fill=(255, 255, 255), anchor='mm')

v1_items = [
    ("基本架構完成", "已包含標題、耳機圖與預購按鈕"),
    ("待加強細節", "Hero 標題不夠突出、按鈕顏色太暗"),
    ("功能尚未齊全", "缺少顧客好評推薦與多視角耳機圖"),
    ("狀態評估", "骨架正確，但缺乏商業轉單視覺張力"),
]
vy = col_y1 + 130
for t, dsc in v1_items:
    d.rounded_rectangle([c1_x+25, vy, c1_x+col_w-25, vy+110], radius=12, fill=(15, 23, 42), outline=(71, 85, 105), width=1)
    d.text((c1_x+45, vy+36), t, font=fb(24), fill=(203, 213, 225), anchor='lm')
    d.text((c1_x+45, vy+76), dsc, font=fb(22), fill=(148, 163, 184), anchor='lm')
    vy += 135

# Col 2: Tuning Prompts
c2_x = 720
d.rounded_rectangle([c2_x, col_y1, c2_x+col_w, col_y2], radius=18, fill=(45, 35, 15), outline=(245, 158, 11), width=4)
d.rounded_rectangle([c2_x+20, col_y1+25, c2_x+col_w-20, col_y1+95], radius=12, fill=(217, 119, 6))
d.text((c2_x+col_w//2, col_y1+60), "階段 2：對話微調 (自然語言指令)", font=fb(26), fill=(255, 255, 255), anchor='mm')

prompts_tuning = [
    ("💬 微調 1：視覺強化", "「請把 Hero 標題字體加大，並把按鈕改成亮橘色漸層按鈕！」"),
    ("💬 微調 2：擴充區塊", "「請在產品特色後面加上 3 位顧客的五星好評推薦卡片！」"),
    ("💬 微調 3：互動體驗", "「點擊預購按鈕時平滑捲動到表單，送出後跳出感謝訊息！」"),
]
py = col_y1 + 130
for t, dsc in prompts_tuning:
    d.rounded_rectangle([c2_x+25, py, c2_x+col_w-25, py+150], radius=12, fill=(24, 30, 44), outline=(245, 158, 11), width=2)
    d.text((c2_x+45, py+38), t, font=fb(24), fill=(245, 158, 11), anchor='lm')
    d.text((c2_x+45, py+88), dsc[:18], font=fb(22), fill=(248, 250, 252), anchor='lm')
    d.text((c2_x+45, py+120), dsc[18:], font=fb(22), fill=(248, 250, 252), anchor='lm')
    py += 175

# Col 3: V2 Final
c3_x = 1370
d.rounded_rectangle([c3_x, col_y1, c3_x+col_w, col_y2], radius=18, fill=(16, 42, 34), outline=(16, 185, 129), width=4)
d.rounded_rectangle([c3_x+20, col_y1+25, c3_x+col_w-20, col_y1+95], radius=12, fill=(16, 185, 129))
d.text((c3_x+col_w//2, col_y1+60), "階段 3：最終成品 (V2 商業旗艦版)", font=fb(26), fill=(255, 255, 255), anchor='mm')

v2_items = [
    ("✨ 視覺層次豐富", "亮橘色發光 CTA 按鈕 ＋ 大器科技感標題"),
    ("✨ 完整顧客信任感", "五星好評評價卡片 ＋ 雙版本價格方案比較表"),
    ("✨ 流暢互動回饋", "平滑錨點捲動 ＋ 表單填寫即時驗證視窗"),
    ("✨ 自適應完美呈現", "電腦大螢幕與手機窄螢幕（RWD）皆流暢無比"),
]
vy = col_y1 + 130
for t, dsc in v2_items:
    d.rounded_rectangle([c3_x+25, vy, c3_x+col_w-25, vy+110], radius=12, fill=(15, 23, 42), outline=(16, 185, 129), width=1)
    d.text((c3_x+45, vy+36), t, font=fb(24), fill=(52, 211, 153), anchor='lm')
    d.text((c3_x+45, vy+76), dsc, font=fb(22), fill=(248, 250, 252), anchor='lm')
    vy += 135

# Connecting arrows
d.text((675, 480), "➔", font=fb(52), fill=(245, 158, 11), anchor='mm')
d.text((1325, 480), "➔", font=fb(52), fill=(16, 185, 129), anchor='mm')

img.save(os.path.join(pic_dir, 'ch2_iterative_tuning.png'), quality=95)
print("ch2_iterative_tuning.png done!")

print("ALL 6 INFOGRAPHIC DIAGRAMS GENERATED SUCCESSFULLY!")
