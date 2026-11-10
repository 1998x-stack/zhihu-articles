#!/usr/bin/env python3
"""Audit edition-safe series progress across manuscripts, chapter manifests and READMEs.

book.json is the editorial source of truth for chapter visibility (not for
independent review approval). --write ONLY refreshes the derived progress
block in README.md and progress_summary in chapter-state.json. It never
promotes any chapter from outline to draft or final automatically.
"""
from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path, PurePosixPath
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- SERIES_PROGRESS:START -->"
END = "<!-- SERIES_PROGRESS:END -->"
STATUSES = ("outline", "draft", "final")
REVIEW_STATUSES = {"PENDING", "CHANGES_REQUIRED", "PASS"}
DRAFT_MARKERS = re.compile(r"工作初稿|研究初稿|研究性正文初稿|正文初稿|章节初稿|非虚构初稿|完整候审稿")
ID_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"Expected JSON object: {path}")
    return value


def dump(value: dict) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def discover(root: Path = ROOT) -> list[Path]:
    catalog = load(root / "catalog.json")
    directories = []
    for genre in catalog["genres"]:
        archive = root / genre["archive"]
        if not archive.is_dir():
            continue
        for directory in sorted(archive.iterdir()):
            if directory.is_dir() and (directory / "README.md").is_file():
                directories.append(directory)
    return directories


def number_for(chapter: dict) -> str | None:
    stem = PurePosixPath(chapter["file"]).stem
    number = re.match(r"^(\d{2})(?:-|$)", stem)
    return number.group(1) if number else None


def status_counts(chapters: list[dict]) -> Counter:
    return Counter(ch["status"] for ch in chapters)


def progress(root: Path, directory: Path) -> tuple[dict, dict, dict]:
    book = load(directory / "book.json")
    workflow = load(directory / "workflow-state.json")
    if book.get("id") != directory.name or book.get("schema_version") != 1:
        raise ValueError(f"{directory}: book.json id/schema_version mismatch")
    chapters = book.get("chapters")
    if not isinstance(chapters, list) or not chapters:
        raise ValueError(f"{directory}: book.json chapters missing")
    seen_ids, seen_files = set(), set()
    for chapter in chapters:
        chapter_id, relative, status = chapter.get("id"), chapter.get("file"), chapter.get("status")
        if not isinstance(chapter_id, str) or not ID_PATTERN.fullmatch(chapter_id):
            raise ValueError(f"{directory}: invalid chapter id: {chapter_id}")
        if chapter_id in seen_ids:
            raise ValueError(f"{directory}: duplicate chapter id: {chapter_id}")
        seen_ids.add(chapter_id)
        if status not in STATUSES:
            raise ValueError(f"{directory}: invalid status for {chapter_id}: {status}")
        if not all(isinstance(chapter.get(key), str) and chapter[key].strip() for key in ("title", "part")):
            raise ValueError(f"{directory}: missing title/part for {chapter_id}")
        if not isinstance(relative, str) or "\\" in relative:
            raise ValueError(f"{directory}: invalid file path for {chapter_id}")
        candidate = PurePosixPath(relative)
        if candidate.is_absolute() or ".." in candidate.parts or candidate.suffix != ".md":
            raise ValueError(f"{directory}: unsafe Markdown path for {chapter_id}")
        manuscript = (directory / relative).resolve()
        if not manuscript.is_relative_to(directory.resolve()) or not manuscript.is_file():
            raise ValueError(f"{directory}: missing/outside manuscript {relative}")
        if relative in seen_files:
            raise ValueError(f"{directory}: duplicate manuscript {relative}")
        seen_files.add(relative)
        # A long, actual manuscript marked as an outline is a common source
        # of stale Pages counts. Only raise on explicit draft identity in text:
        # do not assume every long outline is a completed draft.
        if status == "outline" and manuscript.stat().st_size > 5000:
            opening = manuscript.read_text(encoding="utf-8")[:1000]
            if DRAFT_MARKERS.search(opening) and "不是正文" not in opening:
                raise ValueError(
                    f"{directory}: {relative} says it is a draft but book.json marks outline"
                )
    current = workflow.get("review_status")
    if current not in REVIEW_STATUSES or not isinstance(workflow.get("final_approved"), bool):
        raise ValueError(f"{directory}: invalid workflow review/final status")
    if any(c["status"] == "final" for c in chapters) and not workflow["final_approved"]:
        raise ValueError(f"{directory}: final chapters require explicit approval; never infer from file size")
    counts = status_counts(chapters)
    proposals_dir = directory / "proposals"
    proposals = sum(1 for chapter in chapters if proposals_dir.joinpath(
        (number_for(chapter) or "no-number") + ".md"
    ).is_file())
    summary = {
        "source": "book.json",
        "total": len(chapters),
        "draft": counts["draft"],
        "outline": counts["outline"],
        "final": counts["final"],
        "proposals": proposals,
        "review_status": current,
        "final_approved": workflow["final_approved"],
    }
    return book, workflow, summary


