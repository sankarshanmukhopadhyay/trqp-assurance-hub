---
owner: maintainers
last_reviewed: 2026-08-25
tier: 0
---

# Release Policy

The TRQP Assurance Hub is the adoption front door and coordinated-release authority for the TRQP Operational Trust Stack. Releases must demonstrate usable assurance value, not routine activity.

## Release classes

| Class | Allowed when | Example |
|---|---|---|
| Patch | Security fix, broken CI, broken internal link, schema regression, incorrect release metadata | `v1.11.1` |
| Minor | New adopter-facing Hub capability with tests, documentation, and evidence impact | `v1.12.0` |
| Coordinated Stack | A validated Hub/CTS/TSPP compatibility tuple provides meaningful adopter value or a capability/compatibility change makes a new tuple necessary | `TRQP Stack 2026.1 — Coconut` |
| No release | Typo, prose polish, non-substantive link rearrangement, exploratory notes | Batch into next milestone |

Component releases retain independent semantic versioning. A component release does not automatically cause a coordinated Stack release.

## Coordinated Stack cadence

The target cadence is approximately monthly when meaningful capability has accumulated. A coordinated release may be cut earlier when a capability, compatibility, security, evidence, or authority change makes a newly validated tuple materially necessary for adopters.

The release decision is capability-driven rather than calendar-driven: a month may pass without a Stack release when there is no meaningful new adopter contract to publish.

## Coordinated Stack naming

Each coordinated Stack release receives:

- a stable machine identity of the form `trqp-stack-YYYY.N`;
- a human-facing title of the form `TRQP Stack YYYY.N — <codename>`; and
- a randomly selected codename from the Wikipedia **List of Indian state trees**.

The codename is descriptive release identity only and carries no protocol, assurance-level, or authority semantics. The selected common and scientific names are recorded in the immutable Stack manifest so release naming remains auditable.

## Required release evidence

Every Hub component release must provide:

- a compatibility tuple for Hub, CTS, and TSPP;
- validation commands and outcomes in `docs/release-validation.md` or the release note;
- a documentation impact summary;
- an evidence impact summary covering produced, consumed, or validated artifacts; and
- an adoption impact summary for at least one role: implementer, assessor, operator, relying party, or governance steward.

Every coordinated Stack release must additionally provide:

- a machine-readable immutable Stack manifest;
- exact component tags and commit SHAs;
- pinned TSMM/TIS authority versions;
- a successful `stack-release-eligibility` workflow on the merged release baseline;
- the workflow run identifier and candidate evidence artifact digest;
- a clean-room bootstrap result;
- deterministic CTS replay evidence;
- whole-stack semantic replay equivalence;
- fail-closed negative-case evidence;
- an executable adopter walkthrough; and
- synchronized adopter-facing documentation across the Hub, CTS, and TSPP entry points.

## Release blockers

A release must not be cut when:

- required validation commands fail;
- the decisive coordinated-release workflow is missing or not green for a Stack release;
- README version or compatibility metadata is inconsistent with the declared component releases;
- cross-repository compatibility references disagree;
- a schema, example, manifest, or producer contract changes without corresponding documentation;
- new assurance claims are prose-only and not tied to machine-verifiable evidence; or
- the release record cannot identify the authority, scope, provenance, evidence, and invalidation conditions behind its claims.

## Authority and supersession

The Hub may declare that a particular component tuple has passed coordinated integration and assurance gates. This does not transfer TSPP control authority, CTS conformance/replay authority, TSMM semantic authority, TIS schema/portfolio authority, or upstream TRQP specification authority to the Hub.

A coordinated release is immutable historical evidence. When compatibility or assurance conditions change, publish a new Stack release or explicitly supersede the prior release; do not rewrite the historical tuple.

## Red-team release provenance and publication integrity

A coordinated release must verify the exact eligibility workflow ID/path, successful execution on the declared merged-main commit, required mapped gate-step conclusions, and an unedited human acceptance comment authored by the declared decision authority. The workflow must preserve a cryptographic content digest for each published release asset and attach an artifact provenance attestation. Repackaging the Actions eligibility artifact produces different bytes and a different digest; the publication `SHA256SUMS` binds the final assets, while the eligibility manifest retains its own distinct source-artifact digest. Historic Lotus artifacts are not retroactively signed.

Release workflows have narrowly scoped write permission; dependency updates affecting release controls require manual review rather than privileged `pull_request_target` auto-merge. A passing stack gate demonstrates release-pipeline eligibility, not positive conformance of its intentionally failing reference target, and is not independent deployment certification.

### Publication validator reproducibility

The privileged publication job installs an explicit, pinned release-validator dependency set after checking out the validated merged-main commit. It produces attestation subjects from files in the workflow workspace and verifies the release manifest, executed eligibility steps, and human judgment before release creation. The human judgment may bind the immutable machine tag or the equivalent explicitly named coordinated release identity; the recorded workflow ID, commit, evidence digest, and acceptance statement are always mandatory. A successful PR test of the verifier does not replace a production exercise of the attestation/publication workflow; that evidence is required before the next coordinated release is declared complete.

## Independent verification for a future coordinated publication

Download the manifest, evidence zip and `SHA256SUMS` from the *same* published release tag and run `sha256sum -c SHA256SUMS` in that directory. Verify the GitHub build-provenance attestation against the expected source repository/workflow identity and those final asset digests using `gh attestation verify` with an appropriate identity policy. Compare the immutable manifest to its recorded eligibility run ID, verified merged-main SHA, successful mapped decisive-test steps and authorized human judgment. If any source, signature, revocation/currentness or release asset is unavailable, that part of the assurance conclusion remains unverified.

The October Lotus artifacts predate the attestation workflow and are not retroactively signed. Successful CI tests verify the code's expected behavior, **not** successful live publication of a new signed release. The first release to use the strengthened publication workflow must retain its live attestation and consumer-verification results as release evidence.

## Eligibility dependency provenance

The coordinated eligibility workflow constrains Python dependencies to exact versions observed in the successful 2026-11-14 main eligibility run. It disallows implicit pip upgrades, verifies dependency consistency with `pip check`, and retains the resolved environment in its release-evidence artifact. This reduces resolver drift for the next candidate, but the constraints are **not a hash-locked, hermetic software supply-chain attestation**. Future release readiness must assess full distribution hashes and trusted-index provenance as warranted by its threat model; a version pin alone cannot authenticate downloaded code. The release's build-provenance attestation refers to final workflow assets and is distinct from third-party dependency integrity.
