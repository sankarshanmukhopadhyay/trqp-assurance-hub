---
owner: maintainers
last_reviewed: 2026-06-29
tier: 1
---

# TSMM/TIS Runtime Assurance Contract

This document defines how TRQP Assurance Hub v1.8.0 projects combined assurance evidence into the portfolio architecture established by TSMM v0.21.0 and Trust Infrastructure Schemas v0.10.0.

The Hub remains the assurance orchestration layer. TSMM supplies the semantic model for authority, delegation, evidence, lifecycle, decision, and effect. TIS supplies executable artifact contracts that can be validated, referenced, signed, and audited.

## Contract summary

| Layer | Responsibility | Hub v1.8.0 handling |
|---|---|---|
| TSMM | Defines what the trust system claim means | Captured in `tsmm_mapping` in the Combined Assurance Manifest |
| TIS | Defines machine-readable artifact contracts | Captured in `tis_artifacts` in the Combined Assurance Manifest |
| CTS | Produces protocol conformance evidence | Referenced as conformance evidence and optionally as a TIS conformance declaration |
| TSPP | Produces security and privacy posture evidence | Referenced as posture evidence and optionally as TIS assurance/control evidence |
| Hub | Publishes combined assurance | Produces CAM, public assurance summary, and adoption evidence |

## Authority, delegation, and scope

Every assurance publication should answer four questions:

| Question | Expected evidence |
|---|---|
| Who had authority to evaluate or publish the assurance claim? | `tsmm_mapping.authority.authority_id` and operator/assessor evidence |
| What authority type was exercised? | `tsmm_mapping.authority.authority_type` |
| What was the delegated scope? | `tsmm_mapping.authority.delegation_scope` |
| What is outside the scope of reliance? | `tsmm_mapping.authority.scope_limitations` and public summary limitations |

The Hub does not manufacture authority. It records the authority basis asserted by the operator, assessor, or governance process and links that assertion to evidence.

## TIS artifact references

The optional `tis_artifacts` block in `schemas/combined-assurance-manifest.schema.json` records TIS-compatible artifacts without requiring the Hub to vendor TIS schemas.

| CAM field | TIS artifact contract | Governance purpose |
|---|---|---|
| `evidence_bundle_manifest` | `evidence/evidence-bundle-manifest.schema.json` | Binds the evidence set and integrity metadata |
| `conformance_declaration` | `conformance/conformance-declaration.schema.json` | Declares what conformance was evaluated, by whom, and under what profile |
| `decision_receipt` | `decision/decision-receipt.schema.json` | Records the assurance decision, policy basis, evidence, and effect |
| `registry_publication` | `registry/registry-publication-profile.schema.json` | Records publication of assurance or registry state |
| `status_or_revocation_evidence` | `profiles/vti/status-list-reference.schema.json` | Records lifecycle, suspension, revocation, expiry, or activation evidence |

These references can be local paths, artifact URIs, or release-bundle paths. Where feasible, include a `sha256` value so the referenced artifact is tamper-evident.

## Decision and effect

The Hub treats assurance publication as a bounded decision:

```text
Evidence + profile + lifecycle state -> assurance publication decision -> public reliance effect
```

The `tsmm_mapping.decision` object records:

- `decision_type`: the class of decision, such as `assurance_publication`;
- `policy_basis`: the profile, rule, or governance baseline used;
- `effect`: the downstream effect being admitted, such as publication of a public assurance summary.

This prevents a passing CTS or TSPP run from being misread as unlimited certification.

## Lifecycle, enforcement, and revocation

Lifecycle evidence is part of operational assurance. A target can pass a point-in-time run and later become suspended, revoked, retired, or out of policy.

Hub v1.8.0 therefore keeps lifecycle state in two places:

| Surface | Role |
|---|---|
| `lifecycle` block | Operational status visible in CAM and public summary |
| `tis_artifacts.status_or_revocation_evidence` | TIS-compatible evidence reference for status or revocation checks |

Relying parties should treat lifecycle state as a live assurance input. A missing status or revocation channel is a limitation, especially for AL3 and AL4 use.

## Auditability

A v1.8.0 assurance package should preserve:

- shared `run_id` and `target_id` across CTS, TSPP, and Hub;
- artifact paths and hashes;
- profile identifiers and tool versions;
- authority and scope limitations;
- lifecycle and revocation evidence;
- decision receipt or equivalent decision record;
- public summary limitations.

This is the minimum viable audit trail for cross-repo operational assurance.
