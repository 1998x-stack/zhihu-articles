"""Regression tests for cross-series progress and editorial gate separation."""
import json
from pathlib import Path
import tempfile
import unittest

from check_series_progress import (ROOT, START, END, readme_block, replace_readme,
                                   chapter_state_errors, progress, run, series_json_errors)


class SeriesProgressTests(unittest.TestCase):
    def make_series(self, root: Path, status: str = "outline", text: str = "# Ch 01\n\n提纲。\n"):
        archive = root / "articles/nonfiction/history-science"
        directory = archive / "test-series"
        manuscript = directory / "draft/01.md"
        manuscript.parent.mkdir(parents=True)
        manuscript.write_text(text, encoding="utf-8")
        (root / "catalog.json").write_text(json.dumps({
            "genres": [{"archive": "articles/nonfiction/history-science"}]
        }), encoding="utf-8")
        (directory / "book.json").write_text(json.dumps({
            "schema_version": 1, "id": "test-series",
            "chapters": [{"id": "chapter-01", "title": "Test", "part": "Part I",
                          "file": "draft/01.md", "status": status}]
        }), encoding="utf-8")
        (directory / "workflow-state.json").write_text(json.dumps({
            "review_status": "PENDING", "final_approved": False, "current_revision": 0
        }), encoding="utf-8")
        (directory / "README.md").write_text("# Test\n\nContent\n", encoding="utf-8")
        return directory

    def test_all_real_series_are_consistent(self):
        count, errors = run(ROOT)
        self.assertEqual(count, 14)
        self.assertEqual(errors, [])

    def test_readme_generated_block_is_idempotent(self):
        values = {"total": 2, "draft": 1, "outline": 1, "final": 0,
                  "proposals": 0, "review_status": "PENDING", "final_approved": False}
        original = "# A series\n\nThe opening.\n"
        new = replace_readme(original, values)
        self.assertEqual(new, replace_readme(new, values))
        self.assertEqual(new.count(START), 1)
        self.assertEqual(new.count(END), 1)
        self.assertIn("工作初稿 1 篇", new)
        self.assertIn(readme_block(values), new)

    def test_missing_and_stale_derived_files_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = self.make_series(root)
            count, errors = run(root)
            self.assertEqual(count, 1)
            self.assertTrue(any("README progress" in x for x in errors))
            self.assertTrue(any("chapter-state.json" in x for x in errors))
            self.assertEqual(run(root, write=True)[1], [])
            self.assertEqual(run(root)[1], [])
            (directory / "book.json").write_text(json.dumps({
                "schema_version": 1, "id": "test-series",
                "chapters": [{"id": "chapter-01", "title": "Test", "part": "Part I",
                              "file": "draft/01.md", "status": "draft"}]
            }), encoding="utf-8")
            self.assertTrue(any("stale" in x for x in run(root)[1]))
            self.assertEqual(run(root, write=True)[1], [])
            self.assertEqual(run(root)[1], [])

    def test_declared_outline_cannot_hide_evident_draft(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = self.make_series(root, text="# Title\n\n> **非虚构研究初稿**\n\n" + "正文段落。" * 900)
            with self.assertRaisesRegex(ValueError, "marks outline"):
                progress(root, directory)

    def test_finals_require_actual_editorial_approval(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = self.make_series(root, status="final")
            with self.assertRaisesRegex(ValueError, "explicit approval"):
                progress(root, directory)

    def test_proposals_do_not_become_approved_drafts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            directory = self.make_series(root)
            proposal = directory / "proposals/01.md"
            proposal.parent.mkdir()
            proposal.write_text("# Pending candidate\n" + "正文。" * 3000, encoding="utf-8")
            _, _, summary = progress(root, directory)
            self.assertEqual((summary["draft"], summary["outline"], summary["proposals"]), (0, 1, 1))

    def test_optional_partial_chapter_ledger_not_forced_to_include_all(self):
        chapter = {"id": "chapter-01", "file": "draft/01.md", "status": "draft"}
        book = {"chapters": [chapter]}
        workflow = {"review_status": "PENDING", "final_approved": False, "current_revision": 0}
        directory = Path("test-series")
        self.assertEqual(chapter_state_errors(directory, book, workflow, {
            "chapter_status": {"01": "draft"}, "manuscript_revision": 0
        }), [])
        mismatch = chapter_state_errors(directory, book, workflow, {"chapter_status": {"01": "outline"}})
        self.assertTrue(any("!=" in x for x in mismatch))

    def test_numeric_series_manifest_conflict_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            directory = Path(tmp)
            (directory / "series.json").write_text(json.dumps({
                "chapters": [{"id": "01", "status": "draft_unreviewed"}]
            }), encoding="utf-8")
            book = {"chapters": [{"id": "chapter-01", "file": "draft/01.md", "status": "outline"}]}
            self.assertTrue(series_json_errors(directory, book))

    def test_invalid_readme_markers_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "malformed"):
            replace_readme("# Test\n\n" + START + "\n", {
                "total": 1, "draft": 1, "outline": 0, "final": 0,
                "proposals": 0, "review_status": "PENDING", "final_approved": False
            })


if __name__ == "__main__":
    unittest.main()
