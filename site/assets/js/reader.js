(() => {
  "use strict";

  const root = document.documentElement;
  const body = document.body;
  const header = document.querySelector(".reader-header");
  const sidebar = document.getElementById("reader-sidebar");
  const overlay = document.getElementById("sidebar-overlay");
  const toggles = [
    document.getElementById("toc-toggle"),
    document.querySelector(".mobile-chapters-button")
  ].filter(Boolean);
  const progress = document.getElementById("reading-progress");
  const progressLabel = document.getElementById("reading-percent");
  const sectionLabel = document.getElementById("reader-current-section");
  const backTop = document.getElementById("back-top");
  const themeButton = document.querySelector(".theme-toggle");
  const typeButton = document.querySelector(".type-toggle");
  const chapterHero = document.querySelector(".chapter-heading");
  const headings = [...document.querySelectorAll(".prose h2, .prose h3")];
  const reduceMotion = !!(window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  let size = 1;
  let queued = false;
  let sectionName = "";

  try {
    const savedTheme = localStorage.getItem("reading-room-theme");
    if (savedTheme === "dark" || savedTheme === "light") {
      root.dataset.theme = savedTheme;
    }
    const savedSize = Number(localStorage.getItem("reading-room-font-size"));
    if (Number.isFinite(savedSize) && savedSize >= .85 && savedSize <= 1.3) {
      size = savedSize;
    }
    if (localStorage.getItem("reading-room-font-family") === "sans") {
      body.classList.add("reader-sans-mode");
    }
  } catch (_) {
    // The reader remains fully functional if storage is blocked.
  }
  root.style.setProperty("--reader-font-scale", String(size));

  function remember(key, value) {
    try { localStorage.setItem(key, value); } catch (_) {}
  }

  function setSidebar(open) {
    sidebar.classList.toggle("is-open", open);
    overlay.hidden = !open;
    toggles.forEach(button => button.setAttribute("aria-expanded", String(open)));
    body.style.overflow = open ? "hidden" : "";
  }

  toggles.forEach(button => button.addEventListener("click", () => {
    setSidebar(!sidebar.classList.contains("is-open"));
  }));
  overlay.addEventListener("click", () => setSidebar(false));
  window.addEventListener("keydown", event => {
    if (event.key === "Escape" && sidebar.classList.contains("is-open")) {
      setSidebar(false);
      toggles[0]?.focus();
    }
  });
  sidebar.addEventListener("click", event => {
    if (event.target.closest(".toc-chapter")) setSidebar(false);
  });
  const mobileLayout = window.matchMedia ? window.matchMedia("(max-width: 770px)") : null;
  if (mobileLayout) {
    const closeOnDesktop = event => { if (!event.matches) setSidebar(false); };
    if (mobileLayout.addEventListener) mobileLayout.addEventListener("change", closeOnDesktop);
    else if (mobileLayout.addListener) mobileLayout.addListener(closeOnDesktop);
  }

  function changeSize(delta) {
    size = Math.round(Math.min(1.3, Math.max(.85, size + delta)) * 100) / 100;
    root.style.setProperty("--reader-font-scale", String(size));
    remember("reading-room-font-size", String(size));
    updateProgress();
  }

  document.querySelector(".font-minus").addEventListener("click", () => changeSize(-.1));
  document.querySelector(".font-plus").addEventListener("click", () => changeSize(.1));

  function updateTypeButton() {
    const isSans = body.classList.contains("reader-sans-mode");
    typeButton.setAttribute("aria-pressed", String(isSans));
    typeButton.setAttribute("aria-label",
      isSans ? "切换为衬线正文字体" : "切换为无衬线正文字体");
    typeButton.title = isSans ? "切换为书籍衬线字体" : "切换为现代无衬线字体";
  }
  typeButton.addEventListener("click", () => {
    const isSans = body.classList.toggle("reader-sans-mode");
    remember("reading-room-font-family", isSans ? "sans" : "serif");
    updateTypeButton();
    updateProgress();
  });
  updateTypeButton();

  themeButton.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    themeButton.setAttribute("aria-label", next === "dark" ? "切换浅色主题" : "切换深色主题");
    remember("reading-room-theme", next);
  });
  themeButton.setAttribute("aria-label",
    root.dataset.theme === "dark" ? "切换浅色主题" : "切换深色主题");

  if (chapterHero) {
    const cue = document.createElement("div");
    cue.className = "reader-hero-scroll";
    cue.setAttribute("aria-hidden", "true");
    const words = document.createElement("span");
    words.textContent = "SCROLL TO EXPLORE";
    const arrow = document.createElement("span");
    arrow.className = "scroll-arrow";
    arrow.textContent = "↓";
    cue.append(words, arrow);
    chapterHero.append(cue);
  }

  // Scroll-based movement is limited to one decorative hero; paragraphs never parallax.
  function updateCurrentSection() {
    let current = "";
    for (const heading of headings) {
      if (heading.getBoundingClientRect().top <= 122) {
        current = heading.textContent.trim();
      } else {
        break;
      }
    }
    if (current !== sectionName) {
      sectionName = current;
      sectionLabel.textContent = current;
      sectionLabel.classList.toggle("is-visible", !!current);
    }
  }

  function updateProgress() {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    const percent = max > 0
      ? Math.min(100, Math.max(0, window.scrollY / max * 100))
      : 100;

    progress.style.width = percent.toFixed(2) + "%";
    progressLabel.textContent = Math.round(percent) + "%";
    header.classList.toggle("is-scrolled", window.scrollY > 24);
    body.classList.toggle("reader-scrolled", window.scrollY > 24);
    backTop.classList.toggle("visible", window.scrollY > 650);
    updateCurrentSection();

    if (chapterHero && !reduceMotion && window.scrollY < 1100) {
      chapterHero.style.setProperty("--hero-shift",
        Math.min(80, Math.round(window.scrollY * .1)) + "px");
    }
  }

  window.addEventListener("scroll", () => {
    if (queued) return;
    queued = true;
    requestAnimationFrame(() => {
      queued = false;
      updateProgress();
    });
  }, { passive: true });
  window.addEventListener("resize", updateProgress, { passive: true });
  window.addEventListener("load", updateProgress, { once: true });

  backTop.addEventListener("click", () => window.scrollTo({
    top: 0,
    behavior: reduceMotion ? "auto" : "smooth"
  }));

  // Make the reveal progressive and fail-open: without JS or observer, every
  // heading, illustration and note stays visible.
  function enableReveals() {
    if (reduceMotion || !("IntersectionObserver" in window)) return;
    const targets = document.querySelectorAll([
      ".prose h2", ".prose h3", ".prose blockquote", ".prose img",
      ".prose .admonition", ".prose table",
      ".reader-book-hero", ".reader-chapter-list .toc-part"
    ].join(","));
    if (!targets.length) return;
    const observer = new IntersectionObserver(entries => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        entry.target.classList.add("is-inview");
        observer.unobserve(entry.target);
      }
    }, { rootMargin: "0px 0px -6% 0px", threshold: .06 });
    targets.forEach(target => {
      target.classList.add("motion-reveal");
      observer.observe(target);
    });
    root.classList.add("reader-motion-enabled");
  }
  enableReveals();

  // Refined pointer-responsive light, only for fine-pointer devices.
  if (chapterHero && !reduceMotion && window.matchMedia &&
      window.matchMedia("(pointer: fine)").matches) {
    let pointerFrame = 0;
    let pointerX = 77;
    let pointerY = 23;
    chapterHero.addEventListener("pointermove", event => {
      const rect = chapterHero.getBoundingClientRect();
      pointerX = Math.max(0, Math.min(100,
        (event.clientX - rect.left) / rect.width * 100));
      pointerY = Math.max(0, Math.min(100,
        (event.clientY - rect.top) / rect.height * 100));
      if (pointerFrame) return;
      pointerFrame = requestAnimationFrame(() => {
        chapterHero.style.setProperty("--pointer-x", pointerX.toFixed(1) + "%");
        chapterHero.style.setProperty("--pointer-y", pointerY.toFixed(1) + "%");
        pointerFrame = 0;
      });
    }, { passive: true });
    chapterHero.addEventListener("pointerleave", () => {
      chapterHero.style.setProperty("--pointer-x", "77%");
      chapterHero.style.setProperty("--pointer-y", "23%");
    });
  }

  updateProgress();
  // MathJax can change the document's final height after page load.
  if (window.MathJax?.startup?.promise) {
    window.MathJax.startup.promise.then(updateProgress).catch(() => {});
  }
})();