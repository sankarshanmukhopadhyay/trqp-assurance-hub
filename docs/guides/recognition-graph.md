# Recognition graph semantics

Recognition relationships are rarely isolated.
In real ecosystems they form a **recognition graph**: registries recognize other registries, operators, auditors, and authorities within scoped trust frameworks.

This guide defines lightweight semantics for reasoning about recognition graphs **without** redefining TRQP transport.

## Nodes

Common node types (non-normative):

- Registry
- Operator
- Auditor / assessor
- Authority (policy issuer)
- Trust framework

Nodes should be referenced using stable identifiers (DID, URL, or URN).

## Edges

Edges are expressed as **Recognition Assertions**.

- `recognizes` — issuer asserts reliance on the subject within a scope.
- `recognizes_with_conditions` — issuer relies on the subject if conditions hold.
- `does_not_recognize` — issuer asserts non-reliance.
- `revoked` — issuer revokes a previously asserted recognition.

## Scope boundaries

Recognition is only meaningful when bounded.
Scopes should include at least:

- `domain` (trust framework or ecosystem boundary)
- optionally `jurisdictions` and `credential_types`

## Propagation expectations

This repo does not mandate transitive trust.

However, implementers should expect verifiers and ecosystem participants to apply practical rules:

- Recognition is **not** automatically transitive.
- Conditional recognition may be treated as active only when conditions are met and evidence is current.
- Revocation of a recognition edge should trigger re-evaluation of dependent edges.

## Minimal scenario

Example scenario:

- Registry A recognizes Registry B (scope: Framework X, IN).
- Registry A recognizes Auditor C.
- Registry A recognizes Registry B **with conditions**, requiring B to publish control satisfaction.

In this setup, verifiers can:

- inspect the recognition assertion,
- verify evidence references,
- check lifecycle state and revocation status,
- decide whether to rely on Registry B outputs.
