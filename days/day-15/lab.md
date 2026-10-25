# Lab 15: Hunt beyond the alert

## 0. Before you start

**Access:** KQL-capable Logs workspace for synthetic path; licensed Advanced Hunting for live XDR path.

**Dependencies:** Day 14 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D15-setup, D15-proof, D15-fault, D15-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

There is no new alert, but the threat report suggests a suspicious process and a reused identity.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Write a hypothesis before querying: a user with a failed-logon burst later ran a suspicious lab process and accessed an export. State expected evidence, benign alternatives and falsification criteria.

2. Run queries/00-synthetic.kql in Sentinel Logs, inspect the output and compare with data/answer-key.json. Then adapt queries/02-correlation.kql against the ingested custom table. Explain where, project, summarize, bin and join.

3. In Defender Advanced Hunting use getschema or the built-in schema panel to choose DeviceProcessEvents, DeviceNetworkEvents, DeviceLogonEvents or EmailEvents for your question. Run queries/03-xdr-process.kql only in the correct service; an absent table means missing product/data, not KQL syntax failure.

4. Read an available Threat analytics report and distinguish reported actor behavior, your actual exposure and observed activity. Adapt a hunt to available fields/time windows and document the report date and relevance.

5. Save the Sentinel hunt, add an appropriate ATT&CK mapping and run it. Bookmark relevant real lab events if supported, attach notes/entities and link to a lab incident. Record query execution, findings and next run; a negative hunt result is valid evidence.

6. Promote a hunt to a detection proposal only after testing baseline noise, source availability, schedule, identifiers and operational owner. Save both the suspicious result and a benign counterexample.

## 4. Prove it

A tested hypothesis, correct table choice, saved hunt and negative/positive interpretation with evidence.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Replace a case-insensitive comparison with a case-sensitive exact match that drops a known variant in the synthetic query.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Normalize the relevant field or use the appropriate operator; test the counterexample and explain the performance/precision tradeoff. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map H01, H02, H03, H04, I01 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

Hunting starts with a question, such as whether an account behaved unusually, even when no alert has appeared. A good hunt tests both suspicious and harmless explanations. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ15.md) · [All days](../index.html)
