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

## Control → Artifact → Evidence matrix (AL3/AL4)

This matrix makes AL3 and AL4 expectations **explicitly auditable** by mapping each control objective to the minimum set of artifacts and evidence types required.

Legend:
- **Artifact**: a named deliverable (document, dataset, log export, signed statement, test report)
- **Evidence type**: what an assessor can actually verify (signature, hash, timestamp, run output, log trail, third‑party report)

| Control objective | AL3 required artifact(s) | Evidence type | AL4 additional requirement |
|---|---|---|---|
| Governance and accountability | Governance policy; roles & responsibilities; decision records | Published doc(s) with versioning; change log | Time‑bound governance attestations; operational KPIs for governance execution |
| Scope and system boundary | Scope statement; dependency inventory; assumptions & constraints | Versioned inventory; review sign‑off | Continuous dependency monitoring; drift alerts and periodic boundary re‑validation |
| Trust list lifecycle | Trust list policy; publication process; issuance/revocation procedures | Signed policy; published trust list snapshots; audit trail | Continuous trust list monitoring; revocation SLAs; automated publication integrity checks |
| Key management and signing controls | Key management policy; key custody model; rotation plan | Signed policy; rotation records; key metadata; evidence of HSM/KMS controls (where applicable) | Measured rotation compliance; key compromise detection signals; incident playbooks exercised |
| Change management | Change control procedure; release notes; approval workflow | Version control history; approvals; release artifacts | Continuous change telemetry; time‑to‑detect and time‑to‑rollback metrics; automated policy checks |
| Conformance testing | Conformance test run evidence; test report; environment declaration | Test outputs; hashes; run identifiers; reproducible config | Continuous conformance monitoring (scheduled runs); regression alerting and trend metrics |
| Incident response | Incident response plan; escalation matrix; comms templates | Versioned plan; tabletop exercise record; incident postmortems (if any) | Continuous incident metrics; on‑call readiness evidence; periodic drills with measurable outcomes |
| Vulnerability and patch management | Vulnerability intake process; patch policy; remediation workflow | Ticket trail; patch records; remediation closure evidence | Continuous vulnerability scanning evidence; MTTR metrics; SLA compliance reporting |
| Independent verification | Third‑party assessment report OR independent internal audit report | Signed assessment report; assessor identity; scope mapping | Recurring independent reviews (time‑bound); evidence of follow‑up verification |
| Remediation closure | Remediation log; closure criteria; closure records | Ticket closure trail; evidence of retest; signed closure statement | Continuous remediation tracking; aging metrics; automated closure validation signals |
| Auditability and record integrity | Evidence bundle index; retention policy; integrity controls | Hashes; timestamps; signed bundle index; retention configuration | Continuous log integrity checks; immutable audit trails; periodic sampling reports |
| Continuous monitoring (AL4 focus) | N/A (Recommended at AL3) | N/A | Monitoring plan; telemetry export; alerting rules; periodic attestation of monitoring operation |
| Renewal and recertification | Renewal plan; re‑assessment triggers | Versioned plan; trigger log | Scheduled attestations; automated trigger detection; renewal evidence bundles over time |

## How to use this matrix

1. Select the assurance level (AL1–AL4) you are claiming.
2. Treat **Required** artifacts as non-negotiable inputs to evaluation.
3. For **Recommended** artifacts you omit, document rationale in a short note and include it in the evidence bundle metadata or operator declaration.
4. Prefer machine-readable artifacts (JSON) over prose-only documents.

## Worked examples

- AL3 example bundle: `examples/al3-evidence-bundle/`
- AL4 example bundle: `examples/al4-evidence-bundle/`

These examples are intentionally minimal and meant to be adapted to your environment.
