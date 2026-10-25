# Lab 3: Windows tells its story

## 0. Before you start

**Access:** Sentinel plus one isolated supported Windows lab VM; AMA and DCR management rights. VM costs apply.

**Dependencies:** Day 2 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D03-setup, D03-proof, D03-fault, D03-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

A reception workstation reports repeated failed logons. Collect useful Windows evidence without collecting everything.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Create one small supported Windows VM in the lab group if your budget allows. Use Azure Run Command for benign commands and keep public RDP closed; do not expose a password-based login to the internet. Record VM, disk and network charges.

2. Install the Windows Security Events via AMA solution from Content hub. In its connector create a DCR, associate only the lab VM, and select a documented event set or a custom XPath for required Security events. Expected: association names the intended VM; the AMA extension reports healthy.

3. Check Windows audit policy for successful/failed logon events using auditpol /get /category:*. Save the current policy before any change. Generate one harmless failed login against a disposable local test account, followed by a successful login. Avoid real accounts and repeated lockouts.

4. Query Heartbeat | where TimeGenerated > ago(1h), then SecurityEvent | where TimeGenerated > ago(2h) | where EventID in (4624,4625). Compare Computer and account fields with the VM. Expected: heartbeat and relevant Security events after delivery.

5. Design a WEF alternative: source-initiated subscriptions, domain/group policy prerequisites, collector subscription, WinRM/authentication, ForwardedEvents channel, and AMA collection from the collector. In a supplied domain lab configure it; without AD, submit the design and mark WEF as design-only.

6. Document a troubleshooting tree: VM association > agent health > audit policy > XPath/channel > egress > workspace/time. Save a minimal collection decision and privacy justification.

## 4. Prove it

Trace a test failure from Windows Security log to SecurityEvent; produce a WEF plan with clear prerequisites.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Temporarily query EventID 4626 instead of 4625; for a live DCR fault use a duplicate training DCR only, never the sole collection path.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Correct the filter, rerun with a wider time window, and show why a healthy heartbeat alone does not prove Security-event delivery. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map C01, C02, C03 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

A workstation can record successful and failed sign-ins, much like a reception access register. We choose which entries to collect so the register remains useful. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ3.md) · [All days](../index.html)
