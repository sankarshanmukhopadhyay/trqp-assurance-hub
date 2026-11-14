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
    import re
    for label, entry in (("source", source), ("replay", replay)):
        if not entry.get("run_id"):
            raise DeterminismEvidenceError(f"CTS replay {label} run_id missing")
        if not re.fullmatch(r"[0-9a-f]{64}", str(entry.get("semantic_sha256", ""))):
            raise DeterminismEvidenceError(f"CTS replay {label} semantic hash invalid")
    if source["run_id"] == replay["run_id"]:
        raise DeterminismEvidenceError("CTS replay must identify two distinct executions")

    summary = report.get("summary") or {}
    prohibited = int(summary.get("prohibited_difference_count", 0) or 0)
    differences = report.get("differences")
    if not isinstance(differences, list):
        raise DeterminismEvidenceError("CTS replay differences must be an array")
    permitted = sum(1 for item in differences if isinstance(item, dict) and item.get("permitted") is True)
    observed_prohibited = len(differences) - permitted
    try:
        count = int(summary.get("difference_count", 0))
        permitted_count = int(summary.get("permitted_difference_count", 0))
    except (ValueError, TypeError):
        raise DeterminismEvidenceError("CTS replay difference counts invalid")
    if count != len(differences) or prohibited != observed_prohibited or permitted_count != permitted:
        raise DeterminismEvidenceError("CTS replay summary disagrees with comparison differences")
    if source["semantic_sha256"] != replay["semantic_sha256"] and prohibited == 0:
        raise DeterminismEvidenceError("CTS replay semantic hashes differ without prohibited differences")
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
