# DeDi Experimental Profile (Decentralized Directory Protocol)

**Status:** Experimental (non-normative)  
**Upstream protocol:** https://github.com/LF-Decentralized-Trust-labs/decentralized-directory-protocol  
**Snapshot date:** 2026-03-03

## What this profile is

This profile provides a **provisional semantic mapping** from DeDi directory artifacts into the TRQP Assurance Hub's directory assurance model (controls, evidence patterns, lifecycle & revocation semantics).

This profile:
- **DOES NOT** modify or extend the upstream DeDi protocol.
- **DOES** define how DeDi implementations **MAY** be evaluated using Hub controls and evidence bundles.

## DeDi artifacts covered

| DeDi artifact | Purpose | Hub alignment |
|---|---|---|
| `public_key` | Discover active keys and key rotation metadata | Input to signature validation + key management evidence |
| `revoke` | Publish negative list / revocations | Revocation semantics + status feed alignment |
| `membership` | Represent affiliation / membership assertions | Directory entry semantics (subject + role + status) |
| `Beckn_subscriber` | Subscriber record (ecosystem-specific record type) | Treated as a directory record type under the same publication & integrity expectations |

## How to use this profile

1. Publish DeDi artifacts following the upstream protocol.
2. Produce a Hub-style **evidence bundle** that:
   - includes the DeDi artifacts (or references with checksums),
   - includes operator declarations and governance policy,
   - includes any applicable lifecycle assertions and incident/rotation proofs for higher assurance targets.
3. Validate structure using the TRQP Conformance Suite's DeDi experimental checks (schema validation + basic wiring checks).

## Compatibility and stability

- The Hub core semantics (AL definitions, evidence bundle patterns) remain canonical.
- Profile-specific checks and mappings may evolve as the upstream DeDi protocol and ecosystem conventions mature.

## Mapping matrix

See `docs/reference/dedi-mapping-matrix.md`
- Machine-readable matrix: `docs/reference/dedi-mapping-matrix.yaml` for the one-page spine linking DeDi artifacts to Hub controls, CTS checks, and expected evidence.

