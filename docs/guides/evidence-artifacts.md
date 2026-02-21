# Evidence artifacts and expectations

This guide clarifies what evidence artifacts are expected at different assurance levels (AL1–AL4),
without turning the README into a policy wall.

The goal is pragmatic: enable implementers and auditors to agree on **what gets produced**,
**what it should contain**, and **how it’s referenced** in combined assurance.

## Scope and non-goals

- This document describes **artifact expectations**, not full normative security requirements.
- AL3 and AL4 are described as **draft expectations** (reserved) until TRQP-TSPP defines them normatively.

## Core artifact types

### Conformance evidence bundle
Produced by the TRQP Conformance Suite runner/profile. Should include:
- tool + version + profile identifier
- target identifier (endpoint base URL or registry identifier)
- requirement IDs → test results (pass/fail/skip) + rationale
- timestamps + run identifier
- optional logs and diagnostics (redacted where needed)

### TSPP posture evidence bundle
Produced by TRQP-TSPP for a given AL profile. Should include:
- tool + version + AL profile (AL1/AL2/etc.)
- target identifier + environment metadata
- control IDs → checks → outcomes + rationale
- timestamps + run identifier
- optional security-relevant signals (rate limiting presence, header policies, signing expectations, etc.)

### Combined Assurance Manifest
A small JSON document that binds multiple evidence bundles to the same build/run identity:
- build_id, target, timestamp
- tool runs (name/version/profile/run_id)
- pointers to evidence artifacts (paths/URIs/checksums if available)

Schema:
- `schemas/combined-assurance-manifest.schema.json`

Example:
- `examples/combined-assurance-manifest.example.json`

## Artifact expectations matrix (AL1–AL4)

Legend:
- **Required**: MUST be produced for a compliant run at this level
- **Recommended**: SHOULD be produced; acceptable to omit with rationale
- **Optional**: MAY be produced

| Artifact | AL1 | AL2 | AL3 (draft) | AL4 (draft) | Notes |
|---|---|---|---|---|---|
| Conformance evidence bundle | Required | Required | Required | Required | Baseline for protocol behavior assurance |
| TSPP posture evidence bundle | Required | Required | Required | Required | Baseline for deployment posture assurance |
| Combined Assurance Manifest | Recommended | Required | Required | Required | Required from AL2 upward to prevent provenance ambiguity |
| Version tuple declaration (hub + suite + tspp) | Recommended | Required | Required | Required | Prefer tags; else `main@<sha>` |
| Evidence bundle checksums | Optional | Recommended | Required | Required | Enables integrity verification across hops |
| CI run link or signed provenance attestation | Optional | Recommended | Required | Required | CI URL acceptable early; migrate to attestations later |
| Redaction report (what was removed and why) | Optional | Recommended | Required | Required | Particularly important as evidence gets richer |
| Operator declaration (who ran it, under what authority) | Optional | Optional | Recommended | Required | For high consequence contexts |
| Retention policy pointer | Optional | Recommended | Required | Required | Links to evidence retention and access policy |

## Practical guidance for implementers

- Start with AL1 + AL2 and ensure you can reliably produce:
  - both evidence bundles
  - a Combined Assurance Manifest (at least from AL2)
- Treat AL3/AL4 rows as forward-looking expectations until TSPP publishes normative definitions.

## Change control

If an artifact becomes “Required” at a given AL, that is a compatibility-sensitive change and should be:
- called out in release notes
- reflected in the hub compatibility matrix
