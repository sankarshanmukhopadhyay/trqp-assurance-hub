---
owner: maintainers
last_reviewed: 2026-07-03
tier: 1
---

# Hub ↔ CTS ↔ TSPP crosswalk

This table maps each Hub control ID (from `tools/control-catalog.json`) to the
Conformance Suite (CTS) test IDs that exercise it and the TSPP requirement IDs
that assert it. Use this to understand which toolchain checks cover which
governance control.

**Source of truth for control semantics:** `tools/control-catalog.json`
**Source of truth for CTS test definitions:** `tests/core_tests.yaml` (trqp-conformance-suite)
**Source of truth for TSPP requirements:** `docs/requirements.md` (TRQP-TSPP)

## Control → test mapping

| Hub Control ID | Control title | CTS test IDs | TSPP requirement IDs | Notes |
|---|---|---|---|---|
| `TRQP-CTRL-01` | Policy and governance publication | TC-HTTP-001, TC-HTTP-002 | TSPP-META-01, TSPP-META-02 | Baseline protocol publication and metadata conformance |
| `TRQP-CTRL-02` | Evidence bundle integrity | TC-AUTHZ-001, TC-RECOG-001, TC-FRESH-001, TC-FRESH-002 | TSPP-FRESH-01, TSPP-FRESH-02, TSPP-FRESH-03, TSPP-AL2-01, TSPP-AL2-02 | Response freshness and signing integrity; AL2+ for signature verification |
| `TRQP-CTRL-03` | Directory status lifecycle and revocation | TC-RECOG-001, TC-HTTP-002 | TSPP-RECOG-01, TSPP-RECOG-02, TSPP-FRESH-03 | Recognition statement shape, freshness, and lifecycle semantics |
| `TRQP-CTRL-04` | Registry operator identity assurance | TC-SEC-001, TC-SEC-002 | TSPP-AL3-01, TSPP-AL3-02, TSPP-AL3-03, TSPP-AL4-02 | Auth posture, signing, independent assessment, key protection |
| `TRQP-CTRL-07` | Incident response and disclosure | TC-ERR-001, TC-ERR-010 | TSPP-ERR-01, TSPP-ENUM-01, TSPP-AL4-03, TSPP-AL4-05 | Uniform error surface, enumeration resistance, monitoring, audit log |

## Test → control reverse index

| CTS test ID | Test name | Hub control(s) | TSPP requirement(s) |
|---|---|---|---|
| TC-HTTP-001 | Accept JSON Content-Type | TRQP-CTRL-01 | TSPP-META-01 |
| TC-HTTP-002 | Success response is JSON | TRQP-CTRL-01, TRQP-CTRL-03 | TSPP-META-01, TSPP-RECOG-01 |
| TC-ERR-001 | Invalid schema yields structured error | TRQP-CTRL-07 | TSPP-ERR-01 |
| TC-AUTHZ-001 | Authorization decision present | TRQP-CTRL-02 | TSPP-FRESH-01 |
| TC-RECOG-001 | Recognition statement present | TRQP-CTRL-02, TRQP-CTRL-03 | TSPP-RECOG-01, TSPP-FRESH-03 |
| TC-OPS-001 | Correlation ID echo | TRQP-CTRL-07 | TSPP-ERR-01 |
| TC-ERR-010 | Error includes code fields | TRQP-CTRL-07 | TSPP-ERR-01 |
| TC-SEC-001 | High-Assurance requires auth | TRQP-CTRL-04 | TSPP-AL3-01 |
| TC-SEC-002 | Replay detection rejects reused nonce | TRQP-CTRL-04 | TSPP-AL2-01 |
| TC-CTX-001 | Context timestamp evaluated as-of time | TRQP-CTRL-02 | TSPP-CTX-01 |
| TC-FRESH-001 | Authorization freshness fields present | TRQP-CTRL-02 | TSPP-FRESH-01, TSPP-FRESH-02 |
| TC-FRESH-002 | Recognition freshness fields present | TRQP-CTRL-02, TRQP-CTRL-03 | TSPP-FRESH-03 |

