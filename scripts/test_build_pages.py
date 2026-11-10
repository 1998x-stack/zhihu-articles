"""Tests for the public GitHub Pages ebook bookshelf and chapter reader."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from build_pages import ROOT, build, discover_books, safe_path, validate_books


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
                "read/linear-algebra-history/chapter-01/index.html",
                "read/the-laws-of-chance-probability/chapter-01/index.html",
                "read/the-making-of-calculus/prologue/index.html",
                "read/graph-theory-history/chapter-01/index.html",
                "read/heat-and-time-thermodynamics-history/prologue/index.html",
                "read/fields-of-light-electromagnetism-history/prologue/index.html",
                "read/ideal-gas-law-two-centuries/chapter-04/index.html",
                "read/network-science-history/chapter-32/index.html",
                "read/deep-learning-history/chapter-18/index.html",
                "read/reinforcement-learning-history/chapter-15/index.html",
                "read/ledger-of-empire-china-fiscal-history/chapter-12/index.html",
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
            self.assertEqual(len(books), 14)
            self.assertEqual({b["id"] for b in books}.__len__(), 14)
            self.assertEqual(books[1]["chapterCount"], 27)
            self.assertEqual(books[2]["chapterCount"], 42)
            chapter_totals = {
                "linear-algebra-history": 34,
                "the-laws-of-chance-probability": 38,
                "the-making-of-calculus": 37,
                "graph-theory-history": 38,
                "heat-and-time-thermodynamics-history": 34,
                "fields-of-light-electromagnetism-history": 34,
                "ideal-gas-law-two-centuries": 17,
                "network-science-history": 34,
                "deep-learning-history": 32,
                "reinforcement-learning-history": 34,
                "ledger-of-empire-china-fiscal-history": 47,
            }
            for book_id, total in chapter_totals.items():
                book = next(b for b in books if b["id"] == book_id)
                self.assertEqual(book["chapterCount"], total, book_id)
                overview = (output / "read" / book_id / "index.html").read_text(encoding="utf-8")
                if book_id in {"deep-learning-history", "reinforcement-learning-history", "ledger-of-empire-china-fiscal-history"}:
                    self.assertNotIn("cover", book)
                    self.assertIn("reader-cover-placeholder", overview)
                else:
                    self.assertEqual(book["cover"], "assets/covers/" + book_id + ".png")
                    self.assertTrue((output / book["cover"]).is_file(), book_id)
                    self.assertIn('class="reader-cover"', overview)
                    self.assertIn('src="../../assets/covers/' + book_id + '.png"', overview)
                exported = json.loads((output / "read" / book_id / "book.json").read_text(encoding="utf-8"))
                self.assertEqual(len(exported["chapters"]), total)
                self.assertTrue(all(ch["href"].startswith("read/" + book_id + "/") for ch in exported["chapters"]))
            self.assertIn("章节占位", (output / "read/network-science-history/chapter-32/index.html").read_text(encoding="utf-8"))
            self.assertIn("正文初稿", (output / "read/ideal-gas-law-two-centuries/chapter-04/index.html").read_text(encoding="utf-8"))
            # Existing manuscripts use several distinct LaTeX delimiters.
            # These must survive Markdown -> HTML cleanup for MathJax.
            gas_html = (output / "read/ideal-gas-law-two-centuries/prologue/index.html").read_text(encoding="utf-8")
            self.assertIn('class="arithmatex"', gas_html)
            self.assertIn(r"pv=R(267+t)", gas_html)
            self.assertIn(r"\[", gas_html)
            self.assertIn(r"\(R\)", gas_html)
            maths_html = (output / "read/linear-algebra-history/chapter-01/index.html").read_text(encoding="utf-8")
            self.assertIn(r"\begin{cases}", maths_html)
            self.assertIn('class="arithmatex"', maths_html)
            loss_html = (output / "read/the-loss-of-certainty-math-crises/chapter-02/index.html").read_text(encoding="utf-8")
            self.assertIn(r"\(\sqrt2\)", loss_html)
            self.assertIn("reader-math-warning", gas_html)
            self.assertIn("readingRoomMathFallback", gas_html)

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

    def test_series_discovery_is_complete(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        curated = json.loads((ROOT / "site/assets/data/books.json").read_text(encoding="utf-8"))
        discovered = discover_books(catalog, curated)
        self.assertEqual(len(discovered), 14)
        self.assertEqual(len({book["id"] for book in discovered}), len(discovered))
        for book_id, drafts in (
            ("deep-learning-history", 18),
            ("reinforcement-learning-history", 15),
            ("ledger-of-empire-china-fiscal-history", 12),
        ):
            entry = next(book for book in discovered if book["id"] == book_id)
            self.assertEqual(entry["source"]["repository"], "self")
            manifest = ROOT / entry["source"]["manifest"]
            chapters = json.loads(manifest.read_text(encoding="utf-8"))["chapters"]
            self.assertEqual(sum(ch["status"] == "draft" for ch in chapters), drafts)

    def test_missing_manifest_fails_loudly(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            series = root / "articles/nonfiction/history-science/new-series"
            series.mkdir(parents=True)
            (series / "README.md").write_text("# New series", encoding="utf-8")
            with patch("build_pages.ROOT", root):
                with self.assertRaisesRegex(ValueError, "missing book.json"):
                    discover_books({"genres": [{
                        "archive": "articles/nonfiction/history-science",
                        "skill": "genre-history-science", "kind": "非虚构"
                    }]}, [])

    def test_math_syntax_families_and_plain_currency(self):
        import markdown
        snippet = (
            r"行内 $x^2$、\(\frac{a}{b}\)，另有价格 $20 and $30。"
            + "\n\n" + r"$$E=mc^2$$"
            + "\n\n" + r"\[\int_0^1 x\,dx=\frac12\]"
            + "\n\n" + "\\begin{align}\na &= b\\\\\nc &= d\n\\end{align}"
            + "\n\n" + "代码 " + chr(96) + "$not_math$" + chr(96) + " 不应变公式"
        )
        rendered = markdown.markdown(
            snippet,
            extensions=["extra", "pymdownx.arithmatex"],
            extension_configs={"pymdownx.arithmatex": {"generic": True, "smart_dollar": True}},
        )
        self.assertGreaterEqual(rendered.count('class="arithmatex"'), 4)
        self.assertIn(r"\(x^2\)", rendered)
        self.assertIn(r"\(\frac{a}{b}\)", rendered)
        self.assertIn(r"\[E=mc^2\]", rendered)
        self.assertIn(r"\[\int_0^1", rendered)
        self.assertIn(r"\begin{align}", rendered)
        self.assertIn("$20 and $30", rendered)
        self.assertIn("$not_math$", rendered)

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
