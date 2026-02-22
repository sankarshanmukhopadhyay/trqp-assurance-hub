# Evidence artifacts and expectations

This guide clarifies what evidence artifacts are expected at different assurance levels (AL1–AL4).

AL3 and AL4 are documented as **draft expectations** until TRQP-TSPP defines them normatively.

## Artifact expectations matrix (AL1–AL4)

Legend:
- **Required**: MUST be produced for a compliant run at this level
- **Recommended**: SHOULD be produced; acceptable to omit with rationale
- **Optional**: MAY be produced

| Artifact | AL1 | AL2 | AL3 (draft) | AL4 (draft) | Notes |
|---|---|---|---|---|---|
| Conformance evidence bundle | Required | Required | Required | Required | Protocol behavior assurance |
| TSPP posture evidence bundle | Required | Required | Required | Required | Deployment posture assurance |
| Combined Assurance Manifest | Recommended | Required | Required | Required | Required from AL2 upward to prevent provenance ambiguity |
| Version tuple declaration | Recommended | Required | Required | Required | Prefer tags; else `main@<sha>` |
| Evidence bundle checksums | Optional | Recommended | Required | Required | Integrity verification across hops |
| CI run link or provenance attestation | Optional | Recommended | Required | Required | CI URL acceptable early; migrate to attestations later |
| Redaction report | Optional | Recommended | Required | Required | What was removed and why |
| Operator declaration | Optional | Optional | Recommended | Required | Authority context for high consequence |
| Retention policy pointer | Optional | Recommended | Required | Required | Evidence retention/access policy |
| Control catalog reference | Optional | Recommended | Required | Required | Stable control IDs enable auditability |
| Control Satisfaction Declaration | Optional | Recommended | Required | Required | Machine-readable control coverage and evidence links |
| Lifecycle Assertion | Optional | Recommended | Required | Required | Declares lifecycle state and transition evidence |
| Recognition Assertion | Optional | Optional | Recommended | Required | Signable recognition edges with scope + evidence |
| Revocation bulletin / notice | Optional | Optional | Recommended | Required | Structured notice for trust-impacting revocations |
