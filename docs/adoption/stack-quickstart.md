---
layout: default
title: "TRQP Stack quickstart"
nav_exclude: true
---

# TRQP Stack quickstart

Use this page when you want the validated TRQP components to behave as one adopter workflow rather than selecting repository versions independently.

## 1. Inspect the candidate tuple

The unreleased tuple is declared in `stack/releases/candidate/manifest.json`. It identifies the exact TSPP, Conformance Suite and Assurance Hub tags and commits, plus TSMM/TIS authority versions. A candidate is not a release.

```bash
python tools/stack_validate.py --check-remote
```

This fails if the manifest is incomplete, a component ref is mutable, or a declared tag does not resolve to the pinned commit.

## 2. Bootstrap a clean workspace

```bash
python tools/stack_bootstrap.py --clean
```

The command clones only the tagged component versions in the manifest and verifies their commits. No adopter-side compatibility choice is required.

## 3. Execute the declared components

```bash
python tools/stack_evaluate.py
```

This invokes each component's `assurance-check` surface and writes a candidate run record to `artifacts/stack-candidate/run-manifest.json`.

## 4. Run the release-readiness gate

```bash
make stack-release-check
```

The local gate validates the Hub, the candidate tuple, remote tag provenance, and fail-closed release-readiness tests. GitHub Actions additionally runs the existing cross-repository combined-assurance flow against the same immutable TSPP/CTS releases.

## Evidence expected before release

A coordinated release is eligible only when CI demonstrates: immutable tuple resolution, clean bootstrap, TSPP evidence validity, CTS conformance and deterministic replay, shared run/target correlation, combined assurance, provenance/integrity, negative-case rejection, and an executable walkthrough.

## Authority boundary

The Assurance Hub owns coordinated release declaration and compatibility evidence. TSPP remains authoritative for its controls and posture semantics. CTS remains authoritative for protocol conformance and replay-comparison semantics. TSMM/TIS retain their declared semantic/schema authority. A stack release therefore records tested interoperability; it does not transfer normative authority.

## Release prohibition

Do not change the candidate status to `validated`, create a Stack tag, or publish a coordinated release until the release-readiness workflow is green and the maintainer deliberately performs the release step.
