# Assurance tier model

CTR-ACB aligns certification tiers to the repository’s assurance levels (AL1–AL4).

The intent is to preserve a single mental model: **higher AL = more stringent evidence requirements + more stringent evaluation behaviors**.

Canonical definitions for AL1–AL4 live in: `docs/guides/assurance-levels.md`.

## Tier summary

| Tier | Evaluation posture | Typical assessor | Evidence requirements (summary) |
|---|---|---|---|
| AL1 | Self-declared posture | Operator | Minimal, structured artifacts suitable for basic claims |
| AL2 | Self-attested with evidence | Operator (peer review optional) | Evidence bundle + manifest; limited spot checks |
| AL3 | Independently reviewed | Independent assessor | Audit-style evidence: control satisfaction + lifecycle assertions + remediation closure |
| AL4 | High consequence / regulated | Accredited assessor / multi-party | Operational assurance: AL3 + continuous monitoring evidence + operationalized revocation/renewal |

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
