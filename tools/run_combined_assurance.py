#!/usr/bin/env python3
from pathlib import Path
import argparse,json,hashlib,datetime,yaml
from jsonschema import Draft202012Validator
p=argparse.ArgumentParser(); p.add_argument('--cts-report',required=True); p.add_argument('--tspp-report',required=True); p.add_argument('--out',default='artifacts/combined-assurance'); p.add_argument('--release-set',default='ots-2026-07'); a=p.parse_args()
r=Path(__file__).resolve().parents[1]; c=json.loads(Path(a.cts_report).read_text()); t=json.loads(Path(a.tspp_report).read_text()); out=Path(a.out); out.mkdir(parents=True,exist_ok=True)
def eq(k):
 if c.get(k)!=t.get(k): raise SystemExit(f'fail-closed: {k} mismatch: {c.get(k)!r} != {t.get(k)!r}')
eq('run_id'); eq('target_id')
reg=yaml.safe_load((r/'data/compatibility-registry.yaml').read_text()); rel=next((x for x in reg['release_sets'] if x['id']==a.release_set and x['status']=='supported'),None)
if not rel: raise SystemExit('fail-closed: unsupported release tuple')
def status(d):
 s=d.get('summary',{}); return 'fail' if int(s.get('FAIL',0) or 0)>0 else ('pass' if int(s.get('PASS',0) or 0)>0 else 'indeterminate')
cs,ts=status(c),status(t); outcome='fail' if 'fail' in (cs,ts) else ('pass' if cs==ts=='pass' else 'indeterminate')
now='2026-07-20T00:00:00Z'; arts=[]
for role,path in [('cts',Path(a.cts_report)),('tspp',Path(a.tspp_report))]: arts.append({'role':role,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
manifest={'schema_version':'1.0','release_set':rel,'run_id':c['run_id'],'target_id':c['target_id'],'artifacts':arts,'producer_results':{'cts':cs,'tspp':ts}}
dec={'schema_version':'1.0','decision_id':f"decision:{c['run_id']}",'outcome':outcome,'scope':'TRQP conformance and TSPP posture evidence composition','target':c['target_id'],'evidence_considered':arts,'conditions':[],'limitations':['This conclusion evaluates supplied evidence and is not external certification.'],'findings':[],'issued_at':now,'expires_at':None,'supersedes':None,'revoked':False,'revocation_reason':None}
(out/'combined-assurance-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n'); (out/'assurance-decision.json').write_text(json.dumps(dec,indent=2)+'\n')
Draft202012Validator(json.loads((r/'schemas/assurance-decision.schema.json').read_text())).validate(dec)
(out/'traceability-report.json').write_text(json.dumps({'run_id':c['run_id'],'target_id':c['target_id'],'chain':['TRQP requirement','CTS test','CTS evidence','TSPP control','TSPP evidence','Hub assurance decision'],'remediation_targets':{'conformance':'trqp-conformance-suite','posture':'TRQP-TSPP','composition':'trqp-assurance-hub'}},indent=2)+'\n')
print(f'combined assurance: {outcome}')
