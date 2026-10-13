import os

os.makedirs("PIC", exist_ok=True)

# -------------------------------------------------------------------------
# SVG 1: ch5_why_need_backend.svg (1600 x 880)
# -------------------------------------------------------------------------
svg1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 880" width="1600" height="880">
  <defs>
    <linearGradient id="bg-grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0b1120"/>
      <stop offset="50%" stop-color="#0f172a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="card-blue" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="rgba(56, 189, 248, 0.1)"/>
    </linearGradient>
    <linearGradient id="card-purple" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="rgba(129, 140, 248, 0.12)"/>
    </linearGradient>
    <linearGradient id="card-green" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="rgba(16, 185, 129, 0.12)"/>
    </linearGradient>
    <filter id="shadow1" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.4"/>
    </filter>
  </defs>

  <!-- Background -->
  <rect width="1600" height="880" fill="url(#bg-grad1)"/>

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
    <rect x="0" y="0" width="140" height="28" rx="14" fill="#38bdf8" fill-opacity="0.15"/>
    <text x="70" y="19" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">第 5 章 · 架構全景圖</text>
    <text x="0" y="60" fill="#f8fafc" font-size="28" font-weight="800" font-family="system-ui, sans-serif">為什麼靜態網頁需要後端？GitHub Pages 與 GAS 的黃金組合</text>
    <text x="0" y="88" fill="#94a3b8" font-size="15" font-family="system-ui, sans-serif">拆解「純靜態網頁」的本質限制，以及如何透過「Google Apps Script」打造零成本全功能商業站點</text>
  </g>

  <!-- 3 Columns Architecture -->
  <!-- Column 1: Front-end Static (GitHub Pages) -->
  <g transform="translate(80, 165)">
    <rect width="440" height="570" rx="16" fill="url(#card-blue)" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow1)"/>
    
    <rect x="25" y="24" width="130" height="28" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="90" y="43" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">前端：靜態託管</text>
    <text x="170" y="44" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">GitHub Pages 網頁</text>

    <!-- Component details -->
    <rect x="25" y="70" width="390" height="150" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="45" y="100" fill="#38bdf8" font-size="14" font-weight="700" font-family="system-ui, sans-serif">✔ 負責工作：視覺展示與互動</text>
    <text x="45" y="128" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• HTML5：產品結構與商品預購表單</text>
    <text x="45" y="152" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• CSS3：現代科技美學、RWD 行動適配</text>
    <text x="45" y="176" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• JavaScript：表單驗證、點擊事件監聽</text>
    <text x="45" y="200" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 全球 CDN 免費高頻寬託管</text>

    <!-- Bottlenecks / Pain points -->
    <rect x="25" y="240" width="390" height="200" rx="10" fill="#0f172a" stroke="#f43f5e" stroke-width="1.2"/>
    <rect x="40" y="255" width="115" height="24" rx="4" fill="#f43f5e" fill-opacity="0.2"/>
    <text x="97" y="272" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">❌ 靜態網頁痛點</text>

    <g transform="translate(45, 305)">
      <text x="0" y="0" fill="#fca5a5" font-size="13" font-weight="600" font-family="system-ui, sans-serif">1. 無法持久保存訪客資料：</text>
      <text x="0" y="20" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">表單一重整，客戶輸入的姓名信箱立即消失。</text>
      
      <text x="0" y="50" fill="#fca5a5" font-size="13" font-weight="600" font-family="system-ui, sans-serif">2. 無法主動寄送通知信：</text>
      <text x="0" y="70" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">瀏覽器受安全限制，不能直接以站長身分寄信。</text>

      <text x="0" y="100" fill="#fca5a5" font-size="13" font-weight="600" font-family="system-ui, sans-serif">3. 傳統後端門檻過高：</text>
      <text x="0" y="120" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">租用 AWS/GCP 伺服器每年需花費數千元。</text>
    </g>

    <!-- Bottom summary tag -->
    <rect x="25" y="460" width="390" height="85" rx="8" fill="#1e1b4b" stroke="#818cf8" stroke-width="1"/>
    <text x="45" y="490" fill="#818cf8" font-size="13" font-weight="700" font-family="system-ui, sans-serif">💡 解決方案：</text>
    <text x="45" y="514" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">使用 fetch() 將資料非同步 POST 到雲端後端，</text>
    <text x="45" y="534" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">由 Google 雲端免費替我們完成存檔與寄信！</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <g transform="translate(535, 430)">
    <polygon points="0,0 24,12 0,24" fill="#818cf8"/>
    <text x="12" y="-12" fill="#818cf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">fetch(POST)</text>
  </g>

  <!-- Column 2: Serverless Middle (Google Apps Script) -->
  <g transform="translate(580, 165)">
    <rect width="440" height="570" rx="16" fill="url(#card-purple)" stroke="#818cf8" stroke-width="1.8" filter="url(#shadow1)"/>
    
    <rect x="25" y="24" width="130" height="28" rx="6" fill="#818cf8" fill-opacity="0.2"/>
    <text x="90" y="43" fill="#818cf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">樞紐：無伺服器</text>
    <text x="170" y="44" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">Google Apps Script</text>

    <!-- Core strengths -->
    <rect x="25" y="70" width="390" height="150" rx="10" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="45" y="100" fill="#818cf8" font-size="14" font-weight="700" font-family="system-ui, sans-serif">⚡ 核心特點：零伺服器維護</text>
    <text x="45" y="128" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 100% 免費無伺服器架構（Serverless）</text>
    <text x="45" y="152" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 免安裝 Node.js、免部屬 Linux 系統</text>
    <text x="45" y="176" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Google 官方自動擴展與負載平衡</text>
    <text x="45" y="200" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 現代 JavaScript 語法，學習曲線平緩</text>

    <!-- Pipeline tasks -->
    <rect x="25" y="240" width="390" height="200" rx="10" fill="#0f172a" stroke="#818cf8" stroke-width="1"/>
    <rect x="40" y="255" width="140" height="24" rx="4" fill="#818cf8" fill-opacity="0.2"/>
    <text x="110" y="272" fill="#a5b4fc" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">⚙️ doPost(e) 處理中心</text>

    <g transform="translate(45, 305)">
      <text x="0" y="0" fill="#e2e8f0" font-size="13" font-weight="600" font-family="system-ui, sans-serif">1. 接收與解析前端 JSON 封包</text>
      <text x="0" y="20" fill="#94a3b8" font-size="12" font-family="'JetBrains Mono', monospace">name, email, phone, plan, notes</text>

      <text x="0" y="50" fill="#e2e8f0" font-size="13" font-weight="600" font-family="system-ui, sans-serif">2. 指揮 Google 試算表寫入</text>
      <text x="0" y="70" fill="#94a3b8" font-size="12" font-family="'JetBrains Mono', monospace">SpreadsheetApp.appendRow([...])</text>

      <text x="0" y="100" fill="#e2e8f0" font-size="13" font-weight="600" font-family="system-ui, sans-serif">3. 調用 Gmail 自動發送感謝信</text>
      <text x="0" y="120" fill="#94a3b8" font-size="12" font-family="'JetBrains Mono', monospace">GmailApp.sendEmail(email, ...)</text>
    </g>

    <!-- Bottom summary tag -->
    <rect x="25" y="460" width="390" height="85" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
    <text x="45" y="490" fill="#34d399" font-size="13" font-weight="700" font-family="system-ui, sans-serif">✔ 成果回應：</text>
    <text x="45" y="514" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">回傳 { status: 'success' } JSON 數據給前端，</text>
    <text x="45" y="534" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">網頁即時呈現「預購成功！」提示彈窗。</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <g transform="translate(1035, 430)">
    <polygon points="0,0 24,12 0,24" fill="#34d399"/>
    <text x="12" y="-12" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">API 控制</text>
  </g>

  <!-- Column 3: Google Ecosystem -->
  <g transform="translate(1080, 165)">
    <rect width="440" height="570" rx="16" fill="url(#card-green)" stroke="#34d399" stroke-width="1.5" filter="url(#shadow1)"/>
    
    <rect x="25" y="24" width="130" height="28" rx="6" fill="#34d399" fill-opacity="0.2"/>
    <text x="90" y="43" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">後端：雲端生態系</text>
    <text x="170" y="44" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">Google 官方服務群</text>

    <!-- Service 1: Google Sheets -->
    <rect x="25" y="70" width="390" height="150" rx="10" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <rect x="40" y="85" width="160" height="24" rx="4" fill="#10b981" fill-opacity="0.2"/>
    <text x="120" y="102" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">📊 Google 試算表 (Sheets)</text>
    <text x="45" y="132" fill="#cbd5e1" font-size="13" font-weight="600" font-family="system-ui, sans-serif">你的「視覺化無代碼資料庫」：</text>
    <text x="45" y="154" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">• 支援 1,000 萬格容量，存取數萬筆訂單</text>
    <text x="45" y="174" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">• 即時線上多人協作，手機 App 隨時查看</text>
    <text x="45" y="194" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">• 一鍵匯出 Excel、CSV 進行商業財務分析</text>

    <!-- Service 2: Gmail API -->
    <rect x="25" y="240" width="390" height="150" rx="10" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <rect x="40" y="255" width="130" height="24" rx="4" fill="#ef4444" fill-opacity="0.2"/>
    <text x="105" y="272" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">✉️ Gmail 郵件系統</text>
    <text x="45" y="302" fill="#cbd5e1" font-size="13" font-weight="600" font-family="system-ui, sans-serif">你的「專屬客戶關係通知員」：</text>
    <text x="45" y="324" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">• 透過自己的 Gmail 官方伺服器發信</text>
    <text x="45" y="344" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">• 送達率高，不易被判為垃圾郵件</text>
    <text x="45" y="364" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">• 支援客製化姓名與訂購方案 HTML 排版</text>

    <!-- Service 3: Future Expansion -->
    <rect x="25" y="410" width="390" height="135" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
    <rect x="40" y="425" width="140" height="24" rx="4" fill="#f59e0b" fill-opacity="0.2"/>
    <text x="110" y="442" fill="#fbbf24" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">🚀 未來彈性擴充能力</text>
    <text x="45" y="472" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• LINE Notify / 機器人推播（第 7 章）</text>
    <text x="45" y="494" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 綠界 ECPay 金流串接驗證（第 8 章）</text>
    <text x="45" y="516" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• Google 日曆預約行程與雲端硬碟備份</text>
  </g>

  <!-- Bottom Global Banner -->
  <g transform="translate(80, 765)">
    <rect width="1440" height="65" rx="12" fill="#1e293b" stroke="#475569" stroke-width="1"/>
    <text x="40" y="38" fill="#f8fafc" font-size="15" font-weight="600" font-family="system-ui, sans-serif">💡 結論：靜態網頁負責「門面外觀」，GAS 負責「大腦運算」，Google 試算表負責「資料庫」。三者結合，就是當今初學者最低成本、最高效的雲端全端解決方案！</text>
  </g>
