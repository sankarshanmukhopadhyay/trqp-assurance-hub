#!/usr/bin/env python3
"""
Generate a TRQP Combined Assurance Manifest that conforms to:
  schemas/combined-assurance-manifest.schema.json

Design goals:
- Zero-magic: explicit args map directly to schema fields
- Portable: stdlib-only by default (jsonschema validation optional)
- CI-friendly: stable output, deterministic timestamp option
- Operational-stack aware: can ingest CTS/TSPP report metadata directly
"""
from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


def _utc_now_rfc3339() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _parse_artifact(spec: str) -> Dict[str, Any]:
    parts = spec.split(":")
    if len(parts) < 2:
        raise ValueError(f"Invalid --artifact '{spec}'. Expected 'kind:path[:produced_by...]'.")
    kind, path = parts[0].strip(), parts[1].strip()
    if not kind or not path:
        raise ValueError(f"Invalid --artifact '{spec}'. kind and path are required.")

    a: Dict[str, Any] = {"kind": kind, "path": path}
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
    p = base_dir / artifact["path"]
    if p.exists() and p.is_file():
        artifact["sha256"] = _sha256_file(p)


def _load_json(path: Optional[str]) -> Dict[str, Any]:
    if not path:
        return {}
    return json.loads(Path(path).read_text(encoding="utf-8"))


def _validate(schema_path: Path, doc: Dict[str, Any]) -> None:
    try:
        from jsonschema import Draft202012Validator  # type: ignore
    except Exception as e:  # pragma: no cover
        raise RuntimeError("jsonschema is not installed. Install with: python -m pip install jsonschema") from e

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    Draft202012Validator(schema).validate(doc)


def _infer_status(report: Dict[str, Any], fail_key: str = "FAIL", pass_key: str = "PASS") -> Optional[str]:
    summary = report.get("summary", {}) if isinstance(report, dict) else {}
    if not summary:
        return None
    fails = int(summary.get(fail_key, 0) or 0)
    passes = int(summary.get(pass_key, 0) or 0)
    if fails > 0:
        return "fail"
    if passes > 0:
        return "pass"
    return "partial"


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(description="Generate a Combined Assurance Manifest (JSON).")
    p.add_argument("--manifest-version", default="0.2.0")
    p.add_argument("--generated-at", default=None)
    p.add_argument("--run-id", default=None, help="Shared operational stack run identifier.")
    p.add_argument("--target-id", default=None, help="Stable evaluated service identifier.")

    p.add_argument("--build-id", required=True)
    p.add_argument("--target", required=True)
    p.add_argument("--hub-commit", default=None)
    p.add_argument("--ci-run-url", default=None)

    p.add_argument("--cs-version", default=None)
    p.add_argument("--cs-profile-id", default=None)
    p.add_argument("--cs-run-id", default=None)
    p.add_argument("--tspp-version", default=None)
    p.add_argument("--tspp-assurance-level", default=None, choices=["AL1", "AL2", "AL3", "AL4"])
    p.add_argument("--tspp-run-id", default=None)

    p.add_argument("--cts-report", default=None, help="Optional CTS report JSON to ingest.")
    p.add_argument("--tspp-report", default=None, help="Optional TSPP report JSON to ingest.")

    p.add_argument("--artifact", action="append", default=[])
    p.add_argument("--base-dir", default=".")

    p.add_argument("--overall-status", default=None, choices=["pass", "fail", "partial"])
    p.add_argument("--conformance-status", default=None, choices=["pass", "fail", "partial"])
    p.add_argument("--tspp-status", default=None, choices=["pass", "fail", "partial"])
    p.add_argument("--notes", default=None)

    p.add_argument("--generator-name", default="trqp-assurance-hub:generate-manifest")
    p.add_argument("--generator-version", default=None)
    p.add_argument("--generator-uri", default="https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub")

    p.add_argument("--out", required=True)
    p.add_argument("--schema", default=None)
    args = p.parse_args(argv)

    generated_at = args.generated_at or _utc_now_rfc3339()
    cts_report = _load_json(args.cts_report)
    tspp_report = _load_json(args.tspp_report)

    run_id = args.run_id or cts_report.get("run_id") or tspp_report.get("run_id") or args.build_id
    target_id = args.target_id or cts_report.get("target_id") or tspp_report.get("target_id") or args.target

    build: Dict[str, Any] = {
        "build_id": args.build_id,
        "target": args.target,
        "run_id": run_id,
        "target_id": target_id,
    }
    if args.hub_commit:
        build["commit"] = args.hub_commit
    if args.ci_run_url:
        build["ci_run_url"] = args.ci_run_url

    cs_version = args.cs_version or cts_report.get("tool", {}).get("version") or cts_report.get("suite_version")
    cs_profile_id = args.cs_profile_id or cts_report.get("profile_id") or cts_report.get("profile")
    cs_run_id = args.cs_run_id or cts_report.get("run_id")
    tspp_version = args.tspp_version or tspp_report.get("tool", {}).get("version") or tspp_report.get("tool_version")
    tspp_assurance_level = args.tspp_assurance_level or tspp_report.get("assurance_level") or tspp_report.get("target", {}).get("expected_assurance_level")
    tspp_run_id = args.tspp_run_id or tspp_report.get("run_id")

    if not all([cs_version, cs_profile_id, cs_run_id, tspp_version, tspp_assurance_level, tspp_run_id]):
        missing = [
            name for name, value in [
                ("cs-version", cs_version),
                ("cs-profile-id", cs_profile_id),
                ("cs-run-id", cs_run_id),
                ("tspp-version", tspp_version),
                ("tspp-assurance-level", tspp_assurance_level),
                ("tspp-run-id", tspp_run_id),
            ] if not value
        ]
        raise SystemExit(f"Missing tool metadata for manifest generation: {', '.join(missing)}")

    doc: Dict[str, Any] = {
        "manifest_version": args.manifest_version,
        "generated_at": generated_at,
        "build": build,
        "tools": {
            "trqp_conformance_suite": {
                "version": cs_version,
                "profile_id": cs_profile_id,
                "run_id": cs_run_id,
            },
            "trqp_tspp": {
                "version": tspp_version,
                "assurance_level": tspp_assurance_level,
                "run_id": tspp_run_id,
            },
        },
        "artifacts": [],
        "generator": {
            "name": args.generator_name,
            **({"version": args.generator_version} if args.generator_version else {}),
            **({"uri": args.generator_uri} if args.generator_uri else {}),
        },
    }

    base_dir = Path(args.base_dir).resolve()
    artifacts: List[Dict[str, Any]] = []
    for spec in args.artifact:
        a = _parse_artifact(spec)
        _maybe_add_sha256(a, base_dir)
        artifacts.append(a)
    doc["artifacts"] = artifacts

    conformance_status = args.conformance_status or _infer_status(cts_report)
    tspp_status = args.tspp_status or _infer_status(tspp_report)
    overall_status = args.overall_status
    if not overall_status:
        statuses = [s for s in [conformance_status, tspp_status] if s]
        if "fail" in statuses:
            overall_status = "fail"
        elif statuses and all(s == "pass" for s in statuses):
            overall_status = "pass"
        elif statuses:
            overall_status = "partial"

    if any([overall_status, conformance_status, tspp_status, args.notes]):
        summary: Dict[str, Any] = {}
        if overall_status:
            summary["overall_status"] = overall_status
        if conformance_status:
            summary["conformance_status"] = conformance_status
        if tspp_status:
            summary["tspp_status"] = tspp_status
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
