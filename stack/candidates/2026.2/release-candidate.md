# TRQP Stack 2026.2 release candidate freeze

This record freezes the exact Stack 2026.2 release candidate only after all ten additional lifecycle gates have executable evidence.

## Frozen component tuple

- TRQP-TSPP: `stack-2026.2-rc1` at `e952641fe28dd03b8015ed0ce22da053d9160a4a`
- TRQP CTS: `stack-2026.2-rc1` at `da3d1f7b49625c774a17188e0d61f2101dcb1ba5`
- TRQP Assurance Hub: `stack-2026.2-rc1` at `3d60913a04263b3990ca735ecd3161ae081dc449`
- TSMM semantic authority: `v0.24.0`
- TIS portable-contract authority: `v0.15.0` at `edda0e87ced40797d22e3df542099871c57fcb59`

The RC refs are release-candidate anchors, not claims that final component version tags have already been published.

## Freeze rule

Any movement of an RC ref, component commit, TSMM/TIS authority baseline, or release manifest invalidates this freeze and requires a new eligibility replay.

## Human judgment boundary

Freezing the tuple does not itself authorize publication. The clean adopter walkthrough and complete eligibility replay must succeed against this exact tuple before the release decision can be accepted.
