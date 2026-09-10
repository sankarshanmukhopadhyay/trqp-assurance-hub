---
layout: default
title: "TRQP Stack 2026.3 — Banyan"
nav_exclude: true
---

# TRQP Stack 2026.3 — Banyan

TRQP Stack 2026.3 publishes profile-aware compositional assurance as a coordinated Stack capability.

## Coordinated tuple

- TRQP Conformance Suite `v1.10.0` at `1e5dc2646c75390444d9ae86f3d6136d7c033463`.
- TRQP-TSPP `v0.17.0` at `328e19c71f407ebdb2bc92828a3ae037a843f285`.
- TRQP Assurance Hub `v1.13.0` at `5346b83545bf042360eb32691dfc907135d233dd`.
- TSMM authority version `0.24.0` at `8ddfd52c876faf368241bc11101681fb1fe49398`.
- TIS authority version `0.15.0` at `edda0e87ced40797d22e3df542099871c57fcb59`.

## What changed

The Stack can now compose ecosystem-profile conclusions from producer-owned CTS core-conformance evidence and TSPP security/privacy posture evidence while preserving source authority. A Hub-local positive conclusion cannot override producer FAIL, INDETERMINATE, stale, missing, or otherwise non-current evidence.

Ayra is the first profile exercised through this contract. Ayra profile semantics remain authoritative upstream; the Stack consumes the pinned profile requirements and does not redefine them. Response signing remains a profile SHOULD, while TSPP owns the corresponding signing-posture evidence.

The release also carries forward the Stack 2026.2 lifecycle guarantees for invalidation, reassessment, authority drift, supersession, and post-change recomposition.

## Assurance evidence

Publication is bound to merged-main `stack-release-eligibility` run `34504670330` at Hub commit `0cf5c5ec3b82918faeb9905eec9a4e83f7f3965f`.

The retained candidate evidence artifact is `trqp-stack-release-candidate-34504670330` with digest `sha256:35ea47a0d3bb8c07368f58c9bd1ea6667d3a515bc6adb29b2646f0c8522513ca`.

The decisive workflow proved immutable tuple resolution, clean-room bootstrap, tagged component assurance surfaces, frozen profile-aware consumer behavior, CTS deterministic replay, TSPP evidence generation, repeated cross-source composition, whole-stack semantic replay equivalence, and fail-closed negative/profile cases.

## Governance and authority

This coordinated release does not transfer authority. TRQP upstream remains authoritative for protocol semantics; CTS for executable conformance/replay evidence; TSPP for security/privacy posture evidence; ecosystem profile authorities for their profile requirements; TSMM for canonical trust-system semantics; TIS for portable contracts; and the Hub for composition and coordinated release declaration.

Governance legitimacy remains dependent on applicable external evidence and is not inferred from API correctness alone.

## Release judgment

Human release judgment `ACCEPT` was recorded on Hub issue #86 as comment `5622360301` after the release-decisive evidence was available. That judgment authorizes publication of this exact immutable tuple only.
