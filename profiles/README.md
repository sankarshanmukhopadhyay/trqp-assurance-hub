---
layout: default
title: TRQP assurance profiles
nav_exclude: true
---

# TRQP assurance profiles

Profiles extend TRQP assurance without redefining TRQP. The protocol specification remains authoritative for core TRQP semantics; each named profile's upstream source remains authoritative for profile semantics. This repository records version-bound derived assurance propositions and evidence.

Each profile lives under `profiles/<name>/profile.yaml` and MUST validate against `schemas/trqp-profile-contract.schema.json`. The contract binds the profile to a TRQP version and an exact upstream source revision. Requirements are resolved separately so that profile-specific policy cannot silently override generic TRQP behaviour.

## Authority model

| Layer | Authority | Hub responsibility |
|---|---|---|
| TRQP core protocol | Upstream TRQP specification | Consume/compose protocol-conformance evidence and preserve protocol version/binding provenance |
| Ecosystem profile | Profile publisher, such as Ayra Forum | Maintain a version-bound downstream requirement projection and evaluate profile-owned propositions |
| Protocol conformance evidence | TRQP Conformance Suite | Consume CTS evidence; do not redefine CTS-owned core semantics |
| Security/privacy posture | TRQP-TSPP | Consume posture evidence; do not redefine TSPP control/posture semantics |
| Profile assurance composition | TRQP Assurance Hub | Resolve profile, determine applicability, bind evidence, aggregate dimensions and publish assurance artifacts |
| Governance legitimacy | Applicable external governance authority/evidence | Report only what evidence supports; absence of external evidence remains indeterminate |

CTS #40/#46 and TSPP #85/#88 now provide explicit profile-consumable producer contracts. The Hub composes those producer-owned results rather than treating profile metadata as permission to reinterpret them. Deterministic Hub-local observations remain useful for isolated fixture testing, but once applicable producer evidence is supplied it is authoritative for the producer-owned proposition and there is no silent fallback to a conflicting local PASS.

## Resolution

Validate a contract:

```bash
python tools/validate_trqp_profile.py --profile profiles/example/profile.yaml
```

Resolve a registered profile deterministically:

```bash
python tools/validate_trqp_profile.py --id example --version 0.1.0
```

Unknown or ambiguous profile/version pairs fail explicitly. A run with no selected profile continues to use the existing TRQP assurance path.

## Result model

Profile propositions use bounded states:

- `PASS` — sufficient applicable evidence supports the proposition;
- `FAIL` — applicable evidence contradicts a required proposition;
- `INDETERMINATE` — evidence, applicability or authority is insufficient to conclude;
- `NOT_APPLICABLE` — the proposition does not apply to the assessed target/run;
- `NOT_IMPLEMENTED` — an optional capability is absent without being a mandatory failure.

Important invariants are enforced in code and tests:

- missing evidence cannot become `PASS`;
- an operational/transport error cannot become `authorized: false` or `recognized: false`;
- an optional capability that is absent need not become `FAIL`;
- unknown applicability remains `INDETERMINATE`;
- success in one assurance dimension cannot conceal failure or uncertainty in another;
- there is no single unsupported `ayra_compliant: true` boolean.

## Assurance dimensions

The current profile-aware model keeps at least these dimensions visible:

1. **TRQP core/profile conformance** — protocol and profile requirements executable against the target;
2. **Extensions** — optional capabilities and conditional semantics;
3. **Operational** — HTTP/error/rate-limit and related operational observations;
4. **Security** — applicable transport/signing posture observations;
5. **Authority** — DID syntax/resolution, service discovery and governance-discovery evidence.

Governance legitimacy is deliberately not inferred from API correctness, DID syntax, endpoint discovery or controller evidence alone.

## Ayra profile binding

The current Ayra assurance projection is bound to:

- profile: `ayra-trqp`;
- profile version: `0.6.0-draft`;
- profiled TRQP version: `2.0`;
- Ayra source revision: `ec7768572592b50ba3f4102c026c2449148b5e11`.

Executable assessment first verifies this binding. A different profile identity, version or source revision is not silently assessed using the pinned Ayra semantics.

## Producer evidence composition

For CTS-owned core propositions, the Hub can consume the CTS profile-consumable contract and map exact CTS test results into the profile proposition graph. The current Ayra mapping includes:

| Ayra proposition | CTS producer observation |
|---|---|
| `PROP-AYRA-CORE-001` | `TC-AUTHZ-001` |
| `PROP-AYRA-CORE-002` | `TC-RECOG-001` |

A CTS `FAIL` remains `FAIL`. `REASSESS_REQUIRED`, `INVALID`, protocol/binding mismatch, or missing mapped evidence becomes `INDETERMINATE` for the Hub profile conclusion; the Hub does not revive an older local fixture result to manufacture a positive conclusion.

TSPP uses the equivalent producer boundary for security/privacy posture. Profile-relevant TSPP lifecycle state remains producer-owned and cannot be weakened by Hub profile metadata.

## Evidence chain

Every material conclusion should remain traceable through:

```text
normative requirement
  -> assurance proposition
  -> producer/local observation
  -> captured evidence
  -> dimension result
  -> published assurance conclusion
```

The reproducible Ayra bundle generator emits:

```text
assurance.json
assurance.md
requirement-results.json
authority-evidence.json
endpoint-evidence.json
negative-tests.json
provenance.json
```

Machine evidence is authoritative over the rendered Markdown report. The report is generated from machine state and tested for semantic consistency.

## Reproducible fixture run

The repository CI exercises the representative Ayra fixture path. A local deterministic bundle can be produced with:

```bash
python -m tools.build_ayra_assurance_bundle \
  tests/fixtures/ayra/conformant.json \
  tests/fixtures/ayra/authority-success.json \
  --run-id ayra-local-001 \
  --observed-at 2026-09-10T15:30:00Z \
  --out /tmp/ayra-bundle
```

This fixture demonstrates the evidence pipeline. It is not independent certification or a claim about any production Ayra registry.

## Adversarial coverage

The negative suite attempts to falsify consequential boundaries, including cross-profile or wrong-revision semantic reuse, malformed identifiers and Problem Details, operational errors masquerading as negative trust decisions, incorrect rate-limit and unsupported-extension behaviour, unsafe discovered endpoints, stale or contradictory authority evidence, missing or invalid signing evidence, false promotion of governance legitimacy, stale producer evidence, and producer-result override attempts.

Residual threats that deterministic fixtures do not prove are recorded in [`docs/ayra-assurance-residual-threats.md`](../docs/ayra-assurance-residual-threats.md).

## Candidate TRQP v3 compatibility

The current Ayra profile remains a TRQP v2 profile. A separate compatibility matrix compares it with the downstream experimental candidate-v3 work without treating that candidate as upstream authority.

See [`docs/ayra-v3-compatibility.md`](../docs/ayra-v3-compatibility.md).

Any change to either pinned source revision requires compatibility reassessment. Historical evidence remains historical; an old matrix must not continue to claim that it represents the current relationship after either source changes.

## Cross-repository composition

The producer boundary is now:

```text
CTS core conformance evidence
        +
TSPP posture evidence
        +
profile-owned constraints / authority evidence
        ↓
Assurance Hub composition
```

The Hub composes those independent authorities; it does not replace them.

## Authority boundary

A profile adapter MAY add tests for profile constraints and extensions. It MUST NOT mutate the meaning of TRQP core requirements. Assurance output must preserve protocol and profile conclusions separately, and missing evidence must never be promoted to success.
