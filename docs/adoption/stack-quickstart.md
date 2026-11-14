---
layout: default
title: "TRQP Stack quickstart"
nav_exclude: true
---

# TRQP Stack quickstart

Use this page when you want the validated TRQP components to behave as one adopter workflow rather than selecting repository versions independently.

## Current validated release

**TRQP Stack 2026.4 — Lotus** is the current published coordinated release. Its immutable record is under `stack/releases/2026.4/`. The [Banyan walkthrough](stack-2026.3-walkthrough.md) remains useful as a historical profile-aware example.

The validated tuple is:

| Layer | Release | Exact commit |
|---|---:|---|
| TRQP-TSPP | v0.18.1 | `c1735099cf4bca98c3b4e4f67c151e5508687851` |
| TRQP Conformance Suite | v1.11.1 | `0738c3cf86fddb99d761ed21d63d870eefdc5f76` |
| TRQP Assurance Hub | v1.14.0 | `fd2296226dacbe3d5009179803fde23eead1cc6f` |
| TSMM | 0.24.0 | `8ddfd52c876faf368241bc11101681fb1fe49398` |
| TIS | 0.15.0 | `edda0e87ced40797d22e3df542099871c57fcb59` |

## 1. Understand the release contract

A coordinated Stack release means the declared component versions have been exercised together under the Stack eligibility gate. It removes adopter-side version selection while preserving the independent authority and version lifecycle of each repository.

For future releases, the next proposed tuple is first recorded in `stack/releases/candidate/manifest.json`. A candidate is not a release.

## 2. Validate the candidate or current tuple

For release engineering against the current candidate manifest:

```bash
python tools/stack_validate.py --check-remote
```

This fails if the candidate manifest is incomplete, a component ref is mutable, or a declared tag does not resolve to the pinned commit.

For adoption of Stack 2026.4, inspect `stack/releases/2026.4/manifest.json` and `stack/releases/2026.4/publication.json` for the immutable component tags, commits, authority versions, decisive workflow run, human release judgment, evidence artifact digest, and publication metadata.

## 3. Bootstrap a clean workspace

```bash
python tools/stack_bootstrap.py --clean
```

The bootstrap command clones only the tagged component versions declared by the release engineering manifest and verifies their commits. No adopter-side compatibility choice is required.

The same clean-room property was a mandatory eligibility condition for Stack 2026.4. **Note:** The commands shown above run the candidate release-engineering manifest by default; use the immutable 2026.4 release manifest and attached release evidence when evaluating the published tuple.

## 4. Execute the declared components

```bash
python tools/stack_evaluate.py
```

This invokes each component's `assurance-check` surface and writes a run record to `artifacts/stack-candidate/run-manifest.json` during release engineering.

The coordinated Stack workflow correlates TSPP and CTS evidence using the same run and target identity before the Hub produces combined assurance. In Stack 2026.4, state-bound composition additionally requires shared verified snapshot identity; Banyan's profile-aware composition consumes producer-owned CTS and TSPP evidence while preserving their authority boundaries.

## 5. Verify release eligibility

```bash
make stack-release-check
```

The local gate validates the Hub, candidate tuple, remote tag provenance, and fail-closed release-readiness tests. The `stack-release-eligibility` GitHub Actions workflow additionally performs clean bootstrap, tagged component execution, CTS deterministic replay, profile-aware producer/consumer validation, combined assurance composition, whole-stack semantic replay comparison, negative cases, and candidate evidence publication.

Stack 2026.4 passed the decisive eligibility workflow on merged `main`, received the required visible human `ACCEPT` judgment, and then passed a fresh post-acceptance merged-main eligibility run before automated publication.

## Scope of target-state evidence

Matching producer digests proves correlation of the supplied snapshot, not that the snapshot accurately describes the live deployment. A relying party must establish deployment provenance, freshness, authority, and post-publication status through applicable independent evidence. The current release does not assert certification.

## Evidence a coordinated release provides

A coordinated release is publishable only when CI demonstrates immutable tuple resolution, clean bootstrap, TSPP evidence validity, CTS conformance and deterministic replay, shared run/target correlation, profile-aware evidence composition, combined assurance, provenance/integrity, negative-case rejection, whole-stack semantic replay equivalence, and an executable walkthrough.

The release record preserves the exact workflow run, evidence artifact digest, human release judgment, and publication metadata so the claim can be audited later.

## Authority boundary

The Assurance Hub owns coordinated release declaration and compatibility evidence. TSPP remains authoritative for its controls and posture semantics. CTS remains authoritative for protocol conformance and replay-comparison semantics. Ecosystem profile authorities remain authoritative for profile normative strength. TSMM and TIS retain their declared semantic/schema authority.

A Stack release therefore records **tested interoperability and assurance evidence**; it does not transfer normative authority or infer governance legitimacy from API correctness.

## Release cadence

Coordinated Stack releases are capability-driven and are published when meaningful capability has accumulated and the complete tuple passes the release gate. Component releases continue independently and do not automatically trigger a Stack release.
