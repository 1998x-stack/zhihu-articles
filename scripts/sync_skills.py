#!/usr/bin/env python3
"""Copy one canonical skill tree to all compatibility directories, or verify them."""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".opencode/skills"
DESTINATIONS = [ROOT / x for x in (".pi/skills", ".codex/skills", ".agents/skills")]


def collect(folder: Path) -> dict[str, bytes]:
    if not folder.is_dir():
        return {}
    return {p.relative_to(folder).as_posix(): p.read_bytes() for p in folder.rglob("*") if p.is_file()}


def sync(write: bool = False) -> list[str]:
    expected = collect(SOURCE)
    if not expected:
        return ["Canonical source directory is missing/empty"]
    errors: list[str] = []
    for dest in DESTINATIONS:
        actual = collect(dest)
        for relative, data in expected.items():
            if actual.get(relative) == data:
                continue
            if write:
                target = dest / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(SOURCE / relative, target)
            else:
                errors.append(f"{dest.relative_to(ROOT)}/{relative}: missing or content mismatch")
        for extra in sorted(set(actual) - set(expected)):
            if write:
                # Remove only stale files under managed skill mirrors; never touch article content.
                (dest / extra).unlink()
            else:
                errors.append(f"{dest.relative_to(ROOT)}/{extra}: unexpected file")
    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Report drift without modifying any file")
    mode.add_argument("--write", action="store_true", help="Mirror the canonical tree, removing stale files")
    args = parser.parse_args()
    issues = sync(write=args.write)
    if issues:
        print("\n".join(issues), file=sys.stderr)
        sys.exit(1)
    if args.write:
        # A write is successful only if all mirrors now match.
        issues = sync(write=False)
        if issues:
            print("\n".join(issues), file=sys.stderr)
            sys.exit(1)
    print("OK: all Skill files are byte-identical across four project directories.")
