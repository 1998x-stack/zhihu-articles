#!/usr/bin/env python3
"""Build the public GitHub Pages bookshelf from curated metadata only.

Never copy manuscript drafts, editorial QA, research or agent prompts to Pages.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
COVER_PATH = re.compile(r"^assets/covers/[a-z0-9-]+\.png$")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate_books(genres: list[dict], books: list[dict]) -> None:
    genre_ids = {genre["skill"] for genre in genres}
    seen: set[str] = set()
    if not isinstance(books, list):
        raise ValueError("books.json must be a list")
    for index, book in enumerate(books):
        book_id = book.get("id", "")
        if not isinstance(book_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", book_id):
            raise ValueError(f"Invalid book id at position {index}")
        if book_id in seen:
            raise ValueError(f"Duplicate book id: {book_id}")
        seen.add(book_id)
        if book.get("genre") not in genre_ids:
            raise ValueError(f"Unknown genre for {book_id}: {book.get('genre')}")
        for key in ("title", "author", "status", "description", "url"):
            if not isinstance(book.get(key), str) or not book[key].strip():
                raise ValueError(f"{book_id} requires nonempty {key}")
        url = urlparse(book["url"])
        if url.scheme != "https" or not url.netloc:
            raise ValueError(f"{book_id} must use an HTTPS project URL")
        read_url = book.get("readUrl")
        if read_url:
            parsed = urlparse(read_url)
            if parsed.scheme != "https" or not parsed.netloc:
                raise ValueError(f"{book_id} must use an HTTPS reader URL")
        cover = book.get("cover")
        if cover is not None:
            if not isinstance(cover, str) or not COVER_PATH.fullmatch(cover):
                raise ValueError(f"Invalid PNG cover path for {book_id}")
            if not (SITE / cover).is_file():
                raise ValueError(f"Cover PNG not found for {book_id}: {cover}")
        palette = book.get("palette", [])
        if not isinstance(palette, list) or len(palette) != 2 or not all(re.fullmatch(r"#[0-9a-fA-F]{6}", str(v)) for v in palette):
            raise ValueError(f"{book_id} needs a pair of hexadecimal cover colors")
        if not isinstance(book.get("tags", []), list):
            raise ValueError(f"{book_id} tags must be a list")


def build(output: Path) -> None:
    out = output.resolve()
    # Only accept a fresh build directory, not the source tree or a manuscript path.
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
    (out / "assets/css").mkdir(parents=True)
    (out / "assets/js").mkdir(parents=True)
    (out / "assets/data").mkdir(parents=True)
    (out / "assets/covers").mkdir(parents=True)

    for path in ("index.html", "assets/css/main.css", "assets/js/app.js", "assets/favicon.svg"):
        target = out / path
        shutil.copy2(SITE / path, target)

    for cover in (SITE / "assets/covers").glob("*.png"):
        shutil.copy2(cover, out / "assets/covers" / cover.name)

    (out / "assets/data/genres.json").write_text(
        json.dumps(genres, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (out / "assets/data/books.json").write_text(
        json.dumps(books, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    (out / ".nojekyll").touch()
    print(f"Built {len(books)} books in {len(genres)} shelves → {out}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build the public e-book library")
    parser.add_argument("--out", default=str(ROOT / "_site"), type=Path)
    args = parser.parse_args()
    build(args.out)
