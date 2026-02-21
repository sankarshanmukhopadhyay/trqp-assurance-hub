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
  1) protocol behavior conformance (does it implement TRQP correctly?) and  
  2) deployment posture checks (is it hardened for the risk tier?).

- **Evidence bundle**  
  A machine-readable artifact produced by a runner/profile that enables third parties (auditors, ecosystem authorities, procurement) to verify what was tested and what the results were.

- **Combined Assurance Manifest**  
  A small JSON file that links multiple evidence bundles (e.g., Conformance Suite + TRQP‑TSPP) to a single **build_id** and **target**, with tool/version provenance.

- **Known-good version set**  
  A version tuple (Hub + Conformance Suite + TSPP) that the maintainers have verified to work together.

## Status words used in this repo

- **pass**: requirements satisfied
- **fail**: one or more requirements not satisfied
- **partial**: mixed outcome, or an incomplete run with usable partial evidence

## Assurance levels (AL1–AL4)

TRQP‑TSPP uses assurance levels to express increasing security/privacy expectations.

- **AL1/AL2**: active and documented today
- **AL3/AL4**: reserved for future expansion unless/ until defined in TRQP‑TSPP
