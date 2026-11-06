#!/usr/bin/env python3
"""Explicit article-state transitions; never infers editorial or factual approval."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile

from workflow_gate import evaluate


def load_state(root: Path) -> dict:
    path = root / "workflow-state.json"
    if not path.is_file():
        raise ValueError("Missing workflow-state.json; migrate legacy work explicitly")
    state = json.loads(path.read_text(encoding="utf-8"))
    if state.get("lane") not in ("fiction", "nonfiction"):
        raise ValueError("Invalid fictionality lane")
    if type(state.get("current_revision")) is not int or state["current_revision"] < 0:
        raise ValueError("Invalid current_revision")
    return state


def save_state(root: Path, state: dict) -> None:
    path = root / "workflow-state.json"
    root.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".workflow-state-", suffix=".json", dir=str(root))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(state, stream, indent=2, ensure_ascii=False)
            stream.write("\n")
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)


def report_passed(root: Path, revision: int) -> None:
    for rel in ("qa/continuity-report.md", "qa/developmental-review.md"):
        path = root / rel
        if not path.is_file():
            raise ValueError(f"Missing review report: {rel}")
        txt = path.read_text(encoding="utf-8")
        v = re.search(r"(?m)^revision_count:\s*(\d+)\s*$", txt)
        status = re.search(r"(?m)^status:\s*(\w+)\s*$", txt)
        if v is None or int(v.group(1)) != revision or status is None or status.group(1) != "PASS":
            raise ValueError(f"Report is stale or not PASS: {rel}")


def transition(root: Path, action: str, *, confirm: bool = False, reason: str = "") -> dict:
    state = load_state(root)
    revision = state["current_revision"]

    if action == "evidence-verified":
        if state["lane"] != "nonfiction":
            raise ValueError("Evidence approval is only mandatory for nonfiction")
        if not (root / "research.md").is_file():
            raise ValueError("Research evidence file is missing")
        if not confirm:
            raise ValueError("Review the sources first; use --confirm after real verification")
        state["evidence_verified"] = True

    elif action == "outline-approved":
        if not confirm:
            raise ValueError("Use --confirm only after reviewing the actual outline")
        if not (root / "brief.md").is_file() or not (root / "outline.md").is_file():
            raise ValueError("Missing brief.md or outline.md")
        if state["lane"] == "nonfiction":
            if not state["evidence_verified"] or not (root / "claim-ledger.md").is_file():
                raise ValueError("Nonfiction needs verified research and claim ledger first")
        else:
            if not (root / "story-bible.md").is_file() or not (root / "plot-ledger.md").is_file():
                raise ValueError("Fiction needs character/world bible and plot ledger first")
        state["outline_approved"] = True

    elif action == "review-passed":
        if not confirm:
            raise ValueError("Use --confirm only after independent editorial review")
        if state["unresolved_blockers"]:
            raise ValueError("Cannot mark PASS with unresolved blocking issues")
        if evaluate(root, "draft"):
            raise ValueError("Cannot approve review before the draft gate passes")
        report_passed(root, revision)
        state["review_status"] = "PASS"
        state["reviewed_revision"] = revision

    elif action == "edited":
        if evaluate(root, "edit"):
            raise ValueError("Cannot mark an unreviewed or blocked draft as edited")
        p = root / "edited.md"
        if not p.is_file() or not p.read_text(encoding="utf-8").strip():
            raise ValueError("A real edited.md is required")
        state["edited_revision"] = revision

    elif action == "finalize":
        if not confirm:
            raise ValueError("Use --confirm only after final manuscript verification")
        if evaluate(root, "final"):
            raise ValueError("The current revision does not pass the final gate")
        source = root / "edited.md"
        final = root / "final.md"
        if final.exists() and final.read_bytes() != source.read_bytes():
            raise ValueError("Existing final.md differs from edited.md; start a revision to archive it")
        final.write_bytes(source.read_bytes())
        record = root / "qa/final-approval.md"
        record.parent.mkdir(parents=True, exist_ok=True)
        record.write_text(
            f"# Final Approval\n\nrevision_count: {revision}\napproved: true\n\n"
            "Checked current-version review, unresolved blockers, edit version and evidence gate.\n",
            encoding="utf-8",
        )
        state["final_approved"] = True

    elif action == "new-revision":
        if not reason.strip():
            raise ValueError("Revision must have an explicit reason")
        archived = root / "history" / f"final-r{revision}.md"
        old_final = root / "final.md"
        if old_final.is_file():
            archived.parent.mkdir(parents=True, exist_ok=True)
            if archived.exists():
                raise ValueError("Archive destination already exists; resolve before revising")
            shutil.move(str(old_final), str(archived))
        revision += 1
        state["current_revision"] = revision
        state["review_status"] = "PENDING"
        state["reviewed_revision"] = None
        state["edited_revision"] = None
        state["final_approved"] = False
        # Existing blockers remain unresolved until the editor verifies the corrections.
        log = root / "qa/revision-log.md"
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("a", encoding="utf-8") as stream:
            stream.write(f"\n- Revision {revision}: {reason.strip()} (previous approvals invalidated)\n")
    else:
        raise ValueError("Unknown state transition: " + action)

    save_state(root, state)
    return state


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article_dir", type=Path)
    parser.add_argument("action", choices=[
        "evidence-verified", "outline-approved", "review-passed",
        "edited", "finalize", "new-revision"
    ])
    parser.add_argument("--confirm", action="store_true", help="Explicit approval after real review")
    parser.add_argument("--reason", default="", help="Required reason for new-revision")
    args = parser.parse_args()
    try:
        state = transition(args.article_dir, args.action, confirm=args.confirm, reason=args.reason)
    except (ValueError, OSError, json.JSONDecodeError) as err:
        print(f"BLOCKED: {err}", file=sys.stderr)
        return 1
    print(f"OK: {args.action}; revision={state['current_revision']}; review={state['review_status']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
