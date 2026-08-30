# TRQP Stack 2026.2 release candidate freeze

This record freezes the exact Stack 2026.2 release candidate only after all ten additional lifecycle gates have executable evidence and the component releases have immutable version tags.

## Frozen component tuple

- TRQP-TSPP: `v0.16.1` at `12315679dd79bcaced5f27a35bfc1d22560de52d`
- TRQP CTS: `v1.9.1` at `ea3fed33a1edc3313735405f433a23f9d154d903`
- TRQP Assurance Hub: `v1.12.0` at `7f7aae84eb41ffd8ea672dae00955c5714ffd3de`
- TSMM semantic authority: `v0.24.0`
- TIS portable-contract authority: `v0.15.0` at `edda0e87ced40797d22e3df542099871c57fcb59`

The TSPP and CTS patch releases repair clean-room flagship status-contract defects discovered by the adopter walkthrough; lifecycle and reassessment semantics are unchanged from v0.16.0/v1.9.0. Each component version is an immutable annotated Git tag resolving to the exact declared commit.

## Freeze rule

Any movement or replacement of a version tag, component commit, TSMM/TIS authority baseline, or release manifest invalidates this freeze and requires a new eligibility replay.

## Human judgment boundary

Freezing the tuple does not itself authorize publication. The clean adopter walkthrough and complete eligibility replay must succeed against this exact immutable tuple before the release decision can be accepted.
