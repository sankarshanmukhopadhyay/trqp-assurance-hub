#!/usr/bin/env python3
"""Validate and resolve a version-bound TRQP assurance profile."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schemas" / "trqp-profile-contract.schema.json"


def load_profile(path: Path) -> dict:
    document = yaml.safe_load(path.read_text(encoding="utf-8"))
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(document)
    return document


def resolve(profile_id: str, profile_version: str, profiles_dir: Path) -> tuple[Path, dict]:
    matches = []
    for path in sorted(profiles_dir.glob("*/profile.yaml")):
        document = load_profile(path)
        if document["profile_id"] == profile_id and document["profile_version"] == profile_version:
            matches.append((path, document))
    if not matches:
        raise ValueError(f"unknown profile: {profile_id}@{profile_version}")
    if len(matches) != 1:
        raise ValueError(f"ambiguous profile: {profile_id}@{profile_version}")
    return matches[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile")
    parser.add_argument("--id")
    parser.add_argument("--version")
    parser.add_argument("--profiles-dir", default=str(ROOT / "profiles"))
    args = parser.parse_args()
    if args.profile:
        load_profile(Path(args.profile))
        print(f"valid: {args.profile}")
        return 0
    if not (args.id and args.version):
        parser.error("provide --profile or both --id and --version")
    path, _ = resolve(args.id, args.version, Path(args.profiles_dir))
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
