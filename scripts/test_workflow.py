"""Runtime lifecycle-gate unit tests using synthetic artifacts (not literary evaluation)."""
from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from workflow_gate import evaluate


class WorkflowGateTests(unittest.TestCase):
    def setUp(self):
        self.context = tempfile.TemporaryDirectory()
        self.addCleanup(self.context.cleanup)
        self.root = Path(self.context.name)
        self.state = {
            "schema_version": "2.0",
            "lane": "fiction", "current_revision": 0,
            "outline_approved": True, "evidence_verified": False,
            "review_status": "PENDING", "reviewed_revision": None,
            "unresolved_blockers": [], "edited_revision": None,
            "final_approved": False
        }
        for filename in ("brief.md", "outline.md", "story-bible.md", "plot-ledger.md"):
            self.touch(filename)
        self.write_state()

    def touch(self, path, content="placeholder"):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")

    def write_state(self):
        self.touch("workflow-state.json", json.dumps(self.state))

    def passed_reviews(self):
        self.touch("draft/01.md")
        self.touch("chapter-state.json", "{}")
        self.touch("qa/continuity-report.md", f"# Review\nrevision_count: {self.state['current_revision']}\nstatus: PASS\n")
        self.touch("qa/developmental-review.md", f"# Review\nrevision_count: {self.state['current_revision']}\nstatus: PASS\n")
        self.state["review_status"] = "PASS"
        self.state["reviewed_revision"] = self.state["current_revision"]
        self.write_state()

    def test_fiction_draft_gate(self):
        self.assertEqual(evaluate(self.root, "draft"), [])
        self.state["outline_approved"] = False
        self.write_state()
        self.assertTrue(any("Outline" in e for e in evaluate(self.root, "draft")))

    def test_nonfiction_evidence_first(self):
        self.state["lane"] = "nonfiction"
        self.write_state()
        self.assertTrue(evaluate(self.root, "draft"))
        self.touch("research.md")
        self.touch("claim-ledger.md")
        self.state["evidence_verified"] = True
        self.write_state()
        self.assertEqual(evaluate(self.root, "draft"), [])

    def test_review_must_pass_and_be_same_version(self):
        self.passed_reviews()
        self.assertEqual(evaluate(self.root, "edit"), [])
        self.state["current_revision"] = 1
        self.write_state()
        self.assertTrue(any("stale" in e or "mismatch" in e for e in evaluate(self.root, "edit")))

    def test_unresolved_blocker_prevents_line_edit(self):
        self.passed_reviews()
        self.state["unresolved_blockers"] = ["PLOT-004"]
        self.write_state()
        self.assertTrue(any("Unresolved" in e for e in evaluate(self.root, "edit")))

    def test_reports_must_match_current_revision(self):
        self.passed_reviews()
        self.touch("qa/continuity-report.md", "revision_count: 5\nstatus: PASS\n")
        self.assertTrue(any("Report revision mismatch" in e for e in evaluate(self.root, "edit")))

    def test_nonfiction_chapter_claims_are_required(self):
        self.state["lane"] = "nonfiction"
        self.state["evidence_verified"] = True
        self.touch("research.md")
        self.touch("claim-ledger.md")
        self.write_state()
        self.passed_reviews()
        self.assertTrue(any(".claims.json" in e for e in evaluate(self.root, "edit")))
        self.touch("draft/01.claims.json", "{}")
        self.assertEqual(evaluate(self.root, "edit"), [])

    def test_final_gate_requires_edited_revision(self):
        self.passed_reviews()
        self.touch("edited.md")
        self.assertTrue(any("Edited manuscript" in e for e in evaluate(self.root, "final")))
        self.state["edited_revision"] = 0
        self.write_state()
        self.assertEqual(evaluate(self.root, "final"), [])

    def test_publish_needs_matching_final_approval(self):
        self.passed_reviews()
        self.touch("edited.md")
        self.state["edited_revision"] = 0
        self.write_state()
        self.assertTrue(evaluate(self.root, "publish"))
        self.touch("final.md")
        self.touch("qa/final-approval.md", "revision_count: 0\napproved: true\n")
        self.state["final_approved"] = True
        self.write_state()
        self.assertEqual(evaluate(self.root, "publish"), [])

    def test_legacy_article_without_state_requires_migration(self):
        (self.root / "workflow-state.json").unlink()
        self.assertTrue(any("legacy articles" in e for e in evaluate(self.root, "draft")))


if __name__ == "__main__":
    unittest.main()
