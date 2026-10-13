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
      .card-sub {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 600; font-size: 15px; text-anchor: middle; }}
      .item-title {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 700; font-size: 17px; fill: #f8fafc; }}
      .item-desc {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 400; font-size: 14.5px; fill: #cbd5e1; }}
      .pill-text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft JhengHei", sans-serif; font-weight: 600; font-size: 13.5px; fill: #ffffff; text-anchor: middle; }}
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>
  <rect width="{width}" height="{height}" fill="#0b0f19"/>
{content}
</svg>"""

# ==============================================================================
# DIAGRAM 1: ch3_github_ecosystem.svg (1600 x 860)
# 教學目的：從本機開發到全球發布的完整生命週期架構圖
# ==============================================================================
content_1 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">從本機開發到全球發布：GitHub 運作全景圖</text>
  <text x="800" y="78" class="subtitle">為什麼我們需要 GitHub？串聯「本機工作區」與「全球公開網站」的關鍵橋樑</text>

  <!-- Step 1: Local PC -->
  <g filter="url(#shadow)">
    <rect x="60" y="130" width="440" height="680" rx="18" fill="#151b2b" stroke="#6366f1" stroke-width="3"/>
    <rect x="80" y="150" width="400" height="52" rx="10" fill="#6366f1"/>
    <text x="280" y="182" class="card-title">① 本機開發環境 (Local PC)</text>
    <text x="280" y="224" class="card-sub" fill="#a5b4fc">【你的電腦與 Antigravity】</text>

    <!-- Content 1 -->
    <rect x="80" y="245" width="400" height="110" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="105" y="280" class="item-title">💻 Antigravity 專案資料夾</text>
    <text x="105" y="310" class="item-desc">位於本地硬碟：C:\\Antigravity\\web-demo\\</text>
    <text x="105" y="335" class="item-desc">包含 index.html、style.css 與 PIC/ 照片</text>

    <!-- Content 2 -->
    <rect x="80" y="375" width="400" height="110" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="105" y="410" class="item-title">💾 本地 Git 版本控制 (Commit)</text>
    <text x="105" y="440" class="item-desc">建立時光機存檔點，記錄每次修改</text>
    <text x="105" y="465" class="item-desc">即使改壞也能一鍵安全復原</text>

    <!-- Bottleneck Alert -->
    <rect x="80" y="505" width="400" height="140" rx="12" fill="#3c1923" stroke="#f43f5e" stroke-width="1.5"/>
    <text x="105" y="540" font-family="sans-serif" font-weight="700" font-size="16px" fill="#fb7185">⚠️ 遇到的瓶頸痛點：</text>
    <text x="105" y="572" class="item-desc">• 目前網頁只有「你自己」的電腦看得到</text>
    <text x="105" y="602" class="item-desc">• 無法傳送網址給朋友、客戶或主管瀏覽</text>
    <text x="105" y="632" class="item-desc">• 電腦一旦關機或硬碟損毀，檔案就消失！</text>

    <!-- Action Arrow Box -->
    <rect x="80" y="665" width="400" height="60" rx="10" fill="#4f46e5"/>
    <text x="280" y="702" font-family="sans-serif" font-weight="700" font-size="16px" fill="#ffffff" text-anchor="middle">準備執行：git push 同步上雲端 ➔</text>
  </g>

  <!-- Vector Arrow 1 -->
  <polygon points="525,440 555,460 525,480" fill="#6366f1"/>

  <!-- Step 2: GitHub Cloud -->
  <g filter="url(#shadow)">
    <rect x="580" y="130" width="440" height="680" rx="18" fill="#0f1e30" stroke="#0ea5e9" stroke-width="3"/>
    <rect x="600" y="150" width="400" height="52" rx="10" fill="#0284c7"/>
    <text x="800" y="182" class="card-title">② GitHub 雲端代管 (Cloud Hub)</text>
    <text x="800" y="224" class="card-sub" fill="#38bdf8">【全球最大的程式碼雲端保險箱】</text>

    <!-- Content 1 -->
    <rect x="600" y="245" width="400" height="110" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="625" y="280" class="item-title">☁️ 雲端儲存庫 (Repository / Repo)</text>
    <text x="625" y="310" class="item-desc">永不遺失的專案雲端備份</text>
    <text x="625" y="335" class="item-desc">無論換電腦、重灌都能隨時抓取回來</text>

    <!-- Content 2 -->
    <rect x="600" y="375" width="400" height="110" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="625" y="410" class="item-title">🤖 與 AI 助理 (Antigravity) 串接</text>
    <text x="625" y="440" class="item-desc">支援 GitHub CLI 授權登入 (gh auth login)</text>
    <text x="625" y="465" class="item-desc">讓 AI 能替你自主自動推播更新</text>

    <!-- Value box -->
    <rect x="600" y="505" width="400" height="140" rx="12" fill="#0c4a6e" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="625" y="540" font-family="sans-serif" font-weight="700" font-size="16px" fill="#7dd3fc">✨ 核心價值解鎖：</text>
    <text x="625" y="572" class="item-desc">• 全球 1 億＋ 開發者與頂尖科技公司採用</text>
    <text x="625" y="602" class="item-desc">• 完整的版本時間軸，記錄誰在何時改了碼</text>
    <text x="625" y="632" class="item-desc">• 免費享有強大的持續整合與網站託管！</text>

    <!-- Action Arrow Box -->
    <rect x="600" y="665" width="400" height="60" rx="10" fill="#0369a1"/>
    <text x="800" y="702" font-family="sans-serif" font-weight="700" font-size="16px" fill="#ffffff" text-anchor="middle">啟動託管：開啟 GitHub Pages ➔</text>
  </g>

  <!-- Vector Arrow 2 -->
  <polygon points="1045,440 1075,460 1045,480" fill="#0ea5e9"/>

  <!-- Step 3: Public Website -->
  <g filter="url(#shadow)">
    <rect x="1100" y="130" width="440" height="680" rx="18" fill="#102820" stroke="#10b981" stroke-width="3"/>
    <rect x="1120" y="150" width="400" height="52" rx="10" fill="#059669"/>
    <text x="1320" y="182" class="card-title">③ 全球公開網頁 (GitHub Pages)</text>
    <text x="1320" y="224" class="card-sub" fill="#6ee7b7">【全世界只要有網址都能連上】</text>

    <!-- Content 1 -->
    <rect x="1120" y="245" width="400" height="110" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="1145" y="280" class="item-title">🌐 免費專屬 HTTPS 商業網址</text>
    <text x="1145" y="310" class="item-desc">內建 SSL 安全憑證，瀏覽器不跳警告</text>
    <text x="1145" y="335" class="item-desc">格式：https://[帳號].github.io/[專案名]/</text>

    <!-- Content 2 -->
    <rect x="1120" y="375" width="400" height="110" rx="12" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="1145" y="410" class="item-title">⚡ 全球 CDN 極速自動分發</text>
    <text x="1145" y="440" class="item-desc">微軟與 GitHub 雲端全球機房加速</text>
    <text x="1145" y="465" class="item-desc">手機、平板、電腦開網頁秒載入！</text>

    <!-- Result Banner -->
    <rect x="1120" y="505" width="400" height="140" rx="12" fill="#064e3b" stroke="#34d399" stroke-width="1.5"/>
    <text x="1145" y="540" font-family="sans-serif" font-weight="700" font-size="16px" fill="#6ee7b7">🎉 最終達成目標：</text>
    <text x="1145" y="572" class="item-desc">• 你的降噪耳機銷售官網正式上線開賣！</text>
    <text x="1145" y="602" class="item-desc">• 可直接貼到 LINE、FB、IG 讓客戶下單</text>
    <text x="1145" y="632" class="item-desc">• 免租用主機、免買網址，0 成本營運！</text>

    <!-- Milestone Box -->
    <rect x="1120" y="665" width="400" height="60" rx="10" fill="#047857"/>
    <text x="1320" y="702" font-family="sans-serif" font-weight="700" font-size="16px" fill="#ffffff" text-anchor="middle">成就達成：正式成為線上網站站長！</text>
  </g>
"""

# ==============================================================================
# DIAGRAM 2: ch3_signup_and_url.svg (1600 x 820)
# 教學目的：Google 一鍵註冊流程 ＋ Username 網址結構解密
# ==============================================================================
content_2 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">GitHub 快速註冊與 Username 網址結構解密</text>
  <text x="800" y="78" class="subtitle">推薦 Continue with Google 註冊方式，並掌握影響一輩子網址的 Username 命名原則</text>

  <!-- Left Card: Google Signup Steps -->
  <g filter="url(#shadow)">
    <rect x="60" y="130" width="710" height="640" rx="18" fill="#151b2b" stroke="#6366f1" stroke-width="3"/>
    <rect x="80" y="150" width="670" height="56" rx="12" fill="#4f46e5"/>
    <text x="415" y="186" class="card-title">🚀 推薦註冊方式：Continue with Google (一鍵授權)</text>

    <!-- Step 1 -->
    <rect x="85" y="230" width="660" height="85" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="110" y="265" class="item-title">[步驟 1] 前往官網點選「Continue with Google」</text>
    <text x="110" y="295" class="item-desc">網址：github.com/signup ➔ 點選 Google 圖示免去繁瑣輸入信箱流程</text>

    <!-- Step 2 -->
    <rect x="85" y="330" width="660" height="85" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="110" y="365" class="item-title">[步驟 2] 務必挑選「個人長期持有的 Gmail 帳號」</text>
    <text x="110" y="395" class="item-desc">避免使用學校 (.edu) 或公司帳號，畢業離職帳號被收回將導致作品遺失！</text>

    <!-- Step 3 -->
    <rect x="85" y="430" width="660" height="85" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="110" y="465" class="item-title">[步驟 3] 註冊後到 Settings 補設「獨立專用密碼」</text>
    <text x="110" y="495" class="item-desc">方便第 4 章在命令列終端機透過 GitHub CLI (gh auth login) 自動發布</text>

    <!-- Step 4 -->
    <rect x="85" y="530" width="660" height="85" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1.5"/>
    <text x="110" y="565" class="item-title">[步驟 4] 開啟 2FA 雙重身分驗證 (強制安全政策)</text>
    <text x="110" y="595" class="item-desc">使用 Google Authenticator 或 Microsoft Authenticator 手機 App 綁定保護</text>

    <!-- Bottom summary -->
    <rect x="85" y="635" width="660" height="55" rx="10" fill="#312e81"/>
    <text x="415" y="670" font-family="sans-serif" font-weight="700" font-size="16px" fill="#c7d2fe" text-anchor="middle">💡 效益：30 秒快速通關，安全有保障！</text>
  </g>

  <!-- Right Card: URL Structure Anatomy -->
  <g filter="url(#shadow)">
    <rect x="830" y="130" width="710" height="640" rx="18" fill="#0f1e30" stroke="#0ea5e9" stroke-width="3"/>
    <rect x="850" y="150" width="670" height="56" rx="12" fill="#0284c7"/>
    <text x="1185" y="186" class="card-title">🔍 重要！你的 Username 如何決定未來的官方網址？</text>

    <!-- Big URL Breakdown Box -->
    <rect x="855" y="230" width="660" height="150" rx="12" fill="#0f172a" stroke="#0ea5e9" stroke-width="2"/>
    <text x="1185" y="270" font-family="sans-serif" font-weight="700" font-size="15px" fill="#7dd3fc" text-anchor="middle">【 GitHub Pages 網站網址解剖公式 】</text>
    
    <!-- URL Components -->
    <rect x="880" y="295" width="610" height="60" rx="8" fill="#1e293b"/>
    <text x="900" y="333" font-family="Courier New, monospace" font-weight="700" font-size="17px" fill="#94a3b8">https://</text>
    <text x="990" y="333" font-family="Courier New, monospace" font-weight="700" font-size="20px" fill="#38bdf8">your-name</text>
    <text x="1105" y="333" font-family="Courier New, monospace" font-weight="700" font-size="17px" fill="#94a3b8">.github.io/</text>
    <text x="1225" y="333" font-family="Courier New, monospace" font-weight="700" font-size="20px" fill="#34d399">my-product</text>
    <text x="1355" y="333" font-family="Courier New, monospace" font-weight="700" font-size="17px" fill="#94a3b8">/</text>

    <!-- Component Explanations -->
    <rect x="855" y="400" width="660" height="100" rx="10" fill="#162e44" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="880" y="435" font-family="sans-serif" font-weight="700" font-size="17px" fill="#38bdf8">🔹 前段：your-name（你的 GitHub Username）</text>
    <text x="880" y="465" class="item-desc">• 代表你的個人/品牌網域，永久固定於 github.io 之前</text>
    <text x="880" y="488" class="item-desc">• 命名原則：簡短、好記、純英文小寫與數字，避免複雜亂碼！</text>

    <rect x="855" y="515" width="660" height="100" rx="10" fill="#14362a" stroke="#10b981" stroke-width="1.5"/>
    <text x="880" y="550" font-family="sans-serif" font-weight="700" font-size="17px" fill="#34d399">🔹 後段：my-product（你的專案 Repo 名稱）</text>
    <text x="880" y="580" class="item-desc">• 代表此網站的專案名稱（例如：smart-headphone、landing-demo）</text>
    <text x="880" y="603" class="item-desc">• 一個帳號可以建立無數個不同 Repo，擁有無數個專屬網站！</text>

    <!-- Good vs Bad Example -->
    <rect x="855" y="635" width="660" height="55" rx="10" fill="#0c4a6e"/>
    <text x="1185" y="670" font-family="sans-serif" font-weight="700" font-size="15.5px" fill="#ffffff" text-anchor="middle">✔ 好名字：alex-dev、clive-tw  ｜  ✖ 避免：user129384_xyz99</text>
  </g>
"""

# ==============================================================================
# DIAGRAM 3: ch3_core_concepts.svg (1600 x 840)
# 教學目的：GitHub 4 大核心術語白話對照圖（文組也能秒懂）
# ==============================================================================
content_3 = """
  <!-- Top Banner -->
  <rect x="0" y="0" width="1600" height="96" fill="#0f172a"/>
  <line x1="0" y1="96" x2="1600" y2="96" stroke="#334155" stroke-width="2"/>
  <text x="800" y="44" class="title">GitHub 4 大核心術語白話對照圖</text>
  <text x="800" y="78" class="subtitle">不要被英文名詞嚇到！用生活中的譬喻，30 秒輕鬆掌握版本控制與發布核心概念</text>

  <!-- 4 Cards Grid (2 x 2) -->

  <!-- CARD 1: Repository -->
  <g filter="url(#shadow)">
    <rect x="60" y="130" width="710" height="315" rx="16" fill="#151b2b" stroke="#6366f1" stroke-width="2.5"/>
    <rect x="80" y="150" width="670" height="48" rx="10" fill="#6366f1"/>
    <text x="415" y="181" class="card-title">1. Repository（儲存庫 / 簡稱 Repo）</text>

    <rect x="85" y="215" width="660" height="55" rx="8" fill="#312e81"/>
    <text x="415" y="249" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#c7d2fe" text-anchor="middle">💡 生活白話比喻：【雲端專屬置物櫃 / 雲端專案資料夾】</text>

    <text x="110" y="305" font-family="sans-serif" font-weight="600" font-size="16.5px" fill="#f8fafc">• 專門用來存放你「某一個特定網站或專案」所有檔案的雲端空間。</text>
    <text x="110" y="340" class="item-desc">• 一個 Repo 就是一個獨立資料夾，裡面有 HTML、CSS、JS 與照片。</text>
    <text x="110" y="375" class="item-desc">• 可以設定為「公開（Public，讓大家看網頁）」或「私有（Private，自己看）」。</text>
    <text x="110" y="410" font-family="sans-serif" font-weight="600" font-size="15px" fill="#a5b4fc">➔ 本課實例：我們建立一個名為 antigravity-course 的 Repo 來放耳機網站！</text>
  </g>

  <!-- CARD 2: Commit -->
  <g filter="url(#shadow)">
    <rect x="830" y="130" width="710" height="315" rx="16" fill="#0f1e30" stroke="#0ea5e9" stroke-width="2.5"/>
    <rect x="850" y="150" width="670" height="48" rx="10" fill="#0284c7"/>
    <text x="1185" y="181" class="card-title">2. Commit（提交 / 歷史存檔點）</text>

    <rect x="855" y="215" width="660" height="55" rx="8" fill="#0c4a6e"/>
    <text x="1185" y="249" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#bae6fd" text-anchor="middle">💡 生活白話比喻：【遊戲存檔點（Save Point）+ 時光機標籤】</text>

    <text x="880" y="305" font-family="sans-serif" font-weight="600" font-size="16.5px" fill="#f8fafc">• 記錄「誰、在什麼時候、修改了哪些程式碼」的一張歷史快照紀錄。</text>
    <text x="880" y="340" class="item-desc">• 每次存檔時都附帶一句訊息（如「完成耳機 Hero 區塊」、「換新圖」）。</text>
    <text x="880" y="375" class="item-desc">• 如果改壞了版面，隨時可以點擊歷史紀錄「一鍵坐時光機還原」。</text>
    <text x="880" y="410" font-family="sans-serif" font-weight="600" font-size="15px" fill="#7dd3fc">➔ 本課實例：每次叫 Antigravity 改完網頁，它都會自動幫你建立 Commit！</text>
  </g>

  <!-- CARD 3: Push -->
  <g filter="url(#shadow)">
    <rect x="60" y="475" width="710" height="315" rx="16" fill="#2d1e0f" stroke="#f59e0b" stroke-width="2.5"/>
    <rect x="80" y="495" width="670" height="48" rx="10" fill="#d97706"/>
    <text x="415" y="526" class="card-title">3. Push（推送 / 雲端同步上傳）</text>

    <rect x="85" y="560" width="660" height="55" rx="8" fill="#78350f"/>
    <text x="415" y="594" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#fde68a" text-anchor="middle">💡 生活白話比喻：【按下『同步到雲端』按鈕（Upload to Cloud）】</text>

    <text x="110" y="650" font-family="sans-serif" font-weight="600" font-size="16.5px" fill="#f8fafc">• 把你在本機電腦裡存好的 Commit 存檔點，正式傳送到 GitHub 雲端。</text>
    <text x="110" y="685" class="item-desc">• 只要沒有 Push，你的所有修改都只留在本機，雲端跟別人都看不到。</text>
    <text x="110" y="720" class="item-desc">• 一旦 Push 成功，雲端資料庫瞬間同步更新，永久安全備份。</text>
    <text x="110" y="755" font-family="sans-serif" font-weight="600" font-size="15px" fill="#fde68a">➔ 本課實例：終端機執行 git push，即可把剛做好的產品頁秒傳到 GitHub！</text>
  </g>

  <!-- CARD 4: GitHub Pages -->
  <g filter="url(#shadow)">
    <rect x="830" y="475" width="710" height="315" rx="16" fill="#102820" stroke="#10b981" stroke-width="2.5"/>
    <rect x="850" y="495" width="670" height="48" rx="10" fill="#059669"/>
    <text x="1185" y="526" class="card-title">4. GitHub Pages（全球免費網站託管主機）</text>

    <rect x="855" y="560" width="660" height="55" rx="8" fill="#064e3b"/>
    <text x="1185" y="594" font-family="sans-serif" font-weight="700" font-size="16.5px" fill="#6ee7b7" text-anchor="middle">💡 生活白話比喻：【免費的全球 24 小時開張店面 ＋ 專屬門牌】</text>

    <text x="880" y="650" font-family="sans-serif" font-weight="600" font-size="16.5px" fill="#f8fafc">• GitHub 贈送給每位開發者的頂級福利：免費靜態網站伺服器！</text>
    <text x="880" y="685" class="item-desc">• 免買網址、免租虛擬主機、免設定 Linux 伺服器、內建 HTTPS 加密。</text>
    <text x="880" y="720" class="item-desc">• 只要將 Repo 的 main 分支開啟 Pages，全世界任何人都能立即造訪！</text>
    <text x="880" y="755" font-family="sans-serif" font-weight="600" font-size="15px" fill="#6ee7b7">➔ 本課實例：第 4 章我們將利用 GitHub CLI 一秒開啟 Pages，讓耳機官網上線！</text>
  </g>
"""

# Write out files
files = [
    ("ch3_github_ecosystem.svg", 1600, 860, content_1),
    ("ch3_signup_and_url.svg", 1600, 820, content_2),
    ("ch3_core_concepts.svg", 1600, 840, content_3),
]

for filename, w, h, body in files:
    full_path = os.path.join(pic_dir, filename)
    svg_code = svg_wrap(w, h, body)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(svg_code)
    print(f"Generated {filename} successfully ({len(svg_code)} bytes)")

print("ALL CHAPTER 3 SVG DIAGRAMS GENERATED SUCCESSFULLY!")
