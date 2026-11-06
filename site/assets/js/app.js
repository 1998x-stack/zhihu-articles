(() => {
  "use strict";
  const root = document.documentElement;
  const nav = document.getElementById("category-nav");
  const mobile = document.getElementById("mobile-categories");
  const shelves = document.getElementById("shelves");
  const search = document.getElementById("book-search");
  const summary = document.getElementById("result-summary");
  const clearFilter = document.getElementById("clear-filter");
  const dialog = document.getElementById("book-dialog");
  const dialogContent = document.getElementById("dialog-content");
  const dialogClose = document.getElementById("dialog-close");
  const themeButton = document.getElementById("theme-toggle");
  const state = { category: "all", query: "", genres: [], books: [] };
  const colors = ["#566d70", "#293f42"];

  function el(tag, className = "", text = "") {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }
  function safeHex(value, fallback) {
    return /^#[0-9a-f]{6}$/i.test(value || "") ? value : fallback;
  }
  function countFor(id) {
    return id === "all" ? state.books.length : state.books.filter(book => book.genre === id).length;
  }
  function matches(book) {
    if (state.category !== "all" && book.genre !== state.category) return false;
    const q = state.query.toLocaleLowerCase("zh-CN");
    if (!q) return true;
    const genre = state.genres.find(item => item.skill === book.genre);
    const text = [book.title, book.subtitle, book.author, book.description, book.type, genre?.name, ...(book.tags || [])]
      .filter(Boolean).join(" ").toLocaleLowerCase("zh-CN");
    return text.includes(q);
  }
  function makeFilter(label, id, count, mobileMode = false) {
    const button = el("button", mobileMode ? "" : "category-btn");
    button.type = "button";
    button.dataset.category = id;
    const name = el("span", "", label);
    const total = el("span", "", String(count).padStart(2, "0"));
    button.append(name, total);
    button.addEventListener("click", () => {
      state.category = id;
      render();
      document.getElementById("library").scrollIntoView({ behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "auto" : "smooth", block: "start" });
    });
    return button;
  }
  function renderFilters() {
    nav.replaceChildren();
    mobile.replaceChildren();
    const items = [{ name: "全部藏书", skill: "all" }, ...state.genres];
    items.forEach(item => {
      const count = countFor(item.skill);
      const desktopButton = makeFilter(item.name, item.skill, count);
      const mobileButton = makeFilter(item.name, item.skill, count, true);
      const current = state.category === item.skill;
      desktopButton.classList.toggle("active", current);
      mobileButton.classList.toggle("active", current);
      desktopButton.setAttribute("aria-pressed", String(current));
      mobileButton.setAttribute("aria-pressed", String(current));
      nav.append(desktopButton);
      mobile.append(mobileButton);
    });
  }
  function coverFor(book) {
    const visual = el("div", "book-visual");
    visual.style.setProperty("--cover-start", safeHex(book.palette?.[0], colors[0]));
    visual.style.setProperty("--cover-end", safeHex(book.palette?.[1], colors[1]));
    visual.style.setProperty("--cover-ink", safeHex(book.coverInk, "#fff5e6"));
    visual.append(
      el("span", "cover-eyebrow", book.coverEyebrow || "THE READING ROOM"),
      el("strong", "cover-title", book.coverShort || book.title),
      el("span", "cover-bottom", book.coverFooter || "AN ORIGINAL STORY")
    );
    // An absent PNG intentionally uses the typographic e-book cover above.
    if (typeof book.cover === "string" && /^assets\/covers\/[a-z0-9-]+\.png$/.test(book.cover)) {
      const image = el("img");
      image.src = "./" + book.cover;
      image.alt = book.title + "封面";
      image.loading = "lazy";
      image.addEventListener("error", () => image.remove(), { once: true });
      visual.append(image);
    }
    return visual;
  }
  function renderBook(book) {
    const card = el("article", "book-card");
    const cover = el("button", "cover-button");
    cover.type = "button";
    cover.setAttribute("aria-label", "查看《" + book.title + "》详情");
    cover.append(coverFor(book));
    cover.addEventListener("click", () => openBook(book));
    const meta = el("div", "book-meta");
    const kind = el("div", "book-kind", book.type || "原创作品");
    const title = el("h4");
    const titleButton = el("button", "", book.title);
    titleButton.type = "button";
    titleButton.addEventListener("click", () => openBook(book));
    title.append(titleButton);
    const author = el("div", "book-author", book.author || "独立创作");
    const status = el("span", "book-status");
    status.append(el("span", "status-dot"), document.createTextNode(book.status || "馆藏作品"));
    meta.append(kind, title, author, status);
    card.append(cover, meta);
    return card;
  }
  function renderShelves() {
    shelves.replaceChildren();
    const filtered = state.books.filter(matches);
    const visibleGenres = state.category === "all"
      ? state.genres
      : state.genres.filter(item => item.skill === state.category);
    if (filtered.length === 0 && (state.query || state.category !== "all")) {
      const empty = el("div", "no-results");
      empty.append(el("strong", "", "暂时没有找到这本书"), el("div", "", "试试其他书名、关键词，或者返回全部书架。"));
      shelves.append(empty);
      summary.textContent = "找到 0 部作品";
      return;
    }
    let shown = 0;
    visibleGenres.forEach((genre, index) => {
      const books = filtered.filter(book => book.genre === genre.skill);
      if (state.query && !books.length) return;
      shown += books.length;
      const section = el("section", "shelf-section" + (!books.length ? " is-empty" : ""));
      section.id = "shelf-" + genre.skill;
      section.setAttribute("aria-label", genre.name + "书架");
      const heading = el("div", "shelf-titlebar");
      const h = el("h3");
      h.append(el("span", "shelf-number", String(state.genres.indexOf(genre) + 1).padStart(2, "0")), document.createTextNode(genre.name), el("span", "shelf-subtitle", genre.kind === "虚构" ? "FICTION" : "NONFICTION"));
      heading.append(h, el("span", "shelf-count", books.length ? books.length + " 部作品" : "等待新作"));
      section.append(heading);
      if (books.length) {
        const bookshelf = el("div", "bookshelf");
        books.forEach(book => bookshelf.append(renderBook(book)));
        section.append(bookshelf);
      } else {
        const empty = el("div", "empty-shelf");
        empty.append(el("span", "", "✳"), document.createTextNode("这个书架，正在等待第一本书。"));
        section.append(empty);
      }
      shelves.append(section);
    });
    summary.textContent = state.query || state.category !== "all"
      ? "找到 " + shown + " 部作品"
      : "共 " + shown + " 部作品 · " + state.genres.length + " 个主题";
  }
  function openBook(book) {
    dialogContent.replaceChildren();
    const layout = el("div", "dialog-layout");
    const cover = coverFor(book);
    const info = el("div", "dialog-info");
    info.append(el("div", "dialog-overline", (book.type || "原创作品") + " / " + (book.status || "馆藏作品")));
    const title = el("h2", "", "《" + book.title + "》");
    title.id = "dialog-title";
    info.append(title);
    if (book.subtitle) info.append(el("div", "dialog-en", book.subtitle));
    info.append(el("p", "dialog-description", book.description || "更多内容，敬请期待。"));
    const tags = el("div", "dialog-tags");
    (book.tags || []).slice(0, 6).forEach(tag => tags.append(el("span", "", tag)));
    info.append(tags);
    const actions = el("div", "dialog-actions");
    const source = el("a", "primary-action", "查看作品与目录 ↗");
    source.href = book.url;
    source.target = "_blank";
    source.rel = "noopener noreferrer";
    actions.append(source);
    if (book.readUrl && /^https:\/\//.test(book.readUrl)) {
      const read = el("a", "secondary-action", "开始阅读 ↗");
      read.href = book.readUrl;
      read.target = "_blank";
      read.rel = "noopener noreferrer";
      actions.append(read);
    }
    info.append(actions, el("p", "dialog-notice", book.note || "作品仍在创作中。站内陈列不代表正式出版或审稿通过。"));
    layout.append(cover, info);
    dialogContent.append(layout);
    if (typeof dialog.showModal === "function") dialog.showModal();
    else dialog.setAttribute("open", "");
  }
  function render() {
    renderFilters();
    renderShelves();
    clearFilter.hidden = !state.query && state.category === "all";
  }
  function changeTheme() {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    themeButton.setAttribute("aria-label", next === "dark" ? "切换至浅色主题" : "切换至深色主题");
    try { localStorage.setItem("reading-room-theme", next); } catch (_) {}
  }
  function initializeTheme() {
    try {
      const saved = localStorage.getItem("reading-room-theme");
      if (saved === "dark" || saved === "light") root.dataset.theme = saved;
    } catch (_) {}
    themeButton.setAttribute("aria-label", root.dataset.theme === "dark" ? "切换至浅色主题" : "切换至深色主题");
  }
  async function init() {
    initializeTheme();
    document.getElementById("year").textContent = String(new Date().getFullYear());
    themeButton.addEventListener("click", changeTheme);
    search.addEventListener("input", () => { state.query = search.value.trim(); render(); });
    clearFilter.addEventListener("click", () => { state.query = ""; state.category = "all"; search.value = ""; render(); search.focus(); });
    dialogClose.addEventListener("click", () => dialog.close ? dialog.close() : dialog.removeAttribute("open"));
    dialog.addEventListener("click", event => { if (event.target === dialog) dialog.close(); });
    try {
      const responses = await Promise.all([
        fetch("./assets/data/genres.json"),
        fetch("./assets/data/books.json")
      ]);
      if (!responses.every(response => response.ok)) throw new Error("无法读取馆藏索引");
      const [genres, books] = await Promise.all(responses.map(response => response.json()));
      if (!Array.isArray(genres) || !Array.isArray(books)) throw new Error("馆藏索引格式有误");
      state.genres = genres;
      state.books = books;
      document.getElementById("genre-count").textContent = String(genres.length);
      document.getElementById("book-count").textContent = String(books.length).padStart(2, "0");
      render();
    } catch (error) {
      shelves.replaceChildren(el("div", "no-results", "书架暂时无法载入。请刷新页面，或从 GitHub 仓库查看作品目录。"));
      summary.textContent = "馆藏加载失败";
      console.error("Reading Room:", error);
    }
  }
  init();
})();