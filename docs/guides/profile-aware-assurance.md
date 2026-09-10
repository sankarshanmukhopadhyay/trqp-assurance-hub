---
layout: default
title: Profile-aware TRQP assurance
nav_order: 35
owner: maintainers
last_reviewed: 2026-09-10
---

# Profile-aware TRQP assurance

The TRQP Assurance Hub can evaluate a named ecosystem profile in addition to the underlying TRQP protocol. The first implemented profile is the Ayra TRQP Profile.

The governing rule is:

> **Profile assurance extends TRQP assurance; it does not redefine TRQP.**

The Hub is an assurance composition layer. It does not become specification authority for TRQP or for the ecosystem profile being assessed.

## Authority model

| Layer | Authority | Hub responsibility |
|---|---|---|
| TRQP core protocol | Upstream TRQP specification | Consume/compose protocol-conformance evidence and preserve protocol version/binding provenance |
| Ecosystem profile | Profile publisher, such as Ayra Forum | Maintain a version-bound downstream requirement projection and evaluate profile-owned propositions |
| Protocol conformance evidence | TRQP Conformance Suite | Consume CTS evidence where available; do not redefine CTS-owned core semantics |
| Security/privacy posture | TRQP-TSPP | Consume posture evidence where available; do not redefine TSPP control/posture semantics |
| Profile assurance composition | TRQP Assurance Hub | Resolve profile, determine applicability, bind evidence, aggregate dimensions and publish assurance artifacts |
| Governance legitimacy | Applicable external governance authority/evidence | Report only what evidence supports; absence of external evidence remains indeterminate |

Cross-repository producer-contract follow-up is tracked in CTS issue #40 and TSPP issue #85. Until those integrations are implemented, the Ayra adapter contains deterministic proving observations for some core and posture-adjacent propositions. Those proving observations do not transfer core-conformance or posture authority to the Hub.

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

1. **TRQP core/profile conformance** — protocol and profile requirements that are executable against the target;
2. **Extensions** — optional capabilities and their conditional semantics;
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

## Evidence chain

Every material conclusion should remain traceable through:

```text
normative requirement
  -> assurance proposition
  -> executable observation/test
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

The negative suite attempts to falsify consequential boundaries, including:

- cross-profile or wrong-revision semantic reuse;
- malformed identifiers and Problem Details;
- operational errors masquerading as negative trust decisions;
- incorrect rate-limit and unsupported-extension behaviour;
- unsafe discovered endpoints;
- stale or contradictory authority evidence;
- missing or invalid signing evidence;
- false promotion of governance legitimacy.

Residual threats that deterministic fixtures do not prove are recorded in [Ayra assurance residual threats](../ayra-assurance-residual-threats.md).

## Candidate TRQP v3 compatibility

The current Ayra profile remains a TRQP v2 profile. A separate compatibility matrix compares it with the downstream experimental candidate-v3 work without treating that candidate as upstream authority.

See [Ayra TRQP v2 / candidate-v3 compatibility](../ayra-v3-compatibility.md).

Any change to either pinned source revision requires compatibility reassessment. Historical evidence remains historical; an old matrix must not continue to claim that it represents the current relationship after either source changes.

## Cross-repository next steps

The first Hub implementation intentionally proved the profile boundary before requiring changes in every producer repository. The next integration step is to remove avoidable duplicate observations by consuming producer-owned evidence:

- **CTS #40** — expose profile-consumable protocol-conformance evidence with exact test-set/run/protocol provenance;
- **TSPP #85** — expose profile-aware security/privacy posture evidence and lifecycle/applicability metadata.

This preserves the Stack boundary:

```text
CTS core conformance evidence
        +
TSPP posture evidence
        +
profile-owned constraints / authority evidence
        ↓
Assurance Hub composition
```

The Hub should compose those independent authorities, not replace them.
