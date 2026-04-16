#!/usr/bin/env python3
"""Validate an Operational Stack bundle directory end to end."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def validate_schema(doc: dict, schema_path: Path) -> None:
    from jsonschema import Draft202012Validator  # type: ignore

    schema = load_json(schema_path)
    Draft202012Validator(schema).validate(doc)


def require_equal(label: str, left, right) -> None:
    if left != right:
        raise RuntimeError(f"{label} mismatch: {left!r} != {right!r}")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Validate an Operational Stack bundle directory.")
    p.add_argument("--bundle-dir", required=True)
    args = p.parse_args(argv)

    bundle_dir = Path(args.bundle_dir).resolve()
    manifest_path = bundle_dir / "combined-assurance-manifest.json"
    metadata_path = bundle_dir / "metadata" / "stack-run.json"
    cts_path = bundle_dir / "conformance" / "cts-report.json"
    tspp_path = bundle_dir / "posture" / "tspp-report.json"

    for required in [manifest_path, metadata_path, cts_path, tspp_path]:
        if not required.exists():
            raise RuntimeError(f"Missing required operational stack artifact: {required}")

    manifest = load_json(manifest_path)
    metadata = load_json(metadata_path)
    cts = load_json(cts_path)
    tspp = load_json(tspp_path)

    validate_schema(manifest, ROOT / "schemas" / "combined-assurance-manifest.schema.json")

    build = manifest.get("build", {})
    require_equal("CTS vs TSPP run_id", cts.get("run_id"), tspp.get("run_id"))
    require_equal("CTS vs TSPP target_id", cts.get("target_id"), tspp.get("target_id"))
    require_equal("manifest build.run_id vs CTS report", build.get("run_id"), cts.get("run_id"))
    require_equal("manifest build.run_id vs TSPP report", build.get("run_id"), tspp.get("run_id"))
    require_equal("manifest build.target_id vs CTS report", build.get("target_id"), cts.get("target_id"))
    require_equal("manifest build.target_id vs TSPP report", build.get("target_id"), tspp.get("target_id"))
    require_equal("metadata run_id vs manifest", metadata.get("run_id"), build.get("run_id"))
    require_equal("metadata target_id vs manifest", metadata.get("target_id"), build.get("target_id"))
    require_equal("metadata build_id vs manifest", metadata.get("build_id"), build.get("build_id"))
    require_equal("metadata target vs manifest", metadata.get("target"), build.get("target"))

    for artifact in manifest.get("artifacts", []):
        rel = artifact["path"]
        artifact_path = bundle_dir / rel
        if not artifact_path.exists():
            raise RuntimeError(f"Manifest references missing artifact: {rel}")
        if "sha256" in artifact:
            actual = sha256_file(artifact_path)
            require_equal(f"sha256 for {rel}", artifact["sha256"], actual)

    if metadata.get("artifacts", {}).get("cts_report") != "conformance/cts-report.json":
        raise RuntimeError("metadata.artifacts.cts_report must reference conformance/cts-report.json")
    if metadata.get("artifacts", {}).get("tspp_report") != "posture/tspp-report.json":
        raise RuntimeError("metadata.artifacts.tspp_report must reference posture/tspp-report.json")

    print(f"Operational Stack bundle validated successfully: {bundle_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1)
