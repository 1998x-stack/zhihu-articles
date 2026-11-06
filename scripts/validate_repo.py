#!/usr/bin/env python3
"""Static contracts for all 25 writing skills, branches and mirrored roots."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
ROOTS = [".opencode/skills", ".pi/skills", ".codex/skills", ".agents/skills"]


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    catalog = json.loads((root / "catalog.json").read_text(encoding="utf-8"))
    flow = json.loads((root / "workflow.json").read_text(encoding="utf-8"))
    ids = [catalog["core_skill"]] + [g["skill"] for g in catalog["genres"]] + [s["skill"] for s in catalog["stages"]]
    if len(ids) != len(set(ids)):
        errors.append("Duplicate Skill ID")
    if len(catalog["genres"]) != 10:
        errors.append("Expected exactly ten genre definitions")
    if len(catalog["stages"]) != len(flow["stage_contracts"]):
        errors.append("catalog.json and workflow.json disagree on stage count")
    if set(s["skill"] for s in catalog["stages"]) != set(flow["stage_contracts"]):
        errors.append("Stage identifiers differ across catalog and workflow")

    canonical = root / ROOTS[0]
    if not canonical.is_dir():
        return ["Missing canonical skill root"]
    source_files = {
        p.relative_to(canonical).as_posix(): p.read_bytes()
        for p in canonical.rglob("*") if p.is_file()
    }
    expected_dirs = set(ids)
    actual_dirs = {p.split("/", 1)[0] for p in source_files}
    if expected_dirs != actual_dirs:
        errors.append(f"Unexpected/missing skill directories: {sorted(expected_dirs ^ actual_dirs)}")
    for sid in ids:
        if not NAME.fullmatch(sid) or len(sid) > 64:
            errors.append(f"Invalid portable Skill name: {sid}")
            continue
        skill_path = f"{sid}/SKILL.md"
        prompt_path = f"{sid}/prompt.txt"
        for path in (skill_path, prompt_path):
            if path not in source_files:
                errors.append(f"Missing {path}")
        raw = source_files.get(skill_path, b"").decode("utf-8")
        front = re.match(r"^---\n([\s\S]*?)\n---\n", raw)
        if front is None:
            errors.append(f"Missing YAML frontmatter: {skill_path}")
            continue
        name_match = re.search(r"^name:\s*(.*?)\s*$", front.group(1), re.M)
        description_match = re.search(r"^description:\s*(.*?)\s*$", front.group(1), re.M)
        if name_match is None or name_match.group(1) != sid:
            errors.append(f"Invalid name: {sid}")
        if description_match is None or not (1 <= len(description_match.group(1)) <= 1024):
            errors.append(f"Missing/long description: {sid}")
        if len(source_files.get(prompt_path, b"")) < 200:
            errors.append(f"Prompt too short: {sid}")

    core = source_files.get("chief-narrative-editor/prompt.txt", b"").decode("utf-8")
    if len(core) < 4000 or "## 九、最终输出规范" not in core:
        errors.append("Full original chief-editor prompt missing or shortened")
    for g in catalog["genres"]:
        sid = g["skill"]
        if f"{sid}/prompt-original.txt" not in source_files:
            errors.append(f"Missing archival genre prompt: {sid}")
        if not (root / g["archive"] / ".gitkeep").is_file():
            errors.append(f"Missing genre archive: {g['archive']}")
    for sid in ("story-architect", "chapter-writer", "developmental-editor"):
        if f"{sid}/prompt-original.txt" not in source_files:
            errors.append(f"Missing original workflow prompt: {sid}")

    for mirror in ROOTS[1:]:
        folder = root / mirror
        if not folder.is_dir():
            errors.append(f"Missing mirror root: {mirror}")
            continue
        actual = {
            p.relative_to(folder).as_posix(): p.read_bytes()
            for p in folder.rglob("*") if p.is_file()
        }
        if set(actual) != set(source_files):
            missing = set(source_files) - set(actual)
            unexpected = set(actual) - set(source_files)
            errors.append(f"Mirror file list mismatch {mirror}: missing={len(missing)}, extra={len(unexpected)}")
        for path in sorted(set(source_files) & set(actual)):
            if source_files[path] != actual[path]:
                errors.append(f"Mirror content mismatch: {mirror}/{path}")

    if flow["discovery_roots"]["codex"] != ".agents/skills":
        errors.append("Codex standard discovery root must be .agents/skills")
    if flow["discovery_roots"]["legacy_codex_archive"] != ".codex/skills":
        errors.append("Legacy .codex folder must be documented as archive")
    for lane in ("fiction", "nonfiction"):
        order = flow["branches"][lane]
        if len(order) != len(set(order)):
            errors.append(f"Duplicate stage in {lane} branch")
        if any(x not in flow["stage_contracts"] for x in order):
            errors.append(f"Unknown stage in {lane} branch")
            continue
        if order[0] != "topic-development" or order[-1] != "publication-package":
            errors.append(f"Invalid first/last stage in {lane}")
        for common in ("continuity-audit", "developmental-editor", "line-edit", "final-approval"):
            if common not in order:
                errors.append(f"Missing common stage {common} in {lane}")
        owned: dict[str, str] = {}
        for sid in order:
            stage = flow["stage_contracts"][sid]
            if stage["lane"] not in ("both", lane):
                errors.append(f"Cross-lane stage {sid} in {lane}")
            for output in stage["writes"]:
                if output in owned:
                    errors.append(f"Two owners for {lane} {output}: {owned[output]} and {sid}")
                owned[output] = sid
        if lane == "nonfiction":
            if not (order.index("fact-research") < order.index("nonfiction-architect") < order.index("nonfiction-writer")):
                errors.append("Nonfiction requires evidence before outline and writing")
            if "chapter-writer" in order:
                errors.append("Fiction writer appears in nonfiction branch")
        if lane == "fiction" and ("nonfiction-writer" in order or "nonfiction-architect" in order):
            errors.append("Nonfiction-only stage appears in fiction branch")

    template_files = [
        "metadata.yaml", "workflow-state.json", "brief.md", "outline.md",
        "story-bible.md", "plot-ledger.md", "claim-ledger.md", "chapter-state.json",
        "research.md", "edited.md", "revised.md", "final.md",
        "qa/continuity-report.md", "qa/developmental-review.md",
        "qa/revision-log.md", "qa/final-approval.md"
    ]
    for rel in template_files:
        if not (root / "articles" / "_template" / rel).is_file():
            errors.append(f"Missing article template: {rel}")
    try:
        state = json.loads((root / "articles" / "_template" / "workflow-state.json").read_text(encoding="utf-8"))
        if state["schema_version"] != "2.0" or state["final_approved"] is not False:
            errors.append("Template workflow-state must start unapproved")
    except (ValueError, KeyError) as exc:
        errors.append(f"Invalid workflow state template: {exc}")

    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join("ERROR " + p for p in failures), file=sys.stderr)
        sys.exit(1)
    print("OK: 25 skills, 4 identical copies, 10 genre archives, branched workflow, unique file ownership and templates.")
