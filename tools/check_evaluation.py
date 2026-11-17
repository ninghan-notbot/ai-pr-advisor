#!/usr/bin/env python3
"""Check native-session evidence; never grade advice by length or certify professional quality."""
import argparse, hashlib, json
from pathlib import Path

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def observed_reads(events, files):
    commands = [e['item'] for e in events if e.get('type') == 'item.completed'
                and e.get('item', {}).get('type') == 'command_execution'
                and e['item'].get('exit_code') == 0]
    text = '\n'.join(c.get('aggregated_output', '') for c in commands)
    return sorted(name for name, body in files.items() if body.strip() and body.strip() in text)

def validate_run(folder, fixture, project):
    meta = json.loads((folder/'run.json').read_text()); failures=[]; evidence=[]; sessions=set(); all_reads=set()
    expected_fixture=hashlib.sha256(json.dumps(fixture,ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    if meta.get('fixture_sha256') != expected_fixture: failures.append('fixture_mismatch')
    installed=project/'.agents/skills/ai-pr-advisor'
    files={str(p.relative_to(installed)):p.read_text() for p in installed.rglob('*') if p.is_file()} if installed.exists() else {}
    hashes={name:hashlib.sha256(body.encode()).hexdigest() for name,body in files.items()}
    if hashes != meta.get('skill_sha256'): failures.append('payload_mismatch')
    if meta.get('forced_skill_invocation') or meta.get('forced_file_read'): failures.append('not_natural_invocation')
    for i,prompt in enumerate(fixture['turns'],1):
        inp=folder/f'turn-{i}.input.txt';out=folder/f'turn-{i}.output.md';ev=folder/f'turn-{i}.events.jsonl'
        if not all(p.exists() for p in [inp,out,ev]) or len(meta['turns'])<i:
            failures.append(f'turn_{i}_missing'); continue
        t=meta['turns'][i-1]
        if inp.read_text()!=prompt or digest(inp)!=t.get('input_sha256'): failures.append(f'turn_{i}_input_mismatch')
        if not out.read_text().strip() or digest(out)!=t.get('output_sha256'): failures.append(f'turn_{i}_output_mismatch')
        events=[json.loads(line) for line in ev.read_text().splitlines() if line.strip()]
        ids={e['thread_id'] for e in events if e.get('type')=='thread.started'}
        sessions.update(ids)
        if not ids or ids!={t.get('session_id')}: failures.append(f'turn_{i}_session_mismatch')
        if not any(e.get('type')=='turn.completed' for e in events):failures.append(f'turn_{i}_not_completed')
        reads=observed_reads(events,files);all_reads.update(reads)
        evidence.append(dict(turn=i,actual_files_read=reads,output_sha256=digest(out)))
    if len(sessions)!=1: failures.append('session_not_continuous')
    if not meta.get('complete'): failures.append('incomplete_run')
    return dict(scenario=fixture['id'],condition=meta['condition'],integrity='PASS' if not failures else 'FAIL',
        failures=failures,native_skill_body_read='SKILL.md' in all_reads,actual_files_read=sorted(all_reads),turns=evidence)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--runs',type=Path,required=True)
    p.add_argument('--fixtures',type=Path,required=True);p.add_argument('--projects',type=Path,required=True)
    a=p.parse_args();fixtures={x['id']:x for x in json.loads(a.fixtures.read_text())};results=[];settings=set()
    for run in sorted(a.runs.iterdir()):
        if not run.is_dir() or not (run/'run.json').exists():continue
        meta=json.loads((run/'run.json').read_text());settings.add((meta['model_requested'],meta['reasoning_effort'],meta['host_version']))
        results.append(validate_run(run,fixtures[meta['scenario']],a.projects/(meta['condition']+'-project')))
    failures=[] if len(settings)==1 else ['model_settings_differ']
    report=dict(status='PASS' if results and not failures and all(r['integrity']=='PASS' for r in results) else 'FAIL',
        settings=sorted(settings),failures=failures,professional_quality='NOT_GRADED',results=results)
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if report['status']!='PASS':raise SystemExit(1)
if __name__=='__main__':main()
