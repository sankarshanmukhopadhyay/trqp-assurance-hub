# Control framework

This document defines how CTR-ACB controls are specified so they can be **audited** and **automated**.

A control is *certifiable* when it is:

- stated as a **normative requirement** (SHALL / SHOULD / MAY)
- tied to **objective evidence**
- associated with an **evaluation method**
- mapped to **assurance tiers** (AL1–AL4)

## Control template

Each control in `tools/control-catalog.json` MUST include the minimum fields below (additional fields MAY be added as the catalog evolves):

- `id`: stable identifier (e.g., `GOV-001`)
- `name`: short name
- `objective`: normative statement of the control intent
- `tiers`: which assurance tiers the control applies to (`AL1`–`AL4`)
- `severity`: impact if not satisfied (`minor` / `major` / `critical`)

Optional (recommended for certification-grade catalogs):

- `evidence`: expected evidence artifact kinds and pointers
- `evaluation`: how an evaluator verifies the control (automatable where possible)
## Evidence binding model

Controls are *not* satisfied by prose. They are satisfied by artifacts.

Primary evidence binders:

- **Control Satisfaction Declaration** (`TRQPControlSatisfactionDeclaration`)
- **Certification Attestation** (`TRQPCertificationAttestation`)

The Control Satisfaction Declaration links:

- control IDs → status (`pass`/`fail`/`n/a`)
- evidence references (files, URLs, attestations)
- evaluator notes (optional)

## Practical guidance

- Prefer **machine-verifiable checks** (schema validation, signature verification, checksum verification).
- When manual review is unavoidable, record **review scope** and **sampling method** in the Control Satisfaction Declaration.
- Keep control IDs stable. Controls can evolve, but IDs should not churn.

See also: [`../guides/control-objectives.md`](../guides/control-objectives.md).