# Operator declaration (AL1 — optional)

**Registry operator:** Example Trust Registry Operator
**Target environment:** https://registry.example.org
**Declaration date:** 2026-01-15

## Scope

This declaration covers the AL1 assurance claim for the Example TRQP Trust Registry.
At AL1, the operator asserts that:

- Protocol conformance evidence has been produced using the TRQP Conformance Suite v1.3.0 baseline profile.
- Deployment posture evidence has been produced using TRQP-TSPP v0.9.0 at AL1.
- All artifact versions are pinned to tagged releases.

## Omissions

The following Recommended artifacts are omitted at AL1 with rationale:

| Artifact | Omission rationale |
|---|---|
| Evidence bundle checksums | Not required at AL1; will be added at AL2. |
| CI run link | Local run; CI integration planned for AL2 upgrade. |

## Upgrade intent

This operator intends to upgrade to AL2 in the next release cycle by adding
checksums, explicit CI provenance, and a version-pinned Combined Assurance Manifest.
