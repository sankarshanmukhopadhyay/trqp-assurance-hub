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
