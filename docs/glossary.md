# Glossary

This repo tries to keep TRQP adoption **product-like**: fewer moving parts for adopters, clearer contracts for maintainers.

## Terms

- **Assurance Hub (this repo)**  
  The *integration surface*: onboarding, compatibility guidance, shared schemas, and example workflows.

- **Runner / Engine**  
  The executable that runs tests and produces artifacts (evidence bundles, reports).  
  Example: the TRQP Conformance Suite runner.

- **Profile Pack**  
  A versioned set of requirements, test plans, mappings, and expected evidence outputs.  
  Examples: a “baseline” protocol conformance profile; a “TSPP AL1” security/privacy profile.

- **Combined assurance**  
  A single assurance story that combines:
  1) protocol behavior conformance (does it implement TRQP correctly?), and  
  2) deployment posture checks (is it hardened for the risk tier?).

- **Evidence bundle**  
  A machine-readable artifact produced by a runner/profile that enables third parties (auditors, ecosystem authorities, procurement) to verify what was tested and what the results were.

- **Combined Assurance Manifest**  
  A small JSON file that links multiple evidence bundles (e.g., Conformance Suite + TRQP-TSPP) to a single **build_id** and **target**, with tool/version provenance.

- **Known-good version set**  
  A version tuple (Hub + Conformance Suite + TSPP) that the maintainers have verified to work together.

## Status words used in this repo

- **pass**: requirements satisfied
- **fail**: one or more requirements not satisfied
- **partial**: mixed outcome, or an incomplete run with usable partial evidence
- **skip**: not applicable or not executed (with rationale)

## Assurance levels (AL1–AL4)

TRQP-TSPP uses assurance levels to express increasing security/privacy expectations.

### AL1 — Baseline internet hygiene (implemented)

Intended for implementations that are public-facing but operating under **standard threat assumptions**.

Typical expectations (illustrative, not exhaustive):
- Basic endpoint security posture and sane defaults
- Minimal privacy leakage (avoid oversharing metadata)
- Deterministic error handling and operational stability signals
- Logging suitable for troubleshooting (without collecting unnecessary personal data)

### AL2 — Hardened posture (implemented)

Intended for implementations that are **materially relied upon** (ecosystem infrastructure, high value targets).

Typical expectations (illustrative, not exhaustive):
- Stronger controls around authz/authn, rate limiting, and abuse resistance
- Clear integrity expectations for machine-consumed responses
- Better operational controls and auditability (traceability of changes, run outputs)
- More stringent privacy protections and minimization

### AL3 — High assurance (reserved / draft semantics)

**Status:** reserved for future definition in TRQP-TSPP.

Draft intent (so readers understand the ladder):
- Stronger evidence requirements (repeatable test runs, stricter provenance)
- More explicit threat-model alignment and adversarial resilience expectations
- Enhanced audit controls (e.g., stronger change management evidence)
- Tighter privacy requirements for sensitive ecosystems

### AL4 — Critical assurance (reserved / draft semantics)

**Status:** reserved for future definition in TRQP-TSPP.

Draft intent:
- Designed for **critical infrastructure** and high-consequence environments
- Maximum rigor on provenance, integrity, and operational controls
- Strongest audit posture and least-privilege operational model
- Highest privacy bar (minimization + protection against inference where practical)

> Note: AL3/AL4 semantics are intentionally marked as **reserved** until TRQP-TSPP defines normative requirements. This glossary provides draft intent only to prevent “mystery ladder” confusion.
