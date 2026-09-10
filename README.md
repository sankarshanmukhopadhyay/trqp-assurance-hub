---
owner: maintainers
last_reviewed: 2026-09-10
tier: 0
---

# TRQP Assurance Hub

The TRQP Assurance Hub is the **evidence aggregation, compatibility coordination, and assurance publication layer** in the TRQP Operational Trust Stack. It combines protocol-conformance evidence from the TRQP Conformance Suite with security/privacy posture evidence from TRQP-TSPP, evaluates declared assurance and ecosystem profiles, and publishes machine-readable combined assurance for downstream review.

It is also the **adopter front door and coordinated Stack release authority**. A coordinated Stack release does not create a fourth implementation product; it declares which independently versioned component releases have been exercised together and preserves the evidence behind that claim.

> **Current Hub component release:** v1.11.0  
> **Current coordinated stack:** TRQP Stack 2026.1 — Coconut  
> **Lifecycle:** Active  
> **Maturity:** Candidate  
> **Operational status:** Active validation

| Attribute | Value |
|---|---|
| Portfolio tier | Flagship |
| Primary role | Assurance aggregation, profile evaluation, compatibility coordination, release evidence publication |
| Portfolio contract role | `assurance-aggregator` |
| Primary output | Combined Assurance Manifest, profile assurance evidence and assurance decision |
| Validation | `make validate` |
| Assurance evidence | `make assurance-check` |
| Stack release gate | `make stack-release-check` |
| Evidence output | `artifacts/combined-assurance/` plus reproducible profile-specific evidence bundles |
| Governance authority | [`GOVERNANCE.md`](GOVERNANCE.md) and [`PROJECT-STATUS.yaml`](PROJECT-STATUS.yaml) |
| Current Stack record | [`stack/releases/2026.1/`](stack/releases/2026.1/) |
| Canonical adopter workflow | [`docs/adoption/stack-quickstart.md`](docs/adoption/stack-quickstart.md) |
| Profile-aware assurance guide | [`docs/guides/profile-aware-assurance.md`](docs/guides/profile-aware-assurance.md) |
| Documentation site | https://sankarshanmukhopadhyay.github.io/trqp-assurance-hub/ |

## Start here: TRQP Stack 2026.1 — Coconut

If your goal is to adopt, evaluate, procure, or assess the complete TRQP assurance workflow, **start with the coordinated Stack release rather than choosing repository versions independently**.

TRQP Stack 2026.1 — Coconut validates this tuple:

| Layer | Release | Authority / output |
|---|---:|---|
| TRQP-TSPP | v0.15.0 | Security/privacy controls and posture evidence |
| TRQP Conformance Suite | v1.8.0 | Protocol conformance and deterministic replay evidence |
| TRQP Assurance Hub | v1.11.0 | Evidence aggregation and assurance publication |
| TSMM | v0.24.0 | Semantic authority |
| TIS | v0.14.1 | Schema and portfolio authority |

The canonical machine-readable release record is [`stack/releases/2026.1/manifest.json`](stack/releases/2026.1/manifest.json). The human-readable release explanation is [`stack/releases/2026.1/README.md`](stack/releases/2026.1/README.md).

### Why an adopter benefits

A coordinated Stack release answers the compatibility question before deployment: **which exact versions are known to work together under the declared assurance model?**

The release gate verifies immutable component resolution, clean-room bootstrap, component evidence generation, deterministic CTS replay, combined-assurance validation, cross-repository run/target correlation, provenance and artifact integrity, fail-closed negative cases, whole-stack semantic replay equivalence, and the executable adopter walkthrough.

This means an adopter can select one validated tuple, reproduce it, inspect every underlying authority boundary, and obtain a portable evidence chain without reverse-engineering compatibility across three repositories.

## Authority and scope

The Hub is authoritative for:

- assurance evidence ingestion and composition;
- assurance profile and ecosystem-profile evaluation;
- combined assurance decision generation;
- portable assurance publication;
- coordinated compatibility tuple declaration;
- Stack integration verification; and
- coordinated release eligibility evidence.

The Hub **does not** own the upstream TRQP protocol specification, ecosystem profile specifications such as the Ayra TRQP Profile, TSPP control/posture semantics, CTS raw conformance execution or replay-comparison semantics, TSMM semantics, TIS schema authority, governance legitimacy, or external certification/accreditation.

A Stack release therefore proves tested interoperability without collapsing repository-local authority.

## Runtime assurance flow

```text
TRQP-TSPP posture/control evidence
                +
TRQP Conformance Suite conformance evidence
                +
CTS deterministic replay evidence
                +
version-bound ecosystem profile constraints/evidence
                ↓
      TRQP Assurance Hub
                ↓
Combined Assurance Manifest
+ profile assurance bundle
+ assurance decision
+ traceability report
                ↓
Relying-party / assessor / procurement / ecosystem review
```

The machine-readable authority chain is:

