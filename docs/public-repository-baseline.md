# Public repository baseline

This record captures controls reviewed under issue #53. It is repository assurance evidence, not external certification.

| Control | State | Evidence | Residual risk |
|---|---|---|---|
| Purpose/maturity/adoption/authority | PASS | `README.md`, `PROJECT-STATUS.yaml`, `GOVERNANCE.md` | None identified. |
| Licensing/release provenance | PASS | `LICENSE`, `NOTICE`, `CHANGELOG.md`, `CITATION.cff` | Publication remains maintainer judgment. |
| Security reporting/supported versions | PASS | `SECURITY.md` | Hosted private-reporting enablement remains platform evidence. |
| Contribution/community/support | PASS | `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SUPPORT.md` | None identified. |
| Dependency update management | PASS | `.github/dependabot.yml`, `.github/DEPENDABOT_AUTOMERGE.md` | Hosted Dependabot enablement remains platform evidence. |
| Default-branch governance | PASS | active `protect-main` observed 2026-09-05: PRs, conversation resolution, linear history, delete/non-fast-forward protection, strict required `validate`, no bypass actors | Required check name must remain synchronized with CI. |
| Assurance evidence integrity | PASS | validation tooling, assurance-level and combined-assurance docs | Workflow green is not itself an assurance conclusion. |
| Authority boundary | PASS | `GOVERNANCE.md`, combined-assurance guidance | Hub does not acquire TSPP protocol or registry operational authority. |

## Completion boundary

The applicable public-repository baseline is complete when the associated remediation PR merges with required checks green. Hosted GitHub security-feature enablement is not inferred from repository files.
