#!/usr/bin/env python3
"""Build an ebook bookshelf and chapter HTML from explicit per-book manifests.

Only files explicitly referenced by book.json become reader pages. Research,
editorial documents, AI prompts, and unlisted manuscript files are not copied.
"""
from __future__ import annotations

import argparse
from collections import Counter
from html import escape
import json
from pathlib import Path, PurePosixPath
import re
import shutil
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
COVER_PATH = re.compile(r"^assets/covers/[a-z0-9-]+\.png$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MEDIA_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}
REPOSITORIES = {
    "self": (ROOT, "1998x-stack/zhihu-articles"),
    "1998x-stack/The-Empty-Spaces": (
        ROOT / "external" / "the-empty-spaces",
        "1998x-stack/The-Empty-Spaces",
    ),
}
ALLOWED_STATUSES = {"draft": "正文初稿 · 待审校", "outline": "待撰写 · 章节占位", "final": "已审定"}
CHAPTER_URL = "read/{book_id}/{chapter_id}/"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_path(base: Path, relative: str) -> Path:
    """Allow only normalized, in-tree relative paths from the curated manifests."""
    if not isinstance(relative, str) or not relative or "\\" in relative:
        raise ValueError(f"Invalid relative path: {relative!r}")
    name = PurePosixPath(relative)
    if name.is_absolute() or any(p in ("..", ".") for p in name.parts):
        raise ValueError(f"Unsafe relative path: {relative!r}")
    root = base.resolve()
    candidate = (root / relative).resolve()
    if not candidate.is_relative_to(root):
        raise ValueError(f"Path escapes its book root: {relative}")
    return candidate


def validate_books(genres: list[dict], books: list[dict]) -> None:
    genre_ids = {genre["skill"] for genre in genres}
    seen: set[str] = set()
    if not isinstance(books, list):
        raise ValueError("books.json must be a list")
    for i, book in enumerate(books):
        book_id = book.get("id", "")
        if not isinstance(book_id, str) or not SLUG.fullmatch(book_id):
            raise ValueError(f"Invalid book id at position {i}")
        if book_id in seen:
            raise ValueError(f"Duplicate book id: {book_id}")
        seen.add(book_id)
        if book.get("genre") not in genre_ids:
            raise ValueError(f"Unknown genre for {book_id}: {book.get('genre')}")
        for key in ("title", "author", "status", "description", "url"):
            if not isinstance(book.get(key), str) or not book[key].strip():
                raise ValueError(f"{book_id} requires nonempty {key}")
        if urlsplit(book["url"]).scheme != "https":
            raise ValueError(f"{book_id} must use an HTTPS project URL")
        read_url = book.get("readUrl")
        if read_url and urlsplit(read_url).scheme != "https":
            raise ValueError(f"{book_id} must use an HTTPS reader URL")
        cover = book.get("cover")
        if cover is not None:
            if not isinstance(cover, str) or not COVER_PATH.fullmatch(cover):
                raise ValueError(f"Invalid PNG cover path for {book_id}")
            if not (SITE / cover).is_file():
                raise ValueError(f"Cover PNG not found for {book_id}: {cover}")
        palette = book.get("palette", [])
        if not isinstance(palette, list) or len(palette) != 2 or not all(
            re.fullmatch(r"#[0-9a-fA-F]{6}", str(c)) for c in palette
        ):
            raise ValueError(f"{book_id} needs a pair of hexadecimal cover colors")
        if not isinstance(book.get("tags", []), list):
            raise ValueError(f"{book_id} tags must be a list")
        source = book.get("source")
        if source:
            if not isinstance(source, dict) or source.get("repository") not in REPOSITORIES:
                raise ValueError(f"Invalid source repository for {book_id}")
            manifest = source.get("manifest")
            if not isinstance(manifest, str) or not manifest.endswith(".json"):
                raise ValueError(f"Invalid book manifest for {book_id}")


def read_manifest(book: dict, external_root: Path | None):
    source = book.get("source")
    if not source:
        return None
    source_root, github_repo = REPOSITORIES[source["repository"]]
    if source["repository"] != "self" and external_root is not None:
        source_root = external_root
    manifest_file = safe_path(source_root, source["manifest"])
    if not manifest_file.is_file():
        return None
    manifest = load_json(manifest_file)
    if manifest.get("id") != book["id"] or manifest.get("schema_version") != 1:
        raise ValueError(f"Invalid per-book manifest identity for {book['id']}")
    chapters = manifest.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        raise ValueError(f"{book['id']} requires at least one chapter")
    seen_ids: set[str] = set()
    seen_files: set[str] = set()
    for chapter in chapters:
        chapter_id = chapter.get("id")
        if not isinstance(chapter_id, str) or not SLUG.fullmatch(chapter_id):
            raise ValueError(f"Invalid chapter id in {book['id']}")
        if chapter_id in seen_ids:
            raise ValueError(f"Duplicate chapter id {chapter_id} in {book['id']}")
        seen_ids.add(chapter_id)
        if chapter.get("status") not in ALLOWED_STATUSES:
            raise ValueError(f"Missing or invalid chapter status: {chapter_id}")
        if not chapter.get("title") or not chapter.get("part"):
            raise ValueError(f"Missing title/part: {book['id']}/{chapter_id}")
        file = safe_path(manifest_file.parent, chapter.get("file"))
        if file.suffix.lower() != ".md" or not file.is_file():
            raise ValueError(f"Missing Markdown file: {file}")
        if str(file) in seen_files:
            raise ValueError(f"Duplicate Markdown mapping: {file}")
        seen_files.add(str(file))
        chapter["_path"] = file
    return manifest, manifest_file, source_root, github_repo


def make_toc(chapters: list[dict], book: dict, root_prefix: str, active: str) -> str:
    items = []
    last_part = None
    for chapter in chapters:
        part = chapter["part"]
        if part != last_part:
            items.append('<div class="toc-part">' + escape(part) + "</div>")
            last_part = part
        current = chapter["id"] == active
        label = ALLOWED_STATUSES[chapter["status"]]
        href = root_prefix + CHAPTER_URL.format(book_id=book["id"], chapter_id=chapter["id"])
        items.append(
            '<a class="toc-chapter' + (' active' if current else '') + '" '
            + ('aria-current="page" ' if current else '')
            + 'href="' + escape(href, quote=True) + '">'
            + '<span>' + escape(chapter["title"]) + '</span>'
            + '<small class="' + escape(chapter["status"]) + '">' + escape(label) + "</small>"
            + "</a>"
        )
    return "\n".join(items)


def fix_links(html: str, source_file: Path, source_root: Path,
              repo: str, route_by_file: dict[Path, str], book_id: str,
              out: Path, root_prefix: str) -> str:
    from bs4 import BeautifulSoup
    import bleach

    soup = BeautifulSoup(html, "html.parser")
    for anchor in soup.find_all("a", href=True):
        href = str(anchor["href"])
        parts = urlsplit(href)
        if parts.scheme or parts.netloc or href.startswith("#"):
            if parts.scheme in {"https", "http"}:
                anchor["rel"] = "noopener noreferrer"
            continue
        if not parts.path:
            continue
        try:
            target = (source_file.parent / unquote(parts.path)).resolve()
            if not target.is_relative_to(source_root.resolve()):
                anchor["href"] = "#"
            elif target in route_by_file:
                anchor["href"] = root_prefix + route_by_file[target] + (
                    "#" + parts.fragment if parts.fragment else ""
                )
            else:
                rel = target.relative_to(source_root.resolve()).as_posix()
                anchor["href"] = "https://github.com/" + repo + "/blob/main/" + quote(rel, safe="/") + (
                    "#" + parts.fragment if parts.fragment else ""
                )
                anchor["rel"] = "noopener noreferrer"
        except (ValueError, OSError):
            anchor["href"] = "#"
    for img in soup.find_all("img", src=True):
        raw = str(img["src"])
        parts = urlsplit(raw)
        if parts.scheme in {"https", "http"}:
            img["loading"] = "lazy"
            continue
        if parts.scheme or parts.netloc or not parts.path:
            img.decompose()
            continue
        target = (source_file.parent / unquote(parts.path)).resolve()
        source_root_abs = source_root.resolve()
        if not target.is_relative_to(source_root_abs) or target.suffix.lower() not in MEDIA_EXTS or not target.is_file():
            img.decompose()
            continue
        rel = target.relative_to(source_root_abs)
        destination = out / "media" / book_id / rel
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(target, destination)
        img["src"] = root_prefix + "media/" + book_id + "/" + quote(rel.as_posix(), safe="/")
        img["loading"] = "lazy"

    tagset = set(bleach.sanitizer.ALLOWED_TAGS) | {
        "p", "h1", "h2", "h3", "h4", "h5", "h6", "pre", "code", "br", "hr",
        "div", "span", "img", "table", "thead", "tbody", "tr", "th", "td", "sup", "sub", "del", "input"
    }
    clean_html = bleach.clean(
        str(soup),
        tags=tagset,
        attributes={
            "*": ["id", "class", "title"],
            "a": ["id", "class", "title", "href", "rel"],
            "img": ["src", "alt", "title", "loading"],
            "th": ["align"],
            "td": ["align"],
            "input": ["type", "checked", "disabled"],
        },
        protocols={"http", "https", "mailto"},
        strip=True,
    )
    return clean_html


def markdown_body(chapter: dict, source_root: Path, repo: str,
                  route_by_file: dict[Path, str], book_id: str,
                  out: Path, root_prefix: str) -> str:
    import markdown
    from bs4 import BeautifulSoup

    content = chapter["_path"].read_text(encoding="utf-8")
    html = markdown.markdown(
        content,
        extensions=["extra", "toc", "footnotes", "sane_lists", "admonition", "pymdownx.arithmatex"],
        extension_configs={
            # Normalize $...$, \(...\), $...$, \[...\], and TeX environments
            # before Markdown consumes backslashes; generic HTML survives bleach.
            "pymdownx.arithmatex": {"generic": True, "smart_dollar": True},
        },
        output_format="html5",
    )
    soup = BeautifulSoup(html, "html.parser")
    first_heading = soup.find("h1")
    if first_heading is not None and first_heading.find_previous(["h1", "h2", "h3"]) is None:
        first_heading.decompose()
    return fix_links(str(soup), chapter["_path"], source_root, repo,
                     route_by_file, book_id, out, root_prefix)


def write_page(template: str, path: Path, values: dict[str, str]) -> None:
    page = template
    for key, value in values.items():
        page = page.replace("{{" + key + "}}", value)
    if re.search(r"\{\{[A-Z_]+\}\}", page):
        raise ValueError(f"Unfilled template marker for {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(page, encoding="utf-8")


def build_readers(out: Path, books: list[dict], external_root: Path | None,
                  require_all_sources: bool = False) -> int:
    template = (SITE / "reader.html").read_text(encoding="utf-8")
    sources = []
    for book in books:
        source = read_manifest(book, external_root)
        if source is None:
            if require_all_sources:
                raise ValueError(f"Missing book.json or external checkout for {book['id']}")
            print(f"Warning: skipping reader for {book['id']} (book source unavailable)")
            continue
        sources.append((book, *source))

    route_by_file = {}
    for book, manifest, manifest_file, source_root, repo in sources:
        for ch in manifest["chapters"]:
            file = ch["_path"].resolve()
            if file in route_by_file:
                raise ValueError(f"Markdown chapter reused by two books: {file}")
            route_by_file[file] = CHAPTER_URL.format(book_id=book["id"], chapter_id=ch["id"])

    total = 0
    for book, manifest, manifest_file, source_root, repo in sources:
        book_id = book["id"]
        chapters = manifest["chapters"]
        book["readPath"] = "read/" + book_id + "/"
        book["chapterCount"] = len(chapters)
        root = "../../"
        toc = make_toc(chapters, book, root, "")
        counts = Counter(ch["status"] for ch in chapters)
        if book.get("cover"):
            book_cover = ('<img class="reader-cover" src="' + root +
                          escape(book["cover"], quote=True) + '" alt="' +
                          escape(book["title"], quote=True) + '的封面">')
        else:
            # Books without a commissioned PNG still need a readable cover on
            # their overview page. Colors are validated as six-digit hex.
            bg1, bg2 = book["palette"]
            ink = book.get("coverInk", "#fff5e6")
            if not isinstance(ink, str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", ink):
                ink = "#fff5e6"
            book_cover = (
                '<div class="reader-cover reader-cover-placeholder" role="img" aria-label="' +
                escape(book["title"], quote=True) + '的排版式临时封面" style="' +
                '--cover-start:' + bg1 + ';--cover-end:' + bg2 +
                ';--cover-ink:' + ink + ';">' +
                '<span class="reader-cover-overline">' +
                escape(book.get("coverEyebrow") or "THE READING ROOM") + '</span>' +
                '<strong class="reader-cover-name">' +
                escape(book.get("coverShort") or book["title"]) + '</strong>' +
                '<span class="reader-cover-footer">' +
                escape(book.get("coverFooter") or "AN ORIGINAL WORK") + '</span>' +
                '</div>'
            )
        overview = (
            '<div class="reader-book-hero">' + book_cover +
            '<div><p class="reader-kicker">THE READING ROOM / 全书目录</p>' +
            '<h1>' + escape(book["title"]) + '</h1>' +
            '<p class="reader-english">' + escape(book.get("subtitle", "")) + '</p>' +
            '<p>' + escape(book["description"]) + '</p>' +
            '<p class="reader-progress">' + str(len(chapters)) + ' 个章节 · ' +
            str(counts["draft"]) + ' 篇初稿 · ' + str(counts["outline"]) + ' 篇待撰写</p>' +
            '</div></div><h2>阅读目录</h2><div class="reader-chapter-list">' +
            make_toc(chapters, book, root, "") + "</div>"
        )
        write_page(template, out / "read" / book_id / "index.html", {
            "ROOT": root, "DOCUMENT_TITLE": escape(book["title"]),
            "BOOK_TITLE": escape(book["title"]), "CHAPTER_TITLE": escape("全书目录"),
            "BOOK_HREF": "./", "SIDEBAR": toc, "CONTENT": overview,
            "CHAPTER_STATUS": '<span class="reader-state">创作中 · 非正式出版稿</span>',
            "FOOTER_NAV": '<a href="' + escape(root + CHAPTER_URL.format(book_id=book_id, chapter_id=chapters[0]["id"])) + '">从第一篇开始阅读 →</a>',
            "READ_NOTICE": escape(manifest.get("reading_notice", "")),
        })
        public_chapters = []
        for index, chapter in enumerate(chapters):
            root = "../../../"
            toc = make_toc(chapters, book, root, chapter["id"])
            chapter_path = out / CHAPTER_URL.format(book_id=book_id, chapter_id=chapter["id"]) / "index.html"
            article = markdown_body(chapter, source_root, repo, route_by_file,
                                    book_id, out, root)
            notice = ('该章节尚在写作规划中。下方为原始占位 Markdown，内容不是正式正文。'
                      if chapter["status"] == "outline" else
                      '以下为创作初稿，尚未完成正式事实核查与编辑审校。' if chapter["status"] == "draft"
                      else '本章已标记为审定版本。')
            body = (
                '<header class="chapter-heading"><p class="reader-kicker">' +
                escape(chapter["part"]) + '</p><h1>' + escape(chapter["title"]) + '</h1>' +
                '<p class="chapter-notice">' + escape(notice) + '</p></header>' +
                '<div class="prose">' + article + '</div>'
            )
            prev = ('<a href="../' + escape(chapters[index - 1]["id"]) +
                    '/">← 上一章<span>' + escape(chapters[index - 1]["title"]) +
                    '</span></a>') if index else '<span></span>'
            next_link = ('<a href="../' + escape(chapters[index + 1]["id"]) +
                         '/">下一章 →<span>' + escape(chapters[index + 1]["title"]) +
                         '</span></a>') if index + 1 < len(chapters) else '<a href="../">返回全书目录 →</a>'
            write_page(template, chapter_path, {
                "ROOT": root,
                "DOCUMENT_TITLE": escape(chapter["title"] + " | " + book["title"]),
                "BOOK_TITLE": escape(book["title"]),
                "CHAPTER_TITLE": escape(chapter["title"]),
                "BOOK_HREF": "../",
                "SIDEBAR": toc,
                "CONTENT": body,
                "CHAPTER_STATUS": '<span class="reader-state">' + escape(ALLOWED_STATUSES[chapter["status"]]) + '</span>',
                "FOOTER_NAV": prev + next_link,
                "READ_NOTICE": escape(manifest.get("reading_notice", "")),
            })
            public_chapters.append({k: chapter[k] for k in ("id", "title", "part", "status", "file")})
            public_chapters[-1]["href"] = CHAPTER_URL.format(book_id=book_id, chapter_id=chapter["id"])
            total += 1
        (out / "read" / book_id / "book.json").write_text(
            json.dumps({"schema_version": 1, "id": book_id, "title": book["title"],
                        "chapters": public_chapters}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
    return total


def build(output: Path, external_root: Path | None = None,
          require_all_sources: bool = False) -> None:
    out = output.resolve()
    forbidden = [ROOT.resolve(), SITE.resolve(), (ROOT / "articles").resolve()]
    if out in forbidden or SITE.resolve() in out.parents or (ROOT / "articles").resolve() in out.parents:
        raise ValueError("Output must not replace the repository, site sources or manuscripts")
    if ROOT.resolve() in out.parents and out.name not in {"_site", "dist"}:
        raise ValueError("Use _site or dist for builds inside this repository")

    catalog = load_json(ROOT / "catalog.json")
    genres = [{"name": item["name"], "skill": item["skill"], "kind": item["kind"]} for item in catalog["genres"]]
    books = load_json(SITE / "assets/data/books.json")
    validate_books(genres, books)

    if out.exists():
        shutil.rmtree(out)
    (out / "assets/data").mkdir(parents=True)
    (out / "assets/covers").mkdir(parents=True)
    for file in ("index.html", "assets/css/main.css", "assets/css/reader.css", "assets/css/reader-apple.css",
                 "assets/js/app.js", "assets/js/reader.js", "assets/favicon.svg"):
        target = out / file
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(SITE / file, target)
    for cover in (SITE / "assets/covers").glob("*.png"):
        shutil.copy2(cover, out / "assets/covers" / cover.name)

    chapter_count = build_readers(out, books, external_root, require_all_sources)
    (out / "assets/data/genres.json").write_text(
        json.dumps(genres, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "assets/data/books.json").write_text(
        json.dumps(books, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / ".nojekyll").touch()
    print(f"Built {len(books)} books in {len(genres)} shelves and {chapter_count} readable chapters → {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the public ebook library")
    parser.add_argument("--out", default=str(ROOT / "_site"), type=Path)
    parser.add_argument("--external-root", type=Path,
                        default=ROOT / "external" / "the-empty-spaces")
    parser.add_argument("--require-all-sources", action="store_true")
    args = parser.parse_args()
    build(args.out, args.external_root, args.require_all_sources)
