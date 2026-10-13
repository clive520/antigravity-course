import os
from PIL import Image, ImageDraw, ImageFont

font_bold_path = r'C:\Windows\Fonts\msjhbd.ttc'
font_reg_path = r'C:\Windows\Fonts\msjh.ttc'

def f_bold(sz): return ImageFont.truetype(font_bold_path, sz)
def f_reg(sz): return ImageFont.truetype(font_reg_path, sz)

pic_dir = r'c:\Antigravity\Antigravity教學\PIC'

def draw_folder_icon(d, x, y, w=28, h=22, col=(129, 140, 248)):
    d.rounded_rectangle([x, y+4, x+w, y+h], radius=3, fill=col)
    d.polygon([(x, y+4), (x+w*0.4, y+4), (x+w*0.5, y), (x, y)], fill=col)

def draw_mic_icon(d, cx, cy, col=(15, 23, 42)):
    d.rounded_rectangle([cx-6, cy-14, cx+6, cy+4], radius=6, fill=col)
    d.arc([cx-12, cy-9, cx+12, cy+9], start=0, end=180, fill=col, width=3)
    d.line([cx, cy+9, cx, cy+15], fill=col, width=3)
    d.line([cx-8, cy+15, cx+8, cy+15], fill=col, width=3)

# ==============================================================================
# DIAGRAM 1: ch1_ide_layout.png (Antigravity 2.0 Layout - 2200x1260)
# ==============================================================================
print("Generating ch1_ide_layout.png...")
W, H = 2200, 1260
img = Image.new('RGB', (W, H), (10, 14, 23))
d = ImageDraw.Draw(img, 'RGBA')

