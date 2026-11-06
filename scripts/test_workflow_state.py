"""Test explicit workflow state changes, revision invalidation and final archival."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from workflow_gate import evaluate
from workflow_state import transition


class WorkflowTransitionTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.state = {
            "schema_version": "2.0", "lane": "fiction", "current_revision": 0,
            "outline_approved": False, "evidence_verified": False,
            "review_status": "PENDING", "reviewed_revision": None,
            "unresolved_blockers": [], "edited_revision": None,
            "final_approved": False
        }
        self.touch("brief.md")
        self.touch("outline.md")
        self.touch("story-bible.md")
        self.touch("plot-ledger.md")
        self.touch("chapter-state.json", "{}")
        self.touch("draft/01.md", "Completed fictional chapter")
        self.persist()

    def touch(self, name, content="present"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def persist(self):
        self.touch("workflow-state.json", json.dumps(self.state))

    def reviews(self, revision=0):
        for name in ("continuity-report.md", "developmental-review.md"):
            self.touch("qa/" + name, f"revision_count: {revision}\nstatus: PASS\n")

    def ready(self):
        transition(self.root, "outline-approved", confirm=True)
        self.reviews()
        transition(self.root, "review-passed", confirm=True)
        self.touch("edited.md", "A polished and reviewed fictional chapter")
        transition(self.root, "edited")

    def test_outline_requires_explicit_approval(self):
        with self.assertRaises(ValueError):
            transition(self.root, "outline-approved")
        self.assertFalse(json.loads((self.root / "workflow-state.json").read_text())["outline_approved"])

    def test_review_requires_existing_matching_reports(self):
        transition(self.root, "outline-approved", confirm=True)
        with self.assertRaises(ValueError):
            transition(self.root, "review-passed", confirm=True)
        self.reviews(1)
        with self.assertRaises(ValueError):
            transition(self.root, "review-passed", confirm=True)

    def test_finalize_works_only_after_review_and_edit(self):
        self.ready()
        with self.assertRaises(ValueError):
            transition(self.root, "finalize")
        transition(self.root, "finalize", confirm=True)
        self.assertEqual(evaluate(self.root, "publish"), [])
        self.assertEqual((self.root / "final.md").read_text(), (self.root / "edited.md").read_text())

    def test_revision_invalidates_old_approval_and_archives_final(self):
        self.ready()
        transition(self.root, "finalize", confirm=True)
        new = transition(self.root, "new-revision", reason="Fix contradictory motive")
        self.assertEqual(new["current_revision"], 1)
        self.assertEqual(new["review_status"], "PENDING")
        self.assertIsNone(new["reviewed_revision"])
        self.assertIsNone(new["edited_revision"])
        self.assertFalse(new["final_approved"])
        self.assertFalse((self.root / "final.md").exists())
        self.assertTrue((self.root / "history/final-r0.md").exists())
        self.assertTrue(evaluate(self.root, "edit"))

    def test_template_final_placeholder_can_be_replaced_at_initial_approval(self):
        self.ready()
        self.touch("final.md", "# Placeholder awaiting approval")
        transition(self.root, "finalize", confirm=True)
        self.assertEqual((self.root / "final.md").read_text(), (self.root / "edited.md").read_text())

    def test_blockers_remain_until_explicitly_resolved_and_rereviewed(self):
        self.ready()
        transition(self.root, "add-blocker", reason="PLOT-004")
        self.assertTrue(evaluate(self.root, "edit"))
        with self.assertRaises(ValueError):
            transition(self.root, "resolve-blocker", reason="PLOT-004")
        transition(self.root, "resolve-blocker", reason="PLOT-004", confirm=True)
        self.assertTrue(evaluate(self.root, "edit"))
        self.reviews()
        transition(self.root, "review-passed", confirm=True)
        self.assertEqual(evaluate(self.root, "edit"), [])

    def test_nonfiction_evidence_approval(self):
        self.state["lane"] = "nonfiction"
        self.persist()
        with self.assertRaises(ValueError):
            transition(self.root, "evidence-verified", confirm=True)
        self.touch("research.md", "Verified source inventory")
        with self.assertRaises(ValueError):
            transition(self.root, "evidence-verified")
        transition(self.root, "evidence-verified", confirm=True)
        with self.assertRaises(ValueError):
            transition(self.root, "outline-approved", confirm=True)
        self.touch("claim-ledger.md")
        transition(self.root, "outline-approved", confirm=True)
        self.assertEqual(evaluate(self.root, "draft"), [])


if __name__ == "__main__":
    unittest.main()
