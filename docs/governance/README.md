# Documentation freshness policy

This repository treats documentation as a production interface. Tier 0–Tier 1 docs MUST be kept current; CI enforces a freshness SLA using `docs/governance/freshness-policy.yml` and frontmatter metadata.

## Metadata requirements

Tier 0–Tier 1 documents MUST include YAML frontmatter:

```yaml
owner: <team-or-handle>
last_reviewed: YYYY-MM-DD
tier: 0|1|2|3
```

## Enforcement

- CI fails when `last_reviewed` exceeds the SLA threshold for the declared tier.
- Exceptions MUST be tracked as issues and referenced in the PR description.
