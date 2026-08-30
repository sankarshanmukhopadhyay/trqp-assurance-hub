#!/usr/bin/env python3
"""Validate the repository's cross-repository portfolio integration contract."""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/'portfolio'/'integration-contract.json'; VERSION=ROOT/'VERSION'
EXPECTED_SEMANTIC=('sankarshanmukhopadhyay/trust-systems-meta-model','0.24.0')
EXPECTED_SCHEMA=('sankarshanmukhopadhyay/trust-infrastructure-schemas','0.15.0')
ALL_TRQP={'sankarshanmukhopadhyay/TRQP-TSPP','sankarshanmukhopadhyay/trqp-assurance-hub','sankarshanmukhopadhyay/trqp-conformance-suite'}
REQUIRED_KEYS={'contractVersion','repository','release','role','authority','provides','consumes','evidence','relationships','revocation'}
def result(name,passed,detail): return {'check':name,'passed':passed,'detail':detail}
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--output',type=Path); args=parser.parse_args()
    data=json.loads(CONTRACT.read_text(encoding='utf-8')); release=VERSION.read_text(encoding='utf-8').strip()
    checks=[result('required-keys',REQUIRED_KEYS<=data.keys(),'required contract fields are present'),result('contract-version',data.get('contractVersion')=='1.0','contractVersion must be 1.0'),result('release-pin',data.get('release')==release,f'contract release must equal VERSION ({release})')]
    authority=data.get('authority',{}); semantic=authority.get('semanticAuthority',{}); schema=authority.get('schemaAuthority',{})
    checks.append(result('semantic-authority',(semantic.get('repository'),semantic.get('version'))==EXPECTED_SEMANTIC and bool(semantic.get('artifacts')),'TSMM 0.24.0 must be declared with artifacts'))
    checks.append(result('schema-authority',(schema.get('repository'),schema.get('version'))==EXPECTED_SCHEMA and bool(schema.get('artifacts')),'TIS 0.15.0 must be declared with artifacts'))
    missing=[e.get('path') for e in data.get('evidence',[]) if not (ROOT/e.get('path','')).is_file()]; checks.append(result('evidence-exists',not missing,f'missing evidence: {missing}' if missing else 'all declared evidence exists'))
    repository=data.get('repository'); peers={r.get('repository') for r in data.get('relationships',[])}; checks.append(result('cross-repo-relations',(ALL_TRQP-{repository})<=peers,'both TRQP peer repositories must be declared'))
    revocation=data.get('revocation',{}); checks.append(result('revocation',bool(revocation.get('triggers')) and bool(revocation.get('effect')),'invalidation triggers and effect must be explicit'))
    payload={'valid':all(i['passed'] for i in checks),'repository':repository,'release':release,'contractVersion':data.get('contractVersion'),'authority':authority,'checks':checks}; rendered=json.dumps(payload,indent=2,sort_keys=True)+'\n'; print(rendered,end='')
    if args.output:
        output=args.output if args.output.is_absolute() else ROOT/args.output; output.parent.mkdir(parents=True,exist_ok=True); output.write_text(rendered,encoding='utf-8')
    return 0 if payload['valid'] else 1
if __name__=='__main__': raise SystemExit(main())
