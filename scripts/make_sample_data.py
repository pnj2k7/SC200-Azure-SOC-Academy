"""Refresh synthetic lab data; stdlib only. Does not send data or create resources."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import Counter
import json
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).replace(microsecond=0)
events=[]
def add(minutes,source,account,device,ip,action,detail,correlation):
    events.append(dict(TimeGenerated=(now-timedelta(minutes=minutes)).isoformat().replace('+00:00','Z'),EventId=f'E{len(events)+1:02}',Source=source,Account=account,Device=device,IP=ip,Action=action,Detail=detail,CorrelationId=correlation))
add(12,'Email','maya@wardlight.example','','203.0.113.50','EmailDelivered','Fictional supplier invoice; message WL-MSG-001','CASE-INVOICE')
for x in range(8):add(11-x*.2,'Identity','maya@wardlight.example','WL-RECEPTION-01','203.0.113.50','SignInFailed','Disposable lab account failure','CASE-INVOICE')
add(8,'Identity','maya@wardlight.example','WL-RECEPTION-01','203.0.113.50','SignInSucceeded','Authentication details require further evidence','CASE-INVOICE')
add(6,'Endpoint','maya@wardlight.example','WL-RECEPTION-01','203.0.113.50','ProcessCreated','powershell.exe -Command Write-Output WL-LAB','CASE-INVOICE')
add(3,'Data','maya@wardlight.example','WL-RECEPTION-01','203.0.113.50','FileAccessed','WL-PATIENT-0001 export accessed; transfer unconfirmed','CASE-INVOICE')
for x in range(3):add(10-x,'Identity','svc-backup@wardlight.example','WL-BACKUP-01','192.0.2.20','SignInFailed','Known stale credential after scheduled rotation','CASE-BENIGN')
add(5,'Cloud','engineer@wardlight.example','WL-APP-01','192.0.2.30','ResourceTagged','Approved lab tag change CHG-001','CASE-CLOUD')
(root/'data').mkdir(exist_ok=True)
(root/'data/events.json').write_text(json.dumps(events,indent=2)+'\n',encoding='utf-8')
answer={'rows':len(events),'suspicious_failures':8,'benign_failures':3,'failure_burst_accounts':['maya@wardlight.example'],'correlation_event_ids':['E10','E11','E12'],'actions':dict(Counter(e['Action'] for e in events)),'conclusion':'Sequence supports investigation, not confirmed exfiltration or malware execution.'}
(root/'data/answer-key.json').write_text(json.dumps(answer,indent=2)+'\n',encoding='utf-8')
fields=['TimeGenerated:datetime','EventId:string','Source:string','Account:string','Device:string','IP:string','Action:string','Detail:string','CorrelationId:string']
lines=[]
for e in events:
    # Relative timestamps keep the standalone query useful after its generation day.
    offset=int((now-datetime.fromisoformat(e['TimeGenerated'].replace('Z','+00:00'))).total_seconds())
    values=[f'datetime({e["TimeGenerated"]})']+[json.dumps(e[k]) for k in list(e)[1:]]
    lines.append('  '+', '.join(values))
query='// Standalone synthetic exercise. No ingestion or built-in product tables required.\nlet Events = datatable('+', '.join(fields)+')[\n'+',\n'.join(lines)+'\n];\nEvents\n| where Action == "SignInFailed"\n| summarize Failures=count() by Account, Device, IP\n| where Failures >= 5\n'
(root/'queries/00-synthetic.kql').write_text(query.replace('\\n','\n'),encoding='utf-8')
print(f'Generated {len(events)} synthetic records. Nothing was uploaded.')
