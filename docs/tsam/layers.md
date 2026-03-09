# TSAM Layers

TSAM defines five layers. Implementations MAY realize these layers in different artifacts, but MUST maintain consistency across layers.

## 1. Governance Semantics
Defines terminology, roles, policy lifecycle, and normative constraints.
Governance artifacts MUST be sufficient for an independent implementer to derive system obligations.

## 2. Assurance Levels
Defines maturity tiers and “what must be true” statements per tier.
Assurance levels MUST be upgradeable via explicit evidence deltas.

## 3. Conformance Verification
Defines test suites, validation workflows, and verification criteria.
At least one conformance pathway MUST exist per assurance level.

## 4. Runtime Integrity Controls
Defines operational security controls, infrastructure protections, and distributed systems hardening.
Runtime integrity controls MUST be scoped to the threat model and deployment posture.

## 5. Evidence & Observability
Defines logs, telemetry, build provenance, and audit artifacts.
Evidence production MUST be automatable where feasible and MUST be reviewable by an independent verifier.

Isolation between layers introduces assurance gaps and MUST be treated as a defect.
