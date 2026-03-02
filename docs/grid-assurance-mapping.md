# GRID Assurance Mapping

This document binds TRQP Assurance Levels (AL1–AL4) to **directory eligibility** for GRID-style registrar listings.

The aim is to prevent interpretive drift by stating *what must be true* for a given listing class.

## Mapping (normative)

### AL1 — Not eligible
A registrar listing **MAY** be published for transparency, but **MUST NOT** be treated as an eligible authoritative registrar in GRID.

### AL2 — Informational listing
A registrar listing **MAY** be included for discovery, but **MUST** be flagged as *informational* (non-authoritative) in any consuming system.

Evidence expectation:
- Basic identity binding for the registrar DID
- Published governance policy pointer (URI) is present

### AL3 — Active registrar
A registrar listing **MAY** be treated as an active authoritative registrar in GRID.

Evidence expectation (minimum):
- Governance policy pointer + hash
- Evidence bundle references demonstrating operational controls for issuance and query
- An independent assessment or attestation covering key controls

### AL4 — Critical registrar (high assurance)
A registrar listing **MAY** be treated as critical infrastructure-grade.

Evidence expectation (minimum):
- AL3 evidence, plus
- Stronger control coverage and stronger independence of assessment
- Explicit incident response and revocation playbooks, exercised and evidenced

## Notes

Directory operators **SHOULD** publish their own stricter eligibility rules; this mapping is the minimum shared floor.
