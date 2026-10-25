"""Local evidence analysis; reads synthetic data only."""
from pathlib import Path
from collections import Counter
import json
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'data/events.json').read_text(encoding='utf-8'))
counts=Counter(e['Account'] for e in data if e['Action']=='SignInFailed')
print('Failed sign-ins by account:')
for account,count in sorted(counts.items()): print(f'{account}: {count}')
suspects={a for a,n in counts.items() if n>=5}
print('\nPost-failure events requiring investigation:')
for e in sorted(data,key=lambda r:r['TimeGenerated']):
    if e['Account'] in suspects and e['Action'] in ('SignInSucceeded','ProcessCreated','FileAccessed'):
        print(e['TimeGenerated'],e['EventId'],e['Action'],e['Account'])
print('\nAn accessed export is not proof of a completed transfer.')
