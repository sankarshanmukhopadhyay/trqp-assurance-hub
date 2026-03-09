# Contributing

All contributions must map to requirement IDs, include explicit pass/fail criteria, and produce verifiable evidence.

Use the WG Alignment template for spec mapping proposals.

## Documentation quality gates

This project treats documentation as a production interface.

- Tier 0–Tier 1 docs MUST include YAML frontmatter (`owner`, `last_reviewed`, `tier`).
- CI runs link checking, lightweight doc tests (JSON/YAML parsing + internal link sanity), and freshness SLA enforcement.
- If your change affects APIs, schemas, CLIs, or behavior, you MUST update the relevant docs in the same PR.

See: [`docs/governance/README.md`](docs/governance/README.md)

