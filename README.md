---
owner: maintainers
last_reviewed: 2026-09-10
tier: 0
---

# TRQP Assurance Hub

The TRQP Assurance Hub is the **evidence aggregation, compatibility coordination, and assurance publication layer** in the TRQP Operational Trust Stack. It combines protocol-conformance evidence from the TRQP Conformance Suite with security/privacy posture evidence from TRQP-TSPP, evaluates declared assurance and ecosystem profiles, and publishes machine-readable combined assurance for downstream review.

It is also the **adopter front door and coordinated Stack release authority**. A coordinated Stack release does not create a fourth implementation product; it declares which independently versioned component releases have been exercised together and preserves the evidence behind that claim.

> **Current Hub component release:** v1.13.0  
> **Current coordinated stack:** TRQP Stack 2026.3 — Banyan  
> **Previous coordinated stack:** TRQP Stack 2026.2 — Ashoka  
> **Lifecycle:** Active  
> **Maturity:** Active / release-backed  
> **Operational status:** Published and under continuous validation

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
| Current Stack record | [`stack/releases/2026.3/`](stack/releases/2026.3/) |
| Current Stack release | https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub/releases/tag/trqp-stack-2026.3 |
| Canonical adopter workflow | [`docs/adoption/stack-quickstart.md`](docs/adoption/stack-quickstart.md) |
| Profile-aware assurance walkthrough | [`docs/adoption/stack-2026.3-walkthrough.md`](docs/adoption/stack-2026.3-walkthrough.md) |
| Profile-aware assurance guide | [`profiles/README.md`](profiles/README.md) |
| Documentation site | https://sankarshanmukhopadhyay.github.io/trqp-assurance-hub/ |

## Start here: TRQP Stack 2026.3 — Banyan

If your goal is to adopt, evaluate, procure, or assess the complete TRQP assurance workflow, **start with the coordinated Stack release rather than choosing repository versions independently**.

TRQP Stack 2026.3 — Banyan is the current published coordinated baseline. It adds **profile-aware compositional assurance** while preserving the lifecycle, invalidation, reassessment, authority-drift and supersession guarantees established in Stack 2026.2.

The published tuple is:

| Layer | Release | Exact commit | Authority / output |
|---|---:|---|---|
| TRQP-TSPP | v0.17.0 | `328e19c71f407ebdb2bc92828a3ae037a843f285` | Security/privacy controls and profile-consumable posture evidence |
| TRQP Conformance Suite | v1.10.0 | `1e5dc2646c75390444d9ae86f3d6136d7c033463` | Protocol conformance, deterministic replay and profile-consumable core evidence |
| TRQP Assurance Hub | v1.13.0 | `5346b83545bf042360eb32691dfc907135d233dd` | Profile-aware composition, Ayra first-profile assurance and coordinated publication |
| TSMM | 0.24.0 | `8ddfd52c876faf368241bc11101681fb1fe49398` | Canonical trust-system semantic authority |
| TIS | 0.15.0 | `edda0e87ced40797d22e3df542099871c57fcb59` | Portable schema and contract authority |

The coordinated release was published after the required human release judgment accepted the frozen tuple and the post-acceptance merged-main `stack-release-eligibility` run succeeded. The release record and retained evidence are under [`stack/releases/2026.3/`](stack/releases/2026.3/).

### Why an adopter benefits

A coordinated Stack release answers the compatibility question before deployment: **which exact versions are known to work together under the declared assurance model?**

For Stack 2026.3 the release gate verifies immutable component resolution, clean-room bootstrap, component evidence generation, deterministic CTS replay, profile-aware producer/consumer boundaries, cross-source composition, provenance and artifact integrity, fail-closed negative cases, whole-stack semantic replay equivalence, and the executable adopter walkthrough.

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

The Hub v1.13.0 line adds a reusable profile-assurance boundary, with the **Ayra TRQP Profile v0.6.0-draft** as the first proving implementation. The governing rule is:

> **Profile assurance extends TRQP assurance; it does not redefine TRQP.**

