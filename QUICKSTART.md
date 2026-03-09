---
owner: maintainers
last_reviewed: 2026-03-06
tier: 0
---

# Quickstart — TRQP Conformance Suite

This guide gets you running the CTS against a TRQP endpoint in under 10 minutes.

## Prerequisites

- Python 3.10+
- A running TRQP endpoint (or use the bundled PoC service)

## 1. Clone and install

```bash
git clone https://github.com/sankarshanmukhopadhyay/trqp-conformance-suite
cd trqp-conformance-suite
pip install -r cts/requirements.txt
```

## 2. Start the example SUT (optional)

If you don't have a TRQP endpoint, start the bundled PoC service:

```bash
pip install fastapi uvicorn pynacl
uvicorn examples.poc_service:app --reload
```

The service will listen on `http://127.0.0.1:8000`.

## 3. Configure the SUT

```bash
cp examples/sut.local.yaml.example examples/sut.local.yaml
```

Edit `examples/sut.local.yaml` to point at your endpoint. For the bundled PoC service the defaults work as-is.

To override test-case identifiers so your real SUT receives its own IDs (instead of `did:example:*` placeholders), add an `identifiers:` block:

```yaml
identifiers:
  authority_id: "did:example:your-authority"
  entity_id: "did:example:your-entity"
  subject_authority_id: "did:example:your-subject-authority"
  action: "your-action"
```

## 4. Preview applicable tests (optional)

```bash
python cts/run.py \
  --profile profiles/baseline.yaml \
  --sut examples/sut.local.yaml \
  --out reports/preview \
  --list-tests
```

## 5. Dry run (optional)

Validate inputs and list tests without making HTTP requests:

```bash
python cts/run.py \
  --profile profiles/baseline.yaml \
  --sut examples/sut.local.yaml \
  --out reports/preview \
  --dry-run
```

## 6. Run the Baseline profile

```bash
python cts/run.py \
  --profile profiles/baseline.yaml \
  --sut examples/sut.local.yaml \
  --out reports/run1
```

Evidence artifacts are written to `reports/run1/`: `verdicts.json`, `bundle_descriptor.json`, `checksums.json`, and `bundle.zip`.

## 7. Run the High-Assurance profile

First generate a local signing key:

```bash
python -c "from nacl.signing import SigningKey; from nacl.encoding import Base64Encoder; print(SigningKey.generate().encode(Base64Encoder).decode())"
```

Add the output as `signing_key_b64` in `examples/sut.local.yaml`, then:

```bash
python cts/run.py \
  --profile profiles/high_assurance.yaml \
  --sut examples/sut.local.yaml \
  --out reports/runHA
```

## Next steps

- Compare output to reference reports in `docs/reference-reports/`
- Combine with TRQP-TSPP for a full combined assurance story
- See the TRQP Assurance Hub for evidence bundle guidance

## Related resources

- Full architecture: `docs/ARCHITECTURE.md`
- Evidence bundle model: `docs/evidence_bundles.md`
- Start-here guide (by role): `docs/START_HERE.md`
- TRQP Assurance Hub: https://github.com/sankarshanmukhopadhyay/trqp-assurance-hub
