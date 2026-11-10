"""Deep-learning history final nonfiction batch integrity; not independent approval."""
from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BOOK=ROOT/"articles/nonfiction/history-science/deep-learning-history"


class DeepLearningBatch2830Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.book=json.loads((BOOK/"book.json").read_text(encoding="utf-8"))
        cls.workflow=json.loads((BOOK/"workflow-state.json").read_text(encoding="utf-8"))
        cls.chapter_state=json.loads((BOOK/"chapter-state.json").read_text(encoding="utf-8"))
        cls.research=(BOOK/"research.md").read_text(encoding="utf-8")
        cls.ledger=(BOOK/"claim-ledger.md").read_text(encoding="utf-8")

    def test_book_has_30_real_drafts_and_two_remaining_outlines(self):
        chapters=self.book["chapters"]
        self.assertEqual(len(chapters),32)
        self.assertEqual(sum(c["status"]=="draft" for c in chapters),30)
        self.assertEqual(sum(c["status"]=="outline" for c in chapters),2)
        self.assertEqual({c["number"] for c in chapters if c["status"]=="outline"},{"00","31"})
        self.assertEqual(self.chapter_state["last_chapter"],30)
        self.assertEqual(self.chapter_state["progress_summary"]["draft"],30)
        self.assertEqual(self.chapter_state["progress_summary"]["outline"],2)

    def test_each_chapter_is_substantive_and_cites_scoped_source(self):
        for n in range(28,31):
            num=f"{n:02d}"
            with self.subTest(chapter=num):
                item=next(c for c in self.book["chapters"] if c["number"]==num)
                self.assertEqual(item["status"],"draft")
                self.assertEqual(item["claims_file"],f"draft/{num}.claims.json")
                self.assertEqual(item["review_status"],"PENDING")
                text=(BOOK/item["file"]).read_text(encoding="utf-8")
                self.assertGreaterEqual(len(re.findall(r"[\u4e00-\u9fff]",text)),3500)
                self.assertGreaterEqual(len(re.findall(r"^## [一二三四五六七八九十]+、",text,re.M)),7)
                self.assertIn("工作初稿",text[:500])
                self.assertIn("双审",text)
                claims=json.loads((BOOK/item["claims_file"]).read_text(encoding="utf-8"))
                self.assertEqual(claims["chapter"],num)
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
                    for source in claim["source_ids"]:
                        if source=="AUTHOR_DERIVATION":
                            self.assertIn("假设",text)
                        else:
                            self.assertRegex(source,r"^DL\d{3}$")
                            self.assertIn(source,self.research)
                            self.assertIn(source,item["source_hints"])
                self.assertIn("下一章" if n<30 else "尾声",text)

    def test_no_phantom_final_approval_or_published_book(self):
        self.assertTrue(self.workflow["outline_approved"])
        self.assertTrue(self.workflow["evidence_verified"])
        self.assertEqual(self.workflow["review_status"],"PENDING")
        self.assertFalse(self.workflow["final_approved"])
        self.assertIsNone(self.workflow["reviewed_revision"])
        self.assertIsNone(self.workflow["edited_revision"])
        self.assertEqual(self.workflow["last_completed_working_draft_chapter"],30)
        self.assertFalse(any(c["status"]=="final" for c in self.book["chapters"]))
        for n in (28,29,30):
            self.assertFalse((BOOK/"draft"/f"{n:02d}.md").read_text(encoding="utf-8").startswith("# 已发表"))

    def test_reader_and_batch_indexes_are_synced(self):
        readme=(BOOK/"README.md").read_text(encoding="utf-8")
        batches=(BOOK/"batches/README.md").read_text(encoding="utf-8")
        batch=(BOOK/"batches/28-30.md").read_text(encoding="utf-8")
        for n in (28,29,30):
            self.assertIn(f"draft/{n:02d}.md",readme)
            self.assertIn(f"draft/{n:02d}.md",batch)
            self.assertIn(f"{n:02d}.claims.json",batch)
        self.assertIn("工作初稿 30 篇",readme)
        self.assertIn("策划占位 2 篇",readme)
        self.assertIn("工作初稿三篇",batches)
        self.assertTrue((BOOK/"qa/batch-28-30-self-check.md").exists())
        self.assertTrue((BOOK/"qa/batch-28-30-review-brief.md").exists())
        self.assertIn("独立审稿",batch)


if __name__=="__main__":
    unittest.main()
