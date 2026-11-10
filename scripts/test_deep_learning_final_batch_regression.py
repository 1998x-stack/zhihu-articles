"""Final 28–30 chapters and closing 00/31 manuscript regression checks.

This test protects manuscript/page integrity. It cannot perform independent
fact-checking, scientific peer review, licensing advice or author sign-off.
"""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/"articles/nonfiction/history-science/deep-learning-history"


class DeepLearningFinalBatchRegressionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((BOOK/"book.json").read_text(encoding="utf-8"))
        cls.workflow=json.loads((BOOK/"workflow-state.json").read_text(encoding="utf-8"))
        cls.state=json.loads((BOOK/"chapter-state.json").read_text(encoding="utf-8"))
        cls.research=(BOOK/"research.md").read_text(encoding="utf-8")
        cls.ledger=(BOOK/"claim-ledger.md").read_text(encoding="utf-8")

    def test_public_reader_manifest_stays_honest(self):
        chapters=self.manifest["chapters"]
        self.assertEqual(len(chapters),32)
        self.assertEqual(sum(c["status"]=="draft" for c in chapters),32)
        self.assertEqual({c["number"] for c in chapters if c["status"]=="outline"},set())
        self.assertEqual({c["number"] for c in chapters if c["status"]=="draft" and c["number"] in {"00","31"}},{"00","31"})
        self.assertFalse(any(c["status"]=="final" for c in chapters))
        self.assertEqual(self.state["last_chapter"],31)
        self.assertEqual((self.state["progress_summary"]["draft"],
                          self.state["progress_summary"]["outline"]),(32,0))
        self.assertIn(self.workflow["review_status"],("PENDING","CHANGES_REQUIRED"))
        if self.workflow["review_status"]=="CHANGES_REQUIRED":
            self.assertTrue(self.workflow["unresolved_blockers"])
        self.assertIsNone(self.workflow["reviewed_revision"])
        self.assertFalse(self.workflow["final_approved"])
        self.assertEqual(self.workflow["last_completed_working_draft_chapter"],31)

    def test_three_chapters_are_real_long_form_nonfiction_and_claims_traced(self):
        for i in (28,29,30):
            number=f"{i:02d}"
            chapter=next(x for x in self.manifest["chapters"] if x["number"]==number)
            with self.subTest(number=number):
                self.assertEqual(chapter["status"],"draft")
                self.assertEqual(chapter["claims_file"],f"draft/{number}.claims.json")
                self.assertEqual(chapter["review_status"],"PENDING")
                self.assertTrue(chapter["source_hints"])
                md=(BOOK/chapter["file"]).read_text(encoding="utf-8")
                self.assertGreaterEqual(len(re.findall(r"[\u4e00-\u9fff]",md)),3500)
                self.assertGreaterEqual(len(re.findall(r"^## [一二三四五六七八九十]+、",md,re.M)),7)
                self.assertIn("工作初稿",md[:500])
                self.assertIn("PENDING",md[:500])
                claims=json.loads((BOOK/chapter["claims_file"]).read_text(encoding="utf-8"))
                self.assertEqual(claims["chapter"],number)
                self.assertEqual(claims["status"],"working_draft")
                self.assertEqual(claims["review_status"],"PENDING")
                self.assertFalse(claims["independent_reviewed"])
                self.assertGreaterEqual(len(claims["claims"]),8)
                seen=set()
                for claim in claims["claims"]:
                    self.assertNotIn(claim["claim_id"],seen)
                    seen.add(claim["claim_id"])
                    self.assertTrue(claim["source_ids"])
                    self.assertFalse(claim["independent_reviewed"])
                    self.assertIn(claim["claim_id"],self.ledger)
                    self.assertTrue(claim["limitations"])
                    for source in claim["source_ids"]:
                        if source=="AUTHOR_DERIVATION":
                            self.assertIn("假设",md)
                        else:
                            self.assertRegex(source,r"^DL\d{2,3}$")
                            self.assertIn(source,self.research)
                self.assertIn("https://",md)

    def test_cross_chapter_navigation_and_author_review_material_are_present(self):
        readme=(BOOK/"README.md").read_text(encoding="utf-8")
        batch=(BOOK/"batches/28-30.md").read_text(encoding="utf-8")
        batches=(BOOK/"batches/README.md").read_text(encoding="utf-8")
        for n in ("28","29","30"):
            self.assertIn(f"draft/{n}.md",readme)
            self.assertIn(f"draft/{n}.md",batch)
            self.assertIn(f"{n}.claims.json",readme)
        self.assertIn("工作初稿 32 篇",readme)
        self.assertIn("策划占位 0 篇",readme)
        self.assertIn("工作初稿三篇",batches)
        self.assertTrue((BOOK/"qa/batch-28-30-self-check.md").exists())
        self.assertTrue((BOOK/"qa/batch-28-30-review-brief.md").exists())
        self.assertIn("独立审稿",batch)


if __name__=="__main__":
    unittest.main()