```text
TSMM semantic authority
        ↓
TIS schema / portfolio authority
        ↓
TSPP posture evidence + CTS conformance/replay evidence
        ↓
profile authority + external authority evidence where applicable
        ↓
Assurance Hub aggregation + coordinated-release evidence
```

## Profile-aware assurance

The Hub now includes a reusable profile boundary, with the **Ayra TRQP Profile** as the first proving implementation. The governing rule is:

> **Profile assurance extends TRQP assurance; it does not redefine TRQP.**

Profile evaluation preserves independent result dimensions and the bounded states `PASS`, `FAIL`, `INDETERMINATE`, `NOT_APPLICABLE`, and `NOT_IMPLEMENTED`. Missing evidence cannot become `PASS`, an operational error cannot become an authoritative negative trust decision, and governance legitimacy is not inferred from API correctness or DID discovery alone.

The current Ayra projection is version-bound to Ayra `0.6.0-draft`, TRQP `2.0`, and the exact upstream revision recorded in `profiles/ayra/requirements.yaml`. The compatibility analysis against the downstream experimental candidate TRQP v3 is similarly revision-bound and does not treat candidate-v3 work as upstream authority.

See [`docs/guides/profile-aware-assurance.md`](docs/guides/profile-aware-assurance.md), [`docs/ayra-v3-compatibility.md`](docs/ayra-v3-compatibility.md), and [`docs/ayra-assurance-residual-threats.md`](docs/ayra-assurance-residual-threats.md).

The first proving implementation deliberately contains some deterministic core/posture-adjacent observations so the profile architecture can be exercised end to end. Producer-contract convergence is tracked separately in TRQP Conformance Suite #40 and TRQP-TSPP #85; those follow-ups move producer-owned observations back to their proper evidence authorities without moving Ayra-specific semantics out of the Hub profile layer.

## Evidence artifacts

Primary Hub outputs include:

- `artifacts/combined-assurance/combined-assurance-manifest.json`;
- `artifacts/combined-assurance/assurance-decision.json`;
- `artifacts/combined-assurance/traceability-report.json`; and
- reproducible profile-specific bundles containing machine results, provenance, authority evidence, endpoint evidence, negative-test evidence and a derived human-readable report.

A passing test run alone is not an assurance conclusion. The evidence chain preserves authority, evaluated scope, producer versions, run and target identity, replay-policy provenance, profile/source revision, lifecycle/invalidation conditions, and the evidence consumed by the final decision.

## Decisive Stack release gate

Run:

```bash
make stack-release-check
```

The dedicated `stack-release-eligibility` GitHub Actions workflow extends this with tagged component execution, clean bootstrap, deterministic replay, full combined-assurance composition, semantic replay comparison, negative cases, and candidate evidence publication.

For TRQP Stack 2026.1 — Coconut, the decisive workflow completed successfully on the merged Hub `main` baseline at commit `045ba10ec436ea5d1e9e443894bbbf7bea27472b`. The release record preserves the workflow run and evidence artifact digest.

## Adoption and implementation guides

- [`docs/adoption/stack-quickstart.md`](docs/adoption/stack-quickstart.md) — canonical end-to-end Stack workflow.
- [`docs/guides/combined-assurance.md`](docs/guides/combined-assurance.md) — compose CTS and TSPP evidence.
- [`docs/guides/profile-aware-assurance.md`](docs/guides/profile-aware-assurance.md) — evaluate version-bound ecosystem profiles without collapsing authority boundaries.
- [`docs/guides/evidence-artifacts.md`](docs/guides/evidence-artifacts.md) — evidence artifact model.
- [`docs/guides/public-assurance-publication.md`](docs/guides/public-assurance-publication.md) — publish relying-party-facing assurance.
- [`docs/reference/compatibility-matrix.md`](docs/reference/compatibility-matrix.md) — supported component relationships.
- [`docs/portfolio-integration.md`](docs/portfolio-integration.md) — synchronized portfolio integration.
- [`docs/governance/release-policy.md`](docs/governance/release-policy.md) — component and coordinated Stack release governance.

## Release cadence

Component repositories retain independent semantic versioning. Coordinated Stack releases are expected approximately monthly when meaningful capability has accumulated, and earlier when a capability, compatibility, security, evidence, or authority change makes a new validated tuple materially useful or necessary.

Each coordinated Stack release receives a randomly selected codename from the Wikipedia list of Indian state trees. The codename is human-facing identity only; the stable machine identity remains `trqp-stack-YYYY.N`.

## Invalidation and supersession

Combined assurance, profile-assurance conclusions and coordinated-release claims are conditional. Missing evidence, invalid producer evidence, changed profile/source revisions, incompatible semantic/schema authorities, failed CTS replay determinism, replay-policy incompatibility, or other declared invalidation conditions can make a conclusion unsuitable for continued use.

Historical manifests and profile evidence remain historical evidence. Changed compatibility or profile conditions require reassessment, a new release, or explicit supersession rather than silent rewriting.

Example or self-generated evidence does not constitute independent assurance, certification, or accreditation.

## License

See [`LICENSE`](LICENSE).
