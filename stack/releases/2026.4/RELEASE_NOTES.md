---
layout: default
title: "TRQP Stack 2026.4 — Lotus"
nav_exclude: true
---

# TRQP Stack 2026.4 — Lotus

TRQP Stack 2026.4 publishes state-bound compositional assurance as a coordinated Stack capability.

## Coordinated tuple

- TRQP Conformance Suite `v1.11.1` at `0738c3cf86fddb99d761ed21d63d870eefdc5f76`.
- TRQP-TSPP `v0.18.1` at `c1735099cf4bca98c3b4e4f67c151e5508687851`.
- TRQP Assurance Hub `v1.14.0` at `fd2296226dacbe3d5009179803fde23eead1cc6f`.
- TSMM authority version `0.24.0` at `8ddfd52c876faf368241bc11101681fb1fe49398`.
- TIS authority version `0.15.0` at `edda0e87ced40797d22e3df542099871c57fcb59`.

## What changed

The Stack now binds CTS conformance/replay evidence and TSPP security/privacy posture evidence to the same verified deployed-state identity before the Hub composes them. A shared logical `target_id` is no longer sufficient for the state-bound path: the producers must agree on the verified SHA-256 target-state identity.

The coordinated path fails closed when state evidence is missing, unverifiable, partial, or mismatched. CTS replay evidence is also checked against the same target state so replay cannot silently move to a different deployment.

This capability is protocol-version neutral and does not depend on downstream TRQP v3 candidate work.

## Assurance evidence

Publication is bound to merged-main `stack-release-eligibility` run `36952543474` at Hub commit `0e0037aefa2f51594e95fdddfb25b8047c5e19ac`.

The retained candidate evidence artifact is `trqp-stack-release-candidate-36952543474` with digest `sha256:66e368934bf8cf8cb622d7090a07f582cb6d7cb3e756c6b24f5130e1742c42e0`.

The decisive workflow bootstrapped the immutable component tuple, generated CTS and TSPP evidence independently, verified shared target-state identity, verified CTS replay-state continuity, composed state-bound assurance twice, proved semantic replay equivalence, exercised fail-closed state mismatch behavior, and ran the Stack-specific test suite.

The executable reference target used by the decisive workflow is intentionally non-conformant in CTS. The release gate therefore explicitly requires CTS=fail, TSPP=pass, and combined outcome=fail for that negative fixture. A separate positive state-pair test proves that matching verified state evidence is accepted. The release does not reinterpret a failed target as passing assurance.

## Governance and authority

This coordinated release does not transfer authority. TRQP upstream remains authoritative for protocol semantics; CTS for executable conformance and replay evidence; TSPP for security/privacy posture and reassessment evidence; TSMM for canonical trust-system semantics; TIS for portable contracts; and the Hub for cross-producer correlation, composition, and coordinated release declaration.

TRQP Stack 2026.4 does not depend on `draft/next-trqp` or claim upstream TRQP v3 semantics.

## Release judgment

Human release judgment `ACCEPT` was recorded on Hub issue #104 as comment `5944065290` after the hardened merged-main release evidence was available. That judgment authorizes publication of this exact immutable tuple only.