</svg>'''

# -------------------------------------------------------------------------
# SVG 2: ch5_web_app_flow.svg (1600 x 880)
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
  <g transform="translate(80, 45)">
    <rect x="0" y="0" width="160" height="28" rx="14" fill="#38bdf8" fill-opacity="0.15"/>
    <text x="80" y="19" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">第 5 章 · 通訊時序圖</text>
    <text x="0" y="60" fill="#f8fafc" font-size="28" font-weight="800" font-family="system-ui, sans-serif">GAS Web App 前後端通訊互動全流程解密 (Interactive Data Flow)</text>
    <text x="0" y="88" fill="#94a3b8" font-size="15" font-family="system-ui, sans-serif">訪客在 GitHub Pages 點擊送出到收到感謝信的 5 步驟非同步即時生命週期</text>
  </g>

  <!-- 5 Horizontal Steps -->
  <!-- Step 1: User Action -->
  <g transform="translate(80, 160)">
    <rect width="270" height="460" rx="14" fill="url(#card-grad2)" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="70" height="26" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="55" y="38" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 1</text>
    <text x="20" y="75" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">訪客操作表單</text>
    <text x="20" y="98" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">GitHub Pages 前端</text>

    <!-- UI Mockup -->
    <rect x="15" y="120" width="240" height="210" rx="8" fill="#0f172a" stroke="#334155" stroke-width="1"/>
    <text x="25" y="145" fill="#f8fafc" font-size="12" font-weight="700" font-family="system-ui, sans-serif">早鳥預購表單 (HTML)</text>
    <rect x="25" y="155" width="220" height="24" rx="4" fill="#1e293b"/>
    <text x="35" y="171" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">姓名：王小明</text>
    <rect x="25" y="185" width="220" height="24" rx="4" fill="#1e293b"/>
    <text x="35" y="201" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">信箱：ming@gmail.com</text>
    <rect x="25" y="215" width="220" height="24" rx="4" fill="#1e293b"/>
    <text x="35" y="231" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">方案：旗艦降噪版 ($2,990)</text>
    <rect x="25" y="250" width="220" height="34" rx="6" fill="#2563eb"/>
    <text x="135" y="272" fill="#ffffff" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">🚀 立即預購下單</text>
    <text x="135" y="315" fill="#38bdf8" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">觸發 submit 監聽事件</text>

    <g transform="translate(20, 355)">
      <text x="0" y="0" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 訪客填寫 5 項資訊</text>
      <text x="0" y="22" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 前端 JS 驗證信箱格式</text>
      <text x="0" y="44" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 鎖定按鈕防止重複點擊</text>
      <text x="0" y="66" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 顯示「處理中...」轉圈</text>
    </g>
  </g>

  <!-- Arrow 1 -> 2 -->
  <g transform="translate(360, 380)">
    <polygon points="0,0 16,8 0,16" fill="#38bdf8"/>
  </g>

  <!-- Step 2: fetch POST -->
  <g transform="translate(385, 160)">
    <rect width="270" height="460" rx="14" fill="url(#card-grad2)" stroke="#818cf8" stroke-width="1.5" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="70" height="26" rx="6" fill="#818cf8" fill-opacity="0.2"/>
    <text x="55" y="38" fill="#818cf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 2</text>
    <text x="20" y="75" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">前端 fetch 發送</text>
    <text x="20" y="98" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">非同步打包 JSON 傳遞</text>

    <!-- Code Mockup -->
    <rect x="15" y="120" width="240" height="210" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="25" y="145" fill="#818cf8" font-size="11" font-family="'JetBrains Mono', monospace">// 前端 JavaScript</text>
    <text x="25" y="165" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace">fetch(GAS_URL, {</text>
    <text x="35" y="185" fill="#cbd5e1" font-size="11" font-family="'JetBrains Mono', monospace">method: 'POST',</text>
    <text x="35" y="205" fill="#cbd5e1" font-size="11" font-family="'JetBrains Mono', monospace">body: JSON.stringify({</text>
    <text x="45" y="225" fill="#34d399" font-size="10" font-family="'JetBrains Mono', monospace">name: '王小明',</text>
    <text x="45" y="245" fill="#34d399" font-size="10" font-family="'JetBrains Mono', monospace">email: '...',</text>
    <text x="45" y="265" fill="#34d399" font-size="10" font-family="'JetBrains Mono', monospace">plan: '旗艦版'</text>
    <text x="35" y="285" fill="#cbd5e1" font-size="11" font-family="'JetBrains Mono', monospace">})</text>
    <text x="25" y="305" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace">})</text>

    <g transform="translate(20, 355)">
      <text x="0" y="0" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 資料打包為 JSON 字串</text>
      <text x="0" y="22" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 透過 HTTPS 加密傳輸</text>
      <text x="0" y="44" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 非同步請求（頁面免刷新）</text>
      <text x="0" y="66" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 抵達 Google 伺服器端點</text>
    </g>
  </g>

  <!-- Arrow 2 -> 3 -->
  <g transform="translate(665, 380)">
    <polygon points="0,0 16,8 0,16" fill="#818cf8"/>
  </g>

  <!-- Step 3: GAS doPost -->
  <g transform="translate(690, 160)">
    <rect width="270" height="460" rx="14" fill="url(#card-grad2)" stroke="#a855f7" stroke-width="1.5" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="70" height="26" rx="6" fill="#a855f7" fill-opacity="0.2"/>
    <text x="55" y="38" fill="#c084fc" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 3</text>
    <text x="20" y="75" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">GAS 解析派發</text>
    <text x="20" y="98" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">doPost(e) 入口函式</text>

    <!-- Code Mockup -->
    <rect x="15" y="120" width="240" height="210" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
    <text x="25" y="145" fill="#c084fc" font-size="11" font-family="'JetBrains Mono', monospace">// Google Apps Script</text>
    <text x="25" y="165" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace">function doPost(e) {</text>
    <text x="35" y="185" fill="#94a3b8" font-size="10" font-family="'JetBrains Mono', monospace">let data =</text>
    <text x="35" y="202" fill="#34d399" font-size="10" font-family="'JetBrains Mono', monospace">JSON.parse(e.postData.contents);</text>
    <text x="35" y="225" fill="#cbd5e1" font-size="10" font-family="'JetBrains Mono', monospace">let name = data.name;</text>
    <text x="35" y="245" fill="#cbd5e1" font-size="10" font-family="'JetBrains Mono', monospace">let email = data.email;</text>
    <text x="35" y="265" fill="#cbd5e1" font-size="10" font-family="'JetBrains Mono', monospace">let plan = data.plan;</text>
    <text x="35" y="285" fill="#f59e0b" font-size="10" font-family="'JetBrains Mono', monospace">// 執行雙軌任務...</text>
    <text x="25" y="305" fill="#38bdf8" font-size="11" font-family="'JetBrains Mono', monospace">}</text>

    <g transform="translate(20, 355)">
      <text x="0" y="0" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 接收 e.postData.contents</text>
      <text x="0" y="22" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 解構取得 5 個表單欄位</text>
      <text x="0" y="44" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 自動產生當前下單時間戳記</text>
      <text x="0" y="66" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 啟動雙軌雲端任務</text>
    </g>
  </g>

  <!-- Arrow 3 -> 4 -->
  <g transform="translate(970, 380)">
    <polygon points="0,0 16,8 0,16" fill="#a855f7"/>
  </g>

  <!-- Step 4: Parallel execution -->
  <g transform="translate(995, 160)">
    <rect width="270" height="460" rx="14" fill="url(#card-grad2)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="70" height="26" rx="6" fill="#10b981" fill-opacity="0.2"/>
    <text x="55" y="38" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 4</text>
    <text x="20" y="75" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">雙軌雲端動作</text>
    <text x="20" y="98" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">試算表存檔 + Gmail 寄信</text>

    <!-- Track A: Sheets -->
    <rect x="15" y="120" width="240" height="100" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
    <text x="25" y="142" fill="#34d399" font-size="11" font-weight="700" font-family="system-ui, sans-serif">軌道 A：Google 試算表存檔</text>
    <text x="25" y="162" fill="#94a3b8" font-size="10" font-family="'JetBrains Mono', monospace">sheet.appendRow([</text>
    <text x="35" y="178" fill="#a7f3d0" font-size="9" font-family="'JetBrains Mono', monospace">timestamp, name, email, plan...</text>
    <text x="25" y="195" fill="#94a3b8" font-size="10" font-family="'JetBrains Mono', monospace">]);</text>
    <text x="25" y="210" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">✔ 新增一行紀錄至試算表</text>

    <!-- Track B: Gmail -->
    <rect x="15" y="230" width="240" height="100" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="1"/>
    <text x="25" y="252" fill="#f87171" font-size="11" font-weight="700" font-family="system-ui, sans-serif">軌道 B：Gmail 自動回信</text>
    <text x="25" y="272" fill="#94a3b8" font-size="10" font-family="'JetBrains Mono', monospace">GmailApp.sendEmail(email,</text>
    <text x="35" y="288" fill="#fca5a5" font-size="9" font-family="'JetBrains Mono', monospace">'SmartSound Pro 預購確認',</text>
    <text x="35" y="304" fill="#fca5a5" font-size="9" font-family="'JetBrains Mono', monospace">'感謝您預購...' + htmlBody);</text>
    <text x="25" y="320" fill="#cbd5e1" font-size="10" font-family="system-ui, sans-serif">✔ 寄出精美訂購確認感謝信</text>

    <g transform="translate(20, 355)">
      <text x="0" y="0" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 雙軌皆在 1 秒內極速完成</text>
      <text x="0" y="22" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 試算表成為永續名單資料庫</text>
      <text x="0" y="44" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 訪客手機立即收到訂單通知</text>
      <text x="0" y="66" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 準備封裝回傳值</text>
    </g>
  </g>

  <!-- Arrow 4 -> 5 -->
  <g transform="translate(1275, 380)">
    <polygon points="0,0 16,8 0,16" fill="#10b981"/>
  </g>

  <!-- Step 5: Return Result -->
  <g transform="translate(1300, 160)">
    <rect width="220" height="460" rx="14" fill="url(#card-grad2)" stroke="#34d399" stroke-width="1.8" filter="url(#shadow2)"/>
    <rect x="20" y="20" width="70" height="26" rx="6" fill="#34d399" fill-opacity="0.2"/>
    <text x="55" y="38" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">步驟 5</text>
    <text x="20" y="75" fill="#f8fafc" font-size="17" font-weight="700" font-family="system-ui, sans-serif">回傳與 UI 更新</text>
    <text x="20" y="98" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">彈出預購成功彈窗</text>

    <!-- Result preview -->
    <rect x="15" y="120" width="190" height="210" rx="8" fill="#064e3b" stroke="#34d399" stroke-width="1"/>
    <circle cx="110" cy="160" r="22" fill="#10b981" fill-opacity="0.3"/>
    <text x="110" y="167" fill="#6ee7b7" font-size="20" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">✔</text>
    <text x="110" y="205" fill="#ffffff" font-size="14" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">預購下單成功！</text>
    <text x="110" y="230" fill="#a7f3d0" font-size="11" text-anchor="middle" font-family="system-ui, sans-serif">感謝信已寄至您的信箱</text>
    <rect x="28" y="255" width="164" height="28" rx="4" fill="#022c22" stroke="#34d399" stroke-width="0.8"/>
    <text x="110" y="273" fill="#6ee7b7" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">{"status":"success"}</text>
    <text x="110" y="308" fill="#cbd5e1" font-size="10" text-anchor="middle" font-family="system-ui, sans-serif">按鈕恢復並清空表單</text>

    <g transform="translate(15, 355)">
      <text x="0" y="0" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 前端解析 JSON 回傳值</text>
      <text x="0" y="22" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 顯示預購完成彈窗</text>
      <text x="0" y="44" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 完整體驗流暢無跳轉</text>
      <text x="0" y="66" fill="#cbd5e1" font-size="12" font-family="system-ui, sans-serif">• 商業閉環完美達成！</text>
    </g>
  </g>

  <!-- Bottom Key Security and CORS Note -->
  <g transform="translate(80, 650)">
    <rect width="1440" height="175" rx="14" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>
    <rect x="30" y="22" width="130" height="26" rx="6" fill="#f59e0b" fill-opacity="0.2"/>
    <text x="95" y="39" fill="#f59e0b" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">⚠️ 關鍵技術細節</text>
    <text x="180" y="40" fill="#f8fafc" font-size="16" font-weight="700" font-family="system-ui, sans-serif">跨網域連線（CORS）與 ContentService 回應原理</text>

    <g transform="translate(30, 75)">
      <text x="0" y="0" fill="#cbd5e1" font-size="14" font-family="system-ui, sans-serif"><tspan fill="#38bdf8" font-weight="700">1. 免跨網域阻擋：</tspan> GitHub Pages (例如 your-name.github.io) 與 Google (script.google.com) 屬於不同網域，GAS 必須使用 <code>ContentService.createTextOutput()</code> 並以 <code>JSON</code> 格式封裝回傳，才能避開瀏覽器 CORS 報錯。</text>
      <text x="0" y="30" fill="#cbd5e1" font-size="14" font-family="system-ui, sans-serif"><tspan fill="#818cf8" font-weight="700">2. 權限設定黃金法則：</tspan> Web App 部署時，<strong>「執行身分」必須設定為「我 (Me)」</strong>，而<strong>「存取權限」必須設定為「任何人 (Anyone)」</strong>。這樣訪客不需要登入 Google 帳號，就能順暢送出表單！</text>
      <text x="0" y="60" fill="#cbd5e1" font-size="14" font-family="system-ui, sans-serif"><tspan fill="#34d399" font-weight="700">3. 零伺服器維護：</tspan> 全程無須管理任何 Linux 主機或資料庫叢集，Google 自動處理並行負載，讓你安心專注在產品與行銷！</text>
    </g>
  </g>
</svg>'''

