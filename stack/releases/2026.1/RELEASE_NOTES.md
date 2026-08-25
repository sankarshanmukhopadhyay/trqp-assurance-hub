---
layout: default
title: "TRQP Stack 2026.1 — Coconut release notes"
nav_exclude: true
---

# TRQP Stack 2026.1 — Coconut

TRQP Stack 2026.1 — **Coconut** (*Cocos nucifera*) is the first formal coordinated adopter-facing release of the TRQP Operational Trust Stack.

A coordinated Stack release is a **compatibility and assurance contract**. It does not replace independent component versioning and does not create a fourth implementation product. Instead, it identifies an exact tuple of independently governed releases that has been exercised together and preserves the evidence supporting that interoperability claim.

## Validated release tuple

| Layer | Release | Role |
|---|---:|---|
| TRQP-TSPP | v0.15.0 | Security/privacy posture and control evidence |
| TRQP Conformance Suite | v1.8.0 | Protocol conformance and deterministic replay evidence |
| TRQP Assurance Hub | v1.11.0 | Evidence aggregation and assurance publication |
| TSMM | v0.24.0 | Semantic authority |
| TIS | v0.14.1 | Schema and portfolio authority |

## Why this matters to adopters

Before coordinated Stack releases, an adopter could understand each repository independently but still needed to determine which versions should be used together. Stack 2026.1 removes that ambiguity.

An adopter can now select one validated tuple, follow the canonical workflow, reproduce the three-repository execution, and obtain an evidence chain that identifies component provenance, semantic/schema authority, run and target identity, CTS replay policy, combined assurance, and invalidation conditions.

## Release assurance

The decisive `stack-release-eligibility` workflow passed on the merged release baseline. The release process validates:

- immutable component tag and commit resolution;
- clean-room bootstrap;
- TSPP evidence validity;
- CTS conformance evidence;
- deterministic CTS replay under a declared comparison policy;
- cross-repository run and target correlation;
- combined-assurance composition;
- provenance and artifact integrity;
- fail-closed negative cases;
- whole-stack semantic replay equivalence; and
- the executable adopter walkthrough.

The machine-readable release record is `stack/releases/2026.1/manifest.json`.

## Authority boundaries

The coordinated release does not transfer authority. TRQP-TSPP remains authoritative for its controls, posture computation, and producer evidence. The TRQP Conformance Suite remains authoritative for conformance execution and replay-comparison semantics. The Assurance Hub owns compatibility tuple declaration, integration verification, combined assurance, and coordinated release evidence. TSMM and TIS retain their declared semantic and schema/portfolio authority.

## Documentation synchronization

The release process synchronized the adopter-facing entry points in all three repositories so the same tuple, purpose, and authority boundaries are visible from TSPP, CTS, and Assurance Hub documentation.

## Future cadence

Coordinated Stack releases are expected approximately monthly when meaningful capability has accumulated, or earlier when a capability, compatibility, security, evidence, or authority change makes a new validated tuple materially useful or necessary. Component releases continue independently and do not automatically trigger a Stack release.

Each coordinated release receives a randomly selected codename from the Wikipedia list of Indian state trees. The codename is human-facing identity only; the stable machine identity for this release is `trqp-stack-2026.1`.
