import json
import subprocess
import sys
from pathlib import Path


def state(ch):
    return {
        "algorithm": "sha256",
        "digest": ch * 64,
        "identity": "sha256:" + ch * 64,
        "source": "snapshot.json",
        "status": "verified",
    }


def write_report(path, *, producer, digest="a"):
    if producer == "cts":
        payload = {
            "run_id": "r1",
            "target_id": "target-1",
            "target_state": state(digest),
            "suite_version": "1.11.1",
            "profile_id": "baseline",
            "summary": {"PASS": 1, "FAIL": 0},
        }
    else:
        payload = {
            "run_id": "r1",
            "target_id": "target-1",
            "target_state": state(digest),
            "tool_version": "0.18.1",
            "assurance_level": "AL1",
            "summary": {"PASS": 1, "FAIL": 0},
        }
    path.write_text(json.dumps(payload), encoding="utf-8")


def run_manifest(tmp_path, cts_digest="a", tspp_digest="a"):
    root = Path(__file__).resolve().parents[1]
    cts = tmp_path / "cts.json"
    tspp = tmp_path / "tspp.json"
    out = tmp_path / "manifest.json"
    write_report(cts, producer="cts", digest=cts_digest)
    write_report(tspp, producer="tspp", digest=tspp_digest)
    proc = subprocess.run(
        [
            sys.executable,
            str(root / "tools/generate-manifest.py"),
            "--build-id",
            "build-1",
            "--target",
            "fixture://target-1",
            "--cts-report",
            str(cts),
            "--tspp-report",
            str(tspp),
            "--out",
            str(out),
        ],
        capture_output=True,
        text=True,
    )
    return proc, out


def test_manifest_carries_verified_shared_target_state(tmp_path):
    proc, out = run_manifest(tmp_path)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    manifest = json.loads(out.read_text(encoding="utf-8"))
    assert manifest["build"]["target_state"]["digest"] == "a" * 64
    assert manifest["build"]["target_state"]["status"] == "verified"


def test_manifest_rejects_target_state_mismatch(tmp_path):
    proc, out = run_manifest(tmp_path, cts_digest="a", tspp_digest="b")
    assert proc.returncode != 0
    assert "target_state.digest mismatch" in (proc.stdout + proc.stderr)
    assert not out.exists()


def test_manifest_rejects_missing_target_state(tmp_path):
    root = Path(__file__).resolve().parents[1]
    cts = tmp_path / "cts.json"
    tspp = tmp_path / "tspp.json"
    out = tmp_path / "manifest.json"
    write_report(cts, producer="cts")
    write_report(tspp, producer="tspp")
    c = json.loads(cts.read_text(encoding="utf-8"))
    c.pop("target_state")
    cts.write_text(json.dumps(c), encoding="utf-8")
    proc = subprocess.run(
        [
            sys.executable,
            str(root / "tools/generate-manifest.py"),
            "--build-id",
            "build-1",
            "--target",
            "fixture://target-1",
            "--cts-report",
            str(cts),
            "--tspp-report",
            str(tspp),
            "--out",
            str(out),
        ],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "CTS target_state missing" in (proc.stdout + proc.stderr)
    assert not out.exists()
