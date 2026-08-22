#!/usr/bin/env python3
"""Validation helpers for CTS v1.8+ replay-determinism evidence."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


class DeterminismEvidenceError(ValueError):
    """Raised when CTS determinism evidence is missing, malformed, or invalid."""


def load_and_validate(path: str | Path) -> Dict[str, Any]:
    report_path = Path(path)
    if not report_path.exists():
        raise DeterminismEvidenceError(f"CTS determinism report not found: {report_path}")

    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise DeterminismEvidenceError(f"CTS determinism report is not valid JSON: {exc}") from exc

    required = ["report_version", "policy", "source", "replay", "deterministic", "summary", "differences"]
    missing = [key for key in required if key not in report]
    if missing:
        raise DeterminismEvidenceError(
            "CTS determinism report missing required fields: " + ", ".join(missing)
        )

    policy = report.get("policy") or {}
    for key in ("id", "version", "sha256"):
        if not policy.get(key):
            raise DeterminismEvidenceError(f"CTS determinism policy missing {key}")

    source = report.get("source") or {}
    replay = report.get("replay") or {}
    if not source.get("semantic_sha256") or not replay.get("semantic_sha256"):
        raise DeterminismEvidenceError("CTS determinism report must carry source and replay semantic hashes")

    summary = report.get("summary") or {}
    prohibited = int(summary.get("prohibited_difference_count", 0) or 0)
    if report.get("deterministic") is not True:
        raise DeterminismEvidenceError("CTS replay determinism failed")
    if prohibited != 0:
        raise DeterminismEvidenceError(
            f"CTS replay determinism contains {prohibited} prohibited difference(s)"
        )

    return report


def assurance_projection(report: Dict[str, Any]) -> Dict[str, Any]:
    """Return the stable subset preserved in the Combined Assurance Manifest."""
    return {
        "status": "pass",
        "report_version": report["report_version"],
        "policy": {
            "id": report["policy"]["id"],
            "version": report["policy"]["version"],
            "sha256": report["policy"]["sha256"],
        },
        "source_semantic_sha256": report["source"]["semantic_sha256"],
        "replay_semantic_sha256": report["replay"]["semantic_sha256"],
        "permitted_difference_count": int(
            (report.get("summary") or {}).get("permitted_difference_count", 0) or 0
        ),
        "prohibited_difference_count": 0,
    }
