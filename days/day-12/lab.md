# Lab 12: Defend the cloud workload

## 0. Before you start

**Access:** Defender for Cloud enabled only for an explicitly selected lab workload plan; subscription security permissions; optional sample alerts.

**Dependencies:** Day 11 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D12-setup, D12-proof, D12-fault, D12-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

A workload protection alert points to the application server. Separate a posture weakness from an active incident.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. In Defender for Cloud inventory the subscriptions and enabled plans. Record the exact resource scope, trial dates and meters. Enable only the required lab plan after checking price; do not enable every plan on an existing subscription.

2. Inspect recommendations and secure score separately from security alerts. Pick a lab recommendation and record the preventive weakness, resource ID, owner and remediation; it is not automatically evidence of exploitation.

3. Use the product sample-alert facility if available for your enabled plan. Otherwise open CASE-CLOUD. Record alert name, resource ID, time, severity, evidence and affected workload; label sample alerts explicitly.

4. Investigate the resource through Defender for Cloud and its XDR incident integration where configured. Correlate AzureActivity and available endpoint/network evidence to determine who changed configuration and what occurred inside the VM.

5. Draft a containment change for the disposable resource: remove only an unintended exposure or stop the lab workload after preserving needed evidence. If performing it, capture before/after settings and restoration steps; never block your sole management channel.

6. Disable the trial/plan enabled solely for this segment when done and record the confirmation. Review other workloads for inherited plan settings, extensions and possible continuing charges.

## 4. Prove it

A workload incident report distinguishes sample alert, posture recommendation, actual evidence and verified containment.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Treat the secure-score recommendation as proof of a successful intrusion in the draft incident report.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Separate exposure from observed behavior; identify the missing telemetry and revise the confidence level. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map E03 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

A weak door lock and evidence that someone entered are different findings. Cloud security tools report both weaknesses and suspicious activity; the response must distinguish them. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)

[Daily notes](notes.md) · [Practice](../../practice/PQ12.md) · [All days](../index.html)
