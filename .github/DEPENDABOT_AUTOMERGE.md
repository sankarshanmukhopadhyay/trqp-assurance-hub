# Dependabot automatic merge policy

This repository uses policy-gated automatic merging for low-risk Dependabot pull requests.

## Eligible updates

| Ecosystem | Patch | Minor | Major |
|---|---:|---:|---:|
| GitHub Actions | Automatic after required checks | Automatic after required checks | Manual review |

The workflow only enables GitHub's native auto-merge facility. It does not bypass branch rules, required status checks, required reviews, or merge queue controls.

## Authority and scope

- **Authorised actor:** `dependabot[bot]` only.
- **Permitted ecosystem:** GitHub Actions.
- **Permitted update classes:** semantic-version patch and minor updates.
- **Excluded updates:** major-version changes and updates that Dependabot cannot classify as eligible.
- **Merge method:** merge commit.

## Enforcement boundary

The `main` branch ruleset remains authoritative. Configure required checks for the repository's assurance, quality, and documentation build workflows before enabling repository auto-merge.

Recommended required checks include:

- `combined-assurance`
- `markdown_lint`
- `link_check`
- `validate`
- the Pages `build` job when documentation paths are changed

Do not require the Pages `deploy` job for pull requests because deployment is intentionally suppressed on pull-request events.

## Repository setting

Enable native auto-merge in:

`Settings → General → Pull Requests → Allow auto-merge`

Without this setting, the workflow cannot place an eligible pull request into the auto-merge state.

## Revocation

Automatic merge authority can be revoked by any of the following controls:

1. Disable or delete `.github/workflows/dependabot-automerge.yml`.
2. Disable **Allow auto-merge** in repository settings.
3. Tighten the eligibility conditions in the workflow.
4. Disable Dependabot version updates in `.github/dependabot.yml`.

## Evidence and auditability

Each decision produces machine-verifiable evidence through:

- Dependabot pull-request metadata;
- the `Dependabot policy-gated auto-merge` workflow run;
- required status-check results;
- branch-ruleset evaluation; and
- the resulting merge commit and pull-request timeline.

## Validation procedure

1. Enable **Allow auto-merge** in repository settings.
2. Confirm the `main` ruleset requires all relevant checks.
3. Allow Dependabot to open a patch or minor GitHub Actions update.
4. Confirm the workflow enables auto-merge but does not merge before required checks pass.
5. Confirm a failed required check leaves the pull request open.
6. Confirm a major update remains outside the automatic merge policy.
