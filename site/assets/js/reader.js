(() => {
  "use strict";
  const root = document.documentElement;
  const sidebar = document.getElementById("reader-sidebar");
  const overlay = document.getElementById("sidebar-overlay");
  const toggles = [document.getElementById("toc-toggle"), document.querySelector(".mobile-chapters-button")];
  const progress = document.getElementById("reading-progress");
  const backTop = document.getElementById("back-top");
  const themeButton = document.querySelector(".theme-toggle");
  let size = 1;

  try {
    const saved = localStorage.getItem("reading-room-theme");
    if (saved === "dark" || saved === "light") root.dataset.theme = saved;
    const fontSize = Number(localStorage.getItem("reading-room-font-size"));
    if (Number.isFinite(fontSize) && fontSize >= .85 && fontSize <= 1.3) size = fontSize;
  } catch (_) {}
  root.style.setProperty("--reader-font-scale", String(size));

  function setSidebar(open) {
    sidebar.classList.toggle("is-open", open);
    overlay.hidden = !open;
    toggles.forEach(btn => btn && btn.setAttribute("aria-expanded", String(open)));
    document.body.style.overflow = open ? "hidden" : "";
  }
  toggles.forEach(btn => btn && btn.addEventListener("click", () => setSidebar(!sidebar.classList.contains("is-open"))));
  overlay.addEventListener("click", () => setSidebar(false));
  window.addEventListener("keydown", event => { if (event.key === "Escape") setSidebar(false); });
  sidebar.addEventListener("click", event => {
    if (event.target.closest(".toc-chapter")) setSidebar(false);
  });

  document.querySelector(".font-minus").addEventListener("click", () => changeSize(-.1));
  document.querySelector(".font-plus").addEventListener("click", () => changeSize(.1));
  function changeSize(delta) {
    size = Math.round(Math.min(1.3, Math.max(.85, size + delta)) * 100) / 100;
    root.style.setProperty("--reader-font-scale", String(size));
    try { localStorage.setItem("reading-room-font-size", String(size)); } catch (_) {}
    updateProgress();
  }
  themeButton.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    try { localStorage.setItem("reading-room-theme", next); } catch (_) {}
  });

  let queued = false;
  function updateProgress() {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const percent = max > 0 ? Math.min(100, Math.max(0, window.scrollY / max * 100)) : 100;
    progress.style.width = percent.toFixed(2) + "%";
    backTop.classList.toggle("visible", window.scrollY > 650);
  }
  window.addEventListener("scroll", () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => { queued = false; updateProgress(); });
  }, { passive: true });
  window.addEventListener("resize", updateProgress, { passive: true });
  backTop.addEventListener("click", () => window.scrollTo({ top: 0, behavior: matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth" }));
  updateProgress();
})();