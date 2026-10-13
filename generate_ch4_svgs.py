import os

# Ensure PIC directory exists
os.makedirs("PIC", exist_ok=True)

# -------------------------------------------------------------------------
# SVG 1: ch4_manual_vs_cli.svg (1600 x 880)
# -------------------------------------------------------------------------
svg1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 880" width="1600" height="880">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="card-red" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(30, 41, 59, 0.9)"/>
      <stop offset="100%" stop-color="rgba(244, 63, 94, 0.08)"/>
    </linearGradient>
    <linearGradient id="card-green" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="rgba(30, 41, 59, 0.9)"/>
      <stop offset="100%" stop-color="rgba(56, 189, 248, 0.12)"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="8" stdDeviation="10" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1600" height="880" fill="url(#bg-grad)"/>

  <!-- Grid decoration -->
  <g opacity="0.05" stroke="#ffffff" stroke-width="1">
    <line x1="0" y1="110" x2="1600" y2="110"/>
    <line x1="0" y1="220" x2="1600" y2="220"/>
    <line x1="0" y1="330" x2="1600" y2="330"/>
    <line x1="0" y1="440" x2="1600" y2="440"/>
    <line x1="0" y1="550" x2="1600" y2="550"/>
    <line x1="0" y1="660" x2="1600" y2="660"/>
    <line x1="0" y1="770" x2="1600" y2="770"/>
    <line x1="200" y1="0" x2="200" y2="880"/>
    <line x1="400" y1="0" x2="400" y2="880"/>
    <line x1="600" y1="0" x2="600" y2="880"/>
    <line x1="800" y1="0" x2="800" y2="880"/>
    <line x1="1000" y1="0" x2="1000" y2="880"/>
    <line x1="1200" y1="0" x2="1200" y2="880"/>
    <line x1="1400" y1="0" x2="1400" y2="880"/>
  </g>

  <!-- Header -->
  <g transform="translate(80, 50)">
    <rect x="0" y="0" width="130" height="28" rx="14" fill="#38bdf8" fill-opacity="0.15"/>
    <text x="65" y="19" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">第 4 章 · 發布方式對比</text>
    <text x="0" y="60" fill="#f8fafc" font-size="28" font-weight="800" font-family="system-ui, sans-serif">傳統手動網頁發布 vs. Antigravity + CLI 自動化一鍵上線</text>
    <text x="0" y="88" fill="#94a3b8" font-size="15" font-family="system-ui, sans-serif">比較手動 7 步繁複網頁操作與 AI 對話一鍵發布，看見效率躍升 90% 的關鍵優勢</text>
  </g>

  <!-- Left: Traditional Manual Panel -->
  <g transform="translate(80, 165)">
    <rect width="690" height="580" rx="16" fill="url(#card-red)" stroke="#f43f5e" stroke-width="1.5" stroke-opacity="0.4" filter="url(#shadow)"/>
    
    <!-- Top badge -->
    <rect x="30" y="24" width="140" height="30" rx="6" fill="#f43f5e" fill-opacity="0.2"/>
    <text x="100" y="44" fill="#f43f5e" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">[ 傳統手動模式 ]</text>
    <text x="185" y="44" fill="#cbd5e1" font-size="15" font-weight="600" font-family="system-ui, sans-serif">繁瑣步驟與高錯誤率</text>

    <!-- Manual Steps List -->
    <g transform="translate(30, 75)">
      <!-- Step 1 -->
      <g transform="translate(0, 0)">
        <circle cx="16" cy="16" r="16" fill="#ef4444" fill-opacity="0.25"/>
        <text x="16" y="21" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">1</text>
        <text x="44" y="21" fill="#f1f5f9" font-size="14" font-weight="600" font-family="system-ui, sans-serif">開啟瀏覽器登入 GitHub 官網</text>
      </g>
      <!-- Step 2 -->
      <g transform="translate(0, 48)">
        <circle cx="16" cy="16" r="16" fill="#ef4444" fill-opacity="0.25"/>
        <text x="16" y="21" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">2</text>
        <text x="44" y="21" fill="#f1f5f9" font-size="14" font-weight="600" font-family="system-ui, sans-serif">點擊右上角 New 建立新的空白儲存庫</text>
      </g>
      <!-- Step 3 -->
      <g transform="translate(0, 96)">
        <circle cx="16" cy="16" r="16" fill="#ef4444" fill-opacity="0.25"/>
        <text x="16" y="21" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">3</text>
        <text x="44" y="21" fill="#f1f5f9" font-size="14" font-weight="600" font-family="system-ui, sans-serif">手動填寫 Repository 名稱、勾選 Public、按確認</text>
      </g>
      <!-- Step 4 -->
      <g transform="translate(0, 144)">
        <circle cx="16" cy="16" r="16" fill="#ef4444" fill-opacity="0.25"/>
        <text x="16" y="21" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">4</text>
        <text x="44" y="21" fill="#f1f5f9" font-size="14" font-weight="600" font-family="system-ui, sans-serif">切換回本機終端機，手動輸入 5~6 行 Git 指令</text>
        <text x="44" y="42" fill="#94a3b8" font-size="12" font-family="'JetBrains Mono', monospace">git remote add / git branch -M / git push -u ...</text>
      </g>
      <!-- Step 5 -->
      <g transform="translate(0, 206)">
        <circle cx="16" cy="16" r="16" fill="#ef4444" fill-opacity="0.25"/>
        <text x="16" y="21" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">5</text>
        <text x="44" y="21" fill="#f1f5f9" font-size="14" font-weight="600" font-family="system-ui, sans-serif">推送成功後，再次切換回瀏覽器專案首頁</text>
      </g>
      <!-- Step 6 -->
      <g transform="translate(0, 254)">
        <circle cx="16" cy="16" r="16" fill="#ef4444" fill-opacity="0.25"/>
        <text x="16" y="21" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">6</text>
        <text x="44" y="21" fill="#f1f5f9" font-size="14" font-weight="600" font-family="system-ui, sans-serif">點擊 Settings ➔ 尋找 Pages 選單 ➔ 選擇 Branch 儲存</text>
      </g>
      <!-- Step 7 -->
      <g transform="translate(0, 302)">
        <circle cx="16" cy="16" r="16" fill="#ef4444" fill-opacity="0.25"/>
        <text x="16" y="21" fill="#f87171" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">7</text>
        <text x="44" y="21" fill="#f1f5f9" font-size="14" font-weight="600" font-family="system-ui, sans-serif">重新整理網頁 3~5 次等待部署完成，手動複製網址</text>
      </g>
    </g>

    <!-- Disadvantage Summary Box -->
    <rect x="30" y="445" width="630" height="105" rx="10" fill="#0f172a" stroke="#f43f5e" stroke-width="1" stroke-opacity="0.3"/>
    <text x="50" y="475" fill="#f87171" font-size="14" font-weight="700" font-family="system-ui, sans-serif">[ 痛點總結 ]</text>
    <text x="50" y="502" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 耗時：約 8 ~ 10 分鐘，視窗反覆切換容易漏步</text>
    <text x="50" y="526" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 挫折感：初學者常卡在 remote 網址打錯或 Pages 分支未選</text>
  </g>

  <!-- Right: Antigravity + CLI Panel -->
  <g transform="translate(830, 165)">
    <rect width="690" height="580" rx="16" fill="url(#card-green)" stroke="#38bdf8" stroke-width="2" filter="url(#shadow)"/>
    
    <!-- Top badge -->
    <rect x="30" y="24" width="165" height="30" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="112" y="44" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">[ Antigravity + CLI ]</text>
    <text x="210" y="44" fill="#38bdf8" font-size="15" font-weight="700" font-family="system-ui, sans-serif">自然語言對話 · 全自動一鍵搞定</text>

    <!-- AI Steps -->
    <g transform="translate(30, 75)">
      <!-- AI Step 1: Speak -->
      <g transform="translate(0, 0)">
        <circle cx="18" cy="18" r="18" fill="#38bdf8" fill-opacity="0.25"/>
        <text x="18" y="24" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">1</text>
        <text x="48" y="20" fill="#f8fafc" font-size="15" font-weight="700" font-family="system-ui, sans-serif">學員只要在對話框動口說一句話：</text>
        <rect x="48" y="32" width="580" height="60" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1" stroke-opacity="0.4"/>
        <text x="64" y="56" fill="#38bdf8" font-size="13" font-weight="600" font-family="system-ui, sans-serif">"幫我把耳機網頁推到 GitHub 上面，建立 repo 並開啟 Pages 網址！"</text>
        <text x="64" y="78" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">完全不需記憶複雜的 Git / GitHub 命令語法</text>
      </g>

      <!-- AI Step 2: Background execution -->
      <g transform="translate(0, 115)">
        <circle cx="18" cy="18" r="18" fill="#38bdf8" fill-opacity="0.25"/>
        <text x="18" y="24" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">2</text>
        <text x="48" y="20" fill="#f8fafc" font-size="15" font-weight="700" font-family="system-ui, sans-serif">Antigravity 在背景終端機自動流水線執行：</text>
        <rect x="48" y="32" width="580" height="96" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
        <text x="64" y="56" fill="#34d399" font-size="12" font-family="'JetBrains Mono', monospace">✔ git init &amp;&amp; git add . &amp;&amp; git commit -m "Initial commit"</text>
        <text x="64" y="80" fill="#38bdf8" font-size="12" font-family="'JetBrains Mono', monospace">✔ gh repo create smartsound-page --public --push</text>
        <text x="64" y="104" fill="#818cf8" font-size="12" font-family="'JetBrains Mono', monospace">✔ gh api repos/:owner/:repo/pages (啟用託管服務)</text>
      </g>

      <!-- AI Step 3: Direct URL return -->
      <g transform="translate(0, 265)">
        <circle cx="18" cy="18" r="18" fill="#34d399" fill-opacity="0.25"/>
        <text x="18" y="24" fill="#34d399" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">3</text>
        <text x="48" y="20" fill="#f8fafc" font-size="15" font-weight="700" font-family="system-ui, sans-serif">AI 在對話框直接印出全球專屬上線網址！</text>
        <rect x="48" y="32" width="580" height="48" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1.2"/>
        <text x="64" y="62" fill="#a7f3d0" font-size="14" font-weight="700" font-family="system-ui, sans-serif">🌐 https://&lt;你的帳號&gt;.github.io/smartsound-page/</text>
      </g>
    </g>

    <!-- Advantage Summary Box -->
    <rect x="30" y="445" width="630" height="105" rx="10" fill="#0f172a" stroke="#34d399" stroke-width="1" stroke-opacity="0.4"/>
    <text x="50" y="475" fill="#34d399" font-size="14" font-weight="700" font-family="system-ui, sans-serif">[ 核心優勢 ]</text>
    <text x="50" y="502" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 極速體驗：全程僅需 10 秒，動口完成所有操作</text>
    <text x="50" y="526" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 零挫折感：自動建立 Repository、配置 Pages 分支並驗證連線</text>
  </g>

  <!-- Bottom Global Banner -->
  <g transform="translate(80, 770)">
    <rect width="1440" height="60" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="40" y="36" fill="#f8fafc" font-size="15" font-weight="600" font-family="system-ui, sans-serif">💡 結論：使用 GitHub CLI 將開發者繁瑣的網頁操作完全抽象化，配合 Antigravity 的終端機代理能力，實現真正「動口即上線」！</text>
  </g>
</svg>'''

# -------------------------------------------------------------------------
# SVG 2: ch4_device_flow_auth.svg (1600 x 880)
# -------------------------------------------------------------------------
svg2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 880" width="1600" height="880">
  <defs>
    <linearGradient id="bg-grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="card-grad2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1600" height="880" fill="url(#bg-grad2)"/>

  <!-- Header -->
  <g transform="translate(80, 50)">
    <rect x="0" y="0" width="140" height="28" rx="14" fill="#818cf8" fill-opacity="0.15"/>
    <text x="70" y="19" fill="#818cf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">第 4 章 · 安全授權機制</text>
    <text x="0" y="60" fill="#f8fafc" font-size="28" font-weight="800" font-family="system-ui, sans-serif">GitHub CLI 8 碼代碼安全配對流程（Device Activation）</text>
    <text x="0" y="88" fill="#94a3b8" font-size="15" font-family="system-ui, sans-serif">零密碼外洩！了解 Antigravity 如何透過官方 OAuth Device Flow 安全取得倉庫操作權限</text>
  </g>

  <!-- 4 Step Flow Cards -->
  <!-- Step 1: Terminal trigger -->
  <g transform="translate(80, 165)">
    <rect width="325" height="440" rx="14" fill="url(#card-grad2)" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="80" height="26" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="60" y="38" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 1</text>
    <text x="20" y="75" fill="#f8fafc" font-size="18" font-weight="700" font-family="system-ui, sans-serif">AI 觸發授權指令</text>
    <text x="20" y="102" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">終端機產生一次性安全代碼</text>

    <!-- Terminal preview box -->
    <rect x="18" y="130" width="289" height="200" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <!-- Terminal header dots -->
    <circle cx="34" cy="148" r="4.5" fill="#ef4444"/>
    <circle cx="48" cy="148" r="4.5" fill="#f59e0b"/>
    <circle cx="62" cy="148" r="4.5" fill="#10b981"/>
    <text x="80" y="152" fill="#64748b" font-size="11" font-family="'JetBrains Mono', monospace">Terminal (gh auth)</text>
    <text x="28" y="185" fill="#38bdf8" font-size="12" font-family="'JetBrains Mono', monospace">$ gh auth login</text>
    <text x="28" y="210" fill="#94a3b8" font-size="11" font-family="'JetBrains Mono', monospace">? How would you like to auth?</text>
    <text x="28" y="230" fill="#34d399" font-size="11" font-family="'JetBrains Mono', monospace">> Login with a web browser</text>
    <text x="28" y="260" fill="#f59e0b" font-size="11" font-weight="700" font-family="'JetBrains Mono', monospace">! First copy one-time code:</text>
    <rect x="28" y="272" width="160" height="34" rx="4" fill="#1e1b4b" stroke="#818cf8" stroke-width="1"/>
    <text x="108" y="295" fill="#38bdf8" font-size="15" font-weight="700" text-anchor="middle" font-family="'JetBrains Mono', monospace">ABCD-1234</text>

    <text x="20" y="360" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 系統生成 8 位英數代碼</text>
    <text x="20" y="385" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 代碼僅具 15 分鐘時效性</text>
    <text x="20" y="410" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 密碼全程不經過終端機</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <g transform="translate(415, 370)">
    <polygon points="0,0 20,10 0,20" fill="#38bdf8"/>
  </g>

  <!-- Step 2: Browser Activation -->
  <g transform="translate(445, 165)">
    <rect width="325" height="440" rx="14" fill="url(#card-grad2)" stroke="#818cf8" stroke-width="1.5" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="80" height="26" rx="6" fill="#818cf8" fill-opacity="0.2"/>
    <text x="60" y="38" fill="#818cf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 2</text>
    <text x="20" y="75" fill="#f8fafc" font-size="18" font-weight="700" font-family="system-ui, sans-serif">瀏覽器開啟驗證頁</text>
    <text x="20" y="102" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">前往 GitHub 官方 Device 頁面</text>

    <!-- Browser mockup -->
    <rect x="18" y="130" width="289" height="200" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <!-- Browser tab -->
    <rect x="18" y="130" width="289" height="28" rx="8" fill="#1e293b"/>
    <circle cx="34" cy="144" r="4" fill="#64748b"/>
    <circle cx="46" cy="144" r="4" fill="#64748b"/>
    <rect x="65" y="135" width="220" height="18" rx="4" fill="#0f172a"/>
    <text x="75" y="148" fill="#94a3b8" font-size="10" font-family="'JetBrains Mono', monospace">github.com/login/device</text>
    
    <text x="162" y="185" fill="#f8fafc" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Device Activation</text>
    <text x="162" y="205" fill="#94a3b8" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">輸入剛才終端機顯示的代碼：</text>
    <rect x="45" y="218" width="235" height="42" rx="6" fill="#020617" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="162" y="246" fill="#38bdf8" font-size="16" font-weight="700" text-anchor="middle" font-family="'JetBrains Mono', monospace">ABCD - 1234</text>
    <rect x="85" y="275" width="155" height="30" rx="6" fill="#2563eb"/>
    <text x="162" y="295" fill="#ffffff" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">Continue ➔</text>

    <text x="20" y="360" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 系統自動打開預設瀏覽器</text>
    <text x="20" y="385" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 認證網址為 GitHub 官方網域</text>
    <text x="20" y="410" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 貼上代碼並按 Continue</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <g transform="translate(780, 370)">
    <polygon points="0,0 20,10 0,20" fill="#818cf8"/>
  </g>

  <!-- Step 3: Google Authorize -->
  <g transform="translate(810, 165)">
    <rect width="325" height="440" rx="14" fill="url(#card-grad2)" stroke="#34d399" stroke-width="1.5" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="80" height="26" rx="6" fill="#34d399" fill-opacity="0.2"/>
    <text x="60" y="38" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 3</text>
    <text x="20" y="75" fill="#f8fafc" font-size="18" font-weight="700" font-family="system-ui, sans-serif">點擊授權配對</text>
    <text x="20" y="102" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">Google 帳號已在第 3 章登入</text>

    <!-- Authorize UI Mockup -->
    <rect x="18" y="130" width="289" height="200" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <rect x="18" y="130" width="289" height="28" rx="8" fill="#1e293b"/>
    <text x="162" y="148" fill="#94a3b8" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">GitHub Authorize OAuth App</text>
    <circle cx="162" cy="180" r="18" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
    <text x="162" y="186" fill="#38bdf8" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">gh</text>
    <text x="162" y="215" fill="#f8fafc" font-size="12" font-weight="600" text-anchor="middle" font-family="system-ui, sans-serif">Authorize GitHub CLI</text>
    <text x="162" y="235" fill="#94a3b8" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">允許建立 Repository 與發布 Pages</text>

    <rect x="55" y="258" width="215" height="38" rx="6" fill="#15803d" stroke="#22c55e" stroke-width="1"/>
    <text x="162" y="282" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">✔ Authorize github</text>

    <text x="20" y="360" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 不需再次輸入密碼</text>
    <text x="20" y="385" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 認證身分直接繼承 Google 登入</text>
    <text x="20" y="410" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 單次授權，終生有效</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <g transform="translate(1145, 370)">
    <polygon points="0,0 20,10 0,20" fill="#34d399"/>
  </g>

  <!-- Step 4: Token Saved -->
  <g transform="translate(1175, 165)">
    <rect width="345" height="440" rx="14" fill="url(#card-grad2)" stroke="#f59e0b" stroke-width="1.5" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="80" height="26" rx="6" fill="#f59e0b" fill-opacity="0.2"/>
    <text x="60" y="38" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 4</text>
    <text x="20" y="75" fill="#f8fafc" font-size="18" font-weight="700" font-family="system-ui, sans-serif">本機安全 Token 存檔</text>
    <text x="20" y="102" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">Antigravity 獲得合法操作憑證</text>

    <!-- Key & Token Box -->
    <rect x="18" y="130" width="309" height="200" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <!-- Terminal success -->
    <circle cx="34" cy="148" r="4.5" fill="#ef4444"/>
    <circle cx="48" cy="148" r="4.5" fill="#f59e0b"/>
    <circle cx="62" cy="148" r="4.5" fill="#10b981"/>
    <text x="80" y="152" fill="#64748b" font-size="11" font-family="'JetBrains Mono', monospace">Terminal Output</text>
    
    <text x="28" y="185" fill="#34d399" font-size="12" font-weight="700" font-family="'JetBrains Mono', monospace">✔ Authentication complete.</text>
    <text x="28" y="210" fill="#cbd5e1" font-size="11" font-family="'JetBrains Mono', monospace">- Logged in to github.com</text>
    <text x="28" y="230" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace">- Active account: alex-tw</text>
    <text x="28" y="255" fill="#94a3b8" font-size="10" font-family="'JetBrains Mono', monospace">Token safely stored in:</text>
    <rect x="28" y="265" width="280" height="42" rx="4" fill="#1e1b4b" stroke="#f59e0b" stroke-width="1"/>
    <text x="38" y="290" fill="#f59e0b" font-size="10" font-family="'JetBrains Mono', monospace">~/.config/gh/hosts.yml (加密憑證)</text>

    <text x="20" y="360" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 本機產生安全 OAuth Token</text>
    <text x="20" y="385" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 未來發布不再跳出授權視窗</text>
    <text x="20" y="410" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 隨時可從 GitHub 後台撤銷</text>
  </g>

  <!-- Bottom Security Callout -->
  <g transform="translate(80, 645)">
    <rect width="1440" height="175" rx="14" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect x="30" y="25" width="130" height="28" rx="6" fill="#34d399" fill-opacity="0.2"/>
    <text x="95" y="44" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">🛡️ 安全性承諾</text>
    <text x="180" y="44" fill="#f8fafc" font-size="16" font-weight="700" font-family="system-ui, sans-serif">為什麼 Device Flow 是最安全的授權方式？</text>
    
    <g transform="translate(30, 75)">
      <text x="0" y="0" fill="#cbd5e1" font-size="14" font-family="system-ui, sans-serif"><tspan fill="#38bdf8" font-weight="700">1. 零密碼傳遞：</tspan> Antigravity 與終端機從始至終「完全碰不到你的 Google 或 GitHub 密碼」，避免側錄或外洩風險。</text>
      <text x="0" y="30" fill="#cbd5e1" font-size="14" font-family="system-ui, sans-serif"><tspan fill="#818cf8" font-weight="700">2. 權限最小化：</tspan> 產生的 Token 僅具備代碼推送與建立 Repo 權限，無法變更您的帳號個人隱私或金流資訊。</text>
      <text x="0" y="60" fill="#cbd5e1" font-size="14" font-family="system-ui, sans-serif"><tspan fill="#f59e0b" font-weight="700">3. 隨時可撤銷：</tspan> 若換電腦或不再使用，可在 GitHub 網頁版「Settings ➔ Applications」一鍵刪除該 Token，立即終止連線。</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------------------
# SVG 3: ch4_one_click_pipeline.svg (1600 x 880)
# -------------------------------------------------------------------------
svg3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 880" width="1600" height="880">
  <defs>
    <linearGradient id="bg-grad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="card-grad3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1600" height="880" fill="url(#bg-grad3)"/>

  <!-- Header -->
  <g transform="translate(80, 45)">
    <rect x="0" y="0" width="160" height="28" rx="14" fill="#34d399" fill-opacity="0.15"/>
    <text x="80" y="19" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">第 4 章 · 自動化全景圖</text>
    <text x="0" y="60" fill="#f8fafc" font-size="28" font-weight="800" font-family="system-ui, sans-serif">自然語言一鍵推送：Antigravity 背景全自動流水線</text>
    <text x="0" y="88" fill="#94a3b8" font-size="15" font-family="system-ui, sans-serif">學員只要說一句話，AI 自動替你串聯 Git 版本控制、雲端儲存庫與 Pages 靜態網站伺服器</text>
  </g>

  <!-- Prompt Input Card -->
  <g transform="translate(80, 160)">
    <rect width="1440" height="110" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8" filter="url(#shadow3)"/>
    <rect x="25" y="18" width="160" height="26" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="105" y="36" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">學員送出自然語言提示詞</text>
    <text x="200" y="36" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">口語化吩咐，不需硬記任何命令列參數</text>
    <rect x="25" y="54" width="1390" height="42" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="45" y="80" fill="#f8fafc" font-size="14" font-weight="600" font-family="system-ui, sans-serif">"Antigravity，請幫我建立名為 smartsound-page 的公開 repo，把目前的程式碼和照片推上去，並開啟 Pages 網址！"</text>
  </g>

  <!-- Vertical Arrow Down -->
  <g transform="translate(800, 280)">
    <polygon points="0,0 12,18 -12,18" fill="#38bdf8"/>
  </g>

  <!-- 4 Stages Pipeline -->
  <g transform="translate(80, 310)">
    <!-- Stage 1 -->
    <g transform="translate(0, 0)">
      <rect width="335" height="340" rx="12" fill="url(#card-grad3)" stroke="#38bdf8" stroke-width="1.2" filter="url(#shadow3)"/>
      <rect x="20" y="20" width="80" height="24" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
      <text x="60" y="37" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">階段 01</text>
      <text x="20" y="70" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">專案封裝與追蹤</text>
      <text x="20" y="94" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">掃描檔案與建立暫存區</text>

      <rect x="18" y="115" width="299" height="70" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
      <text x="30" y="142" fill="#38bdf8" font-size="12" font-family="'JetBrains Mono', monospace">$ git init</text>
      <text x="30" y="165" fill="#38bdf8" font-size="12" font-family="'JetBrains Mono', monospace">$ git add .</text>

      <g transform="translate(20, 205)">
        <text x="0" y="0" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 建立本機 <code>.git</code> 資料庫</text>
        <text x="0" y="24" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 打包 HTML、CSS、JS</text>
        <text x="0" y="48" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 打包 PIC 資料夾高畫質圖片</text>
        <text x="0" y="72" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 自動忽略系統暫存檔</text>
      </g>
    </g>

    <!-- Arrow 1 -> 2 -->
    <g transform="translate(345, 170)">
      <polygon points="0,0 16,8 0,16" fill="#38bdf8"/>
    </g>

    <!-- Stage 2 -->
    <g transform="translate(368, 0)">
      <rect width="335" height="340" rx="12" fill="url(#card-grad3)" stroke="#818cf8" stroke-width="1.2" filter="url(#shadow3)"/>
      <rect x="20" y="20" width="80" height="24" rx="6" fill="#818cf8" fill-opacity="0.2"/>
      <text x="60" y="37" fill="#818cf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">階段 02</text>
      <text x="20" y="70" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">建立歷史存檔點</text>
      <text x="20" y="94" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">產生版本控制 Commit 快照</text>

      <rect x="18" y="115" width="299" height="70" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
      <text x="30" y="142" fill="#818cf8" font-size="11" font-family="'JetBrains Mono', monospace">$ git commit -m \</text>
      <text x="30" y="165" fill="#818cf8" font-size="11" font-family="'JetBrains Mono', monospace">  "feat: initial release"</text>

      <g transform="translate(20, 205)">
        <text x="0" y="0" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 記錄本次版本修改歷史</text>
        <text x="0" y="24" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 生成唯一的 SHA 雜湊金鑰</text>
        <text x="0" y="48" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 隨時可坐時光機還原</text>
        <text x="0" y="72" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 本機版本庫正式成立！</text>
      </g>
    </g>

    <!-- Arrow 2 -> 3 -->
    <g transform="translate(713, 170)">
      <polygon points="0,0 16,8 0,16" fill="#818cf8"/>
    </g>

    <!-- Stage 3 -->
    <g transform="translate(736, 0)">
      <rect width="335" height="340" rx="12" fill="url(#card-grad3)" stroke="#34d399" stroke-width="1.2" filter="url(#shadow3)"/>
      <rect x="20" y="20" width="80" height="24" rx="6" fill="#34d399" fill-opacity="0.2"/>
      <text x="60" y="37" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">階段 03</text>
      <text x="20" y="70" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">雲端建庫與推送</text>
      <text x="20" y="94" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">呼叫 GitHub CLI 工具同步</text>

      <rect x="18" y="115" width="299" height="70" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
      <text x="30" y="140" fill="#34d399" font-size="11" font-family="'JetBrains Mono', monospace">$ gh repo create smartsound \</text>
      <text x="30" y="162" fill="#34d399" font-size="11" font-family="'JetBrains Mono', monospace">  --public --source=. --push</text>

      <g transform="translate(20, 205)">
        <text x="0" y="0" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 透過 Token 通過雲端驗證</text>
        <text x="0" y="24" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 建立遠端公開（Public）倉庫</text>
        <text x="0" y="48" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 一鍵將代碼推送至 main 分支</text>
        <text x="0" y="72" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 雲端儲存庫立即生成！</text>
      </g>
    </g>

    <!-- Arrow 3 -> 4 -->
    <g transform="translate(1081, 170)">
      <polygon points="0,0 16,8 0,16" fill="#34d399"/>
    </g>

    <!-- Stage 4 -->
    <g transform="translate(1105, 0)">
      <rect width="335" height="340" rx="12" fill="url(#card-grad3)" stroke="#f59e0b" stroke-width="1.2" filter="url(#shadow3)"/>
      <rect x="20" y="20" width="80" height="24" rx="6" fill="#f59e0b" fill-opacity="0.2"/>
      <text x="60" y="37" fill="#f59e0b" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">階段 04</text>
      <text x="20" y="70" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">啟動 Pages 伺服器</text>
      <text x="20" y="94" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">API 啟用全球靜態網站託管</text>

      <rect x="18" y="115" width="299" height="70" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
      <text x="30" y="140" fill="#f59e0b" font-size="11" font-family="'JetBrains Mono', monospace">$ gh api repos/:owner/:repo \</text>
      <text x="30" y="162" fill="#f59e0b" font-size="11" font-family="'JetBrains Mono', monospace">  /pages -F "source[branch]=main"</text>

      <g transform="translate(20, 205)">
        <text x="0" y="0" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 免開網頁手動點擊 Settings</text>
        <text x="0" y="24" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 綁定 main 分支根目錄發布</text>
        <text x="0" y="48" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• GitHub Actions 啟動自動編譯</text>
        <text x="0" y="72" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 取得專屬正式公開網址！</text>
      </g>
    </g>
  </g>

  <!-- Bottom Result Box -->
  <g transform="translate(80, 680)">
    <rect width="1440" height="150" rx="14" fill="#064e3b" stroke="#34d399" stroke-width="1.8" filter="url(#shadow3)"/>
    <rect x="30" y="20" width="160" height="28" rx="6" fill="#10b981" fill-opacity="0.3"/>
    <text x="110" y="39" fill="#a7f3d0" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">🎉 終端機與對話回報結果</text>
    
    <text x="30" y="78" fill="#ffffff" font-size="17" font-weight="800" font-family="system-ui, sans-serif">全球公開上線網址生成完畢：</text>
    <rect x="30" y="92" width="750" height="40" rx="6" fill="#022c22" stroke="#34d399" stroke-width="1"/>
    <text x="50" y="117" fill="#6ee7b7" font-size="15" font-weight="700" font-family="'JetBrains Mono', monospace">https://&lt;你的帳號&gt;.github.io/smartsound-page/</text>
    
    <text x="810" y="104" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">✔ 任何人點擊連結即可直接檢視你的產品銷售頁！</text>
    <text x="810" y="125" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">✔ 後續有任何修改，只需再次吩咐「幫我推送更新」，幾秒鐘即時同步！</text>
  </g>
</svg>'''

with open("PIC/ch4_manual_vs_cli.svg", "w", encoding="utf-8") as f:
    f.write(svg1)
print(f"Generated ch4_manual_vs_cli.svg successfully ({len(svg1)} bytes)")

with open("PIC/ch4_device_flow_auth.svg", "w", encoding="utf-8") as f:
    f.write(svg2)
print(f"Generated ch4_device_flow_auth.svg successfully ({len(svg2)} bytes)")

with open("PIC/ch4_one_click_pipeline.svg", "w", encoding="utf-8") as f:
    f.write(svg3)
print(f"Generated ch4_one_click_pipeline.svg successfully ({len(svg3)} bytes)")

print("ALL CHAPTER 4 SVG DIAGRAMS GENERATED SUCCESSFULLY!")