## TSPP requirement → control reverse index

| TSPP requirement ID | Summary | Hub control(s) | CTS test IDs |
|---|---|---|---|
| TSPP-META-01 | Metadata published and schema-valid | TRQP-CTRL-01 | TC-HTTP-001, TC-HTTP-002 |
| TSPP-META-02 | Metadata schema conformance | TRQP-CTRL-01 | TC-HTTP-001 |
| TSPP-CTX-01 | Explicit context allowlist declared | TRQP-CTRL-02 | TC-CTX-001 |
| TSPP-CTX-02 | Unknown context key handling | TRQP-CTRL-02 | TC-CTX-001 |
| TSPP-FRESH-01 | Authorization freshness fields | TRQP-CTRL-02 | TC-AUTHZ-001, TC-FRESH-001 |
| TSPP-FRESH-02 | RFC 3339 timestamp format | TRQP-CTRL-02 | TC-FRESH-001 |
| TSPP-FRESH-03 | Recognition freshness fields | TRQP-CTRL-02, TRQP-CTRL-03 | TC-RECOG-001, TC-FRESH-002 |
| TSPP-ERR-01 | Uniform error surface | TRQP-CTRL-07 | TC-ERR-001, TC-ERR-010 |
| TSPP-ENUM-01 | Enumeration side-channel mitigation | TRQP-CTRL-07 | TC-ERR-001 |
| TSPP-RL-01 | Rate limit headers on 429 | TRQP-CTRL-07 | — (TSPP-only; no CTS coverage) |
| TSPP-AL2-01 | Signed envelope shape at AL2 | TRQP-CTRL-02 | TC-SEC-002 |
| TSPP-AL2-02 | Signature verifiable via declared JWKS | TRQP-CTRL-02 | — (TSPP-only) |
| TSPP-AL3-01 | Default signing declared in metadata | TRQP-CTRL-04 | TC-SEC-001 |
| TSPP-AL3-02 | Signed envelope includes meta fields | TRQP-CTRL-02 | TC-AUTHZ-001 |
| TSPP-AL3-03 | Independent assessment URI resolves | TRQP-CTRL-04 | — (TSPP-only) |
| TSPP-AL3-04 | Change control URI resolves | TRQP-CTRL-04 | — (TSPP-only) |
| TSPP-AL4-02 | Key protection declared | TRQP-CTRL-04 | — (TSPP-only) |
| TSPP-AL4-03 | Monitoring declared with retention | TRQP-CTRL-07 | — (TSPP-only) |
| TSPP-AL4-04 | Policy and rollback URIs resolve | TRQP-CTRL-04 | — (TSPP-only) |
| TSPP-AL4-05 | Audit log declared | TRQP-CTRL-07 | — (TSPP-only) |
| TSPP-BRIDGE-01 | Bridge semantic equivalence | TRQP-CTRL-02 | TC-AUTHZ-001, TC-CTX-001 |
| TSPP-RECOG-01–05 | Recognition security and freshness | TRQP-CTRL-03 | TC-RECOG-001, TC-HTTP-002 |

## Coverage gaps

Controls with no CTS test coverage (TSPP-only):

- `TSPP-RL-01` — rate limiting (observable only under burst load; CTS skips if 429 not triggered)
- `TSPP-AL2-02` — JWKS signature verification (requires live key material)
- `TSPP-AL3-03`, `TSPP-AL3-04` — URI resolution checks (require live endpoints)
- `TSPP-AL4-02` through `TSPP-AL4-05` — AL4 governance posture (require metadata declarations beyond protocol shape)

These gaps are expected. CTS covers protocol surface; TSPP covers deployment posture.
A combined assurance run is required to achieve full control coverage.

## CI validation

This crosswalk is validated by `tools/validate_crosswalk.py` in CI:
- Every control ID in `tools/control-catalog.json` must appear in this document.
- Every CTS test ID referenced must exist in `tests/core_tests.yaml` (trqp-conformance-suite).
- Every TSPP requirement ID referenced must exist in `controls/control-registry.json` (TRQP-TSPP).

_Last updated: 2026-03-19_
