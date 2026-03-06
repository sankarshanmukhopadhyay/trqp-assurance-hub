#!/usr/bin/env python3
"""
Generate a TRQP Combined Assurance Manifest that conforms to:
  schemas/combined-assurance-manifest.schema.json

Design goals:
- Zero-magic: explicit args map directly to schema fields
- Portable: stdlib-only by default (jsonschema validation optional)
- CI-friendly: stable output, deterministic timestamp option

Examples
--------
python tools/generate-manifest.py \
  --build-id "$GITHUB_SHA" \
  --target "https://registry.example.org" \
  --hub-commit "$GITHUB_SHA" \
  --ci-run-url "$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID" \
  --cs-version "0.7.1" --cs-profile-id "smoke" --cs-run-id "cts-smoke" \
  --tspp-version "0.5.1" --tspp-assurance-level "AL1" --tspp-run-id "tspp-smoke" \
  --artifact "evidence_bundle:artifacts/conformance-suite-evidence.json:trqp_conformance_suite" \
  --artifact "evidence_bundle:artifacts/tspp-evidence.json:trqp_tspp" \
  --out artifacts/combined-assurance-manifest.json \
  --schema schemas/combined-assurance-manifest.schema.json
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


def _utc_now_rfc3339() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _parse_artifact(spec: str) -> Dict[str, Any]:
    """
    Parse an artifact spec:
      kind:path[:produced_by][:media_type][:format][:notes]

    Only kind and path are required.
    """
    parts = spec.split(":")
    if len(parts) < 2:
        raise ValueError(f"Invalid --artifact '{spec}'. Expected 'kind:path[:produced_by...]'.")
    kind, path = parts[0].strip(), parts[1].strip()
    if not kind or not path:
        raise ValueError(f"Invalid --artifact '{spec}'. kind and path are required.")

    a: Dict[str, Any] = {"kind": kind, "path": path}

    # Optional fields in order
    if len(parts) >= 3 and parts[2].strip():
        a["produced_by"] = parts[2].strip()
    if len(parts) >= 4 and parts[3].strip():
        a["media_type"] = parts[3].strip()
    if len(parts) >= 5 and parts[4].strip():
        a["format"] = parts[4].strip()
    if len(parts) >= 6 and parts[5].strip():
        a["notes"] = parts[5].strip()

    return a


def _maybe_add_sha256(artifact: Dict[str, Any], base_dir: Path) -> None:
    """
    If the artifact path exists on disk, compute sha256 for downstream integrity checks.
    """
    p = base_dir / artifact["path"]
    if p.exists() and p.is_file():
        artifact["sha256"] = _sha256_file(p)


def _validate(schema_path: Path, doc: Dict[str, Any]) -> None:
    """
    Optional JSON Schema validation. Requires 'jsonschema' package.
    """
    try:
        import jsonschema  # type: ignore
        from jsonschema import Draft202012Validator  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError(
            "jsonschema is not installed. Install with: python -m pip install jsonschema"
        ) from e

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(doc)


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Generate a Combined Assurance Manifest (JSON).")
    p.add_argument("--manifest-version", default="0.1.0", help="Manifest schema version (default: 0.1.0).")
    p.add_argument("--generated-at", default=None, help="RFC3339 UTC timestamp. Default: now (UTC).")

    # Build
    p.add_argument("--build-id", required=True, help="Build identifier (e.g., CI SHA or build number).")
    p.add_argument("--target", required=True, help="Target registry base URL tested.")
    p.add_argument("--hub-commit", default=None, help="Commit SHA of orchestrator/hub.")
    p.add_argument("--ci-run-url", default=None, help="CI run URL for traceability.")

    # Tools
    p.add_argument("--cs-version", required=True, help="TRQP Conformance Suite version/tag/sha.")
    p.add_argument("--cs-profile-id", required=True, help="Conformance Suite profile ID (e.g., smoke, baseline).")
    p.add_argument("--cs-run-id", required=True, help="Conformance Suite run identifier.")
    p.add_argument("--tspp-version", required=True, help="TSPP version/tag/sha.")
    p.add_argument("--tspp-assurance-level", required=True, choices=["AL1", "AL2", "AL3", "AL4"], help="TSPP assurance level.")
    p.add_argument("--tspp-run-id", required=True, help="TSPP run identifier.")

    # Artifacts
    p.add_argument(
        "--artifact",
        action="append",
        default=[],
        help="Artifact spec 'kind:path[:produced_by][:media_type][:format][:notes]'. Repeatable.",
    )
    p.add_argument("--base-dir", default=".", help="Base directory for computing sha256 (default: repo root).")

    # Summary (optional)
    p.add_argument("--overall-status", default=None, choices=["pass", "fail", "partial"], help="Overall roll-up status.")
    p.add_argument("--conformance-status", default=None, choices=["pass", "fail", "partial"], help="Conformance roll-up status.")
    p.add_argument("--tspp-status", default=None, choices=["pass", "fail", "partial"], help="TSPP roll-up status.")
    p.add_argument("--notes", default=None, help="Human-readable notes for auditors/adopters.")

    # Generator self-id (optional)
    p.add_argument("--generator-name", default="trqp-assurance-hub:generate-manifest", help="Generator name.")
    p.add_argument("--generator-version", default=None, help="Generator version (SemVer or git SHA).")
    p.add_argument("--generator-uri", default="https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub", help="Generator URI.")

    # Output / validation
    p.add_argument("--out", required=True, help="Output manifest path.")
    p.add_argument("--schema", default=None, help="Optional: schema path to validate against (requires jsonschema).")

    args = p.parse_args(argv)

    generated_at = args.generated_at or _utc_now_rfc3339()

    build: Dict[str, Any] = {"build_id": args.build_id, "target": args.target}
    if args.hub_commit:
        build["commit"] = args.hub_commit
    if args.ci_run_url:
        build["ci_run_url"] = args.ci_run_url

    doc: Dict[str, Any] = {
        "manifest_version": args.manifest_version,
        "build": build,
        "generated_at": generated_at,
        "tools": {
            "trqp_conformance_suite": {
                "version": args.cs_version,
                "profile_id": args.cs_profile_id,
                "run_id": args.cs_run_id,
            },
            "trqp_tspp": {
                "version": args.tspp_version,
                "assurance_level": args.tspp_assurance_level,
                "run_id": args.tspp_run_id,
            },
        },
        "artifacts": [],
        "generator": {
            "name": args.generator_name,
            **({"version": args.generator_version} if args.generator_version else {}),
            **({"uri": args.generator_uri} if args.generator_uri else {}),
        },
    }

    # Artifacts
    base_dir = Path(args.base_dir).resolve()
    artifacts: List[Dict[str, Any]] = []
    for spec in args.artifact:
        a = _parse_artifact(spec)
        _maybe_add_sha256(a, base_dir)
        artifacts.append(a)
    doc["artifacts"] = artifacts

    # Summary (optional)
    if any([args.overall_status, args.conformance_status, args.tspp_status, args.notes]):
        summary: Dict[str, Any] = {}
        if args.overall_status:
            summary["overall_status"] = args.overall_status
        if args.conformance_status:
            summary["conformance_status"] = args.conformance_status
        if args.tspp_status:
            summary["tspp_status"] = args.tspp_status
        if args.notes:
            summary["notes"] = args.notes
        doc["summary"] = summary

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    if args.schema:
        _validate(Path(args.schema), doc)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
