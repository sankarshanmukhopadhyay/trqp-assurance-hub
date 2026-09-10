#!/usr/bin/env python3
"""Bounded Ayra authority/discovery assurance over deterministic observations."""
from __future__ import annotations

from ipaddress import ip_address
from urllib.parse import urlparse


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


def _observed_boolean(value: object) -> str:
    if value is True:
        return "PASS"
    if value is False:
        return "FAIL"
    return "INDETERMINATE"


def assess_authority(observation: dict) -> dict:
    registry_did = observation.get("registry_did")
    method = did_method(registry_did)
    supported = set(observation.get("supported_did_methods", []))
    did_resolved = observation.get("did_resolved")
    service_endpoint = observation.get("trqp_service_endpoint")
    expected_endpoint = observation.get("expected_trqp_endpoint")
    governance = observation.get("governance_framework")
    authority_id = observation.get("authority_id")
    controller_proof = observation.get("controller_proof_valid")
    stale = observation.get("discovery_stale") is True

    syntax_ok = method is not None
    method_result = "INDETERMINATE"
    if syntax_ok:
        method_result = "PASS" if (not supported or method in supported) else "FAIL"

    resolution_result = _observed_boolean(did_resolved)

    if service_endpoint is None:
        endpoint_result = "INDETERMINATE"
    else:
        endpoint_ok = is_safe_https_url(service_endpoint) and (
            expected_endpoint is None or service_endpoint == expected_endpoint
        )
        endpoint_result = "PASS" if endpoint_ok else "FAIL"
    if stale and endpoint_result == "PASS":
        endpoint_result = "INDETERMINATE"

    if not isinstance(governance, dict):
        governance_result = "INDETERMINATE"
    else:
        governance_matches = bool(
            authority_id
            and governance.get("authority_id") == authority_id
            and governance.get("discoverable") is True
        )
        governance_result = "PASS" if governance_matches else "FAIL"
        if governance.get("stale") is True and governance_result == "PASS":
            governance_result = "INDETERMINATE"

    return {
        "identifier_syntax": "PASS" if syntax_ok else "FAIL",
        "did_method": method_result,
        "resolution": resolution_result,
        "service_discovery": endpoint_result,
        "governance_discovery": governance_result,
        "control_evidence": _observed_boolean(controller_proof),
        "governance_legitimacy": "INDETERMINATE",
        "observed_method": method,
    }
