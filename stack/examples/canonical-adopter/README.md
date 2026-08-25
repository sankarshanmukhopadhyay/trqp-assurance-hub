# Canonical TRQP stack adopter case

This fixture is the adopter-facing reference target for coordinated TRQP Stack release eligibility. It exists to prove that a new adopter can start from the Assurance Hub, resolve one declared component tuple, run the three repositories, and inspect evidence without independently choosing compatible versions.

## Decisive test

A stack candidate is eligible only when the following are demonstrated against the declared immutable component tuple:

1. the release tuple resolves to the declared tags and commits;
2. a clean workspace can bootstrap all three components;
3. TSPP and CTS execute their assurance surfaces;
4. CTS replay evidence is deterministic under its declared comparison policy;
5. the Hub consumes correlated evidence and fails closed on invalid inputs;
6. provenance and integrity are preserved; and
7. the documented walkthrough remains executable.

The target descriptor in `target.json` is deliberately small: it defines the shared identity and expected cross-stack properties while the authoritative producer fixtures and evidence semantics remain in TSPP and CTS.

## Run

From the Assurance Hub repository root:

```bash
make stack-release-check
```

For an explicit clean-room run:

```bash
python tools/stack_validate.py --check-remote
python tools/stack_bootstrap.py --clean
python tools/stack_evaluate.py
```

These commands produce candidate validation evidence only. They do not publish or imply a coordinated TRQP Stack release.