def readme_block(summary: dict) -> str:
    approved = "是" if summary["final_approved"] else "否"
    text = (
        f"> **系列进度（自动核对，非出版许可）**："
        f"规划 {summary['total']} 篇 · 工作初稿 {summary['draft']} 篇 · "
        f"策划占位 {summary['outline']} 篇 · 已标记审定 {summary['final']} 篇 · "
        f"独立候审稿 {summary['proposals']} 篇（不计入工作初稿） · "
        f"双审状态 {summary['review_status']} · 最终封版 {approved}。"
    )
    return f"{START}\n{text}\n{END}"


def replace_readme(content: str, summary: dict) -> str:
    block = readme_block(summary)
    has_start, has_end = START in content, END in content
    if has_start != has_end or content.count(START) > 1 or content.count(END) > 1:
        raise ValueError("README has malformed SERIES_PROGRESS marker(s)")
    if has_start:
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
        return pattern.sub(lambda _: block, content, count=1)
    match = re.match(r"^(#[^\n]+\n)", content)
    if not match:
        raise ValueError("README must start with a single top-level title")
    return content[:match.end()] + "\n" + block + "\n" + content[match.end():]


def chapter_state_errors(directory: Path, book: dict, workflow: dict, state: dict) -> list[str]:
    """Cross-check explicitly tracked chapters; allow legacy partial ledgers."""
    errors = []
    chapters = book["chapters"]
    by_id = {x["id"]: x for x in chapters}
    by_no = {number_for(x): x for x in chapters if number_for(x) is not None}
    known = {"draft": "draft", "draft-written": "draft", "outline": "outline",
             "outline-only": "outline", "placeholder": "outline", "final": "final"}
    def compare(key, value):
        chapter = by_id.get(str(key)) or by_no.get(str(key).zfill(2))
        if chapter is None:
            errors.append(f"unknown chapter-state entry: {key}")
        elif value not in known:
            errors.append(f"unsupported chapter-state status {key}: {value}")
        elif known[value] != chapter["status"]:
            errors.append(f"chapter-state {key}={value} != book.json {chapter['status']}")
    for key in ("chapter_status", "chapter_statuses"):
        for number, value in state.get(key, {}).items():
            compare(number, value)
    for chapter_id, data in state.get("chapter_progress", {}).items():
        if isinstance(data, dict) and "status" in data:
            compare(chapter_id, data["status"])
    for item in state.get("chapters", []):
        if isinstance(item, dict):
            number = item.get("chapter_id", item.get("chapter"))
            value = item.get("stage", item.get("status"))
            if number is not None and value is not None:
                compare(number, value)
    if "completed_drafts" in state:
        recorded = set(map(str, state["completed_drafts"]))
        expected = {number_for(c) for c in chapters if c["status"] == "draft"}
        if recorded != expected:
            errors.append(f"completed_drafts mismatch: expected {sorted(expected)}, got {sorted(recorded)}")
    for key in ("last_chapter", "last_written_chapter"):
        if key in state:
            try:
                actual = int(state[key])
                latest = max(int(number_for(c)) for c in chapters if c["status"] == "draft" and number_for(c) is not None and int(number_for(c)) < 90)
            except (ValueError, TypeError):
                errors.append(f"invalid {key}")
            else:
                if actual != latest:
                    errors.append(f"{key}={actual} differs from last drafted numbered chapter {latest}")
    for key in ("current_revision", "manuscript_revision"):
        if key in state and state[key] != workflow.get("current_revision"):
            errors.append(f"{key}={state[key]} != workflow current_revision={workflow.get('current_revision')}")
    if "review_status" in state and state["review_status"] != workflow["review_status"]:
        errors.append("chapter-state review_status differs from workflow-state")
    if "publication_ready" in state and state["publication_ready"] and not workflow["final_approved"]:
        errors.append("chapter-state publication_ready contradicts unapproved final")
    return errors


