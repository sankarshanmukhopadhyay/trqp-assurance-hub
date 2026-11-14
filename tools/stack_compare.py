#!/usr/bin/env python3
"""Compare two JSON assurance artifacts for semantic equivalence."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

DEFAULT_VOLATILE = {"generated_at", "evaluated_at", "created_at", "timestamp", "run_id"}
PRODUCER_REEXECUTION_VOLATILE = DEFAULT_VOLATILE | {
    "artifacts", "evidence_considered", "decision_id", "issued_at"
}


def canonical(value, volatile=DEFAULT_VOLATILE):
    if isinstance(value, dict):
        return {k: canonical(v, volatile) for k, v in sorted(value.items()) if k not in volatile}
    if isinstance(value, list):
        return [canonical(v, volatile) for v in value]
    return value


def digest(path: Path, *, producer_reexecution: bool = False) -> str:
    volatile = PRODUCER_REEXECUTION_VOLATILE if producer_reexecution else DEFAULT_VOLATILE
    data = canonical(json.loads(path.read_text(encoding="utf-8")), volatile)
    encoded = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("left")
    parser.add_argument("right")
    parser.add_argument("--producer-reexecution", action="store_true",
                        help="Compare independently regenerated producer outcomes while excluding volatile artifact identities")
    args = parser.parse_args()
    left, right = (digest(Path(args.left), producer_reexecution=args.producer_reexecution),
                   digest(Path(args.right), producer_reexecution=args.producer_reexecution))
    if left != right:
        print(f"[FAIL] semantic digests differ: {left} != {right}")
        return 1
    print(f"[PASS] semantic replay equivalent: {left}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
