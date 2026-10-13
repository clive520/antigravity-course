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

  // Image Lightbox (Click to Zoom) for all instructional images
  const lessonImages = document.querySelectorAll('.lesson-content img');
  if (lessonImages.length > 0) {
    // Create Lightbox DOM
    const overlay = document.createElement('div');
    overlay.className = 'image-lightbox-overlay';
    overlay.innerHTML = `
      <div class="image-lightbox-toolbar">
        <button type="button" class="image-lightbox-btn" id="lightboxZoomToggle">🔍 切換原始大小</button>
        <button type="button" class="image-lightbox-btn" id="lightboxCloseBtn">✕ 關閉 (ESC)</button>
      </div>
      <div class="image-lightbox-stage" id="lightboxStage">
        <img src="" alt="" class="image-lightbox-img" id="lightboxImg">
      </div>
      <div class="image-lightbox-caption" id="lightboxCaption"></div>
    `;
    document.body.appendChild(overlay);

    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const lightboxCloseBtn = document.getElementById('lightboxCloseBtn');
    const lightboxZoomToggle = document.getElementById('lightboxZoomToggle');
    const lightboxStage = document.getElementById('lightboxStage');

    const openLightbox = (src, alt) => {
      lightboxImg.src = src;
      lightboxImg.alt = alt || '';
      lightboxImg.classList.remove('zoomed-full');
      lightboxZoomToggle.innerText = '🔍 切換 100% 原始尺寸';
      lightboxCaption.innerText = alt ? `${alt}（點擊圖片可切換縮放，按 ESC 關閉）` : '點擊圖片可切換縮放，按 ESC 關閉';
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';
    };

    const closeLightbox = () => {
      overlay.classList.remove('active');
      document.body.style.overflow = '';
    };

    const toggleFullZoom = (e) => {
      if (e) e.stopPropagation();
      const isFull = lightboxImg.classList.toggle('zoomed-full');
      lightboxZoomToggle.innerText = isFull ? '🗗 適應視窗大小' : '🔍 切換 100% 原始尺寸';
    };

    lightboxImg.addEventListener('click', toggleFullZoom);
    lightboxZoomToggle.addEventListener('click', toggleFullZoom);
    lightboxCloseBtn.addEventListener('click', closeLightbox);

    overlay.addEventListener('click', (e) => {
      if (e.target === overlay || e.target === lightboxStage) {
        closeLightbox();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && overlay.classList.contains('active')) {
        closeLightbox();
      }
    });

    lessonImages.forEach((img) => {
      img.setAttribute('title', '點擊放大檢視圖片');
      // Insert a subtle clickable zoom hint pill above each image
      const hint = document.createElement('div');
      hint.className = 'img-zoom-hint';
      hint.innerHTML = '🔍 點擊圖片放大觀看';
      img.parentNode.insertBefore(hint, img);

      const triggerOpen = () => openLightbox(img.src, img.alt);
      img.addEventListener('click', triggerOpen);
      hint.addEventListener('click', triggerOpen);
    });
  }
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

