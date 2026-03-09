# Verify Evidence Bundles

This guide explains how to verify conformance evidence bundles produced by the TRQP Conformance Suite.

Evidence bundles are designed to support **independent verification**:
- integrity of artifacts (hash manifest)
- authenticity of the manifest (signature, High-Assurance)
- reproducibility and auditability (state reference, High-Assurance)

---

## Evidence bundle layout

Typical output directory:

```
reports/<run-id>/
  bundle_descriptor.json
  run.json
  verdicts.json
  manifest.json
  manifest.sig          (High-Assurance only)
  signing_public_key.pem (High-Assurance only, if provided)
  cases/
  bundle.zip
```

---

## Step 1: Verify integrity using `manifest.json`

`manifest.json` contains hashes of artifacts. Recompute hashes and compare.

### Option A: Quick Python verifier (recommended)

Run from the evidence directory (the folder that contains `manifest.json`):

```bash
python - <<'PY'
import json, hashlib, pathlib, sys

base = pathlib.Path(".")
m = json.loads((base/"manifest.json").read_text())
algo = m.get("hash_alg","sha256")
files = m["files"]

def h(path):
    d = getattr(hashlib, algo)()
    with open(path,"rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            d.update(chunk)
    return d.hexdigest()

bad = []
missing = []
for rel, expected in files.items():
    p = base/rel
    if not p.exists():
        missing.append(rel); continue
    got = h(p)
    if got.lower() != expected.lower():
        bad.append((rel, expected, got))

if missing:
    print("MISSING:"); [print(" -", x) for x in missing]
if bad:
    print("MISMATCH:")
    for rel, exp, got in bad:
        print(f" - {rel}\n   expected {exp}\n   got      {got}")
if not missing and not bad:
    print("OK: manifest hashes match artifacts")
PY
```

### Option B: Spot-check with sha256sum (Linux/macOS)

```bash
sha256sum run.json verdicts.json manifest.json
```

This does not validate the full manifest mapping but is useful for quick sanity checks.

---

## Step 2: Verify signature (High-Assurance)

High-Assurance runs may include:
- `manifest.sig` (signature bytes)
- `signing_public_key.pem` (Ed25519 public key)

### Verify Ed25519 signature using Python

Run from the evidence directory:

```bash
python - <<'PY'
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey

pub = serialization.load_pem_public_key(open("signing_public_key.pem","rb").read())
sig = open("manifest.sig","rb").read()
msg = open("manifest.json","rb").read()

pub.verify(sig, msg)
print("OK: signature valid for manifest.json")
PY
```

If verification fails, treat the bundle as **tampered or unauthenticated** unless you have an alternative trust mechanism for the manifest.

---

## Step 3: Confirm state reference (High-Assurance)

High-Assurance conformance depends on stable registry state.

Inspect `run.json` and confirm it contains a `state_reference` value under the SUT section.

Example:

```json
{
  "sut": {
    "endpoint": "https://sut.example.org",
    "version": "1.2.3",
    "state_reference": "snapshothash:abc123"
  }
}
```

If `state_reference` is missing, treat the run as **insufficient for deterministic semantic claims**.

---

## Notes

- Baseline runs may be unsigned and may not include a strong state reference. That is expected.
- High-Assurance runs SHOULD be signed and MUST include state reference (as required by the profile).
- Evidence verification is intended to be straightforward and tool-agnostic. If you add new artifact types, update `manifest.json` generation and the evidence bundle schema accordingly.
