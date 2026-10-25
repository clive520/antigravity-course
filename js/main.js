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

  // Image Lightbox with Box-Selection Zoom & Interactive Pan/Reset
  const lessonImages = document.querySelectorAll('.lesson-content img');
  if (lessonImages.length > 0) {
    // Create Lightbox DOM
    const overlay = document.createElement('div');
    overlay.className = 'image-lightbox-overlay';
    overlay.innerHTML = `
      <div class="image-lightbox-toolbar">
        <div class="image-lightbox-group">
          <button type="button" class="image-lightbox-btn active" id="lightboxModeBox" title="按住滑鼠左鍵框選任意局部，立即放大至全螢幕">🔲 框選放大</button>
          <button type="button" class="image-lightbox-btn" id="lightboxModePan" title="按住滑鼠拖曳移動圖片">✋ 拖曳平移</button>
        </div>
        <div class="image-lightbox-group">
          <button type="button" class="image-lightbox-btn" id="lightboxZoomOut" title="縮小">➖</button>
          <span class="image-lightbox-zoom-level" id="lightboxZoomLevel">100%</span>
          <button type="button" class="image-lightbox-btn" id="lightboxZoomIn" title="放大">➕</button>
        </div>
        <button type="button" class="image-lightbox-btn" id="lightboxResetBtn" title="還原全圖適應視窗">🔄 還原全圖</button>
        <button type="button" class="image-lightbox-btn" id="lightboxCloseBtn" title="關閉燈箱 (ESC)">✕ 關閉</button>
      </div>
      <div class="image-lightbox-stage" id="lightboxStage">
        <div class="image-lightbox-img-wrapper" id="lightboxWrapper">
          <img src="" alt="" class="image-lightbox-img" id="lightboxImg" draggable="false">
        </div>
        <div class="image-lightbox-selection-box" id="lightboxSelectionBox"></div>
      </div>
      <div class="image-lightbox-caption" id="lightboxCaption"></div>
    `;
    document.body.appendChild(overlay);

    const lightboxImg = document.getElementById('lightboxImg');
    const lightboxWrapper = document.getElementById('lightboxWrapper');
    const lightboxSelectionBox = document.getElementById('lightboxSelectionBox');
    const lightboxCaption = document.getElementById('lightboxCaption');
    const lightboxCloseBtn = document.getElementById('lightboxCloseBtn');
    const lightboxResetBtn = document.getElementById('lightboxResetBtn');
    const lightboxZoomIn = document.getElementById('lightboxZoomIn');
    const lightboxZoomOut = document.getElementById('lightboxZoomOut');
    const lightboxZoomLevel = document.getElementById('lightboxZoomLevel');
    const lightboxModeBox = document.getElementById('lightboxModeBox');
    const lightboxModePan = document.getElementById('lightboxModePan');
    const lightboxStage = document.getElementById('lightboxStage');

    let currentMode = 'box'; // 'box' or 'pan'
    let scale = 1;
    let translateX = 0;
    let translateY = 0;
    let isDrawing = false;
    let isPanning = false;
    let startX = 0;
    let startY = 0;
    let panStartX = 0;
    let panStartY = 0;

    const setMode = (mode) => {
      currentMode = mode;
      if (mode === 'box') {
        lightboxModeBox.classList.add('active');
        lightboxModePan.classList.remove('active');
        lightboxStage.classList.remove('mode-pan');
      } else {
        lightboxModePan.classList.add('active');
        lightboxModeBox.classList.remove('active');
        lightboxStage.classList.add('mode-pan');
      }
    };

    lightboxModeBox.addEventListener('click', () => setMode('box'));
    lightboxModePan.addEventListener('click', () => setMode('pan'));

    const updateZoomDisplay = () => {
      lightboxZoomLevel.innerText = `${Math.round(scale * 100)}%`;
    };

    const applyTransform = (animate = false) => {
      lightboxWrapper.style.transition = animate ? 'transform 0.28s cubic-bezier(0.2, 0, 0, 1)' : 'none';
      lightboxWrapper.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
      updateZoomDisplay();
    };

    const resetZoom = (animate = true) => {
      scale = 1;
      translateX = 0;
      translateY = 0;
      applyTransform(animate);
    };

    lightboxResetBtn.addEventListener('click', () => resetZoom(true));

    lightboxZoomIn.addEventListener('click', () => {
      scale = Math.min(scale * 1.35, 16);
      applyTransform(true);
    });

    lightboxZoomOut.addEventListener('click', () => {
      scale = Math.max(scale / 1.35, 0.75);
      if (scale <= 1) {
        scale = 1;
        translateX = 0;
        translateY = 0;
      }
      applyTransform(true);
    });

    // Mouse Wheel Zoom
    lightboxStage.addEventListener('wheel', (e) => {
      e.preventDefault();
      const rect = lightboxStage.getBoundingClientRect();
      const stageCenterX = rect.width / 2;
      const stageCenterY = rect.height / 2;
      const mouseX = e.clientX - rect.left;
      const mouseY = e.clientY - rect.top;

      const x_content = (mouseX - stageCenterX - translateX) / scale;
      const y_content = (mouseY - stageCenterY - translateY) / scale;

      const factor = e.deltaY < 0 ? 1.2 : 0.83;
      let newScale = Math.min(Math.max(scale * factor, 0.75), 16);
      if (newScale <= 1.05 && factor < 1) {
        newScale = 1;
        translateX = 0;
        translateY = 0;
      } else {
        translateX = mouseX - stageCenterX - x_content * newScale;
        translateY = mouseY - stageCenterY - y_content * newScale;
      }
      scale = newScale;
      applyTransform(false);
    }, { passive: false });

    // Drag / Box Selection Mouse Events
    lightboxStage.addEventListener('mousedown', (e) => {
      if (e.button !== 0 && e.button !== 1 && e.button !== 2) return;
      const isRightOrMiddle = e.button === 2 || e.button === 1 || e.shiftKey || e.altKey;

      if (currentMode === 'pan' || isRightOrMiddle) {
        isPanning = true;
        panStartX = e.clientX - translateX;
        panStartY = e.clientY - translateY;
        lightboxStage.style.cursor = 'grabbing';
      } else if (currentMode === 'box' && e.button === 0) {
        isDrawing = true;
        const rect = lightboxStage.getBoundingClientRect();
        startX = e.clientX;
        startY = e.clientY;
        lightboxSelectionBox.style.left = `${startX - rect.left}px`;
        lightboxSelectionBox.style.top = `${startY - rect.top}px`;
        lightboxSelectionBox.style.width = '0px';
        lightboxSelectionBox.style.height = '0px';
        lightboxSelectionBox.style.display = 'block';
      }
    });

    window.addEventListener('mousemove', (e) => {
      if (isPanning) {
        translateX = e.clientX - panStartX;
        translateY = e.clientY - panStartY;
        applyTransform(false);
      } else if (isDrawing) {
        const rect = lightboxStage.getBoundingClientRect();
        const curX = Math.min(Math.max(e.clientX, rect.left), rect.right);
        const curY = Math.min(Math.max(e.clientY, rect.top), rect.bottom);

        const left = Math.min(startX, curX) - rect.left;
        const top = Math.min(startY, curY) - rect.top;
        const width = Math.abs(curX - startX);
        const height = Math.abs(curY - startY);

        lightboxSelectionBox.style.left = `${left}px`;
        lightboxSelectionBox.style.top = `${top}px`;
        lightboxSelectionBox.style.width = `${width}px`;
        lightboxSelectionBox.style.height = `${height}px`;
      }
    });

    window.addEventListener('mouseup', (e) => {
      if (isPanning) {
        isPanning = false;
        lightboxStage.style.cursor = currentMode === 'pan' ? 'grab' : 'crosshair';
      }

      if (isDrawing) {
        isDrawing = false;
        lightboxSelectionBox.style.display = 'none';

        const rect = lightboxStage.getBoundingClientRect();
        const curX = Math.min(Math.max(e.clientX, rect.left), rect.right);
        const curY = Math.min(Math.max(e.clientY, rect.top), rect.bottom);

        const boxLeft = Math.min(startX, curX) - rect.left;
        const boxTop = Math.min(startY, curY) - rect.top;
        const boxWidth = Math.abs(curX - startX);
        const boxHeight = Math.abs(curY - startY);

        // If drawn box is larger than 25px in both dimensions, trigger Box Zoom
        if (boxWidth >= 25 && boxHeight >= 25) {
          const boxCenterX = boxLeft + boxWidth / 2;
          const boxCenterY = boxTop + boxHeight / 2;
          const stageCenterX = rect.width / 2;
          const stageCenterY = rect.height / 2;

          const x_content = (boxCenterX - stageCenterX - translateX) / scale;
          const y_content = (boxCenterY - stageCenterY - translateY) / scale;

          const zoomRatio = Math.min(rect.width / boxWidth, rect.height / boxHeight) * 0.94;
          const newScale = Math.min(Math.max(scale * zoomRatio, 1), 16);

          translateX = - x_content * newScale;
          translateY = - y_content * newScale;
          scale = newScale;

          applyTransform(true);
        }
      }
    });

    // Context menu prevent so right click pan feels smooth
    lightboxStage.addEventListener('contextmenu', (e) => e.preventDefault());

    const openLightbox = (src, alt) => {
      lightboxImg.style.width = '';
      lightboxImg.style.height = '';
      lightboxImg.src = src;
      lightboxImg.alt = alt || '';
      resetZoom(false);
      setMode('box');
      lightboxCaption.innerHTML = alt 
        ? `${alt} <span class="hint">（💡 按住滑鼠左鍵「框選」任一區域立即放大至全螢幕，按「還原全圖」復原）</span>` 
        : '<span class="hint">（💡 按住滑鼠左鍵「框選」任一區域立即放大至全螢幕，按「還原全圖」復原）</span>';
      overlay.classList.add('active');
      document.body.style.overflow = 'hidden';

      const ensureVisible = () => {
        // 保底機制：若遇到無固有尺寸的向量圖導致寬高坍縮
        if (lightboxImg.offsetWidth < 50 || lightboxImg.offsetHeight < 50) {
          const stageRect = lightboxStage.getBoundingClientRect();
          const targetW = Math.min(stageRect.width * 0.92, 1200);
          lightboxImg.style.width = `${targetW}px`;
          lightboxImg.style.height = 'auto';
        }
      };

      if (lightboxImg.complete) {
        ensureVisible();
      } else {
        lightboxImg.onload = ensureVisible;
      }
    };

    const closeLightbox = () => {
      overlay.classList.remove('active');
      document.body.style.overflow = '';
      resetZoom(false);
    };

    lightboxCloseBtn.addEventListener('click', closeLightbox);

    overlay.addEventListener('click', (e) => {
      if (e.target === overlay) {
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

