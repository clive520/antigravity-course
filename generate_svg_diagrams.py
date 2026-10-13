import os

pic_dir = r"c:\Antigravity\Antigravity教學\PIC"
os.makedirs(pic_dir, exist_ok=True)

# Common SVG header & styling
def svg_wrap(width, height, content):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      .title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 800; font-size: 32px; fill: #f8fafc; text-anchor: middle; }}
      .subtitle {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 500; font-size: 17px; fill: #94a3b8; text-anchor: middle; }}
      .card-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 700; font-size: 20px; fill: #ffffff; text-anchor: middle; }}
      .card-sub {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 600; font-size: 15px; text-anchor: middle; }}
      .item-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 700; font-size: 17px; fill: #f8fafc; }}
      .item-desc {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 400; font-size: 14.5px; fill: #cbd5e1; }}
      .badge-text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 600; font-size: 14px; fill: #ffffff; text-anchor: middle; }}
      .pill-text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 600; font-size: 13.5px; fill: #ffffff; text-anchor: middle; }}
      .note-bold {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 700; font-size: 15px; text-anchor: middle; }}
      .note-sub {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 400; font-size: 14px; fill: #94a3b8; text-anchor: middle; }}
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#0b0f19"/>
{content}
</svg>"""

# ==============================================================================
# 1. ch1_ide_layout.svg (1600 x 940)
# ==============================================================================
content_1 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">Google Antigravity 2.0 介面架構導覽</text>
  <text x="800" y="78" class="subtitle">以 AI 代理為核心的全新對話指揮中心：三大核心功能區塊配置圖</text>

  <!-- CARD 1: Left Sidebar -->
  <g filter="url(#shadow)">
    <rect x="40" y="125" width="460" height="770" rx="18" fill="#151b2b" stroke="#6366f1" stroke-width="3"/>
    <rect x="60" y="145" width="420" height="52" rx="10" fill="#6366f1"/>
    <text x="270" y="177" class="card-title">① 左側功能導覽欄 (Left Sidebar)</text>
    <text x="270" y="222" class="card-sub" fill="#a5b4fc">【專案管理與全域設定切換中心】</text>

    <!-- Item 1 -->
    <rect x="60" y="245" width="420" height="72" rx="10" fill="#4f46e5" stroke="#6366f1" stroke-width="1.5"/>
    <text x="80" y="274" class="item-title">[新對話] New Conversation</text>
    <text x="80" y="300" class="item-desc">開啟全新獨立的 AI 對話主視窗</text>

    <!-- Item 2 -->
    <rect x="60" y="330" width="420" height="72" rx="10" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="80" y="359" class="item-title">[專案管理] Projects</text>
    <text x="80" y="385" class="item-desc">綁定並切換本地資料夾工作區（安全沙盒）</text>

    <!-- Item 3 -->
    <rect x="60" y="415" width="420" height="72" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="80" y="444" class="item-title">[設定與權限] Settings</text>
    <text x="80" y="470" class="item-desc">切換手動審查 / 自動同意執行權限</text>

    <!-- Item 4 -->
    <rect x="60" y="500" width="420" height="72" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="80" y="529" class="item-title">[外掛技能] Skills &amp; Plugins</text>
    <text x="80" y="555" class="item-desc">管理自訂提示詞技能、擴充規則與 MCP 工具</text>

    <!-- Item 5 -->
    <rect x="60" y="585" width="420" height="72" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="80" y="614" class="item-title">[排程任務] Scheduled Tasks</text>
    <text x="80" y="640" class="item-desc">管理背景定時任務與自動化排程 (Cron)</text>

    <!-- Bottom Tip Box -->
    <rect x="60" y="685" width="420" height="85" rx="10" fill="#0f172a" stroke="#6366f1" stroke-width="1.5"/>
    <text x="270" y="722" class="note-bold" fill="#a5b4fc">💡 介面特色：點擊左上角圖示可收合此欄</text>
    <text x="270" y="748" class="note-sub">告別傳統混亂的檔案樹，介面乾淨不擁擠！</text>
  </g>

  <!-- CARD 2: Center Chat Canvas -->
  <g filter="url(#shadow)">
    <rect x="525" y="125" width="550" height="770" rx="18" fill="#0f172a" stroke="#0ea5e9" stroke-width="4"/>
    <rect x="545" y="145" width="510" height="52" rx="10" fill="#0284c7"/>
    <text x="800" y="177" class="card-title">② 正中央：對話主畫布 (Chat Canvas) ★ 核心</text>
    <text x="800" y="222" class="card-sub" fill="#38bdf8">【核心操作區：直接在視窗中央指揮 AI 代理】</text>

    <!-- Mock Prompt Box -->
    <rect x="550" y="245" width="500" height="155" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="575" y="278" font-family="sans-serif" font-weight="700" font-size="16px" fill="#7dd3fc">👤 使用者提問示範（自然語言輸入）：</text>
    <text x="575" y="312" font-family="sans-serif" font-weight="600" font-size="16.5px" fill="#f8fafc">「請幫我建立一個耳機銷售網站 index.html，</text>
    <text x="575" y="342" font-family="sans-serif" font-weight="600" font-size="16.5px" fill="#f8fafc">  使用專案 PIC 資料夾照片，並支援手機版 RWD！」</text>
    <text x="575" y="377" font-family="sans-serif" font-weight="600" font-size="15px" fill="#34d399">➔ AI 代理即刻自主建檔、撰寫代碼並回報進度</text>

    <!-- Center Input Box -->
    <rect x="550" y="425" width="500" height="165" rx="12" fill="#181e2c" stroke="#0ea5e9" stroke-width="2.5"/>
    <text x="575" y="462" font-family="sans-serif" font-weight="600" font-size="16.5px" fill="#e2e8f0">中央輸入框：Ask anything, @ to mention, / for actions</text>
    <line x1="550" y1="488" x2="1050" y2="488" stroke="#334155" stroke-width="1.5"/>

    <!-- Badges Row -->
    <rect x="565" y="508" width="105" height="36" rx="8" fill="#10b981"/>
    <text x="617" y="531" class="pill-text">[語音輸入]</text>

    <rect x="680" y="508" width="100" height="36" rx="8" fill="#6366f1"/>
    <text x="730" y="531" class="pill-text">[+ 附加檔案]</text>

    <rect x="790" y="508" width="115" height="36" rx="8" fill="#f59e0b"/>
    <text x="847" y="531" class="pill-text">[/ 斜線指令]</text>

    <rect x="915" y="508" width="115" height="36" rx="8" fill="#ec4899"/>
    <text x="972" y="531" class="pill-text">[@ 提及檔案]</text>

    <!-- Shortcuts note -->
    <text x="800" y="570" font-family="sans-serif" font-weight="500" font-size="13px" fill="#94a3b8" text-anchor="middle">快捷鍵：語音輸入 Ctrl+M ｜ 快捷指令 /grill-me</text>

    <!-- Bottom Highlights -->
    <rect x="550" y="615" width="500" height="155" rx="12" fill="#151b2b" stroke="#334155" stroke-width="1.5"/>
    <text x="575" y="648" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#38bdf8">🔥 新版 Antigravity 2.0 重大特點：</text>
    <text x="575" y="680" class="item-desc">• 擺脫傳統兩側夾縫對話框：對話主畫布佔據畫面正中央！</text>
    <text x="575" y="712" class="item-desc">• 支援一鍵麥克風語音輸入：動口就能吩咐 AI 建立與修改網頁</text>
    <text x="575" y="744" class="item-desc">• 內建反向訪談：不知如何下提示詞時，AI 會主動反問你需求</text>
  </g>

  <!-- CARD 3: Right Auxiliary Pane -->
  <g filter="url(#shadow)">
    <rect x="1100" y="125" width="460" height="770" rx="18" fill="#151b2b" stroke="#10b981" stroke-width="3"/>
    <rect x="1120" y="145" width="420" height="52" rx="10" fill="#10b981"/>
    <text x="1330" y="177" class="card-title">③ 右側輔助面板 (Auxiliary Pane)</text>
    <text x="1330" y="222" class="card-sub" fill="#6ee7b7">【執行成果與程式碼變更審查面板】</text>

    <!-- Item 1 -->
    <rect x="1120" y="245" width="420" height="85" rx="10" fill="#064e3b" stroke="#10b981" stroke-width="1.5"/>
    <text x="1140" y="278" class="item-title">[成果產出物] Artifacts</text>
    <text x="1140" y="308" class="item-desc">檢視 AI 寫出的實作計畫、架構文件與生成圖片</text>

    <!-- Item 2 -->
    <rect x="1120" y="345" width="420" height="85" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="1140" y="378" class="item-title">[程式碼變更] Files Changed</text>
    <text x="1140" y="408" class="item-desc">即時審查被建立/修改的檔案差異（VCS 版本控制）</text>

    <!-- Item 3 -->
    <rect x="1120" y="445" width="420" height="85" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="1140" y="478" class="item-title">[系統終端機] Terminal</text>
    <text x="1140" y="508" class="item-desc">檢視底層命令執行日誌（快速鍵 Ctrl + `）</text>

    <!-- Item 4 -->
    <rect x="1120" y="545" width="420" height="85" rx="10" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="1140" y="578" class="item-title">[背景子代理] Subagents</text>
    <text x="1140" y="608" class="item-desc">監看並行子任務、定時任務與瀏覽器自動化測試</text>

    <!-- Bottom Tip Box -->
    <rect x="1120" y="685" width="420" height="85" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1.5"/>
    <text x="1330" y="722" class="note-bold" fill="#6ee7b7">💡 彈性配置：執行時自動展開，平時可收合</text>
    <text x="1330" y="748" class="note-sub">不搶佔中央視覺，讓專注力回歸對話核心！</text>
  </g>
"""

# ==============================================================================
# 2. ch1_workspace_boundary.svg (1600 x 820)
# ==============================================================================
content_2 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">Project 專案工作區安全邊界示意圖</text>
  <text x="800" y="78" class="subtitle">Antigravity 具備「環境隔離沙盒」：只在授權資料夾內操作，保護個人電腦安全</text>

  <!-- Left Card: Green Safe Sandbox -->
  <g filter="url(#shadow)">
    <rect x="60" y="130" width="710" height="640" rx="18" fill="#102820" stroke="#10b981" stroke-width="3"/>
    <rect x="80" y="150" width="670" height="56" rx="12" fill="#10b981"/>
    <text x="415" y="186" class="card-title">✅ [安全沙盒] AI 獲授權操作工作區</text>

    <!-- Path Bar -->
    <rect x="85" y="225" width="660" height="60" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
    <text x="415" y="262" font-family="sans-serif" font-weight="700" font-size="18px" fill="#f8fafc" text-anchor="middle">📁 授權資料夾路徑：C:\\Antigravity\\web-demo\\</text>

    <!-- Item 1 -->
    <rect x="85" y="305" width="660" height="85" rx="10" fill="#14362a" stroke="#34d399" stroke-width="1"/>
    <text x="110" y="340" font-family="sans-serif" font-weight="700" font-size="18px" fill="#34d399">[允許] 建立與修改網頁檔案</text>
    <text x="110" y="368" class="item-desc">自由新增與編輯 index.html、style.css、main.js 等專案原始碼</text>

    <!-- Item 2 -->
    <rect x="85" y="405" width="660" height="85" rx="10" fill="#14362a" stroke="#34d399" stroke-width="1"/>
    <text x="110" y="440" font-family="sans-serif" font-weight="700" font-size="18px" fill="#34d399">[允許] 讀取專案圖片素材</text>
    <text x="110" y="468" class="item-desc">讀寫本資料夾內的 PIC/ 照片庫，快速插入網頁版面</text>

    <!-- Item 3 -->
    <rect x="85" y="505" width="660" height="85" rx="10" fill="#14362a" stroke="#34d399" stroke-width="1"/>
    <text x="110" y="540" font-family="sans-serif" font-weight="700" font-size="18px" fill="#34d399">[允許] 執行專案終端機命令</text>
    <text x="110" y="568" class="item-desc">執行 git 初始化、GitHub CLI 發布網頁等專案建置指令</text>

    <!-- Safe Guarantee Banner -->
    <rect x="85" y="630" width="660" height="60" rx="10" fill="#065f46"/>
    <text x="415" y="667" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#ffffff" text-anchor="middle">🛡️ 安全保證：AI 所有寫入操作嚴格受限於此資料夾內，絕不外溢！</text>
  </g>

  <!-- Right Card: Red Protected Area -->
  <g filter="url(#shadow)">
    <rect x="830" y="130" width="710" height="640" rx="18" fill="#2d1218" stroke="#f43f5e" stroke-width="3"/>
    <rect x="850" y="150" width="670" height="56" rx="12" fill="#e11d48"/>
    <text x="1185" y="186" class="card-title">🔒 [系統保護] 未授權禁止存取區域</text>

    <!-- Path Bar -->
    <rect x="855" y="225" width="660" height="60" rx="10" fill="#4c1d2c" stroke="#fb7185" stroke-width="1.5"/>
    <text x="1185" y="262" font-family="sans-serif" font-weight="700" font-size="18px" fill="#fecdd3" text-anchor="middle">🚫 外部磁碟與目錄：桌面 / C 槽根目錄 / 個人相片</text>

    <!-- Item 1 -->
    <rect x="855" y="305" width="660" height="85" rx="10" fill="#3c1923" stroke="#fb7185" stroke-width="1"/>
    <text x="880" y="340" font-family="sans-serif" font-weight="700" font-size="18px" fill="#fb7185">[禁止] 個人桌面與我的文件</text>
    <text x="880" y="368" class="item-desc">AI 預設無法越界存取電腦桌面、下載資料夾與私人物件</text>

    <!-- Item 2 -->
    <rect x="855" y="405" width="660" height="85" rx="10" fill="#3c1923" stroke="#fb7185" stroke-width="1"/>
    <text x="880" y="440" font-family="sans-serif" font-weight="700" font-size="18px" fill="#fb7185">[禁止] 作業系統核心根目錄</text>
    <text x="880" y="468" class="item-desc">C:\\Windows 及系統開機檔案受到作業系統與沙盒雙重隔離防護</text>

    <!-- Item 3 -->
    <rect x="855" y="505" width="660" height="85" rx="10" fill="#3c1923" stroke="#fb7185" stroke-width="1"/>
    <text x="880" y="540" font-family="sans-serif" font-weight="700" font-size="18px" fill="#fb7185">[禁止] 私人密碼與個人隱私</text>
    <text x="880" y="568" class="item-desc">未經授權禁止讀取外圍個人文件與機密金鑰，避免個資外洩</text>

    <!-- Warning Banner -->
    <rect x="855" y="630" width="660" height="60" rx="10" fill="#9f1239"/>
    <text x="1185" y="667" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#ffffff" text-anchor="middle">⚠️ 新手守則：切勿將整個桌面或 C:\\ 槽設為專案資料夾！</text>
  </g>
"""

# ==============================================================================
# 3. ch1_permission_modes.svg (1600 x 820)
# ==============================================================================
content_3 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">Antigravity 權限管理模式對照圖</text>
  <text x="800" y="78" class="subtitle">在中央對話輸入框的 Permissions 選單中隨時切換：「逐步審查」或「極速放行」</text>

  <!-- Left Card: Request Review -->
  <g filter="url(#shadow)">
    <rect x="60" y="130" width="710" height="640" rx="18" fill="#0f1e30" stroke="#0ea5e9" stroke-width="3"/>
    <rect x="80" y="150" width="670" height="56" rx="12" fill="#0284c7"/>
    <text x="415" y="186" class="card-title">🛡️ [預設模式] 手動審查模式 (Default / Request Review)</text>

    <!-- Flow box -->
    <rect x="85" y="225" width="660" height="95" rx="10" fill="#182d46" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="415" y="258" font-family="sans-serif" font-weight="700" font-size="16px" fill="#7dd3fc" text-anchor="middle">【運作流程】</text>
    <text x="415" y="292" font-family="sans-serif" font-weight="600" font-size="17px" fill="#f8fafc" text-anchor="middle">提出指令 ➔ 彈出確認視窗 [Approve / Reject] ➔ 人工點擊執行</text>

    <!-- Item 1 -->
    <rect x="85" y="340" width="660" height="75" rx="10" fill="#14263c" stroke="#475569" stroke-width="1"/>
    <text x="110" y="370" font-family="sans-serif" font-weight="700" font-size="17px" fill="#38bdf8">[核心特徵]</text>
    <text x="110" y="398" class="item-desc">AI 在執行任何系統終端機指令前，必須等待你點擊 Approve 授權</text>

    <!-- Item 2 -->
    <rect x="85" y="430" width="660" height="75" rx="10" fill="#14263c" stroke="#475569" stroke-width="1"/>
    <text x="110" y="460" font-family="sans-serif" font-weight="700" font-size="17px" fill="#38bdf8">[適合對象]</text>
    <text x="110" y="488" class="item-desc">初學者、第一次接觸命令行、或正在處理公司正式重要專案</text>

    <!-- Item 3 -->
    <rect x="85" y="520" width="660" height="75" rx="10" fill="#14263c" stroke="#475569" stroke-width="1"/>
    <text x="110" y="550" font-family="sans-serif" font-weight="700" font-size="17px" fill="#38bdf8">[使用體驗]</text>
    <text x="110" y="578" class="item-desc">安全感 100%！但每動都需要手動點擊同意，操作節奏較為緊湊</text>

    <!-- Bottom Advice -->
    <rect x="85" y="630" width="660" height="60" rx="10" fill="#0369a1"/>
    <text x="415" y="667" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#ffffff" text-anchor="middle">💡 學習建議：初次安裝時維持此預設模式最安心！</text>
  </g>

  <!-- Right Card: Always Proceed -->
  <g filter="url(#shadow)">
    <rect x="830" y="130" width="710" height="640" rx="18" fill="#2d1e0f" stroke="#f59e0b" stroke-width="3"/>
    <rect x="850" y="150" width="670" height="56" rx="12" fill="#d97706"/>
    <text x="1185" y="186" class="card-title">⚡ [高效模式] 自動同意模式 (Always Proceed / Auto)</text>

    <!-- Flow box -->
    <rect x="855" y="225" width="660" height="95" rx="10" fill="#463016" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="1185" y="258" font-family="sans-serif" font-weight="700" font-size="16px" fill="#fde68a" text-anchor="middle">【運作流程】</text>
    <text x="1185" y="292" font-family="sans-serif" font-weight="600" font-size="17px" fill="#f8fafc" text-anchor="middle">提出指令 ➔ AI 連續自主執行 (建檔 + 改碼 + 終端機) ➔ 一鍵完工</text>

    <!-- Item 1 -->
    <rect x="855" y="340" width="660" height="75" rx="10" fill="#3c2814" stroke="#475569" stroke-width="1"/>
    <text x="880" y="370" font-family="sans-serif" font-weight="700" font-size="17px" fill="#f59e0b">[核心特徵]</text>
    <text x="880" y="398" class="item-desc">AI 連續執行讀取、寫檔、建檔與指令，完全不打斷使用者思考</text>

    <!-- Item 2 -->
    <rect x="855" y="430" width="660" height="75" rx="10" fill="#3c2814" stroke="#475569" stroke-width="1"/>
    <text x="880" y="460" font-family="sans-serif" font-weight="700" font-size="17px" fill="#f59e0b">[適合對象]</text>
    <text x="880" y="488" class="item-desc">練習獨立網頁、原型快速開發、想體驗 Agentic 全自動流程</text>

    <!-- Item 3 -->
    <rect x="855" y="520" width="660" height="75" rx="10" fill="#3c2814" stroke="#475569" stroke-width="1"/>
    <text x="880" y="550" font-family="sans-serif" font-weight="700" font-size="17px" fill="#f59e0b">[使用體驗]</text>
    <text x="880" y="578" class="item-desc">開發速度極快！建議在乾淨獨立的練習專案資料夾中使用</text>

    <!-- Bottom Advice -->
    <rect x="855" y="630" width="660" height="60" rx="10" fill="#b45309"/>
    <text x="1185" y="667" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#ffffff" text-anchor="middle">🚀 本課程推薦：製作耳機網頁與發布時切換此模式最省時！</text>
  </g>
"""

# ==============================================================================
# 4. ch2_landing_page_anatomy.svg (1600 x 860)
# ==============================================================================
content_4 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">商業產品介紹頁（Landing Page）5 大核心架構解剖</text>
  <text x="800" y="78" class="subtitle">在向 AI 下達提示詞前，先掌握現代高轉換率產品網頁的骨架架構</text>

  <!-- Browser Frame -->
  <g filter="url(#shadow)">
    <rect x="60" y="125" width="1480" height="700" rx="16" fill="#0f172a" stroke="#475569" stroke-width="2.5"/>
    <!-- Browser titlebar -->
    <path d="M 60 141 Q 60 125 76 125 L 1524 125 Q 1540 125 1540 141 L 1540 165 L 60 165 Z" fill="#1e293b"/>
    <!-- 3 Traffic lights -->
    <circle cx="85" cy="145" r="6" fill="#ef4444"/>
    <circle cx="105" cy="145" r="6" fill="#f59e0b"/>
    <circle cx="125" cy="145" r="6" fill="#10b981"/>
    <!-- Address bar mockup -->
    <rect x="250" y="133" width="1100" height="24" rx="6" fill="#0f172a"/>
    <text x="800" y="150" font-family="sans-serif" font-size="13px" fill="#94a3b8" text-anchor="middle">https://yoursite.github.io/product-demo.html</text>

    <!-- Block 1: Navbar -->
    <rect x="90" y="185" width="1420" height="100" rx="12" fill="#182030" stroke="#6366f1" stroke-width="2"/>
    <rect x="110" y="200" width="380" height="36" rx="8" fill="#6366f1"/>
    <text x="300" y="224" class="pill-text">[區塊 1] 頂部導覽列 (Navbar)</text>
    <text x="110" y="265" font-family="sans-serif" font-weight="600" font-size="17.5px" fill="#f8fafc">SmartSound Pro 品牌 Logo  ＋  功能選單導航（特色、圖鑑、定價） ＋  [立即預購] 行動按鈕</text>

    <!-- Block 2: Hero -->
    <rect x="90" y="305" width="1420" height="100" rx="12" fill="#182030" stroke="#0ea5e9" stroke-width="2"/>
    <rect x="110" y="320" width="380" height="36" rx="8" fill="#0284c7"/>
    <text x="300" y="344" class="pill-text">[區塊 2] 主視覺區 (Hero Section)</text>
    <text x="110" y="385" font-family="sans-serif" font-weight="600" font-size="17.5px" fill="#f8fafc">超吸睛主標題  ＋  痛點副標題  ＋  耳機高畫質主圖  ＋  [搶先預購] 主要行動呼籲按鈕 (CTA)</text>

    <!-- Block 3: Features -->
    <rect x="90" y="425" width="1420" height="100" rx="12" fill="#182030" stroke="#10b981" stroke-width="2"/>
    <rect x="110" y="440" width="380" height="36" rx="8" fill="#059669"/>
    <text x="300" y="464" class="pill-text">[區塊 3] 核心賣點 (Features 3 大特色)</text>
    <text x="110" y="505" font-family="sans-serif" font-weight="600" font-size="17.5px" fill="#f8fafc">【🎧 頂級主動降噪】  ｜  【🔋 40 小時超長續航】  ｜  【☁️ 人體工學極致舒適耳罩】</text>

    <!-- Block 4: Gallery & Pricing -->
    <rect x="90" y="545" width="1420" height="100" rx="12" fill="#182030" stroke="#f59e0b" stroke-width="2"/>
    <rect x="110" y="560" width="380" height="36" rx="8" fill="#d97706"/>
    <text x="300" y="584" class="pill-text">[區塊 4] 多角度圖鑑與定價 (Gallery &amp; Pricing)</text>
    <text x="110" y="625" font-family="sans-serif" font-weight="600" font-size="17.5px" fill="#f8fafc">多視角照片展示（正面/側面/情境） ＋  [標準版 $3,990] 與 [旗艦版 $5,990] 雙方案比較表</text>

    <!-- Block 5: Form & Footer -->
    <rect x="90" y="665" width="1420" height="100" rx="12" fill="#182030" stroke="#64748b" stroke-width="2"/>
    <rect x="110" y="680" width="380" height="36" rx="8" fill="#475569"/>
    <text x="300" y="704" class="pill-text">[區塊 5] 預購表單與頁尾 (Form &amp; Footer)</text>
    <text x="110" y="745" font-family="sans-serif" font-weight="600" font-size="17.5px" fill="#f8fafc">姓名/Email/電話線上表單輸入框  ＋  隱私保護政策  ＋  版權聲明與社群連結</text>
  </g>
"""

# ==============================================================================
# 5. ch2_interview_flow.svg (1600 x 780)
# ==============================================================================
content_5 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">「先問答、後動工」反向訪談法三部曲</text>
  <text x="800" y="78" class="subtitle">提示詞不用一次想破頭！請 AI 扮演顧問主動提問，像做選擇題一樣輕鬆敲定需求</text>

  <!-- Step 1 Card -->
  <g filter="url(#shadow)">
    <rect x="60" y="130" width="450" height="600" rx="18" fill="#151b2b" stroke="#6366f1" stroke-width="3"/>
    <rect x="80" y="150" width="410" height="52" rx="10" fill="#6366f1"/>
    <text x="285" y="182" class="card-title">步驟 1：啟動反向訪談</text>
    <text x="285" y="224" class="card-sub" fill="#a5b4fc">【叫 AI 先別急著寫程式！】</text>

    <rect x="80" y="245" width="410" height="455" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="105" y="285" font-family="sans-serif" font-weight="700" font-size="16px" fill="#a5b4fc">💬 使用者輸入開場白提示詞：</text>
    <text x="105" y="325" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">「我想做耳機銷售網頁，</text>
    <text x="105" y="358" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">  請先不要開始寫程式！</text>
    <text x="105" y="391" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">  請扮演網頁企劃顧問，</text>
    <text x="105" y="424" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">  向我提出 4 個關鍵問題</text>
    <text x="105" y="457" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">  並提供選項讓我挑選！」</text>

    <line x1="105" y1="500" x2="465" y2="500" stroke="#334155" stroke-width="1"/>
    <text x="105" y="540" font-family="sans-serif" font-weight="700" font-size="16px" fill="#f59e0b">⚡ 內建捷徑：直接輸入指令</text>
    <text x="105" y="575" font-family="sans-serif" font-weight="600" font-size="16px" fill="#38bdf8">/grill-me 我想做耳機網頁</text>
    <text x="105" y="620" class="item-desc">即可一鍵啟動互動式選擇題訪談！</text>
  </g>

  <!-- Vector Arrow 1 -->
  <polygon points="535,410 565,430 535,450" fill="#a5b4fc"/>

  <!-- Step 2 Card -->
  <g filter="url(#shadow)">
    <rect x="585" y="130" width="450" height="600" rx="18" fill="#0f1e30" stroke="#0ea5e9" stroke-width="3"/>
    <rect x="605" y="150" width="410" height="52" rx="10" fill="#0284c7"/>
    <text x="810" y="182" class="card-title">步驟 2：像做選擇題回答</text>
    <text x="810" y="224" class="card-sub" fill="#38bdf8">【快速挑選符合預期的選項】</text>

    <rect x="605" y="245" width="410" height="455" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="630" y="285" font-family="sans-serif" font-weight="700" font-size="16px" fill="#7dd3fc">🤖 AI 顧問逐一列出問題讓你挑：</text>
    <text x="630" y="325" font-family="sans-serif" font-weight="500" font-size="15.5px" fill="#e2e8f0">1. 配色：(A) 曜石黑  (B) 純白  (C) 霓虹？</text>
    <text x="630" y="365" font-family="sans-serif" font-weight="500" font-size="15.5px" fill="#e2e8f0">2. 賣點：主動降噪、超長續航、舒適？</text>
    <text x="630" y="405" font-family="sans-serif" font-weight="500" font-size="15.5px" fill="#e2e8f0">3. 方案：單一售價 vs 雙版本？</text>
    <text x="630" y="445" font-family="sans-serif" font-weight="500" font-size="15.5px" fill="#e2e8f0">4. 行動：填寫預購表單 vs 外部賣場？</text>

    <line x1="630" y1="485" x2="990" y2="485" stroke="#334155" stroke-width="1"/>
    <text x="630" y="525" font-family="sans-serif" font-weight="700" font-size="16px" fill="#34d399">👤 你只需輕鬆回覆幾個字：</text>
    <text x="630" y="565" font-family="sans-serif" font-weight="600" font-size="15.5px" fill="#f8fafc">「1選A曜石黑、2強調降噪與續航、</text>
    <text x="630" y="598" font-family="sans-serif" font-weight="600" font-size="15.5px" fill="#f8fafc">  3分標準/旗艦兩版、4填預購表單」</text>
    <text x="630" y="640" font-family="sans-serif" font-weight="600" font-size="14.5px" fill="#f59e0b">不用自己憋出一整篇規格，超省力！</text>
  </g>

  <!-- Vector Arrow 2 -->
  <polygon points="1060,410 1090,430 1060,450" fill="#38bdf8"/>

  <!-- Step 3 Card -->
  <g filter="url(#shadow)">
    <rect x="1110" y="130" width="430" height="600" rx="18" fill="#102820" stroke="#10b981" stroke-width="3"/>
    <rect x="1130" y="150" width="390" height="52" rx="10" fill="#059669"/>
    <text x="1325" y="182" class="card-title">步驟 3：精準生成成果</text>
    <text x="1325" y="224" class="card-sub" fill="#6ee7b7">【100% 貼合心中想像與期待】</text>

    <rect x="1130" y="245" width="390" height="455" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="1155" y="285" font-family="sans-serif" font-weight="700" font-size="16px" fill="#6ee7b7">🎉 AI 彙整規格確認書後一鍵動工：</text>
    <text x="1155" y="335" class="item-title">• 自動建立完整結構 index.html</text>
    <text x="1155" y="380" class="item-title">• 精準套用專案 PIC 資料夾耳機照片</text>
    <text x="1155" y="425" class="item-title">• 一次到位！產出完全不偏離預期</text>
    <text x="1155" y="470" class="item-title">• 程式碼結構乾淨、支援手機 RWD</text>

    <rect x="1155" y="530" width="340" height="120" rx="10" fill="#065f46"/>
    <text x="1325" y="575" font-family="sans-serif" font-weight="700" font-size="18px" fill="#ffffff" text-anchor="middle">🎯 巨大優勢：</text>
    <text x="1325" y="615" font-family="sans-serif" font-weight="700" font-size="17px" fill="#fde68a" text-anchor="middle">省下 80% 來回除錯與重做時間！</text>
  </g>
"""

# ==============================================================================
# 6. ch2_iterative_tuning.svg (1600 x 780)
# ==============================================================================
content_6 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">對話式迭代微調（Iterative Tuning）進化路徑</text>
  <text x="800" y="78" class="subtitle">生成第一版後不用自己改程式！動口說一句，AI 自動精準進行局部增量修復</text>

  <!-- Stage 1 Card -->
  <g filter="url(#shadow)">
    <rect x="60" y="130" width="450" height="600" rx="18" fill="#1e293b" stroke="#64748b" stroke-width="3"/>
    <rect x="80" y="150" width="410" height="52" rx="10" fill="#475569"/>
    <text x="285" y="182" class="card-title">階段 1：初版網頁 (V1 原型)</text>
    <text x="285" y="224" class="card-sub" fill="#cbd5e1">【基本骨架建立，待細緻打磨】</text>

    <!-- Item 1 -->
    <rect x="80" y="250" width="410" height="95" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="105" y="285" class="item-title">[骨架完成]</text>
    <text x="105" y="318" class="item-desc">已建立導覽、標題、耳機照片與預購表單</text>

    <!-- Item 2 -->
    <rect x="80" y="360" width="410" height="95" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="105" y="395" class="item-title">[細節不足]</text>
    <text x="105" y="428" class="item-desc">Hero 標題不夠突出、按鈕顏色偏暗缺動感</text>

    <!-- Item 3 -->
    <rect x="80" y="470" width="410" height="95" rx="10" fill="#0f172a" stroke="#475569" stroke-width="1"/>
    <text x="105" y="505" class="item-title">[區塊待補]</text>
    <text x="105" y="538" class="item-desc">缺少顧客好評背書與多角度耳機寫真展示</text>

    <!-- Bottom Status -->
    <rect x="80" y="590" width="410" height="95" rx="10" fill="#0f172a" stroke="#64748b" stroke-width="1.5"/>
    <text x="285" y="630" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#94a3b8" text-anchor="middle">評估：骨架正確，但缺乏商業轉單吸引力</text>
    <text x="285" y="660" font-family="sans-serif" font-weight="500" font-size="14.5px" fill="#cbd5e1" text-anchor="middle">➔ 準備向 AI 下達第 2 輪微調指令</text>
  </g>

  <!-- Vector Arrow 1 -->
  <polygon points="535,410 565,430 535,450" fill="#f59e0b"/>

  <!-- Stage 2 Card -->
  <g filter="url(#shadow)">
    <rect x="585" y="130" width="450" height="600" rx="18" fill="#2d1e0f" stroke="#f59e0b" stroke-width="3"/>
    <rect x="605" y="150" width="410" height="52" rx="10" fill="#d97706"/>
    <text x="810" y="182" class="card-title">階段 2：對話微調 (自然語言指令)</text>
    <text x="810" y="224" class="card-sub" fill="#fde68a">【動口不動手：針對細節下達指令】</text>

    <!-- Prompt 1 -->
    <rect x="605" y="250" width="410" height="130" rx="10" fill="#181e2c" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="630" y="285" font-family="sans-serif" font-weight="700" font-size="16px" fill="#f59e0b">[指令 1：視覺強化]</text>
    <text x="630" y="322" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">「請把 Hero 標題字體加大，</text>
    <text x="630" y="354" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">  並把按鈕改成亮橘色漸層按鈕！」</text>

    <!-- Prompt 2 -->
    <rect x="605" y="395" width="410" height="130" rx="10" fill="#181e2c" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="630" y="430" font-family="sans-serif" font-weight="700" font-size="16px" fill="#f59e0b">[指令 2：擴充區塊]</text>
    <text x="630" y="467" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">「請在產品特色後面加上 3 位顧客</text>
    <text x="630" y="499" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">  的五星好評推薦評價卡片！」</text>

    <!-- Prompt 3 -->
    <rect x="605" y="540" width="410" height="130" rx="10" fill="#181e2c" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="630" y="575" font-family="sans-serif" font-weight="700" font-size="16px" fill="#f59e0b">[指令 3：互動體驗]</text>
    <text x="630" y="612" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">「點擊預購按鈕時平滑捲動到表單，</text>
    <text x="630" y="644" font-family="sans-serif" font-weight="600" font-size="16px" fill="#f8fafc">  送出後跳出感謝訂閱的提示訊息！」</text>
  </g>

  <!-- Vector Arrow 2 -->
  <polygon points="1060,410 1090,430 1060,450" fill="#10b981"/>

  <!-- Stage 3 Card -->
  <g filter="url(#shadow)">
    <rect x="1110" y="130" width="430" height="600" rx="18" fill="#102820" stroke="#10b981" stroke-width="3"/>
    <rect x="1130" y="150" width="390" height="52" rx="10" fill="#059669"/>
    <text x="1325" y="182" class="card-title">階段 3：最終成品 (V2 商業旗艦版)</text>
    <text x="1325" y="224" class="card-sub" fill="#6ee7b7">【視覺精緻、高信任感與高轉換率】</text>

    <!-- Item 1 -->
    <rect x="1130" y="250" width="390" height="95" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="1155" y="285" class="item-title">[視覺層次豐富]</text>
    <text x="1155" y="318" class="item-desc">亮橘色發光 CTA 按鈕 ＋ 大器科技感標題</text>

    <!-- Item 2 -->
    <rect x="1130" y="360" width="390" height="95" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="1155" y="395" class="item-title">[完整信任背書]</text>
    <text x="1155" y="428" class="item-desc">五星好評評價卡片 ＋ 雙版本價格比較表</text>

    <!-- Item 3 -->
    <rect x="1130" y="470" width="390" height="95" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="1155" y="505" class="item-title">[流暢互動體驗]</text>
    <text x="1155" y="538" class="item-desc">平滑錨點捲動 ＋ 表單填寫即時驗證彈窗</text>

    <!-- Item 4 -->
    <rect x="1130" y="580" width="390" height="95" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="1155" y="615" class="item-title">[自適應 RWD]</text>
    <text x="1155" y="648" class="item-desc">電腦大螢幕與手機窄螢幕皆能完美呈現</text>
  </g>
"""

# Write out all 6 SVG files
files = [
    ("ch1_ide_layout.svg", 1600, 940, content_1),
    ("ch1_workspace_boundary.svg", 1600, 820, content_2),
    ("ch1_permission_modes.svg", 1600, 820, content_3),
    ("ch2_landing_page_anatomy.svg", 1600, 860, content_4),
    ("ch2_interview_flow.svg", 1600, 780, content_5),
    ("ch2_iterative_tuning.svg", 1600, 780, content_6),
]

for filename, w, h, body in files:
    full_path = os.path.join(pic_dir, filename)
    svg_code = svg_wrap(w, h, body)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(svg_code)
    print(f"Generated {filename} successfully ({len(svg_code)} bytes)")

print("ALL 6 SVG DIAGRAMS GENERATED WITH 100% PURE VECTOR TEXT!")
