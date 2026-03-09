# Revocation and renewal

Certification is only credible when it is time-bound and revocable.

CTR-ACB defines baseline expectations for **renewal cadence** and **revocation signaling**. Ecosystems can tighten these rules.

## Validity windows

A Certification Attestation includes a `validity` window (`not_before`, `not_after`).

Recommended defaults:

- AL1: 12 months
- AL2: 12 months
- AL3: 6–12 months (risk-based)
- AL4: 3–6 months (high consequence)

## Renewal

Renewal SHOULD:

- re-run schema validation on current artifacts
- re-evaluate controls impacted by significant changes
- update lifecycle assertions where state has changed

## Revocation

Revocation MUST be supported at AL4, and SHOULD be supported from AL3 upward.

A revocation event SHOULD:

- identify the revoked certification (attestation `id`)
- state reason code(s)
- provide effective time
- link to evidence where appropriate

CTR-ACB does not mandate a transport for revocation notices; it requires that revocation is **discoverable** and **actionable** for relying parties at the target tier.

See: `docs/guides/revocation-semantics.md`.