# -------------------------------------------------------------------------
# SVG 3: ch5_sheets_and_editor.svg (1600 x 880)
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
    <rect x="0" y="0" width="160" height="28" rx="14" fill="#10b981" fill-opacity="0.15"/>
    <text x="80" y="19" fill="#10b981" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">第 5 章 · 介面與生態指引</text>
    <text x="0" y="60" fill="#f8fafc" font-size="28" font-weight="800" font-family="system-ui, sans-serif">Google 試算表與 Apps Script 編輯器核心指引</text>
    <text x="0" y="88" fill="#94a3b8" font-size="15" font-family="system-ui, sans-serif">免下載任何安裝檔，瀏覽器 2 步開啟雲端編輯器，掌握三大內建原生核心元件</text>
  </g>

  <!-- Top Entry Flow -->
  <g transform="translate(80, 155)">
    <rect width="1440" height="120" rx="12" fill="#1e293b" stroke="#334155" stroke-width="1.2" filter="url(#shadow3)"/>
    
    <!-- Step 1 -->
    <g transform="translate(30, 20)">
      <circle cx="16" cy="16" r="16" fill="#10b981" fill-opacity="0.2"/>
      <text x="16" y="21" fill="#34d399" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">1</text>
      <text x="44" y="21" fill="#f8fafc" font-size="15" font-weight="700" font-family="system-ui, sans-serif">開啟空白試算表</text>
      <rect x="44" y="32" width="280" height="36" rx="6" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
      <text x="56" y="55" fill="#34d399" font-size="13" font-family="'JetBrains Mono', monospace">https://sheets.new</text>
      <text x="44" y="84" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">瀏覽器輸入快捷網址，自動建立新表格</text>
    </g>

    <!-- Arrow 1 -> 2 -->
    <g transform="translate(390, 58)">
      <polygon points="0,0 16,8 0,16" fill="#34d399"/>
    </g>

    <!-- Step 2 -->
    <g transform="translate(435, 20)">
      <circle cx="16" cy="16" r="16" fill="#38bdf8" fill-opacity="0.2"/>
      <text x="16" y="21" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">2</text>
      <text x="44" y="21" fill="#f8fafc" font-size="15" font-weight="700" font-family="system-ui, sans-serif">頂部選單開啟 Apps Script</text>
      <rect x="44" y="32" width="370" height="36" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="1"/>
      <text x="56" y="55" fill="#38bdf8" font-size="13" font-family="system-ui, sans-serif">擴充功能 (Extensions) ➔ Apps Script</text>
      <text x="44" y="84" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">試算表與後端腳本自動綁定（Container-bound）</text>
    </g>

    <!-- Arrow 2 -> 3 -->
    <g transform="translate(865, 58)">
      <polygon points="0,0 16,8 0,16" fill="#38bdf8"/>
    </g>

    <!-- Step 3 -->
    <g transform="translate(910, 20)">
      <circle cx="16" cy="16" r="16" fill="#818cf8" fill-opacity="0.2"/>
      <text x="16" y="21" fill="#818cf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">3</text>
      <text x="44" y="21" fill="#f8fafc" font-size="15" font-weight="700" font-family="system-ui, sans-serif">進入雲端 IDE 程式碼編輯器</text>
      <rect x="44" y="32" width="455" height="36" rx="6" fill="#0f172a" stroke="#818cf8" stroke-width="1"/>
      <text x="56" y="55" fill="#818cf8" font-size="13" font-family="'JetBrains Mono', monospace">Code.gs (內建語法高亮、版本控管、部署按鈕)</text>
      <text x="44" y="84" fill="#94a3b8" font-size="11" font-family="system-ui, sans-serif">貼上 Antigravity 提供的程式碼即可完成後端撰寫</text>
    </g>
  </g>

  <!-- Middle 3 Core Components -->
  <g transform="translate(80, 305)">
    <!-- Component 1 -->
    <g transform="translate(0, 0)">
      <rect width="460" height="320" rx="14" fill="url(#card-grad3)" stroke="#10b981" stroke-width="1.5" filter="url(#shadow3)"/>
      <rect x="25" y="20" width="130" height="26" rx="6" fill="#10b981" fill-opacity="0.2"/>
      <text x="90" y="38" fill="#34d399" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">核心 1 · 資料庫</text>
      <text x="25" y="75" fill="#f8fafc" font-size="18" font-weight="700" font-family="'JetBrains Mono', monospace">SpreadsheetApp</text>
      <text x="25" y="98" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">試算表引擎（視覺化表格資料庫）</text>

      <rect x="20" y="115" width="420" height="85" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
      <text x="32" y="140" fill="#34d399" font-size="12" font-family="'JetBrains Mono', monospace">let ss = SpreadsheetApp.getActiveSpreadsheet();</text>
      <text x="32" y="162" fill="#34d399" font-size="12" font-family="'JetBrains Mono', monospace">let sheet = ss.getActiveSheet();</text>
      <text x="32" y="184" fill="#a7f3d0" font-size="12" font-weight="700" font-family="'JetBrains Mono', monospace">sheet.appendRow([時間, 姓名, 信箱, 方案]);</text>

      <g transform="translate(25, 225)">
        <text x="0" y="0" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• <code>appendRow()</code> 自動在最後一行追加新訂單</text>
        <text x="0" y="24" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 免寫複雜的 SQL 語法，免維護資料庫伺服器</text>
        <text x="0" y="48" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 每一筆預購資料即時入帳，支援手機隨身查單</text>
        <text x="0" y="72" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 單一試算表高達 1,000 萬儲存格容量</text>
      </g>
    </g>

    <!-- Component 2 -->
    <g transform="translate(490, 0)">
      <rect width="460" height="320" rx="14" fill="url(#card-grad3)" stroke="#ef4444" stroke-width="1.5" filter="url(#shadow3)"/>
      <rect x="25" y="20" width="130" height="26" rx="6" fill="#ef4444" fill-opacity="0.2"/>
      <text x="90" y="38" fill="#f87171" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">核心 2 · 通訊中心</text>
      <text x="25" y="75" fill="#f8fafc" font-size="18" font-weight="700" font-family="'JetBrains Mono', monospace">GmailApp</text>
      <text x="25" y="98" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">郵件引擎（自動化客戶關係管理）</text>

      <rect x="20" y="115" width="420" height="85" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
      <text x="32" y="140" fill="#f87171" font-size="12" font-family="'JetBrains Mono', monospace">GmailApp.sendEmail(email, subject, body, {</text>
      <text x="44" y="162" fill="#fca5a5" font-size="12" font-family="'JetBrains Mono', monospace">name: 'SmartSound 官方團隊',</text>
      <text x="44" y="184" fill="#fca5a5" font-size="12" font-family="'JetBrains Mono', monospace">htmlBody: '感謝預購！您的方案是...'</text>
      <text x="32" y="196" fill="#f87171" font-size="12" font-family="'JetBrains Mono', monospace">});</text>

      <g transform="translate(25, 225)">
        <text x="0" y="0" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 透過自己的 Gmail 官方伺服器寄信，信譽良好</text>
        <text x="0" y="24" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 支援 HTML 富文本排版與產品圖片嵌入</text>
        <text x="0" y="48" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 免費版每日提供 100 封額度（企業版 1500 封）</text>
        <text x="0" y="72" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 訪客下單後立即收到確認信，安心感加倍！</text>
      </g>
    </g>

    <!-- Component 3 -->
    <g transform="translate(980, 0)">
      <rect width="460" height="320" rx="14" fill="url(#card-grad3)" stroke="#38bdf8" stroke-width="1.5" filter="url(#shadow3)"/>
      <rect x="25" y="20" width="130" height="26" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
      <text x="90" y="38" fill="#38bdf8" font-size="12" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">核心 3 · 雲端窗口</text>
      <text x="25" y="75" fill="#f8fafc" font-size="18" font-weight="700" font-family="'JetBrains Mono', monospace">ContentService</text>
      <text x="25" y="98" fill="#94a3b8" font-size="13" font-family="system-ui, sans-serif">Web API 封裝器（跨網域通訊協議）</text>

      <rect x="20" y="115" width="420" height="85" rx="8" fill="#020617" stroke="#334155" stroke-width="1"/>
      <text x="32" y="140" fill="#38bdf8" font-size="12" font-family="'JetBrains Mono', monospace">let response = { status: 'success' };</text>
      <text x="32" y="162" fill="#38bdf8" font-size="12" font-family="'JetBrains Mono', monospace">return ContentService</text>
      <text x="44" y="184" fill="#7dd3fc" font-size="12" font-family="'JetBrains Mono', monospace">.createTextOutput(JSON.stringify(response))</text>
      <text x="44" y="196" fill="#7dd3fc" font-size="12" font-family="'JetBrains Mono', monospace">.setMimeType(ContentService.MimeType.JSON);</text>

      <g transform="translate(25, 225)">
        <text x="0" y="0" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 將執行結果包裝成標準 JSON 格式</text>
        <text x="0" y="24" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 解決瀏覽器跨來源資源共用（CORS）限制</text>
        <text x="0" y="48" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 允許任何網域（GitHub Pages、本機）呼叫 API</text>
        <text x="0" y="72" fill="#cbd5e1" font-size="13" font-family="system-ui, sans-serif">• 每日支援數萬次 API 呼叫，承載中小型網站</text>
      </g>
    </g>
  </g>

  <!-- Bottom Deployment Golden Rule -->
  <g transform="translate(80, 655)">
    <rect width="1440" height="170" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="1.8" filter="url(#shadow3)"/>
    <rect x="30" y="20" width="160" height="28" rx="6" fill="#38bdf8" fill-opacity="0.2"/>
    <text x="110" y="39" fill="#38bdf8" font-size="13" font-weight="700" text-anchor="middle" font-family="system-ui, sans-serif">⭐ 部署 Web App 二大黃金設定</text>
    <text x="210" y="39" fill="#f8fafc" font-size="16" font-weight="700" font-family="system-ui, sans-serif">第 6 章實戰前必須牢記的設定法則（點擊 Deploy ➔ New deployment）：</text>

    <g transform="translate(30, 70)">
      <!-- Rule 1 -->
      <g transform="translate(0, 0)">
        <rect width="660" height="75" rx="8" fill="#0f172a" stroke="#10b981" stroke-width="1"/>
        <text x="20" y="28" fill="#34d399" font-size="14" font-weight="700" font-family="system-ui, sans-serif">規則 1：執行身分 (Execute as) ➔ 選擇「我 (Me: your-account@gmail.com)」</text>
        <text x="20" y="52" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">代表程式碼永遠使用「你的管理者權限」操作試算表與寄發 Gmail，訪客不需具備任何權限即可寫入。</text>
      </g>

      <!-- Rule 2 -->
      <g transform="translate(710, 0)">
        <rect width="670" height="75" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1"/>
        <text x="20" y="28" fill="#f59e0b" font-size="14" font-weight="700" font-family="system-ui, sans-serif">規則 2：誰能存取 (Who has access) ➔ 選擇「任何人 (Anyone)」</text>
        <text x="20" y="52" fill="#94a3b8" font-size="12" font-family="system-ui, sans-serif">代表全世界的網路訪客在 GitHub Pages 上點擊下單時，不需要登入任何 Google 帳號就能成功提交！</text>
      </g>
    </g>
  </g>
</svg>'''

with open("PIC/ch5_why_need_backend.svg", "w", encoding="utf-8") as f:
    f.write(svg1)
print(f"Generated ch5_why_need_backend.svg successfully ({len(svg1)} bytes)")

with open("PIC/ch5_web_app_flow.svg", "w", encoding="utf-8") as f:
    f.write(svg2)
print(f"Generated ch5_web_app_flow.svg successfully ({len(svg2)} bytes)")

with open("PIC/ch5_sheets_and_editor.svg", "w", encoding="utf-8") as f:
    f.write(svg3)
print(f"Generated ch5_sheets_and_editor.svg successfully ({len(svg3)} bytes)")

print("ALL CHAPTER 5 SVG DIAGRAMS GENERATED SUCCESSFULLY!")
