# AL4 evidence bundle example (worked reference)

This folder illustrates a minimal **AL4** evidence bundle structure for operators and assessors.

AL4 is defined in `docs/guides/assurance-levels.md`.

## What this example demonstrates

At AL4, AL3 expectations are extended with:
- Continuous monitoring artifacts (logs/metrics/alerts) relevant to assurance claims
- Operationalized revocation and renewal
- Time-bounded validity and explicit assessor method recording

## Example contents

- `operator-declaration.md`
- `version-tuple.json`
- `combined-assurance-manifest.json`
- `control-satisfaction-declaration.json`
- `lifecycle-assertion.json`
- `monitoring-evidence/` — example operational evidence artifacts
- `revocation-notice.json` — structured revocation bulletin / notice
- `renewal-plan.md` — cadence and procedure for renewal
- `certification-attestation.json` — required at AL4

## Notes

Operational evidence SHOULD be access-controlled and redacted as needed; the redaction rules and retention policy MUST be declared.
