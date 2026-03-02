# TSAM Principles

These principles are normative. A TSAM-aligned implementation MUST satisfy P1–P7.

## P1 — Verifier-first orientation
Assurance definitions MUST be consumable and testable by independent verifiers without privileged context.

## P2 — Normative clarity
Assurance requirements MUST be stated as verifiable predicates (inputs, checks, expected outputs) and MUST avoid purely aspirational language.

## P3 — Evidence binding
Every assurance claim MUST map to evidence artifacts with defined structure, provenance expectations, and verification steps.

## P4 — Runtime awareness
Assurance MUST account for runtime controls and operational behavior, not only governance semantics or documentation.

## P5 — Standards interoperability
Controls SHOULD map to relevant security and distributed systems standards where such mappings reduce ambiguity and improve auditability.

## P6 — Upgrade explicitness
Transitions between assurance levels MUST define required evidence deltas and MUST be achievable through an explicit, documented path.

## P7 — Registry-agnostic applicability
TSAM MUST remain applicable to any trust-bearing distributed system; repo-specific terminology MUST NOT be treated as a prerequisite for the method.
