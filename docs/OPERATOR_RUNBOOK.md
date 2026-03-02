# Operator Runbook: Running Combined Assurance

This runbook is an opinionated, operator-friendly path to generate **portable TRQP assurance evidence** using the Conformance Suite (CTS) and the Security & Privacy Baseline (TSPP).

It is designed so an operator can run the workflow, archive outputs, and share evidence with partners, buyers, or assessors.

## What you will produce

At the end of this run you should have:

- A **CTS conformance evidence bundle**
- A **TSPP security & privacy evidence bundle**
- An optional **combined manifest** (index) that points to both bundles

## Pre-flight

1. Choose your target (SUT: system under test)
   - A running TRQP registry / trust list service, or
   - A reference implementation used for smoke testing

2. Create a working directory

Example:

```
assurance-run/
  cts/
  tspp/
  combined/
```

3. Record versions

You MUST record tool versions used for the run (from each repo’s `VERSION` file or release tag).

## Step 1: Run CTS and generate conformance evidence

Follow the CTS README and `docs/START_HERE.md` in the Conformance Suite repository.

Minimum operator expectations:

- Select a profile (baseline first)
- Run CTS against the SUT
- Export the evidence bundle into `assurance-run/cts/`

You should end up with a CTS evidence bundle directory or archive and machine-readable metadata (run context, verdicts, checksums).

## Step 2: Run TSPP and generate security & privacy baseline evidence

Follow the TSPP README and `docs/deployment-guidance.md` in the TSPP repository.

Minimum operator expectations:

- Select the applicable baseline profile
- Run the harness or validation workflow against the SUT
- Export the evidence bundle into `assurance-run/tspp/`

You should end up with a TSPP evidence bundle directory or archive and machine-readable metadata (requirements coverage, results, and checksums).

## Step 3: Create a combined manifest (optional but recommended)

The combined manifest is a lightweight index that makes it easy to share “one package” of evidence.

Use the Hub tooling if you are using the manifest generator. If you are not, create a simple manifest with:

- Tool versions
- SUT identifier and environment
- Timestamp (or run window)
- Paths to CTS and TSPP bundles
- Hashes for top-level bundles

Store this in `assurance-run/combined/combined-manifest.json`.

## Step 4: Validate completeness

- Cross-check evidence expectations in:
  - `docs/guides/evidence-artifacts.md`
  - `docs/guides/assurance-levels.md`
- Confirm you can answer:
  - What profile was run?
  - What was the target?
  - What passed/failed and why?
  - What artifacts exist, and what are their hashes?

## Step 5: Archive and publish (policy-dependent)

Archive the `assurance-run/` directory for your internal governance record.

If publishing to partners, publish:

- Combined manifest (if used)
- CTS and TSPP evidence bundles
- A short “context note” describing the run

## Notes on determinism

This runbook assumes the tooling is being moved toward deterministic automation.

For audit-grade repeatability, prefer:

- pinned dependencies
- stable run identifiers
- stable bundle packaging

These improvements are tracked as part of repository hardening and will be reflected in future releases.
