"""Tests for the GitHub Pages public-only bookshelf build."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from build_pages import ROOT, build, validate_books


class PagesBuildTests(unittest.TestCase):
    def test_build_publishes_only_curated_static_files(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "public"
            build(output)
            self.assertTrue((output / "index.html").is_file())
            self.assertTrue((output / "assets/css/main.css").is_file())
            self.assertTrue((output / "assets/js/app.js").is_file())
            self.assertTrue((output / "assets/data/genres.json").is_file())
            self.assertTrue((output / ".nojekyll").exists())
            self.assertFalse((output / "articles").exists())
            self.assertFalse((output / "AGENTS.md").exists())
            genres = json.loads((output / "assets/data/genres.json").read_text(encoding="utf-8"))
            books = json.loads((output / "assets/data/books.json").read_text(encoding="utf-8"))
            self.assertEqual(len(genres), len(json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))["genres"]))
            self.assertGreaterEqual(len(books), 3)

    def test_rejects_nonexistent_category(self):
        with self.assertRaisesRegex(ValueError, "Unknown genre"):
            validate_books([{"skill": "genre-existing"}], [{
                "id": "test-book", "genre": "genre-missing", "title": "Test",
                "author": "Test", "status": "draft", "description": "Test",
                "url": "https://example.com", "palette": ["#abcdef", "#fedcba"]
            }])

    def test_cannot_build_over_manuscript_directory(self):
        with self.assertRaises(ValueError):
            build(ROOT / "articles" / "_template")


if __name__ == "__main__":
    unittest.main()
