# Lab 11: Find the data trail

## 0. Before you start

**Access:** Microsoft Purview Audit/eDiscovery and relevant DLP/insider-risk entitlements; Purview role groups and legal authorization in the lab. Synthetic data only.

**Dependencies:** Day 10 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D11-setup, D11-proof, D11-fault, D11-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

A fictional export might contain patient identifiers. Investigate audit, content, Graph and Purview signals without touching real records.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Create a harmless file containing WL-PATIENT-0001 in a disposable SharePoint/OneDrive training location if licensed. Record owner, timestamp and synthetic classification. Never use actual patient data or identify a real employee as an insider.

2. In Purview Audit run a bounded search for the lab user, workload, UTC interval and relevant file actions. Export only minimal results. Record operation, actor, object ID and correlation information; allow audit availability delays.

3. Create a lab eDiscovery case using the currently available Content search workflow. Assign an authorized case investigator, select only the training location and search the unique WL-PATIENT-0001 marker. Preview/search statistics before any export. Record role/licensing limits and delete the lab case after evidence capture where allowed.

4. Inspect a Purview alert/case from the lab or CASE-DATA. Distinguish content discovery, a DLP policy match and an insider-risk finding. Propose scoped remediation, data-owner involvement and evidence preservation without assuming intent.

5. Review Microsoft Graph activity logging prerequisites and diagnostics for your tenant. If enabled query MicrosoftGraphActivityLogs for the lab app/user/time and correlate request metadata with audit activity. Graph activity records are not file-content search results. If the table is absent document setup requirements and use the packet.

6. Build a data-access timeline from audit, content-search result metadata, Graph request evidence and DLP case. Label certainty and minimize exports. Record retention, access restrictions and deletion dates in the evidence pack.

## 4. Prove it

Three distinct evidence types are used correctly: audit activity, content discovery and Graph request logs, plus a justified Purview response.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Use a Content search hit as proof the user downloaded the file.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Obtain the corresponding audit action and correlate actor/object/time; the search hit proves content presence, not the download. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map E02, G01, G02, G03 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

Finding a file and proving that someone downloaded it are different tasks. Use the right record for each question and collect only the information the investigation needs. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ11.md) · [All days](../index.html)