Profile evaluation preserves independent result dimensions and the bounded states `PASS`, `FAIL`, `INDETERMINATE`, `NOT_APPLICABLE`, and `NOT_IMPLEMENTED`. Missing evidence cannot become `PASS`, an operational error cannot become an authoritative negative trust decision, and governance legitimacy is not inferred from API correctness or DID discovery alone.

The current Ayra projection is version-bound to Ayra `0.6.0-draft`, TRQP `2.0`, and the exact upstream revision recorded in `profiles/ayra/requirements.yaml`. The compatibility analysis against the downstream experimental candidate TRQP v3 is similarly revision-bound and does not treat candidate-v3 work as upstream authority.

See [`profiles/README.md`](profiles/README.md), [`docs/ayra-v3-compatibility.md`](docs/ayra-v3-compatibility.md), and [`docs/ayra-assurance-residual-threats.md`](docs/ayra-assurance-residual-threats.md).

CTS and TSPP expose explicit profile-consumable producer contracts. The Hub consumes those producer-owned results rather than duplicating their authority: CTS owns mapped core conformance results; TSPP owns mapped security/privacy posture results; Ayra remains authoritative for Ayra normative strength; and external governance legitimacy remains dependent on independent authority evidence. Producer `FAIL`, `INDETERMINATE`, stale, missing or otherwise non-current evidence cannot be overridden by a Hub-local positive observation.

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

For coordinated publication, a successful merged-main eligibility run is necessary but not sufficient: the immutable tuple and evidence digest must be recorded and the repository's required visible human release judgment must accept publication. Stack 2026.3 completed that governance path and is now the current published release.

## Adoption and implementation guides

- [`docs/adoption/stack-quickstart.md`](docs/adoption/stack-quickstart.md) — canonical end-to-end Stack workflow.
- [`docs/adoption/stack-2026.3-walkthrough.md`](docs/adoption/stack-2026.3-walkthrough.md) — Stack 2026.3 profile-aware evidence and authority walkthrough.
- [`docs/guides/combined-assurance.md`](docs/guides/combined-assurance.md) — compose CTS and TSPP evidence.
- [`profiles/README.md`](profiles/README.md) — evaluate version-bound ecosystem profiles without collapsing authority boundaries.
- [`docs/guides/evidence-artifacts.md`](docs/guides/evidence-artifacts.md) — evidence artifact model.
- [`docs/guides/public-assurance-publication.md`](docs/guides/public-assurance-publication.md) — publish relying-party-facing assurance.
- [`docs/reference/compatibility-matrix.md`](docs/reference/compatibility-matrix.md) — supported component relationships.
- [`docs/portfolio-integration.md`](docs/portfolio-integration.md) — synchronized portfolio integration.
- [`docs/governance/release-policy.md`](docs/governance/release-policy.md) — component and coordinated Stack release governance.

## Historical coordinated releases

- **TRQP Stack 2026.2 — Ashoka** established assurance validity under change, including invalidation, reassessment, authority drift, supersession and post-change recomposition.
- **TRQP Stack 2026.1 — Coconut** established the first coordinated release baseline.

Historical manifests remain evidence of the exact conditions under which those releases were validated; they are not rewritten when a later Stack release becomes current.

## Release cadence

Component repositories retain independent semantic versioning. Coordinated Stack releases are capability-driven: a new Stack release is published only when a materially useful compatibility/assurance capability has accumulated and the complete tuple passes the release gate.

Each coordinated Stack release receives a randomly selected codename from the Wikipedia list of Indian state trees. The codename is human-facing identity only; the stable machine identity remains `trqp-stack-YYYY.N`.

## Invalidation and supersession

Combined assurance, profile-assurance conclusions and coordinated-release claims are conditional. Missing evidence, invalid producer evidence, changed profile/source revisions, incompatible semantic/schema authorities, failed CTS replay determinism, replay-policy incompatibility, or other declared invalidation conditions can make a conclusion unsuitable for continued use.

Historical manifests and profile evidence remain historical evidence. Changed compatibility or profile conditions require reassessment, a new release, or explicit supersession rather than silent rewriting.

Example or self-generated evidence does not constitute independent assurance, certification, or accreditation.

## License

See [`LICENSE`](LICENSE).
