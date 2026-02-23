# Control framework

This document defines how CTR-ACB controls are specified so they can be **audited** and **automated**.

A control is *certifiable* when it is:

- stated as a **normative requirement** (SHALL / SHOULD / MAY)
- tied to **objective evidence**
- associated with an **evaluation method**
- mapped to **assurance tiers** (AL1–AL4)

## Control template

Each control in `tools/control-catalog.json` SHOULD follow this template:

- `id`: stable identifier (e.g., `TR-CTRL-01`)
- `title`: short name
- `requirement`: normative statement
- `evidence`: required/recommended evidence artifacts (with pointers)
- `evaluation`: how an evaluator verifies the control (automatable where possible)
- `severity`: impact if not satisfied (`minor` / `major` / `critical`)
- `tiers`: which assurance tiers the control applies to (`AL1`–`AL4`)

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
