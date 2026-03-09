# Contributing

This repository is an onboarding + coordination layer. Most code/test contributions will land in:

- <https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite>
- <https://github.com/sankarshanmukhopadhyay/TRQP-TSPP>

## Good contributions here

- Documentation improvements
- Compatibility matrix updates
- Combined workflow examples
- Issue routing refinements
- Diagrams and explainers that reduce adopter confusion

## How to propose changes

1. Open an issue describing the change and who it helps (implementers, auditors, integrators)
2. Submit a PR referencing the issue
3. Keep changes small and reviewable

## Documentation style

- Prefer concrete steps over abstract prose
- Avoid repo-internal jargon unless defined
- Optimize for “new implementer in a hurry”

## Documentation quality gates

This project treats documentation as a production interface.

- Tier 0–Tier 1 docs MUST include YAML frontmatter (`owner`, `last_reviewed`, `tier`).
- CI runs link checking, lightweight doc tests (JSON/YAML parsing + internal link sanity), and freshness SLA enforcement.
- If your change affects APIs, schemas, CLIs, or behavior, you MUST update the relevant docs in the same PR.

See: [`docs/governance/README.md`](docs/governance/README.md)

