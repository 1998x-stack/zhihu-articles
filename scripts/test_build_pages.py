"""Tests for the public GitHub Pages ebook bookshelf and chapter reader."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from build_pages import ROOT, build, safe_path, validate_books


class PagesBuildTests(unittest.TestCase):
    def test_build_publishes_only_explicit_chapters_and_public_assets(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "public"
            build(output)
            for path in (
                "index.html", "assets/css/main.css", "assets/css/reader.css", "assets/css/reader-apple.css",
                "assets/js/app.js", "assets/js/reader.js", "assets/data/genres.json",
                "read/the-loss-of-certainty-math-crises/index.html",
                "read/the-loss-of-certainty-math-crises/chapter-02/index.html",
                "read/credit-debt-power-global-financial-history/chapter-03/index.html",
                "read/credit-debt-power-global-financial-history/book.json",
                ".nojekyll",
            ):
                self.assertTrue((output / path).is_file(), path)
            self.assertFalse((output / "articles").exists())
            self.assertFalse((output / "AGENTS.md").exists())
            self.assertFalse((output / "research.md").exists())
            self.assertFalse((output / ".agents").exists())
            genres = json.loads((output / "assets/data/genres.json").read_text(encoding="utf-8"))
            books = json.loads((output / "assets/data/books.json").read_text(encoding="utf-8"))
            self.assertEqual(len(genres), len(json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))["genres"]))
            self.assertEqual(len(books), 3)
            self.assertEqual(books[1]["chapterCount"], 27)
            self.assertEqual(books[2]["chapterCount"], 42)

            chapter_html = (output / "read/the-loss-of-certainty-math-crises/chapter-02/index.html").read_text(encoding="utf-8")
            self.assertIn("希帕索斯的沉船", chapter_html)
            self.assertIn("reader-sidebar", chapter_html)
            self.assertIn('href="../chapter-01/"', chapter_html)
            self.assertIn('href="../chapter-03/"', chapter_html)
            self.assertIn("reader.css", chapter_html)
            self.assertIn("reader-apple.css", chapter_html)
            self.assertIn("reader-current-section", chapter_html)
            self.assertIn("reader-reading-percent", chapter_html)
            self.assertIn("type-toggle", chapter_html)
            self.assertIn("数学里的真假", chapter_html)
            self.assertIn("正文初稿", chapter_html)
            outline_html = (output / "read/credit-debt-power-global-financial-history/chapter-04/index.html").read_text(encoding="utf-8")
            self.assertIn("章节占位", outline_html)
            self.assertIn("不是正式正文", outline_html)
            stylesheet = (output / "assets/css/reader-apple.css").read_text(encoding="utf-8")
            self.assertIn("prefers-reduced-motion", stylesheet)
            self.assertIn("reader-motion-enabled", stylesheet)
            self.assertIn("reader-chapter-list", stylesheet)
            javascript = (output / "assets/js/reader.js").read_text(encoding="utf-8")
            self.assertIn("IntersectionObserver", javascript)
            self.assertIn("reading-room-font-family", javascript)
            self.assertIn("reading-progress", javascript)

    def test_rejects_nonexistent_category(self):
        with self.assertRaisesRegex(ValueError, "Unknown genre"):
            validate_books([{"skill": "genre-existing"}], [{
                "id": "test-book", "genre": "genre-missing", "title": "Test",
                "author": "Test", "status": "draft", "description": "Test",
                "url": "https://example.com", "palette": ["#abcdef", "#fedcba"]
            }])

    def test_no_path_traversal(self):
        with self.assertRaises(ValueError):
            safe_path(ROOT, "../secret.md")
        with self.assertRaises(ValueError):
            safe_path(ROOT, "/etc/passwd")

    def test_missing_remote_fails_in_strict_mode(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(ValueError, "Missing book.json"):
                build(Path(temp) / "strict", Path(temp) / "not-cloned", require_all_sources=True)

    def test_cannot_build_over_manuscript_directory(self):
        with self.assertRaises(ValueError):
            build(ROOT / "articles" / "_template")


if __name__ == "__main__":
    unittest.main()
