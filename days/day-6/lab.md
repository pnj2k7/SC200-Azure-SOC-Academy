# Lab 6: Investigate the workstation

## 0. Before you start

**Access:** Day 5 live setup, Defender response permissions; otherwise supplied endpoint case cards.

**Dependencies:** Day 5 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D06-setup, D06-proof, D06-fault, D06-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

A benign simulation triggers a device alert. Build a timeline and contain the right entity.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Open Defender Help > Simulations & tutorials and choose an available Microsoft-provided benign endpoint tutorial. Read its scope and cleanup first. Run only on the isolated disposable lab device; never download malware or run credential-theft tools.

2. Open the resulting incident/alert, record IDs and UTC times, and pivot to device timeline. Filter the relevant interval. Capture parent/child process, account, command line, network connection and file hash. Expected: the alert is supported by specific events; labels alone are insufficient.

3. Start or inspect automated investigation if supported. Review evidence verdicts and pending actions in Action center. Document approvals, automation level and device group. Explain automatic attack disruption eligibility and inspect its evidence if a tutorial provides it; do not claim it occurred without a recorded action.

4. Collect an investigation package on the disposable VM. If allowed, use live response to list a benign test file and retrieve it using the supported commands. Record session/action IDs and hash; avoid secrets, patient data and unapproved scripts.

5. If remote access and recovery are proven, isolate the disposable VM, confirm the Action center status and then release isolation. Do not isolate the machine you use to manage the lab. Document timing and what communications remain possible.

6. Reclassify the incident using evidence, assign owner and add a closure note. In simulation mode use CASE-ENDPOINT and explicitly mark all actions as proposed; the sample records are not real Defender telemetry.

## 4. Prove it

A defensible timeline and one reversible device action with before/after state, or a clearly marked response plan when unlicensed.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Use the wrong device name from the case packet in a draft containment request; do not execute it.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Cross-check DeviceId, account and UTC time against the incident; require the exact entity ID before acting. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map A07, A08, F01, F02, F03, F04 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

An alert is a warning to investigate. A timeline helps explain what happened before and after the warning; containment limits further harm. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Endpoint pilot](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-defender-endpoint) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ6.md) · [All days](../index.html)
