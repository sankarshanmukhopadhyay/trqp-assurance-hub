import json,subprocess,sys
from pathlib import Path
def test_target_mismatch_fails_closed(tmp_path):
 c={'run_id':'r','target_id':'a','summary':{'PASS':1,'FAIL':0}}; t={'run_id':'r','target_id':'b','summary':{'PASS':1,'FAIL':0}}
 cp=tmp_path/'c.json'; tp=tmp_path/'t.json'; cp.write_text(json.dumps(c)); tp.write_text(json.dumps(t))
 root=Path(__file__).resolve().parents[1]
 p=subprocess.run([sys.executable,str(root/'tools/run_combined_assurance.py'),'--cts-report',str(cp),'--tspp-report',str(tp),'--out',str(tmp_path/'out')],capture_output=True,text=True)
 assert p.returncode!=0 and 'target_id mismatch' in (p.stdout+p.stderr)


def _state(ch):
 return {'algorithm':'sha256','digest':ch*64,'identity':'sha256:'+ch*64,'source':'snapshot.json','status':'verified'}

def test_target_state_mismatch_fails_closed(tmp_path):
 c={'run_id':'r','target_id':'a','target_state':_state('a'),'summary':{'PASS':1,'FAIL':0}}
 t={'run_id':'r','target_id':'a','target_state':_state('b'),'summary':{'PASS':1,'FAIL':0}}
 cp=tmp_path/'c.json'; tp=tmp_path/'t.json'; cp.write_text(json.dumps(c)); tp.write_text(json.dumps(t))
 root=Path(__file__).resolve().parents[1]
 p=subprocess.run([sys.executable,str(root/'tools/run_combined_assurance.py'),'--cts-report',str(cp),'--tspp-report',str(tp),'--out',str(tmp_path/'out')],capture_output=True,text=True)
 assert p.returncode!=0 and 'target_state.digest mismatch' in (p.stdout+p.stderr)

def test_missing_target_state_fails_closed(tmp_path):
 c={'run_id':'r','target_id':'a','summary':{'PASS':1,'FAIL':0}}
 t={'run_id':'r','target_id':'a','target_state':_state('a'),'summary':{'PASS':1,'FAIL':0}}
 cp=tmp_path/'c.json'; tp=tmp_path/'t.json'; cp.write_text(json.dumps(c)); tp.write_text(json.dumps(t))
 root=Path(__file__).resolve().parents[1]
 p=subprocess.run([sys.executable,str(root/'tools/run_combined_assurance.py'),'--cts-report',str(cp),'--tspp-report',str(tp),'--out',str(tmp_path/'out')],capture_output=True,text=True)
 assert p.returncode!=0 and 'CTS target_state missing or unverifiable' in (p.stdout+p.stderr)
