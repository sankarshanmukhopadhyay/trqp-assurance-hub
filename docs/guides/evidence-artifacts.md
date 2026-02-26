# Evidence artifacts and expectations

This guide specifies what evidence artifacts are expected at different assurance levels (AL1–AL4).

- Canonical AL definitions: `docs/guides/assurance-levels.md`
- Worked evidence bundle examples: `examples/al3-evidence-bundle/` and `examples/al4-evidence-bundle/`

## Artifact expectations matrix (AL1–AL4)

Legend:
- **Required**: MUST be produced for a compliant run at this level
- **Recommended**: SHOULD be produced; acceptable to omit with rationale
- **Optional**: MAY be produced

| Artifact | AL1 | AL2 | AL3 | AL4 | Notes |
|---|---|---|---|---|---|
| Conformance evidence bundle | Required | Required | Required | Required | Protocol behavior assurance |
| TSPP posture evidence bundle | Required | Required | Required | Required | Deployment posture assurance |
| Combined Assurance Manifest | Recommended | Required | Required | Required | Required from AL2 upward to prevent provenance ambiguity |
| Version tuple declaration | Recommended | Required | Required | Required | Prefer tags; else `main@<sha>` |
| Evidence bundle checksums | Optional | Recommended | Required | Required | Integrity verification across hops |
| CI run link or provenance attestation | Optional | Recommended | Required | Required | CI URL acceptable early; migrate to attestations over time |
| Redaction report | Optional | Recommended | Required | Required | What was removed and why |
| Operator declaration | Optional | Optional | Recommended | Required | Authority context for high consequence |
| Retention policy pointer | Optional | Recommended | Required | Required | Evidence retention/access policy |
| Control catalog reference | Optional | Recommended | Required | Required | Stable control IDs enable auditability |
| Control Satisfaction Declaration | Optional | Recommended | Required | Required | Machine-readable control coverage and evidence links |
| Lifecycle Assertion | Optional | Recommended | Required | Required | Declares lifecycle state and transition evidence |
| Recognition Assertion | Optional | Optional | Recommended | Required | Signable recognition edges with scope + evidence |
| Certification Attestation | Optional | Optional | Recommended | Required | Binds assessor, scope, validity, and evidence to the certification claim |
| Revocation bulletin / notice | Optional | Optional | Recommended | Required | Structured notice for trust-impacting revocations |

## How to use this matrix

1. Select the assurance level (AL1–AL4) you are claiming.
2. Treat **Required** artifacts as non-negotiable inputs to evaluation.
3. For **Recommended** artifacts you omit, document rationale in a short note and include it in the evidence bundle metadata or operator declaration.
4. Prefer machine-readable artifacts (JSON) over prose-only documents.

## Worked examples

- AL3 example bundle: `examples/al3-evidence-bundle/`
- AL4 example bundle: `examples/al4-evidence-bundle/`

These examples are intentionally minimal and meant to be adapted to your environment.
