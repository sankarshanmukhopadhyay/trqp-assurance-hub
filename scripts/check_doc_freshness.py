#!/usr/bin/env python3
"""
Fail CI if Tier 0–Tier 3 documents exceed their freshness SLA.

Inputs:
- docs/governance/freshness-policy.yml
- Markdown frontmatter fields:
    owner: <string>
    last_reviewed: YYYY-MM-DD
    tier: 0|1|2|3

Exit codes:
- 0: OK
- 1: SLA violations found
- 2: Misconfigured metadata / parse errors
"""
from __future__ import annotations

import fnmatch
import os
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import yaml

FRONTMATTER_RE = re.compile(r"^\s*---\s*\n(.*?)\n---\s*\n", re.DOTALL)

@dataclass
class Policy:
    sla_days: dict[str, int]
    exempt_globs: list[str]

def load_policy(repo_root: Path) -> Policy:
    policy_path = repo_root / "docs" / "governance" / "freshness-policy.yml"
    if not policy_path.exists():
        raise FileNotFoundError(f"Missing policy file: {policy_path}")
    data = yaml.safe_load(policy_path.read_text(encoding="utf-8"))
    sla = {str(k): int(v) for k, v in (data.get("tier_sla_days") or {}).items()}
    if not sla:
        raise ValueError("tier_sla_days is missing or empty in freshness-policy.yml")
    exempt = list(data.get("exempt_globs") or [])
    return Policy(sla_days=sla, exempt_globs=exempt)

def is_exempt(rel_path: str, exempt_globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel_path, g) for g in exempt_globs)

def parse_frontmatter(md_text: str) -> dict[str, str] | None:
    m = FRONTMATTER_RE.match(md_text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
        return {str(k): str(v) for k, v in fm.items()}
    except Exception:
        return None

def days_since(iso_date: str) -> int:
    d = date.fromisoformat(iso_date)
    return (date.today() - d).days

def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    policy = load_policy(repo_root)

    md_files = [p for p in repo_root.rglob("*.md") if ".git" not in str(p)]
    violations = []
    errors = []

    for p in md_files:
        rel = str(p.relative_to(repo_root))
        if is_exempt(rel, policy.exempt_globs):
            continue

        text = p.read_text(encoding="utf-8", errors="ignore")
        fm = parse_frontmatter(text)
        if fm is None:
            # Only enforce metadata presence for Tier 0/1 *critical* entrypoints
            if rel in ("README.md", "QUICKSTART.md", "docs/index.md", "docs/START_HERE.md"):
                errors.append((rel, "Missing frontmatter (owner/last_reviewed/tier required)"))
            continue

        tier = fm.get("tier")
        last_reviewed = fm.get("last_reviewed")

        if tier is None or last_reviewed is None:
            errors.append((rel, "Frontmatter missing required keys: tier, last_reviewed"))
            continue
        if tier not in policy.sla_days:
            errors.append((rel, f"Unknown tier '{tier}'. Expected one of: {sorted(policy.sla_days.keys())}"))
            continue
        try:
            age = days_since(last_reviewed)
        except Exception as e:
            errors.append((rel, f"Invalid last_reviewed date '{last_reviewed}': {e}"))
            continue

        if age > policy.sla_days[tier]:
            violations.append((rel, tier, last_reviewed, age, policy.sla_days[tier], fm.get("owner", "")))

    if errors:
        print("Documentation freshness policy errors:\n")
        for rel, msg in errors:
            print(f"- {rel}: {msg}")
        print("\nFix the metadata above to enable SLA enforcement.")
        return 2

    if violations:
        print("Documentation freshness SLA violations:\n")
        for rel, tier, lr, age, sla, owner in violations:
            print(f"- {rel} (tier {tier}, owner {owner}): last_reviewed={lr} age={age}d > SLA={sla}d")
        return 1

    print("Documentation freshness SLA: OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
