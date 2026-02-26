# Assurance tier model

CTR-ACB aligns certification tiers to the repository’s assurance levels (AL1–AL4).

The intent is to preserve a single mental model: **higher AL = stronger evidence + stronger evaluation**.

## Tier summary

| Tier | Evaluation posture | Typical assessor | Evidence strength |
|---|---|---|---|
| AL1 | Self-declared posture | Operator | Low (structured, but minimal) |
| AL2 | Self-attested with evidence | Operator + peer review optional | Medium (evidence bundles + manifests) |
| AL3 | Independently reviewed | Independent assessor | High (control satisfaction + lifecycle + integrity) |
| AL4 | High consequence / regulated | Accredited assessor / multi-party | Highest (strong provenance + revocation discipline) |

## Tier gates (what changes as you move up)

Across tiers, the baseline tightens:

- **Controls**: from “declare” → “demonstrate” → “verify”
- **Evidence**: from “available” → “bound” → “tamper-evident”
- **Lifecycle**: from “stated” → “asserted” → “revocation-aware”
- **Recognition**: from “optional” → “scoped” → “propagated”

## Recommended assessor expectations

CTR-ACB intentionally does not define accreditation. It does define *minimum behaviors*:

- AL3: assessor identity MUST be recorded in the Certification Attestation
- AL4: assessor identity + method MUST be recorded; revocation and renewal MUST be operationalized
