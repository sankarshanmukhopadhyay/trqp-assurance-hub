# Control objectives

Assurance levels become useful when they can be audited without interpretive dance.

This repo introduces a **candidate control catalog** and a **Control Satisfaction Declaration** artifact.
The goal is to make assurance commitments machine-readable at control granularity.

## Control catalog

The candidate catalog is published as JSON:

- [`tools/control-catalog.json`](../../tools/control-catalog.json)

Each control has:

- a stable `id`,
- a short `name`,
- an `objective` statement.

## Control Satisfaction Declaration

Publishers can claim control status using:

- Schema: [`schemas/control-satisfaction.schema.json`](../../schemas/control-satisfaction.schema.json)
- Example: [`examples/control-satisfaction.example.json`](../../examples/control-satisfaction.example.json)

Statuses are:

- `satisfied`
- `partially_satisfied`
- `not_satisfied`
- `not_applicable`

Each control can reference evidence artifacts (policies, audits, manifests).

## Binding to the Assurance Profile

The Assurance Profile can declare:

- `controls.control_ids` — the in-scope controls for this profile.
- `controls.satisfaction_declaration_ref` — a reference to the satisfaction artifact.

This makes assurance level claims composable and verifiable.
