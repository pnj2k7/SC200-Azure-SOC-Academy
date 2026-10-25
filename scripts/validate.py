"""Meaningful local integrity checks; does not claim live cloud execution."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
import csv,json,ast
root=Path(__file__).resolve().parents[1]
errors=[]
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('href','src') and v:self.links.append(v)
pages=[p for p in root.rglob('*.html') if '_site' not in p.parts]
for p in pages:
    parser=Links();parser.feed(p.read_text(encoding='utf-8'))
    for url in parser.links:
        u=urlsplit(url)
        if u.scheme or url.startswith(('#','//')):continue
        target=(p.parent/unquote(u.path)).resolve()
        if not target.exists():errors.append(f'Broken link: {p.relative_to(root)} -> {url}')
for p in root.rglob('*.py'):
    if '_site' not in p.parts:
        try:ast.parse(p.read_text(encoding='utf-8'))
        except SyntaxError as e:errors.append(f'Python syntax: {p}: {e}')
rows=list(csv.DictReader((root/'coverage/objective-matrix.csv').open(encoding='utf-8')))
expected={f'{g}{i:02}' for g,n in {'A':11,'B':4,'C':7,'D':5,'E':10,'F':4,'G':3,'H':6,'I':4}.items() for i in range(1,n+1)}
if len(rows)!=54 or {r['id'] for r in rows}!=expected:errors.append('Objective mapping does not exactly match the 54 baseline indices.')
for r in rows:
    if not 1<=int(r['day'])<=18:errors.append('Invalid mapped day '+r['id'])
    lab=(root/f'days/day-{r["day"]}/lab.md').read_text(encoding='utf-8')
    if r['id'] not in lab:errors.append('Objective not referenced in mapped lab: '+r['id'])
for n in range(1,19):
    for rel in ('index.html','lab.md','notes.md','slides/briefing.html','plays/quiz.html','artefacts/decision.html'):
        if not (root/f'days/day-{n}'/rel).exists():errors.append(f'Missing day {n} {rel}')
events=json.loads((root/'data/events.json').read_text(encoding='utf-8'))
answer=json.loads((root/'data/answer-key.json').read_text(encoding='utf-8'))
if len(events)!=16 or len({e['EventId'] for e in events})!=16:errors.append('Synthetic event IDs/count invalid.')
if dict(Counter(e['Action'] for e in events))!=answer['actions']:errors.append('Answer key action counts differ.')
counts=Counter(e['Account'] for e in events if e['Action']=='SignInFailed')
if sorted(a for a,n in counts.items() if n>=5)!=answer['failure_burst_accounts']:errors.append('Failure burst answer differs.')
nb=json.loads((root/'notebooks/case-correlation.ipynb').read_text(encoding='utf-8'))
scope={}
for cell in nb['cells']:
    if cell['cell_type']=='code':
        import os
        old=Path.cwd();os.chdir(root)
        try:exec(''.join(cell['source']),scope)
        finally:os.chdir(old)
if errors:
    print('\n'.join(errors));raise SystemExit(1)
print(f'PASS: {len(pages)} HTML pages, 18 day structures, 54 exact objective indices, links, Python syntax, synthetic counts and notebook execution.')
print('Azure deployment, KQL service execution and licensed portal actions remain unverified locally.')
