#!/usr/bin/env python3
"""Fail-closed article lifecycle gate based on manuscript state and actual file presence."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

TARGETS = ("draft", "edit", "final", "publish")
REQUIRED_STATE = {
    "lane", "current_revision", "outline_approved", "evidence_verified",
    "review_status", "reviewed_revision", "unresolved_blockers",
    "edited_revision", "final_approved"
}


def evaluate(directory: Path, target: str) -> list[str]:
    errors: list[str] = []
    if target not in TARGETS:
        return [f"Unknown lifecycle target: {target}"]

    state_file = directory / "workflow-state.json"
    if not state_file.is_file():
        return ["Missing workflow-state.json (legacy articles must be migrated explicitly)"]
    try:
        state = json.loads(state_file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"Unreadable workflow-state.json: {exc}"]
    missing = REQUIRED_STATE - set(state)
    if missing:
        return [f"Missing state fields: {sorted(missing)}"]
    lane = state["lane"]
    revision = state["current_revision"]
    if lane not in ("fiction", "nonfiction"):
        errors.append("lane must be fiction or nonfiction")
    if type(revision) is not int or revision < 0:
        errors.append("current_revision must be a non-negative integer")
    if type(state["outline_approved"]) is not bool:
        errors.append("outline_approved must be boolean")
    if type(state["evidence_verified"]) is not bool:
        errors.append("evidence_verified must be boolean")
    if type(state["final_approved"]) is not bool:
        errors.append("final_approved must be boolean")
    if state["review_status"] not in ("PENDING", "CHANGES_REQUIRED", "PASS"):
        errors.append("Invalid review_status")
    if not isinstance(state["unresolved_blockers"], list):
        errors.append("unresolved_blockers must be a list")
    if errors:
        return errors

    def need(path: str) -> None:
        if not (directory / path).is_file():
            errors.append(f"Missing required file: {path}")

    need("brief.md")
    need("outline.md")
    if state["outline_approved"] is not True:
        errors.append("Outline has not been approved")
    if lane == "fiction":
        need("story-bible.md")
        need("plot-ledger.md")
    else:
        need("research.md")
        need("claim-ledger.md")
        if state["evidence_verified"] is not True:
            errors.append("Nonfiction evidence has not been verified")
    if target == "draft":
        return errors

    drafts = sorted((directory / "draft").glob("[0-9][0-9].md")) if (directory / "draft").is_dir() else []
    if not drafts and not (directory / "revised.md").is_file():
        errors.append("No chapter manuscript or revised.md exists")
    if lane == "fiction":
        need("chapter-state.json")
    else:
        for p in drafts:
            need(f"draft/{p.stem}.claims.json")
    if state["review_status"] != "PASS":
        errors.append("Current review_status is not PASS")
    if state["reviewed_revision"] != revision:
        errors.append("Review is missing or stale for current_revision")
    if state["unresolved_blockers"]:
        errors.append(f"Unresolved blocking issues: {state['unresolved_blockers']}")
    for filename in ("qa/continuity-report.md", "qa/developmental-review.md"):
        need(filename)
        path = directory / filename
        if path.is_file():
            content = path.read_text(encoding="utf-8")
            version = re.search(r"(?m)^revision_count:\s*(\d+)\s*$", content)
            status = re.search(r"(?m)^status:\s*(\w+)\s*$", content)
            if version is None or int(version.group(1)) != revision:
                errors.append(f"Report revision mismatch: {filename}")
            if status is None or status.group(1) != "PASS":
                errors.append(f"Report has not passed: {filename}")
    if target == "edit":
        return errors
    need("edited.md")
    if state["edited_revision"] != revision:
        errors.append("Edited manuscript belongs to another revision")
    if target == "final":
        return errors
    need("final.md")
    need("qa/final-approval.md")
    if state["final_approved"] is not True:
        errors.append("Final approval has not been granted")
    approval = directory / "qa/final-approval.md"
    if approval.is_file():
        txt = approval.read_text(encoding="utf-8")
        version = re.search(r"(?m)^revision_count:\s*(\d+)\s*$", txt)
        approved = re.search(r"(?m)^approved:\s*(true|false)\s*$", txt)
        if version is None or int(version.group(1)) != revision:
            errors.append("Final approval refers to a stale revision")
        if approved is None or approved.group(1) != "true":
            errors.append("Final approval report is not approved")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("article_dir", type=Path)
    parser.add_argument("--target", required=True, choices=TARGETS)
    args = parser.parse_args()
    errors = evaluate(args.article_dir, args.target)
    if errors:
        print("\n".join("BLOCKED: " + error for error in errors), file=sys.stderr)
        return 1
    print(f"PASS: {args.target} gate for {args.article_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
