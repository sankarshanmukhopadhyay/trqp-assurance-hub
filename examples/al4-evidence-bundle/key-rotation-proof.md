# Key rotation proof — example (AL4)

**Rotation event ID:** KEY-ROT-001

## Statement
The operator rotated the signing key used for trust list publication and updated all relevant verifiers/trust list consumers.

## Evidence pointers
- Previous key ID: `kid-2025-12`
- New key ID: `kid-2026-02`
- Rotation timestamp: 2026-02-15T00:00:00Z
- Notification mechanism: publication metadata + operator bulletin

## Verification
- A verifier MUST be able to validate signatures from the rotation boundary.
- Any invalid signature observations MUST be logged and investigated.
