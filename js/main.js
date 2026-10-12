// Theme Toggle & Interactive Utilities
document.addEventListener('DOMContentLoaded', () => {
  // Theme management
  const savedTheme = localStorage.getItem('theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeIcon(savedTheme);

  const themeBtn = document.getElementById('themeToggle');
  if (themeBtn) {
    themeBtn.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme') || 'dark';
      const target = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', target);
      localStorage.setItem('theme', target);
      updateThemeIcon(target);
    });
  }

  // Copy code buttons
  document.querySelectorAll('.copy-btn').forEach(btn => {
    btn.addEventListener('click', async () => {
      const targetId = btn.getAttribute('data-target');
      let textToCopy = '';
      if (targetId) {
        const el = document.getElementById(targetId);
        if (el) textToCopy = el.innerText;
      } else {
        const pre = btn.closest('.code-block').querySelector('pre');
        if (pre) textToCopy = pre.innerText;
      }

      try {
        await navigator.clipboard.writeText(textToCopy);
        const originalText = btn.innerText;
        btn.innerText = '已複製！';
        btn.style.color = '#10b981';
        setTimeout(() => {
          btn.innerText = originalText;
          btn.style.color = '';
        }, 2000);
      } catch (err) {
        console.error('複製失敗:', err);
      }
    });
  });
});

function updateThemeIcon(theme) {
  const icon = document.getElementById('themeIcon');
  if (!icon) return;
  if (theme === 'light') {
    icon.innerHTML = '🌙 深色模式';
  } else {
    icon.innerHTML = '☀️ 淺色模式';
  }
}
