#!/usr/bin/env python3
"""Validate OpenCode skills, prompt coverage and article categorization."""
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
for genre in catalog["genres"]:
    if not (ROOT / genre["archive"] / ".gitkeep").is_file():
        errors.append(f"Missing article category: {genre['archive']}")
for name in ("metadata.yaml","brief.md","story-bible.md","outline.md","research.md","qa-report.md","final.md"):
    if not (ROOT / "articles" / "_template" / name).is_file():
        errors.append(f"Missing article template: {name}")
if errors:
    print("\n".join("ERROR: " + e for e in errors), file=sys.stderr)
    sys.exit(1)
print(f"OK: {len(skill_ids)} Skills, {len(catalog['genres'])} genre archives and article templates validated.")
