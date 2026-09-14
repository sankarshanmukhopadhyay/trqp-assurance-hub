# Experimental TRQP v3 assurance reconciliation

Status: **downstream experimental assurance evidence; not an adopted Trust Over IP specification, profile, or production certification**.

Tracking issue: https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/issues/94

Umbrella tranche: https://github.com/sankarshanmukhopadhyay/tswg-trust-registry-protocol/issues/55

## Isolation rule

This work lives only on `experiment/trqp-v3-candidate`. Stable `main` is intentionally unaffected. The experimental branch is the terminal integration surface for this tranche; there is no merge-to-main path unless a future, separate governance decision is made after upstream reconciliation/adoption.

## Candidate and producer pins

The assurance result is bound to candidate commit `532a570ed8b7b468b7a317030077577b9859c14f` on `sankarshanmukhopadhyay/tswg-trust-registry-protocol: draft/next-trqp`.

Machine-readable inputs:

- `experimental/trqp-v3/source-pin.json` — candidate source and authority boundary;
- `experimental/trqp-v3/producer-pins.json` — exact CTS and TSPP experimental evidence producer commits/artifacts;
- `experimental/trqp-v3/assurance-evidence.json` — requirement-level reconciliation.

A change to the candidate or either producer pin makes affected assurance evidence stale until explicit reconciliation and rerun.

## Evidence model

CTS provides candidate semantic oracle/vector evidence. TSPP provides an independently exercised protocol/profile realization that intentionally does not import the candidate reference evaluator or CTS oracle. Assurance Hub reconciles those bounded claims without creating new normative semantics.

For each requirement:

- `PASS + PASS -> SUPPORTED`;
- any `FAIL -> NOT_SUPPORTED`;
- missing, unknown, stale, conflicting, or otherwise incomplete evidence -> `INDETERMINATE`.

The validator rejects any assurance row that contradicts that rule.

## Current pinned result

All 32 release-significant candidate requirement IDs have pinned CTS `PASS` and TSPP `PASS` evidence, producing `SUPPORTED` at the downstream experimental assurance layer.

This statement is deliberately narrow. It means the pinned candidate obligations have executable semantic vectors and independently pressure-tested protocol/profile evidence in these downstream repositories. It does **not** mean:

- upstream TRQP v3 has been adopted;
- arbitrary production implementations conform;
- deployment-specific security, privacy, governance, or operational assurance has been established; or
- stable TRQP* `main` should change.

## Validate

```bash
make v3-candidate-check
```

CI runs the same checks on pushes to the experimental branch.

## Disposition

If upstream does not adopt the v3 direction, retain or archive this branch as experimental research/evidence and leave `main` unchanged. If upstream later adopts materially equivalent semantics, reconcile the authoritative upstream text first; do not promote evidence merely because names or version numbers match.
