# AL3 evidence bundle example (worked reference)

This folder illustrates a minimal **AL3** evidence bundle structure for operators and assessors.

AL3 is defined in `docs/guides/assurance-levels.md`.

## What this example demonstrates

At AL3, an operator MUST provide evidence that can be independently reviewed, including:
- Control satisfaction mapped to evidence artifacts
- Lifecycle assertions
- Remediation closure records (where relevant)
- Assessor identity captured when certification is claimed

## Example contents

- `governance-policy.md` — example governance policy covering roles, controls, and retention
- `trust-list-snapshot.json` — example published trust list snapshot with integrity fields
- `conformance-declaration-signed.md` — signed operator conformance declaration bound to evidence
- `independent-assessment-report.md` — assessor review report (worked example)

- `operator-declaration.md` — authority and scope statement
- `version-tuple.json` — version declarations for hub/runner/profile artifacts
- `combined-assurance-manifest.json` — links conformance + posture bundles
- `control-satisfaction-declaration.json` — control objectives mapped to evidence
- `lifecycle-assertion.json` — lifecycle state + transition evidence pointers
- `remediation-closure.json` — closure record for a sample nonconformity
- `certification-attestation.json` — optional at AL3 (recommended when claiming certification)

## Notes

These files are templates and SHOULD be adapted to your deployment and governance context.
