# Lab 18: The hospital incident exercise

## 0. Before you start

**Access:** All previous days or their explicit simulation alternatives; a peer/instructor is useful but not required.

**Dependencies:** Day 17 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D18-setup, D18-proof, D18-fault, D18-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

An independent analyst must reconstruct the full case and defend a proportionate response before the pilot closes.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Start a 90-minute capstone using data/scenario-cards.json without opening the answer key. Declare Live or Simulation per capability. Work from immutable evidence copies; record the start timestamp.

2. Triage CASE-CAPSTONE, select severity and owner, reconstruct at least five stages and identify the deliberately benign service-account pattern. Use saved KQL, entity IDs and UTC time. Do not manufacture alerts for a nicer story.

3. Demonstrate one collection validation, one detection test, one scoped automation outcome, one cross-product investigation and one hunt. Where unlicensed, show the corresponding design/simulation and leave live completion Pending.

4. Deliver a five-minute incident brief to the fictional hospital manager: confirmed findings, uncertainty, patient-service impact, recommended containment, recovery criteria and remaining risk. Attach cost and evidence references.

5. Run the cleanup checklist in cleanup.md. Export only redacted evidence first; disable automation/schedules and disconnect collection, remove lab resources, undo tenant-level changes and cancel/disable trial renewal where appropriate. Verify each control independently.

6. Complete every row of coverage/objective-matrix.csv and templates/progress.csv with evidence path and status. Recheck the official blueprint before booking an exam. A completed course is preparation, not an exam-pass guarantee.

## 4. Prove it

A second reader can reproduce the findings, distinguish live from simulated skills and verify teardown.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Choose two faults from the previous days and diagnose them from evidence without looking at the recorded fixes.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Repair the root cause, re-run the proof and document the difference between restoring telemetry and remediating compromise. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map all capstone objectives to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

The final exercise asks you to explain an incident as a responsible colleague would: use evidence, recognise uncertainty, propose proportionate actions and prove that the lab has been closed safely. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Blueprint](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/sc-200) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)

[Daily notes](notes.md) · [Practice](../../practice/PQ18.md) · [All days](../index.html)
