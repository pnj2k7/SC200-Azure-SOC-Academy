# Lab 14: Make the SOC observable

## 0. Before you start

**Access:** Sentinel workbook authoring rights and cost-reader access; previous custom data.

**Dependencies:** Day 13 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D14-setup, D14-proof, D14-fault, D14-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

The CFO asks whether detection is working and what the data costs. Build an honest dashboard.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Run queries/04-operations.kql and verify event counts by source/action. In Sentinel Workbooks create a training workbook with a 24-hour time parameter, source-volume chart, latest-event table and an incident/alert view if those tables are present.

2. Use an Azure Monitor workbook template from the product UI or a blank workbook. Add a Logs query referencing the intended workspace and WardlightEvents_CL, select a visualization and save in the lab group. Reopen under the analyst identity to test access.

3. Add a second panel showing the last-seen time per source. State that zero events can mean no activity or broken collection. Do not label source event volume as incident count or detection success rate.

4. Inspect SOC optimization recommendations available to the workspace. Record one actionable recommendation with prerequisite, owner, cost implication and how you will verify improvement; mark unavailable recommendations explicitly.

5. Review table plan/retention across Analytics, lake and XDR capabilities. Calculate a hypothetical daily ingestion estimate using the cost worksheet and actual region prices. Compare current measured billed usage with estimates; note billing delay and excluded meters.

6. Prepare a small change proposal: tune collection rather than blindly dropping logs; state which detection and hunting requirements depend on every retained source. Save a before/after workbook screenshot and a rollback plan.

## 4. Prove it

A saved workbook separates collection health, detection outcomes and costs; the analyst can reopen it with scoped access.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Set a workbook panel to an unrelated workspace or to a period before ingestion.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Correct the query scope/time parameter and compare with a direct Logs query. Record how a convincing chart can be wrong. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map B03, B04 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

A dashboard is useful only when its numbers have a clear meaning. A quiet chart could mean there were no events, or that collection stopped working. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing) · [Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard)

[Daily notes](notes.md) · [Practice](../../practice/PQ14.md) · [All days](../index.html)
