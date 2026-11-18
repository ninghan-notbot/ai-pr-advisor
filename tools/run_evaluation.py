"""Actual native-session evaluation; no API keys, forced skill mentions or file-read hints."""
import argparse,datetime as dt,hashlib,json,os,subprocess,time,threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

stop=threading.Event()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def run_case(project,fixture,condition,out,model,disabled_skills=()):
    folder=out/(fixture['id']+'-'+condition);folder.mkdir(parents=True,exist_ok=False)
    installed=project/'.agents/skills/ai-pr-advisor'
    payload={str(p.relative_to(installed)):sha(p) for p in installed.rglob('*') if p.is_file()} if installed.exists() else {}
    assert bool(payload)==(condition!='plain')
    meta=dict(scenario=fixture['id'],condition=condition,model_requested=model,reasoning_effort='medium',
        host_version=subprocess.check_output(['codex','--version'],text=True).strip(),
        started_at=dt.datetime.now(dt.timezone.utc).isoformat(),method='native_session_resume',
        forced_skill_invocation=False,forced_file_read=False,web_mode=fixture.get('web_mode','disabled'),skill_sha256=payload,
        fixture_sha256=hashlib.sha256(json.dumps(fixture,ensure_ascii=False,sort_keys=True).encode()).hexdigest(),
        disabled_skills=list(disabled_skills),turns=[])
    sid=None
    for i,prompt in enumerate(fixture['turns'],1):
        if stop.is_set():meta['stopped']='subscription_or_auth_failure_in_batch';break
        (folder/f'turn-{i}.input.txt').write_text(prompt)
        output=folder/f'turn-{i}.output.md'
        cmd=['codex','exec','--ignore-user-config','--model',model,'-c','model_reasoning_effort="medium"',
             '--strict-config','-c','skills.config=['+','.join('{name='+json.dumps(name)+',enabled=false}' for name in disabled_skills)+']','-c','developer_instructions='+json.dumps('For this consultation, use only the host native web search/browse tools for external research. Do not run third-party search CLIs, call external model or metered APIs, install software, read authentication secrets, send messages, purchase anything, or modify production systems. If native web tools are disabled or unavailable, continue conditionally without accessing the network by another route. Local file reads for installed knowledge are allowed.'),'-c','web_search='+json.dumps(fixture.get('web_mode','disabled')),'--sandbox','read-only','--json','-C',str(project),'--output-last-message',str(output)]
        cmd+=['resume',sid,'-'] if sid else ['-']
        started=time.monotonic()
        try:
            r=subprocess.run(cmd,input=prompt,text=True,capture_output=True,timeout=420,
                env={k:v for k,v in os.environ.items() if k not in {'OPENAI_API_KEY','ANTHROPIC_API_KEY','TAVILY_API_KEY','GH_TOKEN','GITHUB_TOKEN'}})
            (folder/f'turn-{i}.events.jsonl').write_text(r.stdout)
            (folder/f'turn-{i}.stderr.log').write_text(r.stderr)
            events=[]
            for line in r.stdout.splitlines():
                try:events.append(json.loads(line))
                except json.JSONDecodeError:pass
            threads=[e['thread_id'] for e in events if e.get('type')=='thread.started']
            current=threads[0] if threads else sid
            forbidden=[e for e in events if e.get('type')=='item.completed' and e.get('item',{}).get('type')=='command_execution' and any(t in e['item'].get('command','') for t in ['tvly search','tvly research','api.openai.com','api.anthropic.com'])]
            if forbidden:
                meta['environment_violation']='forbidden_external_service_command';stop.set()
            if sid and current and sid!=current:raise RuntimeError('Native session changed unexpectedly')
            sid=current
            ok=r.returncode==0 and output.exists() and bool(output.read_text().strip())
            meta['turns'].append(dict(turn=i,status='CAPTURED' if ok else 'FAILED',exit_code=r.returncode,
                seconds=round(time.monotonic()-started,2),session_id=sid,input_sha256=sha(folder/f'turn-{i}.input.txt'),
                output_sha256=sha(output) if output.exists() else None))
            if not ok:
                if any(x in (r.stdout+r.stderr).lower() for x in ['usage limit','quota','not authenticated','sign in']):stop.set()
                break
        except subprocess.TimeoutExpired as e:
            decode=lambda x:x.decode(errors='replace') if isinstance(x,bytes) else x or ''
            (folder/f'turn-{i}.events.jsonl').write_text(decode(e.stdout));(folder/f'turn-{i}.stderr.log').write_text(decode(e.stderr))
            meta['turns'].append(dict(turn=i,status='TIMEOUT'));break
    meta['complete']=len(meta['turns'])==len(fixture['turns']) and all(t['status']=='CAPTURED' for t in meta['turns'])
    (folder/'run.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'scenario':fixture['id'],'condition':condition,'complete':meta['complete'],'turns':len(meta['turns'])}),flush=True)
    return meta

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--work',type=Path,required=True);p.add_argument('--fixtures',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--conditions',nargs='+',default=['plain','skill']);p.add_argument('--model',default='gpt-6-astra')
    p.add_argument('--disable-skill',metavar='NAME',action='append',default=[],
        help='Disable a locally installed skill by name; repeat as needed (default: none)')
    a=p.parse_args();fixtures=json.loads(a.fixtures.read_text());a.out.mkdir(parents=True,exist_ok=False)
    jobs=[(a.work/(c+'-project'),f,c,a.out,a.model,a.disable_skill) for n,f in enumerate(fixtures) for c in (a.conditions if n%2==0 else a.conditions[::-1])]
    with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(lambda x:run_case(*x),jobs))
    (a.out/'batch.json').write_text(json.dumps({'runs':len(results),'complete':sum(x['complete'] for x in results),'forced_read':False,'added_paid_api':False},indent=2)+'\n')
