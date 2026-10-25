# Lab 7: Engineer a reliable detection

## 0. Before you start

**Access:** Sentinel Contributor; custom table from Day 4. Defender custom detections require licensed Advanced Hunting access.

**Dependencies:** Day 6 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D07-setup, D07-proof, D07-fault, D07-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

Turn the recurring failed-sign-in pattern into a tested signal, without flooding the SOC.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Open queries/01-failure-burst.kql. Run it against the custom table; verify the baseline count and the benign service account in the answer key. Then run queries/00-synthetic.kql in Logs for an ingestion-independent comparison.

2. Create a scheduled Sentinel analytics rule named WL-Lab-FailureBurst. Use the provided production-table query, frequency 5 minutes, lookback 15 minutes, threshold above zero. Map Account from Account and Host from Device, and IP from IP where present. Add a lab tag, severity and a relevant ATT&CK technique only after checking the behavior.

3. Configure event grouping and incident creation. Generate a fresh sample batch once with make_sample_data.py and ingest it, wait for a rule run, then verify alert and incident IDs. Query output alone is not proof that scheduling and incident generation work.

4. Compare NRT, scheduled, threat-intelligence and available machine-learning rule templates. Inspect each template prerequisite and supported tables. Deploy NRT only with an eligible query; enable a supplied ML template only if prerequisites and cost are acceptable. Record unsupported options as design-only.

5. Review anomalies and SOC ATT&CK coverage; compare tactics covered by installed rules against telemetry actually arriving. Record a blind spot, a missing source and the control to address it. An installed rule with no data is not effective coverage.

6. In Defender Advanced Hunting build queries/03-xdr-process.kql and retain Timestamp, DeviceId and ReportId as required for that event source. Use Create detection rule with supported frequency and scoped device selection; inspect run history, edit and disable the rule after proof. Do not use the synthetic custom-table query as a Defender custom detection.

## 4. Prove it

Rule query, entity mapping, scheduled-run outcome and tuning rationale are saved; XDR and Sentinel rule lifecycles are distinguished.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Raise the threshold above the sample event count in a disabled copy of the rule. Predict the missed incident.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Restore the documented threshold and test both suspicious and benign sample accounts. Explain false-positive and false-negative consequences. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map D01, D02, D03, D04, D05 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

A detection is a repeatable test for a suspicious pattern. Like a smoke detector, it needs testing: sensitivity that is too high creates noise, while too low can miss danger. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst) · [Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard)

[Daily notes](notes.md) · [Practice](../../practice/PQ7.md) · [All days](../index.html)
