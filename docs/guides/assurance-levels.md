# Assurance levels (AL1–AL4)

← [Back to Docs Index](../index.md)


This repository treats assurance levels as **operational claims** that MUST be backed by evidence artifacts. Higher levels require stronger evidence, stronger evaluation posture, and tighter lifecycle discipline.

> **Design principle:** *A higher AL is not “more paperwork”; it is a stronger, more falsifiable claim about system behavior and governance.*

This guide is the canonical vocabulary for AL3 and AL4 within the Assurance Hub. If upstream definitions (e.g., TRQP-TSPP) evolve, this hub SHOULD update via a versioned change with explicit migration notes.

## Normative keywords

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are to be interpreted as described in RFC 2119.

## Core terms

- **Artifact**: a durable, reviewable object produced by an assurance workflow (e.g., JSON evidence bundle, signed declaration, control satisfaction statement).
- **Evidence bundle**: a machine-readable artifact that contains structured results, provenance, and references needed to support an assurance claim.
- **Combined Assurance Manifest (CAM)**: a small JSON document that links multiple evidence bundles (e.g., protocol + posture) to a single build, target, and scope.
- **Independent verification**: evaluation performed by an assessor who is not the operator and whose identity (and method, where relevant) is recorded.
- **Remediation closure**: documented confirmation that a nonconformity has been addressed, with evidence linking the fix to the detected issue.
- **Continuous monitoring**: ongoing collection and review of operational signals (logs/metrics/alerts) to detect drift, regressions, or violations relevant to assurance claims.

## Assurance level definitions

### AL1 — Baseline conformance and hygiene
At AL1, an operator MUST be able to produce machine-readable evidence showing protocol conformance and minimum deployment posture.

Minimum expectations:
- Evidence bundles are produced for the relevant test runs.
- Results are attributable to a specific version of the artifacts and runner.

### AL2 — Evidence-bound self-attestation
At AL2, the operator MUST bind claims to evidence in a way that reduces provenance ambiguity.

Minimum expectations (in addition to AL1):
- A Combined Assurance Manifest SHOULD be produced and SHOULD link all relevant evidence bundles.
- Version declarations SHOULD be explicit (prefer tags; else `main@<sha>`).
- Integrity signals (e.g., checksums) SHOULD be present.

### AL3 — Independently reviewed assurance
At AL3, claims MUST be reviewable by an **independent assessor** and MUST be supported by artifacts that enable audit-style checking.

Minimum expectations (in addition to AL2):
- A Combined Assurance Manifest MUST be produced for each evaluated scope.
- Evidence bundles MUST include integrity verification (e.g., checksums).
- A **Control Satisfaction Declaration** MUST be produced, mapping control objectives to evidence artifacts.
- A **Lifecycle Assertion** MUST be produced, declaring lifecycle state and transition evidence.
- **Remediation closure** MUST be recorded for detected nonconformities relevant to the evaluated scope.
- Assessor identity MUST be recorded in the **Certification Attestation** (where certification is claimed) or in an equivalent assessor record.

### AL4 — High-consequence / continuously evidenced assurance
At AL4, the assurance claim MUST remain valid under change, and MUST be supported by operational evidence demonstrating ongoing control performance and lifecycle discipline.

Minimum expectations (in addition to AL3):
- **Continuous monitoring artifacts** MUST be produced and retained per a declared retention policy.
- Operational metrics/logs relevant to the assurance claim MUST be reviewable (with access controls and redaction rules documented).
- Revocation and renewal MUST be operationalized (e.g., structured revocation notice and renewal cadence).
- Assessor identity **and method** MUST be recorded in the Certification Attestation (or equivalent).
- Time-bounded validity periods MUST be declared for high-impact claims.

## Related documents

- Evidence artifacts and expectations: `docs/guides/evidence-artifacts.md`
- Worked evidence bundles: `examples/al3-evidence-bundle/` and `examples/al4-evidence-bundle/`
- Certification tier model: `docs/certification-baseline/assurance-tier-model.md`
- Glossary: `docs/glossary.md`