# Assurance profile (candidate)

This repository treats “assurance” as something you can **publish and verify**, not something you merely describe.

An **Assurance Profile** is a machine-readable declaration of:

- the assurance tier you claim (e.g., AL1–AL4),
- governance and operational commitments (retention, redaction, operator responsibility),
- evidence expectations (what artifacts will be produced),
- and optional ecosystem-facing declarations (recognition, discovery pointers, mappings).

This is a **candidate format** intended to operationalize upstream TRQP RFEs without forcing protocol-level changes.

## Files

- Schema: [`schemas/trqp-assurance-profile.schema.json`](../../schemas/trqp-assurance-profile.schema.json)
- Example: [`examples/trqp-assurance-profile.example.json`](../../examples/trqp-assurance-profile.example.json)

## How implementers use it

Recommended flow:

1. Maintain an `assurance-profile.json` alongside your TRQP registry deployment repo.
2. Update it when your assurance posture or governance commitments change.
3. During a build, emit a **Combined Assurance Manifest** that binds:
   - a Conformance Suite run,
   - a TSPP run,
   - and a pointer to the assurance profile.

This lets verifiers and auditors evaluate:

- what you *claimed*,
- what you *produced*,
- and whether the evidence matches the profile.

## Relationship to assurance levels (AL1–AL4)

Assurance levels are treated as:

- **adopter-facing tiers** (procurement-ready), and
- **artifact/evidence requirements** (audit-ready).

For the artifact expectations per level, see:

- [`docs/guides/evidence-artifacts.md`](evidence-artifacts.md)

## Recognition, lifecycle, and discovery declarations

The profile intentionally supports optional sections that are frequently debated upstream:

- **recognition assertions** (who/what you recognize, and on what basis),
- **lifecycle and revocation policies** (what you commit to operationally),
- **discovery pointers** (where a client can learn about endpoints/capabilities).

These are declared as publishable metadata and evidence hooks.
They do not replace upstream protocol semantics.

## Control binding

To make assurance levels operational, the profile can optionally bind to a control catalog and reference a control satisfaction declaration.

- Control objectives: [`docs/guides/control-objectives.md`](control-objectives.md)

## Standalone artifacts

For stronger auditability, this repo introduces standalone, signable artifacts that the profile can reference:

- Recognition Assertion: [`docs/guides/recognition-assertion.md`](recognition-assertion.md)
- Lifecycle state and Lifecycle Assertion: [`docs/guides/lifecycle-state.md`](lifecycle-state.md)

For ecosystem reasoning:

- Recognition graph semantics: [`docs/guides/recognition-graph.md`](recognition-graph.md)
- Assurance-layer revocation semantics: [`docs/guides/revocation-semantics.md`](revocation-semantics.md)
