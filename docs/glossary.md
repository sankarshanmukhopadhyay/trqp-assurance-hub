# Glossary

This repo aims to keep TRQP adoption product-like: fewer moving parts for adopters and clearer contracts for maintainers.

## Terms

- **Assurance Hub (this repo)**
  The integration surface: onboarding, compatibility guidance, shared schemas, and example workflows.

- **Runner / Engine**
  The executable that runs tests and produces artifacts (evidence bundles, reports).

- **Profile pack**
  A versioned set of requirements, test plans, mappings, and expected evidence outputs.

- **Combined assurance**
  A single assurance story that combines:

  1. protocol behavior conformance (does it implement TRQP correctly?)
  2. deployment posture checks (is it hardened for the risk tier?)

- **Evidence bundle**
  A machine-readable artifact produced by a runner/profile that enables third parties to verify what was tested and what the results were.

- **Combined Assurance Manifest**
  A small JSON file that links multiple evidence bundles to a single build identifier and target, with tool/version provenance.

- **Known-good version set**
  A version tuple (Hub + Conformance Suite + TSPP) that maintainers have verified to work together.

## Status words

- **pass**: requirements satisfied
- **fail**: one or more requirements not satisfied
- **partial**: mixed outcome, or an incomplete run with usable partial evidence
- **skip**: not applicable or not executed (with rationale)

## Assurance levels (AL1–AL4)

TRQP‑TSPP uses assurance levels to express increasing security/privacy expectations.

### AL1 — Baseline internet hygiene (implemented)

Intended for implementations that are public-facing but operating under standard threat assumptions.

### AL2 — Hardened posture (implemented)

Intended for implementations that are materially relied upon (ecosystem infrastructure, higher-value targets).

### AL3 — High assurance (reserved / draft semantics)

Status: reserved for future definition in TRQP‑TSPP.

Draft intent:

- stronger evidence requirements and provenance
- explicit threat-model alignment
- enhanced audit controls

### AL4 — Critical assurance (reserved / draft semantics)

Status: reserved for future definition in TRQP‑TSPP.

Draft intent:

- designed for critical infrastructure and high-consequence environments
- maximum rigor on provenance, integrity, and operational controls

> AL3/AL4 are intentionally marked as reserved until TRQP‑TSPP defines normative requirements. This glossary provides draft intent only to prevent ladder confusion.