def series_json_errors(directory: Path, book: dict) -> list[str]:
    path = directory / "series.json"
    if not path.is_file():
        return []
    value = load(path)
    source = {number_for(ch): ch["status"] for ch in book["chapters"]}
    expected_status = {"draft_unreviewed": "draft", "placeholder": "outline",
                       "final": "final"}
    errors = []
    for chapter in value.get("chapters", []):
        no = str(chapter.get("id")).zfill(2)
        raw = chapter.get("status")
        if no not in source or raw not in expected_status or source[no] != expected_status[raw]:
            errors.append(f"series.json {no}={raw} differs from book.json {source.get(no)}")
    return errors


def run(root: Path = ROOT, *, write: bool = False) -> tuple[int, list[str]]:
    failures, processed = [], 0
    for directory in discover(root):
        path = directory.relative_to(root).as_posix()
        try:
            book, workflow, summary = progress(root, directory)
            errors = series_json_errors(directory, book)
            state_path = directory / "chapter-state.json"
            existing = load(state_path) if state_path.is_file() else {
                "schema_version": "1.0",
                "lane": "nonfiction" if "/nonfiction/" in "/" + path + "/" else "fiction",
                "tracking_mode": "derived-publication-index",
                "note": "本文件仅保存派生进度，不代表任何写作或审稿动作已发生。",
            }
            errors += chapter_state_errors(directory, book, workflow, existing)
            if errors:
                failures.extend(f"{path}: {message}" for message in errors)
                continue
            readme_path = directory / "README.md"
            before = readme_path.read_text(encoding="utf-8")
            expected = replace_readme(before, summary)
            after_state = dict(existing)
            after_state["progress_summary"] = summary
            if write:
                if before != expected:
                    readme_path.write_text(expected, encoding="utf-8")
                if existing != after_state or not state_path.is_file():
                    state_path.write_text(dump(after_state), encoding="utf-8")
            else:
                if before != expected:
                    failures.append(f"{path}: README progress block stale/missing; run --write")
                if existing.get("progress_summary") != summary or not state_path.is_file():
                    failures.append(f"{path}: chapter-state.json progress_summary stale/missing; run --write")
            processed += 1
        except (OSError, ValueError, KeyError, TypeError) as exc:
            failures.append(f"{path}: {exc}")
    if not processed:
        failures.append("No series processed")
    return processed, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Update only derived README and chapter-state progress")
    mode.add_argument("--check", action="store_true", help="Check repo progress consistency (default)")
    args = parser.parse_args()
    count, errors = run(write=args.write)
    if errors:
        for err in errors:
            print("ERROR", err, file=sys.stderr)
        return 1
    print(f"OK: {count} series: book.json, README progress, chapter-state.json, series.json and workflow approval match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
