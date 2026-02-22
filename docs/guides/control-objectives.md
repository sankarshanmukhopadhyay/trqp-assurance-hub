# Control objectives (candidate)

This repository uses lightweight **control IDs** so that assurance claims can be:

- referenced consistently across documents,
- mapped to evidence artifacts, and
- evaluated by automated tooling.

These controls are **candidate** controls for TRQP assurance and governance hardening. They are intentionally minimal and meant to be extended.

## Control ID format

`TRQPAH-<DOMAIN>-<NN>`

Domains:

- `GOV` — governance and operating model
- `EVD` — evidence and provenance
- `REC` — recognition assertions
- `LFC` — lifecycle state and revocation hooks

## Controls

| Control ID | Name | Intent | Typical evidence |
|---|---|---|---|
| TRQPAH-GOV-01 | Versioning policy declared | Ensure compatibility/versioning expectations are explicit | Assurance Profile `governance.versioning` + compatibility policy URL |
| TRQPAH-GOV-02 | Evidence retention declared | Ensure retention/access commitments are explicit | Assurance Profile `governance.retention` + retention policy URL |
| TRQPAH-EVD-01 | Combined manifest emitted | Bind evidence bundles to a single build identifier | `combined-assurance-manifest.json` |
| TRQPAH-EVD-02 | Artifact integrity provided | Enable integrity verification across hops | `sha256` fields in manifest artifacts + checksums |
| TRQPAH-REC-01 | Recognition assertions published | Recognition is expressed as auditable objects | `recognition-assertion.json` artifacts |
| TRQPAH-REC-02 | Recognition assertions signable | Recognition claims can be authenticated | Signature envelope / signed representation |
| TRQPAH-LFC-01 | Lifecycle state declared | Reduce ambiguity about operational status | `lifecycle-assertion.json` |
| TRQPAH-LFC-02 | Deprecation/termination notice | Ensure orderly transitions and evidence continuity | Lifecycle transition reason + replacement pointers |
| TRQPAH-EVD-03 | Control satisfaction declared | Make compliance checkable at control granularity | `control-satisfaction.json` |

## Assurance level guidance

This is a pragmatic starting point (not normative):

- **AL1**: GOV-01, EVD-01
- **AL2**: GOV-01, GOV-02, EVD-01, EVD-02
- **AL3**: + REC-01, LFC-01, EVD-03
- **AL4**: + REC-02, LFC-02 (and stronger signature / provenance expectations)
