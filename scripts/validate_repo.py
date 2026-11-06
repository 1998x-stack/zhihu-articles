#!/usr/bin/env python3
"""Validate three mirrored skill trees, prompt coverage and article categorization."""
from __future__ import annotations
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
skill_ids = [catalog["core_skill"]] + [x["skill"] for x in catalog["genres"]] + [x["skill"] for x in catalog["stages"]]
errors = []
pattern = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
if len(skill_ids) != len(set(skill_ids)):
    errors.append("Duplicate skill IDs")
for sid in skill_ids:
    folder = ROOT / ".opencode" / "skills" / sid
    skill = folder / "SKILL.md"
    prompt = folder / "prompt.txt"
    if not pattern.fullmatch(sid):
        errors.append(f"Invalid skill ID: {sid}")
    if not skill.is_file() or not prompt.is_file():
        errors.append(f"Missing SKILL.md or prompt.txt for {sid}")
        continue
    text = skill.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        errors.append(f"Missing YAML frontmatter in {sid}")
        continue
    frontmatter = match.group(1)
    if not re.search(rf"^name:\s*{re.escape(sid)}\s*$", frontmatter, re.M):
        errors.append(f"Skill name mismatch in {sid}")
    d = re.search(r"^description:\s*(.*?)\s*$", frontmatter, re.M)
    if not d or not (1 <= len(d.group(1)) <= 1024):
        errors.append(f"Invalid skill description in {sid}")
    if len(prompt.read_text(encoding="utf-8").strip()) < 200:
        errors.append(f"Prompt too short in {sid}")
SKILL_ROOTS = (".opencode/skills", ".pi/skills", ".codex/skills")
for sid in skill_ids:
    source = ROOT / SKILL_ROOTS[0] / sid
    for mirror_root in SKILL_ROOTS[1:]:
        mirrored = ROOT / mirror_root / sid
        for filename in ("SKILL.md", "prompt.txt"):
            source_file = source / filename
            mirrored_file = mirrored / filename
            if not mirrored_file.is_file():
                errors.append(f"Missing mirrored file: {mirror_root}/{sid}/{filename}")
            elif source_file.is_file() and source_file.read_bytes() != mirrored_file.read_bytes():
                errors.append(f"Mirror mismatch: {mirror_root}/{sid}/{filename}")
for genre in catalog["genres"]:
    if not (ROOT / genre["archive"] / ".gitkeep").is_file():
        errors.append(f"Missing article category: {genre['archive']}")
for name in ("metadata.yaml","brief.md","story-bible.md","outline.md","research.md","qa-report.md","final.md"):
    if not (ROOT / "articles" / "_template" / name).is_file():
        errors.append(f"Missing article template: {name}")
if errors:
    print("\n".join("ERROR: " + e for e in errors), file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(skill_ids)} Skills mirrored across {len(SKILL_ROOTS)} roots, {len(catalog['genres'])} genre archives and article templates validated.")
