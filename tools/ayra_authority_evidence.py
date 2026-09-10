#!/usr/bin/env python3
"""Bounded Ayra authority/discovery assurance over deterministic observations."""
from __future__ import annotations

from ipaddress import ip_address
from urllib.parse import urlparse

from tools.profile_assurance_model import evaluate


def did_method(did: str) -> str | None:
    if not isinstance(did, str) or not did.startswith("did:"):
        return None
    parts = did.split(":", 2)
    return parts[1] if len(parts) == 3 and parts[1] else None


def is_safe_https_url(value: str) -> bool:
    try:
        parsed = urlparse(value)
    except Exception:
        return False
    if parsed.scheme != "https" or not parsed.hostname:
        return False
    host = parsed.hostname.lower()
    if host in {"localhost", "localhost.localdomain"}:
        return False
    try:
        addr = ip_address(host)
        return not (addr.is_private or addr.is_loopback or addr.is_link_local or addr.is_multicast or addr.is_reserved)
    except ValueError:
        return True


def assess_authority(observation: dict) -> dict:
    registry_did = observation.get("registry_did")
    method = did_method(registry_did)
    supported = set(observation.get("supported_did_methods", []))
    did_resolved = observation.get("did_resolved")
    service_endpoint = observation.get("trqp_service_endpoint")
    expected_endpoint = observation.get("expected_trqp_endpoint")
    governance = observation.get("governance_framework")
    authority_id = observation.get("authority_id")

    syntax_ok = method is not None
    method_ok = syntax_ok and (not supported or method in supported)
    resolution_result = evaluate(strength="MUST", applicability="APPLICABLE", implemented=did_resolved is not None, evidence_present=did_resolved is not None, satisfied=did_resolved)

    endpoint_evidence = service_endpoint is not None
    endpoint_ok = bool(endpoint_evidence and is_safe_https_url(service_endpoint) and (expected_endpoint is None or service_endpoint == expected_endpoint))
    endpoint_result = evaluate(strength="SHOULD", applicability="APPLICABLE", implemented=endpoint_evidence, evidence_present=endpoint_evidence, satisfied=endpoint_ok if endpoint_evidence else None)

    governance_present = isinstance(governance, dict)
    governance_matches = bool(governance_present and authority_id and governance.get("authority_id") == authority_id and governance.get("discoverable") is True)
    governance_result = evaluate(strength="MUST", applicability="APPLICABLE", implemented=governance_present, evidence_present=governance_present, satisfied=governance_matches if governance_present else None)

    return {
        "identifier_syntax": "PASS" if syntax_ok else "FAIL",
        "did_method": "PASS" if method_ok else ("FAIL" if syntax_ok else "INDETERMINATE"),
        "resolution": resolution_result,
        "service_discovery": endpoint_result,
        "governance_discovery": governance_result,
        "control_evidence": "INDETERMINATE",
        "governance_legitimacy": "INDETERMINATE",
        "observed_method": method,
    }
