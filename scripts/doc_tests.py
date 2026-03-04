#!/usr/bin/env python3
"""
Lightweight documentation tests with zero repo-specific assumptions:

- Validate that all *.json files under schemas/ and examples/ are parseable JSON.
- Validate that all *.yaml/*.yml under profiles/, requirements/, openapi/, docs/templates/ are parseable YAML.
- Validate that Markdown internal links resolve to existing files (best-effort).

This is intentionally conservative: it catches doc rot without requiring the full runtime stack.
"""
from __future__ import annotations

import os
import re
import sys
import json
from pathlib import Path

import yaml

LINK_RE = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')

def iter_files(root: Path, exts: tuple[str, ...]):
    for p in root.rglob("*"):
        if p.is_file() and p.suffix.lower() in exts and ".git" not in str(p):
            yield p

def validate_json(p: Path) -> str | None:
    try:
        json.loads(p.read_text(encoding="utf-8"))
        return None
    except Exception as e:
        return str(e)

def validate_yaml(p: Path) -> str | None:
    try:
        yaml.safe_load(p.read_text(encoding="utf-8"))
        return None
    except Exception as e:
        return str(e)

def check_markdown_links(repo_root: Path):
    issues = []
    for md in iter_files(repo_root, (".md",)):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for m in LINK_RE.finditer(text):
            url = m.group(1).strip().split()[0]
            if url.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            path = url.split("#")[0]
            if not path or "${" in path or "<" in path:
                continue
            if path.startswith("/"):
                target = (repo_root / path.lstrip("/")).resolve()
            else:
                target = (md.parent / path).resolve()
            if not target.exists():
                issues.append(f"{md.relative_to(repo_root)} -> {url} (missing: {target})")
    return issues

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]

    failures = []

    # JSON parse checks (schemas/examples are high signal)
    for base in ("schemas", "examples", "docs"):
        d = repo_root / base
        if not d.exists():
            continue
        for p in iter_files(d, (".json",)):
            err = validate_json(p)
            if err:
                failures.append(f"Invalid JSON: {p.relative_to(repo_root)}: {err}")

    # YAML parse checks (profiles/requirements/openapi)
    for base in ("profiles", "requirements", "openapi", "docs/templates", "harness/schemas"):
        d = repo_root / base
        if not d.exists():
            continue
        for p in iter_files(d, (".yaml", ".yml")):
            err = validate_yaml(p)
            if err:
                failures.append(f"Invalid YAML: {p.relative_to(repo_root)}: {err}")

    # Markdown internal link checks (best effort)
    failures.extend(check_markdown_links(repo_root))

    if failures:
        print("Documentation tests failed:\n")
        for f in failures[:200]:
            print("-", f)
        if len(failures) > 200:
            print(f"... plus {len(failures)-200} more")
        return 1

    print("Documentation tests: OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
