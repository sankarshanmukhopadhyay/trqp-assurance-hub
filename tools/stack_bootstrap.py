#!/usr/bin/env python3
"""Clone the exact tagged component tuple declared by a TRQP stack manifest."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="stack/releases/candidate/manifest.json")
    parser.add_argument("--workspace", default=".stack-work")
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    workspace = Path(args.workspace)
    if args.clean and workspace.exists():
        shutil.rmtree(workspace)
    workspace.mkdir(parents=True, exist_ok=True)

    for name, component in manifest["components"].items():
        target = workspace / name
        if target.exists():
            shutil.rmtree(target)
        url = f"https://github.com/{component['repository']}.git"
        run(["git", "clone", "--quiet", "--depth", "1", "--branch", component["ref"], url, str(target)])
        actual = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=target, text=True).strip()
        if actual != component["commit"]:
            raise SystemExit(f"{name}: expected {component['commit']} but checked out {actual}")
        print(f"[PASS] {name}: {component['ref']} @ {actual}")

    (workspace / "bootstrap-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"[PASS] clean-room stack workspace ready at {workspace}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
