#!/usr/bin/env python3
from pathlib import Path
import argparse, json, hashlib, yaml
from jsonschema import Draft202012Validator

from cts_determinism import DeterminismEvidenceError, assurance_projection, load_and_validate

p = argparse.ArgumentParser()
p.add_argument('--cts-report', required=True)
p.add_argument('--cts-determinism-report', default=None)
p.add_argument('--tspp-report', required=True)
p.add_argument('--out', default='artifacts/combined-assurance')
p.add_argument('--release-set', default='ots-2026-08')
a = p.parse_args()

r = Path(__file__).resolve().parents[1]
c = json.loads(Path(a.cts_report).read_text())
t = json.loads(Path(a.tspp_report).read_text())
out = Path(a.out)
out.mkdir(parents=True, exist_ok=True)


def eq(k):
    if c.get(k) != t.get(k):
        raise SystemExit(f'fail-closed: {k} mismatch: {c.get(k)!r} != {t.get(k)!r}')


def status(d):
    s = d.get('summary', {})
    return 'fail' if int(s.get('FAIL', 0) or 0) > 0 else ('pass' if int(s.get('PASS', 0) or 0) > 0 else 'indeterminate')


eq('run_id')
eq('target_id')
reg = yaml.safe_load((r / 'data/compatibility-registry.yaml').read_text())
rel = next((x for x in reg['release_sets'] if x['id'] == a.release_set and x['status'] == 'supported'), None)
if not rel:
    raise SystemExit('fail-closed: unsupported release tuple')

# CTS v1.8+ release tuples require independently auditable replay-determinism evidence.
cts_determinism = None
if rel.get('requires', {}).get('cts_replay_determinism'):
    if not a.cts_determinism_report:
        raise SystemExit('fail-closed: supported release tuple requires --cts-determinism-report')
    try:
        raw_determinism = load_and_validate(a.cts_determinism_report)
    except DeterminismEvidenceError as exc:
        raise SystemExit(f'fail-closed: {exc}') from exc
    cts_determinism = assurance_projection(raw_determinism)

cs, ts = status(c), status(t)
outcome = 'fail' if 'fail' in (cs, ts) else ('pass' if cs == ts == 'pass' else 'indeterminate')
now = '2026-08-22T00:00:00Z'
arts = []
for role, path in [('cts', Path(a.cts_report)), ('tspp', Path(a.tspp_report))]:
    arts.append({'role': role, 'path': str(path), 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
if a.cts_determinism_report:
    p_det = Path(a.cts_determinism_report)
    arts.append({
        'role': 'cts_replay_determinism',
        'path': str(p_det),
        'sha256': hashlib.sha256(p_det.read_bytes()).hexdigest(),
    })

producer_results = {'cts': cs, 'tspp': ts}
if cts_determinism:
    producer_results['cts_replay_determinism'] = 'pass'

manifest = {
    'schema_version': '1.1',
    'release_set': rel,
    'run_id': c['run_id'],
    'target_id': c['target_id'],
    'artifacts': arts,
    'producer_results': producer_results,
}
if cts_determinism:
    manifest['cts_replay_determinism'] = cts_determinism

dec = {
    'schema_version': '1.0',
    'decision_id': f"decision:{c['run_id']}",
    'outcome': outcome,
    'scope': 'TRQP conformance, CTS evidence reproducibility, and TSPP posture evidence composition',
    'target': c['target_id'],
    'evidence_considered': arts,
    'conditions': [],
    'limitations': ['This conclusion evaluates supplied evidence and is not external certification.'],
    'findings': [],
    'issued_at': now,
    'expires_at': None,
    'supersedes': None,
    'revoked': False,
    'revocation_reason': None,
}
if cts_determinism:
    dec['conditions'].append(
        'CTS replay determinism is valid only under the recorded comparison policy identity, version, and SHA-256.'
    )

(out / 'combined-assurance-manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
(out / 'assurance-decision.json').write_text(json.dumps(dec, indent=2) + '\n')
Draft202012Validator(json.loads((r / 'schemas/assurance-decision.schema.json').read_text())).validate(dec)
(out / 'traceability-report.json').write_text(json.dumps({
    'run_id': c['run_id'],
    'target_id': c['target_id'],
    'chain': [
        'TRQP requirement',
        'CTS test',
        'CTS evidence',
        'CTS replay determinism policy and report',
        'TSPP control',
        'TSPP evidence',
        'Hub assurance decision',
    ],
    'remediation_targets': {
        'conformance': 'trqp-conformance-suite',
        'reproducibility': 'trqp-conformance-suite',
        'posture': 'TRQP-TSPP',
        'composition': 'trqp-assurance-hub',
    },
}, indent=2) + '\n')
print(f'combined assurance: {outcome}; CTS replay determinism: {"pass" if cts_determinism else "not-required"}')
