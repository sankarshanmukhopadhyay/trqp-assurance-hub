# Operator declaration (AL2)

**Registry operator:** Example Trust Registry Operator
**Target environment:** https://registry.example.org
**Declaration date:** 2026-01-15
**Assurance level claimed:** AL2

## Scope

This declaration covers the AL2 assurance claim for the Example TRQP Trust Registry.
At AL2, the operator asserts that:

- Protocol conformance evidence has been produced using the TRQP Conformance Suite
  v1.3.1 baseline profile with a pinned `run_id` (`run-abc1234`).
- Deployment posture evidence has been produced using TRQP-TSPP v0.9.0 at AL2,
  including signed response verification.
- All toolchain artifact versions are pinned to tagged releases.
- A Combined Assurance Manifest (Required at AL2) has been produced and links
  both evidence bundles with a shared `run_id`.
- Evidence bundle checksums (Recommended at AL2) are included.
- A CI run link is included in the manifest `build.ci_run_url`.

## Omissions

None. All Required and Recommended artifacts for AL2 are present.

## Upgrade intent

To upgrade to AL3, this operator will add: a Control Satisfaction Declaration,
a Lifecycle Assertion, an independent assessor engagement, and a Certification
Attestation capturing assessor identity and method.
