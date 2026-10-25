# Lab 13: Run the incident bridge

## 0. Before you start

**Access:** Sentinel Responder and appropriate XDR incident permissions; previous evidence packs or complete synthetic case packet.

**Dependencies:** Day 12 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D13-setup, D13-proof, D13-fault, D13-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

Join the invoice, identity, endpoint and data signals into a case the hospital can act on.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Open a lab Sentinel/XDR incident or CASE-CAPSTONE. Assign an owner, severity, status and classification reason. Record alert IDs, incident IDs, UTC boundaries and source products rather than relying on a single title.

2. Use entity pages, investigation graph/timeline and linked alerts to reconstruct email > identity > endpoint > data access. A proposed relationship must cite the event that supports it. Identify at least one false correlation.

3. Create a case using the case-management capability available in your tenant; if unavailable use templates/incident-report.md. Add timeline, evidence references, working hypotheses, tasks, owners, next update time and decision log.

4. Build a containment sequence that preserves hospital availability: verify identity, contain test endpoint, restrict suspicious session/app access, then validate the data exposure. Distinguish actions already completed from proposals awaiting approval.

5. Review the Sentinel alert/incident details and automation audit trail. Ensure cross-product alerts are not being counted as independent intrusions merely because the same event appears in several products.

6. Hold a 10-minute incident bridge: analyst states evidence and uncertainty; service owner states clinical impact; incident lead records decision and rollback. Close only after the acceptance criteria and residual risk are recorded.

## 4. Prove it

A reproducible multi-stage timeline and managed case with evidence-linked decisions, owners and recovery checks.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** The packet gives one device’s timestamp in local time. Build the draft timeline without normalizing it and identify the contradiction.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Normalize to UTC, retain original timezone and event IDs, then re-evaluate causality. Temporal proximity alone does not prove lateral movement. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map E07, E09, E10 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

A case connects the warnings, evidence, decisions and people responsible. It should let a colleague understand what is confirmed, what is uncertain and what happens next. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ13.md) · [All days](../index.html)