# Title
d.text((W//2, 50), 'Google Antigravity 2.0 新版介面三大核心區塊導覽', font=f_bold(44), fill=(248, 250, 252), anchor='mm')
d.text((W//2, 105), '全新「AI 代理指揮中心（Agent Command Center）」：對話主畫布直接位於畫面正中央', font=f_reg(26), fill=(148, 163, 184), anchor='mm')

# Main Frame
wx1, wy1, wx2, wy2 = 70, 150, W-70, 1040
d.rounded_rectangle([wx1-3, wy1-3, wx2+3, wy2+3], radius=24, fill=(30, 41, 59), outline=(71, 85, 105), width=3)
d.rounded_rectangle([wx1, wy1, wx2, wy2], radius=22, fill=(17, 22, 34))

# Window Bar
d.rounded_rectangle([wx1, wy1, wx2, wy1+60], radius=22, fill=(24, 30, 44))
d.rectangle([wx1, wy1+35, wx2, wy1+60], fill=(24, 30, 44))
for idx, col in enumerate([(239, 68, 68), (245, 158, 11), (16, 185, 129)]):
    cx = wx1 + 35 + idx * 28
    cy = wy1 + 30
    d.ellipse([cx-8, cy-8, cx+8, cy+8], fill=col)
d.text((W//2, wy1+30), 'Google Antigravity 2.0 桌面應用程式', font=f_bold(20), fill=(148, 163, 184), anchor='mm')

# Zone 1: Left Sidebar (x: 70 -> 480)
z1_x1, z1_y1, z1_x2, z1_y2 = wx1, wy1+60, 500, wy2
d.rectangle([z1_x1, z1_y1, z1_x2, z1_y2], fill=(21, 27, 40))
d.line([z1_x2, z1_y1, z1_x2, z1_y2], fill=(51, 65, 85), width=3)
d.rounded_rectangle([z1_x1+10, z1_y1+10, z1_x2-10, z1_y2-10], radius=16, outline=(129, 140, 248, 220), width=3)

# Zone 1 Header Badge
d.rounded_rectangle([z1_x1+25, z1_y1+20, z1_x1+210, z1_y1+60], radius=10, fill=(99, 102, 241))
d.text((z1_x1+117, z1_y1+40), '① 左側功能導覽欄', font=f_bold(20), fill=(255, 255, 255), anchor='mm')

# New Chat button
d.rounded_rectangle([z1_x1+25, z1_y1+78, z1_x2-25, z1_y1+136], radius=12, fill=(79, 70, 229), outline=(165, 180, 252), width=2)
d.text((z1_x1+45, z1_y1+107), '＋ New Conversation (新對話)', font=f_bold(20), fill=(255, 255, 255), anchor='lm')

# Projects
d.text((z1_x1+28, z1_y1+170), 'PROJECTS（專案管理）', font=f_bold(18), fill=(165, 180, 252), anchor='lm')
d.rounded_rectangle([z1_x2-155, z1_y1+152, z1_x2-25, z1_y1+192], radius=8, fill=(30, 58, 138), outline=(56, 189, 248), width=2)
draw_folder_icon(d, z1_x2-145, z1_y1+160, w=22, h=18, col=(56, 189, 248))
d.text((z1_x2-72, z1_y1+172), '+ 新增專案', font=f_bold(17), fill=(125, 211, 252), anchor='mm')

# Active project
d.rounded_rectangle([z1_x1+25, z1_y1+205, z1_x2-25, z1_y1+305], radius=12, fill=(30, 41, 59), outline=(99, 102, 241), width=2)
draw_folder_icon(d, z1_x1+40, z1_y1+225, w=26, h=20, col=(129, 140, 248))
d.text((z1_x1+76, z1_y1+235), 'SmartSound-Web (作用中)', font=f_bold(19), fill=(248, 250, 252), anchor='lm')
d.text((z1_x1+50, z1_y1+275), '└ 綁定 c:\\Antigravity\\web-demo', font=f_bold(17), fill=(148, 163, 184), anchor='lm')

# Nav Menu items
sb_items = [
    ('●  Scheduled Tasks', '排程背景自動化任務', z1_y1+330),
    ('◆  Skills & Customizations', '外掛技能、規則與 MCP', z1_y1+410),
    ('＞_ Integrated Terminal', '內建終端機 (Ctrl + `)', z1_y1+490),
    ('■  VCS (版本控制面板)', '檢視變更檔案、Commit/Push', z1_y1+570),
    ('★  Settings (權限與設定)', 'Default / Full machine 權限', z1_y1+650),
]
for title, sub, ypos in sb_items:
    d.rounded_rectangle([z1_x1+25, ypos, z1_x2-25, ypos+68], radius=10, fill=(26, 33, 48), outline=(51, 65, 85))
    d.text((z1_x1+42, ypos+23), title, font=f_bold(19), fill=(226, 232, 240), anchor='lm')
    d.text((z1_x1+68, ypos+50), sub, font=f_reg(16), fill=(148, 163, 184), anchor='lm')

# Zone 2: Center Chat Canvas (x: 500 -> 1620)
z2_x1, z2_y1, z2_x2, z2_y2 = 500, wy1+60, 1620, wy2
d.rectangle([z2_x1, z2_y1, z2_x2, z2_y2], fill=(15, 19, 29))
d.rounded_rectangle([z2_x1+10, z2_y1+10, z2_x2-10, z2_y2-10], radius=16, outline=(56, 189, 248, 230), width=3)

# Zone 2 Header Badge
d.rounded_rectangle([z2_x1+30, z2_y1+20, z2_x1+345, z2_y1+60], radius=10, fill=(2, 132, 199))
d.text((z2_x1+187, z2_y1+40), '② 正中央：對話主畫布 (Chat Canvas)', font=f_bold(20), fill=(255, 255, 255), anchor='mm')

c_mid = (z2_x1 + z2_x2) // 2
d.text((c_mid, z2_y1+150), 'What would you like to build today?', font=f_bold(38), fill=(241, 245, 249), anchor='mm')
d.text((c_mid, z2_y1+205), '新版對話框直接位於整個視窗正中央！在此輸入日常中文即可指揮 AI', font=f_bold(22), fill=(148, 163, 184), anchor='mm')

# Project Pill
px1, py1 = z2_x1 + 80, z2_y1 + 265
d.rounded_rectangle([px1, py1, px1+300, py1+48], radius=10, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
draw_folder_icon(d, px1+18, py1+12, w=24, h=20, col=(56, 189, 248))
d.text((px1+55, py1+24), 'SmartSound-Web  ▼', font=f_bold(19), fill=(248, 250, 252), anchor='lm')
d.text((px1+320, py1+24), '← 確認上方目前綁定的專案 (Project)', font=f_bold(19), fill=(56, 189, 248), anchor='lm')

# Main Prompt Box
bx1, by1, bx2, by2 = z2_x1 + 80, z2_y1 + 330, z2_x2 - 80, z2_y1 + 600
d.rounded_rectangle([bx1-3, by1-3, bx2+3, by2+3], radius=24, fill=(30, 41, 59), outline=(56, 189, 248), width=3)
d.rounded_rectangle([bx1, by1, bx2, by2-65], radius=22, fill=(26, 34, 52))

d.text((bx1+32, by1+45), 'Ask anything, @ to mention, / for actions', font=f_reg(23), fill=(148, 163, 184), anchor='lm')
d.text((bx1+32, by1+95), '★ 在這裡輸入提示詞（例如：「請幫我建立一個具備深色科技感的產品首頁...」）', font=f_bold(21), fill=(125, 211, 252), anchor='lm')

# Input bar inside box
cy = by2 - 105
d.ellipse([bx1+28, cy-22, bx1+72, cy+22], fill=(39, 50, 72), outline=(100, 116, 139), width=2)
d.text((bx1+50, cy), '＋', font=f_bold(24), fill=(226, 232, 240), anchor='mm')

d.rounded_rectangle([bx1+88, cy-22, bx1+320, cy+22], radius=10, fill=(39, 50, 72))
d.text((bx1+204, cy), '★ Gemini 3.5 Flash ▼', font=f_bold(18), fill=(226, 232, 240), anchor='mm')

d.rounded_rectangle([bx1+335, cy-22, bx1+605, cy+22], radius=10, fill=(39, 50, 72), outline=(245, 158, 11), width=2)
d.text((bx1+470, cy), 'Permissions: Default ▼', font=f_bold(18), fill=(253, 224, 71), anchor='mm')

# Mic Button
mcx = bx2 - 50
d.ellipse([mcx-25, cy-25, mcx+25, cy+25], fill=(56, 189, 248))
draw_mic_icon(d, mcx, cy, col=(15, 23, 42))

# Bottom tray of input box
d.rounded_rectangle([bx1, by2-65, bx2, by2], radius=22, fill=(20, 26, 39))
d.rectangle([bx1, by2-65, bx2, by2-40], fill=(20, 26, 39))
d.line([bx1, by2-65, bx2, by2-65], fill=(51, 65, 85), width=2)
d.text((bx1+30, by2-32), '● Local ▼', font=f_bold(19), fill=(167, 243, 208), anchor='lm')
d.text((bx1+150, by2-32), '（Local 本機模式：AI 直接在你的專案資料夾內建立與修改網頁）', font=f_bold(18), fill=(148, 163, 184), anchor='lm')

# Chips below input box
chips = [
    ('＋ 附加檔案/資料夾/.zip', bx1+120),
    ('@ 引用專案特定檔案', bx1+380),
    ('/ 呼叫內建技能指令', bx1+620),
    ('語音輸入 (Ctrl+M)', bx1+840),
]
for txt, cx_c in chips:
    d.rounded_rectangle([cx_c-105, by2+25, cx_c+105, by2+70], radius=20, fill=(24, 33, 50), outline=(71, 85, 105), width=2)
    d.text((cx_c, by2+47), txt, font=f_bold(17), fill=(203, 213, 225), anchor='mm')

# Zone 3: Right Auxiliary Pane (x: 1620 -> 2130)
z3_x1, z3_y1, z3_x2, z3_y2 = 1620, wy1+60, wx2, wy2
d.rectangle([z3_x1, z3_y1, z3_x2, z3_y2], fill=(21, 27, 40))
d.line([z3_x1, z3_y1, z3_x1, z3_y2], fill=(51, 65, 85), width=3)
d.rounded_rectangle([z3_x1+10, z3_y1+10, z3_x2-10, z3_y2-10], radius=16, outline=(16, 185, 129, 230), width=3)

d.rounded_rectangle([z3_x1+25, z3_y1+20, z3_x1+330, z3_y1+60], radius=10, fill=(5, 150, 105))
d.text((z3_x1+177, z3_y1+40), '③ 右側輔助面板 (Auxiliary Pane)', font=f_bold(20), fill=(255, 255, 255), anchor='mm')
d.text((z3_x1+28, z3_y1+85), '任務執行時按需展開，免看滿螢幕程式碼', font=f_bold(17), fill=(148, 163, 184), anchor='lm')

# Aux Cards
d.rounded_rectangle([z3_x1+25, z3_y1+120, z3_x2-25, z3_y1+300], radius=12, fill=(28, 37, 54), outline=(52, 211, 153), width=2)
d.text((z3_x1+42, z3_y1+152), '■ Artifacts（產出物與計畫書）', font=f_bold(20), fill=(167, 243, 208), anchor='lm')
d.text((z3_x1+42, z3_y1+192), '• implementation_plan.md 實作計畫', font=f_reg(18), fill=(226, 232, 240), anchor='lm')
d.text((z3_x1+42, z3_y1+228), '• 生成圖片預覽與全螢幕檢視', font=f_reg(18), fill=(226, 232, 240), anchor='lm')
d.text((z3_x1+42, z3_y1+264), '• 點擊可直接在右側留言回饋給 AI', font=f_bold(17), fill=(148, 163, 184), anchor='lm')

d.rounded_rectangle([z3_x1+25, z3_y1+320, z3_x2-25, z3_y1+500], radius=12, fill=(28, 37, 54), outline=(71, 85, 105), width=2)
d.text((z3_x1+42, z3_y1+352), '■ Files Changed（檔案變更審查）', font=f_bold(20), fill=(248, 250, 252), anchor='lm')
d.text((z3_x1+42, z3_y1+392), '+ index.html   (新增產品介紹首頁)', font=f_bold(18), fill=(74, 222, 128), anchor='lm')
d.text((z3_x1+42, z3_y1+428), '+ css/style.css (新增深色主題樣式)', font=f_bold(18), fill=(74, 222, 128), anchor='lm')
d.text((z3_x1+42, z3_y1+464), '• 支援一鍵 Commit 並 Push 到 GitHub', font=f_bold(17), fill=(148, 163, 184), anchor='lm')

d.rounded_rectangle([z3_x1+25, z3_y1+520, z3_x2-25, z3_y1+680], radius=12, fill=(28, 37, 54), outline=(71, 85, 105), width=2)
d.text((z3_x1+42, z3_y1+552), '■ Subagents & Background Tasks', font=f_bold(20), fill=(248, 250, 252), anchor='lm')
d.text((z3_x1+42, z3_y1+592), '• 監控子代理與系統背景指令進度', font=f_reg(18), fill=(226, 232, 240), anchor='lm')
d.text((z3_x1+42, z3_y1+632), '• 支援瀏覽器自動化 (/browser) 錄影', font=f_reg(18), fill=(226, 232, 240), anchor='lm')

# Bottom 3 Callout Cards
leg_y1, leg_y2 = 1060, 1230
cards = [
    (70, 720, (129, 140, 248), '① 左側功能導覽欄 (Left Sidebar)',
     '點選「📁+ 新增專案 (New Project)」綁定你的本機資料夾；',
     '也可在此查看排程任務、外掛技能 (Skills) 與安全權限設定。'),
    (750, 1450, (56, 189, 248), '② 中央對話主畫布 (Chat Canvas)',
     '新版對話框就在畫面正中央！確認上方專案名稱後，',
     '直接在中央輸入框打字、上傳照片或按麥克風語音下達指令。'),
    (1480, W-70, (52, 211, 153), '③ 右側輔助面板 (Auxiliary Pane)',
     '執行任務時按需展開，檢視 AI 寫好的計畫書 (Artifacts)、',
     '審查修改了哪些檔案 (VCS Diff) 與內建終端機運行狀態。'),
]
for x1, x2, col, title, l1, l2 in cards:
    d.rounded_rectangle([x1, leg_y1, x2, leg_y2], radius=16, fill=(21, 28, 42), outline=col, width=3)
    d.text((x1+24, leg_y1+38), title, font=f_bold(22), fill=col, anchor='lm')
    d.text((x1+24, leg_y1+82), l1, font=f_bold(18), fill=(226, 232, 240), anchor='lm')
    d.text((x1+24, leg_y1+118), l2, font=f_bold(18), fill=(226, 232, 240), anchor='lm')

img.save(os.path.join(pic_dir, 'ch1_ide_layout.png'), 'PNG')
print("ch1_ide_layout.png saved!")

# ==============================================================================
# DIAGRAM 2: ch1_workspace_boundary.png (Safe Boundary - 2200x1200)
# ==============================================================================
print("Generating ch1_workspace_boundary.png...")
W2, H2 = 2200, 1200
img2 = Image.new('RGB', (W2, H2), (10, 14, 23))
d2 = ImageDraw.Draw(img2, 'RGBA')

d2.text((W2//2, 55), '專案工作區（Project Workspace）安全邊界原理', font=f_bold(44), fill=(248, 250, 252), anchor='mm')
d2.text((W2//2, 115), '為什麼要指定獨立資料夾？理解 Antigravity 的安全防護罩與電腦隱私保護機制', font=f_reg(26), fill=(148, 163, 184), anchor='mm')

# Left Box: Safe Zone (x: 80 -> 1100, y: 170 -> 1060)
z_safe_x1, z_safe_y1, z_safe_x2, z_safe_y2 = 80, 170, 1100, 1060
d2.rounded_rectangle([z_safe_x1-4, z_safe_y1-4, z_safe_x2+4, z_safe_y2+4], radius=24, fill=(16, 185, 129, 40), outline=(16, 185, 129), width=4)
d2.rounded_rectangle([z_safe_x1, z_safe_y1, z_safe_x2, z_safe_y2], radius=22, fill=(16, 32, 36))

d2.rounded_rectangle([z_safe_x1+30, z_safe_y1+30, z_safe_x1+420, z_safe_y1+85], radius=12, fill=(16, 185, 129))
d2.text((z_safe_x1+225, z_safe_y1+57), '🛡️ 安全授權區 (Active Project)', font=f_bold(24), fill=(15, 23, 42), anchor='mm')
d2.text((z_safe_x1+35, z_safe_y1+125), '目標資料夾：c:\\Antigravity\\web-demo', font=f_bold(24), fill=(167, 243, 208), anchor='lm')
d2.text((z_safe_x1+35, z_safe_y1+165), 'AI 獲准在此專屬安全邊界內執行所有開發動作：', font=f_reg(20), fill=(203, 213, 225), anchor='lm')

safe_tasks = [
    ('✓ 讀取專案架構：', '檢視 HTML、CSS、JS 與 PIC 圖片素材', (52, 211, 153)),
    ('✓ 撰寫與建立檔案：', '自動生成 index.html、樣式表與設定檔', (52, 211, 153)),
    ('✓ 執行開發指令：', '在專案目錄執行 git、npm、測試伺服器', (52, 211, 153)),
    ('✓ 圖片素材運用：', '自動把 PIC/ 內商品圖排版放入網頁中', (52, 211, 153)),
]
for idx, (t1, t2, col) in enumerate(safe_tasks):
    box_y = z_safe_y1 + 215 + idx * 115
    d2.rounded_rectangle([z_safe_x1+30, box_y, z_safe_x2-30, box_y+95], radius=14, fill=(20, 48, 52), outline=(52, 211, 153), width=2)
    d2.text((z_safe_x1+55, box_y+32), t1, font=f_bold(22), fill=col, anchor='lm')
    d2.text((z_safe_x1+55, box_y+66), t2, font=f_bold(20), fill=(241, 245, 249), anchor='lm')

d2.rounded_rectangle([z_safe_x1+30, z_safe_y2-150, z_safe_x2-30, z_safe_y2-30], radius=14, fill=(13, 148, 136, 60), outline=(20, 184, 166), width=2)
d2.text((z_safe_x1+55, z_safe_y2-105), '★ 結論：AI 擁有滿滿生產力，但活動範圍被嚴格限制在專案內！', font=f_bold(22), fill=(153, 246, 228), anchor='lm')
d2.text((z_safe_x1+55, z_safe_y2-65), '完全不會誤觸或更動到你電腦其他資料夾的任何檔案。', font=f_reg(20), fill=(204, 251, 241), anchor='lm')

# Center Arrow / Wall
c_wall_x = 1150
d2.line([c_wall_x, 220, c_wall_x, 1000], fill=(239, 68, 68), width=5)
for y_stop in [360, 560, 760]:
    d2.ellipse([c_wall_x-35, y_stop-35, c_wall_x+35, y_stop+35], fill=(220, 38, 38), outline=(254, 202, 202), width=3)
    d2.text((c_wall_x, y_stop), '✕', font=f_bold(36), fill=(255, 255, 255), anchor='mm')
    d2.text((c_wall_x, y_stop+55), '嚴格阻擋', font=f_bold(18), fill=(252, 165, 165), anchor='mm')

# Right Box: Restricted Zone (x: 1200 -> 2120, y: 170 -> 1060)
z_res_x1, z_res_y1, z_res_x2, z_res_y2 = 1200, 170, 2120, 1060
d2.rounded_rectangle([z_res_x1-4, z_res_y1-4, z_res_x2+4, z_res_y2+4], radius=24, fill=(239, 68, 68, 40), outline=(239, 68, 68), width=4)
d2.rounded_rectangle([z_res_x1, z_res_y1, z_res_x2, z_res_y2], radius=22, fill=(36, 20, 26))

d2.rounded_rectangle([z_res_x1+30, z_res_y1+30, z_res_x1+440, z_res_y1+85], radius=12, fill=(220, 38, 38))
d2.text((z_res_x1+235, z_res_y1+57), '⛔ 嚴禁存取區 (電腦私人資料)', font=f_bold(24), fill=(255, 255, 255), anchor='mm')
d2.text((z_res_x1+35, z_res_y1+125), '專案資料夾以外的整部電腦目錄：', font=f_bold(24), fill=(254, 202, 202), anchor='lm')
d2.text((z_res_x1+35, z_res_y1+165), 'AI 代理完全無法主動擅自讀取或修改以下區域：', font=f_reg(20), fill=(226, 232, 240), anchor='lm')

res_items = [
    ('✕ 電腦桌面與個人文件：', 'C:\\Users\\...\\Desktop (桌面上的私人筆記、工作合約)', (248, 113, 113)),
    ('✕ C 槽系統根目錄：', 'C:\\Windows, Program Files 等作業系統核心檔案', (248, 113, 113)),
    ('✕ 私人相簿與生活照片：', '家庭旅遊照片、證件翻拍圖檔，完全隱密安全', (248, 113, 113)),
    ('✕ 其他硬碟槽與機密檔：', 'D:\\, E:\\ 等個人隨身碟與公司私有資料夾', (248, 113, 113)),
]
for idx, (t1, t2, col) in enumerate(res_items):
    box_y = z_res_y1 + 215 + idx * 115
    d2.rounded_rectangle([z_res_x1+30, box_y, z_res_x2-30, box_y+95], radius=14, fill=(50, 24, 32), outline=(239, 68, 68), width=2)
    d2.text((z_res_x1+55, box_y+32), t1, font=f_bold(22), fill=col, anchor='lm')
    d2.text((z_res_x1+55, box_y+66), t2, font=f_bold(20), fill=(241, 245, 249), anchor='lm')

d2.rounded_rectangle([z_res_x1+30, z_res_y2-150, z_res_x2-30, z_res_y2-30], radius=14, fill=(153, 27, 27, 60), outline=(239, 68, 68), width=2)
d2.text((z_res_x1+55, z_res_y2-105), '🚨 初學者安全守則：永遠不要把桌面或 C 槽設為 Workspace！', font=f_bold(22), fill=(254, 202, 202), anchor='lm')
d2.text((z_res_x1+55, z_res_y2-65), '建立獨立資料夾（如 c:\\Antigravity\\web-demo）才是最安心的做法。', font=f_reg(20), fill=(254, 226, 226), anchor='lm')

# Bottom Summary banner
d2.rounded_rectangle([80, 1080, W2-80, 1160], radius=16, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
d2.text((W2//2, 1120), '💡 總結：給 AI 一個獨立房間（Project Folder），它在裡面幫你把網站蓋到好，而客廳與主臥室永遠不被打擾！', font=f_bold(24), fill=(253, 224, 71), anchor='mm')

img2.save(os.path.join(pic_dir, 'ch1_workspace_boundary.png'), 'PNG')
print("ch1_workspace_boundary.png saved!")

# ==============================================================================
# DIAGRAM 3: ch1_permission_modes.png (Permission Modes - 2200x1200)
# ==============================================================================
print("Generating ch1_permission_modes.png...")
W3, H3 = 2200, 1200
img3 = Image.new('RGB', (W3, H3), (10, 14, 23))
d3 = ImageDraw.Draw(img3, 'RGBA')

d3.text((W3//2, 55), 'Antigravity 2.0 兩大權限模式運作對照圖', font=f_bold(44), fill=(248, 250, 252), anchor='mm')
d3.text((W3//2, 115), '「手動審查（Default）」與「自動同意（Auto-Approve）」的實際執行體驗對照', font=f_reg(26), fill=(148, 163, 184), anchor='mm')

# Left Column: Default Manual Review (x: 80 -> 1070)
d3.rounded_rectangle([80, 170, 1070, 1120], radius=24, fill=(18, 34, 38), outline=(16, 185, 129), width=3)
d3.rounded_rectangle([80, 170, 1070, 260], radius=24, fill=(6, 78, 59))
d3.rectangle([80, 220, 1070, 260], fill=(6, 78, 59))
d3.text((575, 215), '🛡️ 預設安全審查模式（Default / Request Review）', font=f_bold(28), fill=(255, 255, 255), anchor='mm')

# Flow in Left
l_cards = [
    ('步驟 1：你下達開發指令', '「請幫我安裝套件並發布網站到 GitHub」', (241, 245, 249)),
    ('步驟 2：AI 準備執行系統指令', '即將執行：gh repo create smartsound --public', (253, 224, 71)),
    ('步驟 3：彈出確認彈窗（審查關卡）', '畫面跳出 [ Approve（同意）] 或 [ Reject（拒絕）] 按鈕', (110, 231, 183)),
    ('步驟 4：你親自點擊 Approve', '確認指令無危害後按同意，AI 才會真正執行該條指令', (167, 243, 208)),
]
for idx, (t1, t2, col) in enumerate(l_cards):
    cy = 295 + idx * 135
    d3.rounded_rectangle([115, cy, 1035, cy+105], radius=14, fill=(24, 46, 52), outline=(16, 185, 129), width=2)
    d3.text((145, cy+35), t1, font=f_bold(24), fill=col, anchor='lm')
    d3.text((145, cy+72), t2, font=f_reg(20), fill=(226, 232, 240), anchor='lm')
    if idx < 3:
        d3.text((575, cy+120), '↓', font=f_bold(28), fill=(16, 185, 129), anchor='mm')

# Left Summary
d3.rounded_rectangle([115, 875, 1035, 1090], radius=14, fill=(15, 23, 42), outline=(52, 211, 153), width=2)
d3.text((145, 915), '【適合對象】：初學者、重要工作環境、含有機密檔案的電腦', font=f_bold(22), fill=(167, 243, 208), anchor='lm')
d3.text((145, 960), '• 優點：最高安全性，每一條終端機指令你都看得一清二楚。', font=f_reg(20), fill=(226, 232, 240), anchor='lm')
d3.text((145, 1005), '• 特色：AI 絕不擅自執行任何系統命令，完全由你掌握控制權。', font=f_reg(20), fill=(226, 232, 240), anchor='lm')
d3.text((145, 1050), '• 缺點：一長串工作流需要連續手動點選數次 Approve。', font=f_reg(20), fill=(148, 163, 184), anchor='lm')

# Right Column: Auto-Approve (x: 1130 -> 2120)
d3.rounded_rectangle([1130, 170, 2120, 1120], radius=24, fill=(38, 30, 20), outline=(245, 158, 11), width=3)
d3.rounded_rectangle([1130, 170, 2120, 260], radius=24, fill=(146, 64, 14))
d3.rectangle([1130, 220, 2120, 260], fill=(146, 64, 14))
d3.text((1625, 215), '⚡ 自動同意模式（Always Proceed / Auto-Approve）', font=f_bold(28), fill=(255, 255, 255), anchor='mm')

# Flow in Right
r_cards = [
    ('步驟 1：你下達開發指令', '「請幫我建立網頁、初始化 Git 並完成 GitHub 部署」', (241, 245, 249)),
    ('步驟 2：AI 自主分析並連續執行', '自動建立 index.html ➔ 自動產生樣式 ➔ 自動寫好腳本', (253, 224, 71)),
    ('步驟 3：無人值守自動跑完終端機', '自動執行 git init ➔ git commit ➔ gh repo create 發布', (253, 224, 71)),
    ('步驟 4：一口氣回報最終成果！', '「已全部完成！您的網址已部署至 GitHub Pages 🚀」', (167, 243, 208)),
]
for idx, (t1, t2, col) in enumerate(r_cards):
    cy = 295 + idx * 135
    d3.rounded_rectangle([1165, cy, 2085, cy+105], radius=14, fill=(52, 40, 26), outline=(245, 158, 11), width=2)
    d3.text((1195, cy+35), t1, font=f_bold(24), fill=col, anchor='lm')
    d3.text((1195, cy+72), t2, font=f_reg(20), fill=(226, 232, 240), anchor='lm')
    if idx < 3:
        d3.text((1625, cy+120), '↓', font=f_bold(28), fill=(245, 158, 11), anchor='mm')

# Right Summary
d3.rounded_rectangle([1165, 875, 2085, 1090], radius=14, fill=(15, 23, 42), outline=(245, 158, 11), width=2)
d3.text((1195, 915), '【適合對象】：獨立練習專案、快速原型開發（如本課程）', font=f_bold(22), fill=(253, 224, 71), anchor='lm')
d3.text((1195, 960), '• 優點：速度極快！AI 自主連鎖反應跑完全部流程，不用頻繁點按鈕。', font=f_reg(20), fill=(226, 232, 240), anchor='lm')
d3.text((1195, 1005), '• 特色：充分發揮 Agentic AI「代理人自主行動」的強大威力。', font=f_reg(20), fill=(226, 232, 240), anchor='lm')
d3.text((1195, 1050), '• 設定：在中央輸入框點選 Permissions Picker 切換為 Always Proceed。', font=f_reg(20), fill=(148, 163, 184), anchor='lm')

img3.save(os.path.join(pic_dir, 'ch1_permission_modes.png'), 'PNG')
print("ch1_permission_modes.png saved!")

# ==============================================================================
# DIAGRAM 4: ch2_landing_page_anatomy.png (Landing Page Anatomy - 2200x1260)
# ==============================================================================
print("Generating ch2_landing_page_anatomy.png...")
W4, H4 = 2200, 1260
img4 = Image.new('RGB', (W4, H4), (10, 14, 23))
d4 = ImageDraw.Draw(img4, 'RGBA')

d4.text((W4//2, 50), '商業產品介紹頁（Landing Page）5 大核心骨架解剖圖', font=f_bold(44), fill=(248, 250, 252), anchor='mm')
d4.text((W4//2, 105), '在下達提示詞前，先理解現代高轉換率產品頁面的黃金結構，向 AI 描述時更有條理！', font=f_reg(26), fill=(148, 163, 184), anchor='mm')

# Browser Mockup Frame (x: 70 -> 1450, y: 150 -> 1210)
bx1, by1, bx2, by2 = 70, 150, 1450, 1210
d4.rounded_rectangle([bx1-3, by1-3, bx2+3, by2+3], radius=22, fill=(30, 41, 59), outline=(71, 85, 105), width=3)
d4.rounded_rectangle([bx1, by1, bx2, by2], radius=20, fill=(18, 24, 38))

# Browser bar
d4.rounded_rectangle([bx1, by1, bx2, by1+55], radius=20, fill=(30, 41, 59))
d4.rectangle([bx1, by1+30, bx2, by1+55], fill=(30, 41, 59))
for idx, col in enumerate([(239, 68, 68), (245, 158, 11), (16, 185, 129)]):
    cx = bx1 + 30 + idx * 26
    cy = by1 + 27
    d4.ellipse([cx-7, cy-7, cx+7, cy+7], fill=col)
d4.rounded_rectangle([bx1+120, by1+10, bx2-120, by1+44], radius=8, fill=(15, 23, 42))
d4.text(((bx1+bx2)//2, by1+27), 'https://yourname.github.io/smartsound-pro', font=f_bold(18), fill=(148, 163, 184), anchor='mm')

# 1. Nav Bar (y: 215 -> 285)
ny1, ny2 = by1+65, by1+135
d4.rectangle([bx1+10, ny1, bx2-10, ny2], fill=(24, 32, 50))
d4.text((bx1+35, (ny1+ny2)//2), '● SmartSound Pro', font=f_bold(22), fill=(248, 250, 252), anchor='lm')
d4.text((bx1+680, (ny1+ny2)//2), '產品亮點    多角度圖鑑    預購方案    顧客好評', font=f_bold(19), fill=(148, 163, 184), anchor='lm')
d4.rounded_rectangle([bx2-180, ny1+12, bx2-35, ny2-12], radius=10, fill=(79, 70, 229))
d4.text((bx2-107, (ny1+ny2)//2), '立即預購', font=f_bold(18), fill=(255, 255, 255), anchor='mm')

# 2. Hero Section (y: 295 -> 565)
hy1, hy2 = ny2+8, ny2+280
d4.rectangle([bx1+10, hy1, bx2-10, hy2], fill=(15, 20, 32))
d4.text((bx1+50, hy1+55), '頂級主動降噪 · 極致純粹音質', font=f_bold(32), fill=(248, 250, 252), anchor='lm')
d4.text((bx1+50, hy1+105), '專為極致專注與沉浸音樂打造，配備 40 小時超長續航力。', font=f_reg(20), fill=(148, 163, 184), anchor='lm')
d4.rounded_rectangle([bx1+50, hy1+155, bx1+240, hy1+215], radius=10, fill=(14, 165, 233))
d4.text((bx1+145, hy1+185), '搶先早鳥預購 →', font=f_bold(20), fill=(15, 23, 42), anchor='mm')
d4.rounded_rectangle([bx1+260, hy1+155, bx1+430, hy1+215], radius=10, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
d4.text((bx1+345, hy1+185), '觀看產品影片', font=f_bold(20), fill=(226, 232, 240), anchor='mm')

# Paste headphone photo in Hero
draw_hero_img_box = [bx1+760, hy1+20, bx2-45, hy2-20]
d4.rounded_rectangle(draw_hero_img_box, radius=14, fill=(255, 255, 255), outline=(56, 189, 248), width=3)
hp_img = Image.open(os.path.join(pic_dir, 'ATHM20XBT_m01.jpg')).convert('RGB')
hp_img.thumbnail((220, 220))
img4.paste(hp_img, (bx1+790, hy1+30))
d4.text((bx1+1140, (hy1+hy2)//2 - 18), '【 英雄區吸睛主圖 】', font=f_bold(22), fill=(15, 23, 42), anchor='mm')
d4.text((bx1+1140, (hy1+hy2)//2 + 22), '高解析商品視覺 (PIC/ATHM20XBT_m01.jpg)', font=f_bold(17), fill=(71, 85, 105), anchor='mm')

# 3. Features Section (y: 575 -> 775)
fy1, fy2 = hy2+8, hy2+210
d4.rectangle([bx1+10, fy1, bx2-10, fy2], fill=(20, 26, 40))
d4.text(((bx1+bx2)//2, fy1+30), '─── 產品三大核心亮點 ───', font=f_bold(22), fill=(129, 140, 248), anchor='mm')
fc_w = (bx2 - bx1 - 90) // 3
for i, (title, sub) in enumerate([
    ('40dB 深度主動降噪', '雙重麥克風陣列反向聲波過濾'),
    ('40hr 超強續航力', '快充 10 分鐘即可暢聽 5 小時'),
    ('人體工學減壓耳罩', '進口親膚蛋白皮，久戴完全不夾耳')
]):
    fx1 = bx1 + 30 + i * (fc_w + 15)
    fx2 = fx1 + fc_w
    d4.rounded_rectangle([fx1, fy1+60, fx2, fy2-15], radius=12, fill=(28, 37, 56), outline=(51, 65, 85), width=2)
    d4.text(((fx1+fx2)//2, fy1+98), '★ ' + title, font=f_bold(20), fill=(248, 250, 252), anchor='mm')
    d4.text(((fx1+fx2)//2, fy1+142), sub, font=f_reg(17), fill=(148, 163, 184), anchor='mm')

# 4. Pricing Cards (y: 785 -> 995)
py1, py2 = fy2+8, fy2+220
d4.rectangle([bx1+10, py1, bx2-10, py2], fill=(15, 20, 32))
d4.text(((bx1+bx2)//2, py1+28), '─── 限量早鳥預購方案 ───', font=f_bold(22), fill=(56, 189, 248), anchor='mm')
pw = (bx2 - bx1 - 100) // 2
for i, (pname, price, tag, col) in enumerate([
    ('標準版 (Standard Edition)', 'NT$ 3,990', '通勤族日常首選', (148, 163, 184)),
    ('旗艦版 (Pro Max Edition)', 'NT$ 5,990', '★ 最受歡迎 / 附硬殼收納包', (245, 158, 11))
]):
    px1 = bx1 + 40 + i * (pw + 25)
    px2 = px1 + pw
    d4.rounded_rectangle([px1, py1+58, px2, py2-15], radius=12, fill=(26, 34, 52), outline=col, width=2)
    d4.text((px1+25, py1+92), pname, font=f_bold(21), fill=(248, 250, 252), anchor='lm')
    d4.text((px2-25, py1+92), tag, font=f_bold(17), fill=col, anchor='rm')
    d4.text((px1+25, py1+142), price, font=f_bold(30), fill=(16, 185, 129), anchor='lm')
    d4.rounded_rectangle([px2-160, py1+120, px2-25, py1+165], radius=8, fill=(79, 70, 229))
    d4.text((px2-92, py1+142), '選擇此方案', font=f_bold(18), fill=(255, 255, 255), anchor='mm')

# 5. Form & Footer (y: 1005 -> 1200)
oy1, oy2 = py2+8, by2-10
d4.rectangle([bx1+10, oy1, bx2-10, oy2], fill=(24, 30, 46))
d4.text(((bx1+bx2)//2, oy1+30), '─── 線上預購登記表單（整合第 5~8 章後端）───', font=f_bold(20), fill=(16, 185, 129), anchor='mm')
d4.rounded_rectangle([bx1+60, oy1+60, bx1+420, oy1+110], radius=8, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
d4.text((bx1+85, oy1+85), '姓名：王小明', font=f_reg(18), fill=(148, 163, 184), anchor='lm')
d4.rounded_rectangle([bx1+450, oy1+60, bx1+810, oy1+110], radius=8, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
d4.text((bx1+475, oy1+85), 'Email: user@example.com', font=f_reg(18), fill=(148, 163, 184), anchor='lm')
d4.rounded_rectangle([bx1+840, oy1+60, bx2-60, oy1+110], radius=8, fill=(16, 185, 129))
d4.text(((bx1+840+bx2-60)//2, oy1+85), '確認送出登記 (自動寫入 Google Sheets + LINE 推播)', font=f_bold(18), fill=(15, 23, 42), anchor='mm')
d4.text(((bx1+bx2)//2, oy1+150), '© 2026 SmartSound Pro. All rights reserved. | 聯絡我們 | 隱私權政策', font=f_reg(16), fill=(100, 116, 139), anchor='mm')

# Right Callout Cards (x: 1490 -> 2130)
rx1, rx2 = 1490, 2130
cards_info = [
    ('① 頂部導覽列 (Header)', ['品牌名稱、導覽錨點捷徑，以及右上角', '醒目的「立即預購」導購行動按鈕。'], (129, 140, 248), 150, 340),
    ('② 英雄首頁看板 (Hero)', ['全站視線第一焦點！震撼大標題、一句話', '核心價值描述、搶眼按鈕與吸睛耳機主圖。'], (56, 189, 248), 360, 560),
    ('③ 核心特色區 (Features)', ['用 3～4 張卡片搭配小圖示，化繁為簡解說', '產品核心賣點（主動降噪、續航、舒適度）。'], (167, 243, 208), 580, 775),
    ('④ 價格方案表 (Pricing)', ['標準版與旗艦版清晰比價，降低消費者', '決策門檻，直接點擊按鈕跳轉預購。'], (253, 224, 71), 795, 990),
    ('⑤ 預購表單與頁尾 (Footer)', ['收集客戶姓名、Email、電話等重要欄位，', '後續第 5~8 章將無縫串接 GAS、LINE 與金流！'], (16, 185, 129), 1010, 1210)
]
for title, lines_arr, col, y1_c, y2_c in cards_info:
    d4.rounded_rectangle([rx1, y1_c, rx2, y2_c], radius=16, fill=(21, 28, 42), outline=col, width=3)
    d4.text((rx1+24, y1_c+36), title, font=f_bold(23), fill=col, anchor='lm')
    for idx_l, l_txt in enumerate(lines_arr):
        d4.text((rx1+24, y1_c+80 + idx_l*34), l_txt, font=f_bold(19), fill=(226, 232, 240), anchor='lm')

img4.save(os.path.join(pic_dir, 'ch2_landing_page_anatomy.png'), 'PNG')
print("ch2_landing_page_anatomy.png saved!")

# ==============================================================================
# DIAGRAM 5: ch2_interview_flow.png (Reverse Interview - 2200x1150)
# ==============================================================================
print("Generating ch2_interview_flow.png...")
W5, H5 = 2200, 1150
img5 = Image.new('RGB', (W5, H5), (10, 14, 23))
d5 = ImageDraw.Draw(img5, 'RGBA')

d5.text((W5//2, 50), '提示詞進階秘訣：「先問答、後動工」反向訪談法', font=f_bold(44), fill=(248, 250, 252), anchor='mm')
d5.text((W5//2, 105), '不用自己硬擠長篇提示詞！讓 Antigravity 主動提問引導你，3 步驟產出最貼合心意的網頁', font=f_reg(26), fill=(148, 163, 184), anchor='mm')

# Top Comparison Cards (y: 150 -> 300)
d5.rounded_rectangle([70, 150, 1070, 305], radius=16, fill=(45, 22, 32), outline=(239, 68, 68), width=3)
d5.text((105, 190), '× 傳統做法：只講一句模糊指令，讓 AI 自己瞎猜', font=f_bold(24), fill=(252, 165, 165), anchor='lm')
d5.text((105, 235), '你：「幫我做一個賣耳機的網站。」', font=f_bold(20), fill=(241, 245, 249), anchor='lm')
d5.text((105, 272), '結果：配色、區塊、價格全是 AI 亂編的，做出來跟你想的差十萬八千里！', font=f_reg(19), fill=(254, 202, 202), anchor='lm')

d5.rounded_rectangle([1130, 150, 2130, 305], radius=16, fill=(18, 42, 36), outline=(16, 185, 129), width=3)
d5.text((1165, 190), '★ 高手做法：請 AI 先當顧問提問，一問一答釐清後再做', font=f_bold(24), fill=(110, 231, 183), anchor='lm')
d5.text((1165, 235), '你：「我想做耳機網站，請先不要寫程式，先問我幾個問題來釐清需求！」', font=f_bold(20), fill=(241, 245, 249), anchor='lm')
d5.text((1165, 272), '結果：像做選擇題一樣輕鬆回答，做出來的網站 100% 符合你的想像！', font=f_reg(19), fill=(167, 243, 208), anchor='lm')

# 3 Horizontal Step Cards (y: 345 -> 1080)
steps_info = [
    (70, 720, (129, 140, 248), 'STEP 1：你先拋出初步想法', '告訴 AI「先提問、別急著寫程式」',
     [
         ('【你輸入的開場白】：', (165, 180, 252), True),
         ('「我想做一個介紹 SmartSound 降噪耳機', (241, 245, 249), False),
         ('的網頁，但我還沒有想好所有細節。', (241, 245, 249), False),
         ('請你先不要寫程式！', (253, 224, 71), True),
         ('請針對網站風格、必備區塊與方案價格，', (241, 245, 249), False),
         ('一次向我提出 4 個關鍵問題，並提供', (241, 245, 249), False),
         ('建議選項讓我挑選！」', (241, 245, 249), False),
         ('', (0,0,0), False),
         ('★ 也可以直接輸入內建捷徑：', (56, 189, 248), True),
         ('/grill-me 我想做耳機銷售網頁', (125, 211, 252), True),
     ]),
    (770, 1430, (56, 189, 248), 'STEP 2：AI 提問 & 你輕鬆作答', '像填選擇題一樣回答 AI 的問題',
     [
         ('【Antigravity 顧問主動詢問你】：', (125, 211, 252), True),
         ('Q1. 視覺風格偏好？(A)深色科技 (B)明亮極簡', (203, 213, 225), False),
         ('Q2. 主打的 3 個產品核心賣點是什麼？', (203, 213, 225), False),
         ('Q3. 預計提供哪幾種價格方案？', (203, 213, 225), False),
         ('Q4. 頁面底部希望放什麼行動按鈕？', (203, 213, 225), False),
         ('', (0,0,0), False),
         ('【你只需簡短回答】：', (253, 224, 71), True),
         ('「1. 選 A 曜石黑科技感', (241, 245, 249), False),
         ('  2. 主動降噪、40hr 續航、人體工學耳罩', (241, 245, 249), False),
         ('  3. 標準版 $3,990 / 旗艦版 $5,990', (241, 245, 249), False),
         ('  4. 放線上預購登記表單」', (241, 245, 249), False),
     ]),
    (1480, 2130, (52, 211, 153), 'STEP 3：AI 彙整規格並精準產出', '確認規格書無誤後，一鍵生成完美網頁',
     [
         ('【Antigravity 整理出完整規格書】：', (110, 231, 183), True),
         ('● 主題：深色科技感 + 手機版自適應 RWD', (226, 232, 240), False),
         ('● 圖片：自動配置 PIC 資料夾 4 張耳機圖', (226, 232, 240), False),
         ('● 區塊：導覽列 + Hero + 3大賣點 + 價格表', (226, 232, 240), False),
         ('● 互動：底部整合預購表單與彈窗確認', (226, 232, 240), False),
         ('', (0,0,0), False),
         ('【你最後確認下達動工令】：', (253, 224, 71), True),
         ('「太棒了！完全符合我要的，', (241, 245, 249), False),
         ('  請照這份規格開始幫我寫出網頁！」', (241, 245, 249), False),
         ('', (0,0,0), False),
         ('➔ 產出零落差的高質感商業網站！', (167, 243, 208), True),
     ])
]
for x1, x2, col, title, sub, lines in steps_info:
    d5.rounded_rectangle([x1, 345, x2, 1080], radius=20, fill=(21, 28, 42), outline=col, width=3)
    d5.rounded_rectangle([x1, 345, x2, 455], radius=20, fill=(28, 38, 58))
    d5.rectangle([x1, 425, x2, 455], fill=(28, 38, 58))
    d5.line([x1, 455, x2, 455], fill=col, width=3)
    d5.text(((x1+x2)//2, 385), title, font=f_bold(25), fill=col, anchor='mm')
    d5.text(((x1+x2)//2, 425), sub, font=f_bold(18), fill=(203, 213, 225), anchor='mm')

    y_cur = 495
    for txt, tcol, is_b in lines:
        if txt:
            d5.text((x1+30, y_cur), txt, font=f_bold(20) if is_b else f_reg(19), fill=tcol, anchor='lm')
        y_cur += 46

for ax in [735, 1445]:
    d5.text((ax+10, 710), '➔', font=f_bold(44), fill=(56, 189, 248), anchor='mm')

img5.save(os.path.join(pic_dir, 'ch2_interview_flow.png'), 'PNG')
print("ch2_interview_flow.png saved!")

# ==============================================================================
# DIAGRAM 6: ch2_iterative_tuning.png (Iterative Tuning - 2200x1100)
# ==============================================================================
print("Generating ch2_iterative_tuning.png...")
W6, H6 = 2200, 1100
img6 = Image.new('RGB', (W6, H6), (10, 14, 23))
d6 = ImageDraw.Draw(img6, 'RGBA')

d6.text((W6//2, 50), '對話式迭代微調（Iterative Tuning）：動口不動手，讓網頁越改越精緻', font=f_bold(42), fill=(248, 250, 252), anchor='mm')
d6.text((W6//2, 105), '不需要自己進程式碼大海撈針！看哪裡不順眼，直接用一句白話文請 Antigravity 局部修改', font=f_reg(26), fill=(148, 163, 184), anchor='mm')

# 3 Columns: V1 -> Prompts -> V2 (y: 160 -> 1040)
# Col 1: V1
d6.rounded_rectangle([70, 160, 710, 1040], radius=22, fill=(21, 28, 42), outline=(100, 116, 139), width=3)
d6.rounded_rectangle([70, 160, 710, 250], radius=22, fill=(30, 41, 59))
d6.rectangle([70, 220, 710, 250], fill=(30, 41, 59))
d6.text((390, 205), '第 1 版：AI 初次生成的網頁 (V1)', font=f_bold(25), fill=(203, 213, 225), anchor='mm')

d6.rounded_rectangle([105, 290, 675, 480], radius=14, fill=(15, 20, 32), outline=(51, 65, 85), width=2)
d6.text((135, 335), 'SmartSound Pro 降噪耳機', font=f_bold(22), fill=(226, 232, 240), anchor='lm')
d6.text((135, 380), '（標題字體偏小、普通藍色按鈕）', font=f_reg(19), fill=(148, 163, 184), anchor='lm')
d6.rounded_rectangle([135, 415, 290, 460], radius=8, fill=(59, 130, 246))
d6.text((212, 437), '立即預購', font=f_bold(18), fill=(255, 255, 255), anchor='mm')

d6.rounded_rectangle([105, 520, 675, 710], radius=14, fill=(15, 20, 32), outline=(51, 65, 85), width=2)
d6.text((390, 585), '【 只有 3 張基本功能特色卡 】', font=f_bold(22), fill=(148, 163, 184), anchor='mm')
d6.text((390, 635), '尚未加入「顧客真實好評推薦」區塊', font=f_reg(19), fill=(100, 116, 139), anchor='mm')

d6.rounded_rectangle([105, 750, 675, 980], radius=14, fill=(15, 20, 32), outline=(51, 65, 85), width=2)
d6.text((390, 835), '【 點擊預購按鈕毫無反應 】', font=f_bold(22), fill=(148, 163, 184), anchor='mm')
d6.text((390, 885), '尚未加上互動感謝彈窗或動畫回饋', font=f_reg(19), fill=(100, 116, 139), anchor='mm')

# Col 2: Middle Prompts
d6.rounded_rectangle([775, 160, 1425, 1040], radius=22, fill=(18, 30, 48), outline=(56, 189, 248), width=3)
d6.rounded_rectangle([775, 160, 1425, 250], radius=22, fill=(2, 132, 199))
d6.rectangle([775, 220, 1425, 250], fill=(2, 132, 199))
d6.text((1100, 205), '中間過程：你用自然語言下達 3 句微調', font=f_bold(25), fill=(255, 255, 255), anchor='mm')

prompts_mid2 = [
    ('● 微調指令 1（改視覺與配色）：', '「請把 Hero 標題字體放大，並把預購', '按鈕改成更有購買慾望的亮橘色漸層！」', 290),
    ('● 微調指令 2（新增內容區塊）：', '「請在產品特色卡片下方，新增一區『顧', '客五星好評推薦 (Testimonials)』！」', 520),
    ('● 微調指令 3（加上互動體驗）：', '「當客戶點擊預購按鈕時，請平滑捲動到', '表單區，送出後彈出感謝預購視窗！」', 750),
]
for ptitle, pl1, pl2, py in prompts_mid2:
    d6.rounded_rectangle([805, py, 1395, py+190], radius=14, fill=(26, 38, 60), outline=(56, 189, 248), width=2)
    d6.text((835, py+42), ptitle, font=f_bold(21), fill=(125, 211, 252), anchor='lm')
    d6.text((835, py+92), pl1, font=f_bold(19), fill=(241, 245, 249), anchor='lm')
    d6.text((835, py+132), pl2, font=f_bold(19), fill=(241, 245, 249), anchor='lm')

# Col 3: V2
d6.rounded_rectangle([1490, 160, 2130, 1040], radius=22, fill=(18, 38, 34), outline=(16, 185, 129), width=3)
d6.rounded_rectangle([1490, 160, 2130, 250], radius=22, fill=(5, 150, 105))
d6.rectangle([1490, 220, 2130, 250], fill=(5, 150, 105))
d6.text((1810, 205), '最終版：AI 自動增量更新完成 (V2)', font=f_bold(25), fill=(255, 255, 255), anchor='mm')

d6.rounded_rectangle([1525, 290, 2095, 480], radius=14, fill=(15, 23, 36), outline=(245, 158, 11), width=2)
d6.text((1555, 345), '★ 巨幅漸層大標題 + 吸睛視覺', font=f_bold(25), fill=(253, 224, 71), anchor='lm')
d6.rounded_rectangle([1555, 395, 1780, 450], radius=10, fill=(245, 158, 11))
d6.text((1667, 422), '★ 立即搶先預購 →', font=f_bold(20), fill=(15, 23, 42), anchor='mm')

d6.rounded_rectangle([1525, 520, 2095, 710], radius=14, fill=(15, 23, 36), outline=(52, 211, 153), width=2)
d6.text((1810, 585), '★★★★★ 顧客真實好評推薦區', font=f_bold(22), fill=(110, 231, 183), anchor='mm')
d6.text((1810, 635), '「降噪效果超驚艷，戴一整天也不痛！」', font=f_bold(19), fill=(226, 232, 240), anchor='mm')

d6.rounded_rectangle([1525, 750, 2095, 980], radius=14, fill=(15, 23, 36), outline=(52, 211, 153), width=2)
d6.text((1810, 835), '● 完整互動彈窗 + 自動捲動定位', font=f_bold(22), fill=(110, 231, 183), anchor='mm')
d6.text((1810, 885), '只改動需要的區塊，不破壞原有排版！', font=f_bold(19), fill=(226, 232, 240), anchor='mm')

for ax in [735, 1450]:
    d6.text((ax+10, 580), '➔', font=f_bold(44), fill=(56, 189, 248), anchor='mm')

img6.save(os.path.join(pic_dir, 'ch2_iterative_tuning.png'), 'PNG')
print("ch2_iterative_tuning.png saved!")
print("ALL 6 HIGH-DEFINITION DIAGRAMS GENERATED SUCCESSFULLY!")
