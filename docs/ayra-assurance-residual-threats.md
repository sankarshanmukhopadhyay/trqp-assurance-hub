---
layout: default
title: Ayra assurance residual threats
nav_exclude: true
---

# Ayra assurance residual threats

This note records assurance threats that remain intentionally outside the deterministic Ayra profile-assurance suite. Their absence from automated tests MUST NOT be interpreted as evidence of safety, legitimacy, or conformance.

## Residual threats

| Threat | Current disposition | Evidence needed for stronger assurance |
|---|---|---|
| Governance legitimacy | INDETERMINATE by construction | authoritative governance instrument, delegation chain, jurisdictional/legal review where applicable |
| DID controller compromise | not established by DID resolution alone | key-management and controller-compromise evidence, revocation/recovery state |
| DNS/TLS compromise affecting `did:web` or service discovery | bounded URL and discovery checks only | authenticated historical resolution, certificate/DNS evidence, continuity checks |
| Rebinding after URL safety validation | deterministic fixture coverage only | resolver/network controls that pin validated destinations and re-check redirects |
| Signing mechanism instability in Ayra draft | SHOULD-level bounded observation | finalized upstream signing mechanism and version-bound verification procedure |
| Upstream profile drift after pinned revision | execution blocked as INDETERMINATE until reassessed | refreshed requirement catalogue and proposition mapping bound to new upstream revision |
| Live endpoint nondeterminism, throttling, transient failures | not inferred as trust-negative answers | repeated timestamped observations with bounded retry/freshness policy |
| Semantic deception in otherwise schema-valid payloads | selected negative fixtures only | broader domain-specific semantic invariants and upstream clarification where semantics are underspecified |
| Cross-registry authority conflicts | not resolved by local endpoint evidence | authoritative registry-of-registries or governance recognition evidence |

## Governing boundary

The Stack may establish that a DID is syntactically valid, that a method is supported, that a DID resolved, that a service endpoint was discovered, or that a bounded control proof validated. None of these observations alone establishes that an actor is legally or institutionally entitled to exercise the represented authority.

Unknown profile revisions, unavailable external evidence, stale authority evidence, and unresolved legitimacy therefore remain fail-safe states rather than implicit PASS results.
