---
layout: default
title: Ayra TRQP v2 and candidate-v3 compatibility
nav_exclude: true
---

# Ayra TRQP v2 and candidate-v3 compatibility

This document explains the machine-readable matrix in `profiles/ayra/v3-compatibility.yaml`.

## Authority boundary

The current assurance target remains the Ayra TRQP Profile `0.6.0-draft`, bound to TRQP `2.0` and Ayra source revision `ec7768572592b50ba3f4102c026c2449148b5e11`.

The comparison target is the downstream experimental candidate TRQP v3 specification on `sankarshanmukhopadhyay/tswg-trust-registry-protocol`, branch `draft/next-trqp`, revision `539fccb624fc6328aa3bece4831b3291ee78f6be`.

Candidate v3 is not upstream authority and does not supersede current Ayra/TRQP v2 conformance.

## Main compatibility findings

The current Ayra profile remains independently assessable against TRQP v2. Migration readiness is a separate question.

- The strongest continuity is the invariant that transport or processing failures must not be converted into negative trust decisions.
- Error representation is a visible migration point: Ayra currently requires RFC 7807 Problem Details while candidate v3 points materially revised HTTP error responses toward RFC 9457.
- Candidate v3 intentionally separates semantic principals, verification material, authority, endpoint identity and transport state. Ayra's DID-only `_id` constraints therefore require explicit reconciliation rather than being assumed to map transparently.
- Ayra's extension endpoints, 501 behaviour, DID-document service discovery and `authority_id` governance discovery are profile-owned/narrowing semantics unless and until an authoritative v3 binding adopts equivalent requirements.
- TLS, rate limiting and exact endpoint paths remain binding concerns, while candidate v3 intentionally keeps core semantics transport-independent.
- Response signing remains unresolved in both the current Ayra profile and the candidate-v3 comparison surface; it must not be promoted into a universal mandatory requirement by this analysis.

## Reassessment rule

The matrix is valid only for its exact source revisions. A change to either the Ayra profile revision or the candidate-v3 revision marks the comparison `REASSESSMENT_REQUIRED`.

This does not invalidate historical assurance results produced against the previous Ayra profile revision. It invalidates only the claim that the old compatibility analysis remains current.

## Interpretation

Compatibility classifications are analytical signals, not normative decisions:

- `unchanged` indicates no material semantic conflict identified at the pinned revisions;
- `narrowed_by_profile` or `extended_by_profile` means Ayra adds a profile-owned constraint beyond candidate core semantics;
- `changed_in_v3_draft` identifies a concrete candidate migration pressure;
- `conflict_candidate` marks an area requiring explicit design/authority reconciliation;
- `evidence_gap` means the candidate or upstream authority has not defined enough to make a reliable mapping.

No classification authorizes automatic migration, changes the current Ayra profile, or promotes the downstream v3 candidate to normative status.
