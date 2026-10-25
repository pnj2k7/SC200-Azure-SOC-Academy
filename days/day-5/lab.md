# Lab 5: Protect the reception desk

## 0. Before you start

**Access:** Defender for Endpoint Plan 2/equivalent trial entitlement; isolated supported device; appropriate Defender settings/RBAC rights. Intune or supported policy management for ASR.

**Dependencies:** Day 4 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D05-setup, D05-proof, D05-fault, D05-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

Prepare endpoint controls and safe automation settings before the first endpoint case.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. In Defender Settings > Endpoints review licensing and device onboarding. Download the package for the supported lab OS and onboarding method, onboard only the disposable VM, and verify device inventory, sensor health and last-seen timestamp.

2. Create a training device group with a lab-only tag and scoped analyst access. Set an explicit conservative automation level. Test another analyst account and record whether it can read the device and whether response actions are permitted.

3. Review advanced features: live response, automated investigation, EDR in block mode prerequisites, indicators, and device discovery. For each record purpose, permissions, dependencies and actual setting; enable only features used by this lab.

4. Review rule settings such as indicators, alert tuning and exclusions. Create a narrow lab-only rule/indicator with an expiry where supported, inspect scope and remove it after verification. Do not add broad antivirus exclusions.

5. Configure a supported ASR policy in audit mode for the lab group through the available management channel. Record policy ID, scope, device applicability and evaluation. Review custom data collection settings and collect only a benign lab artifact through the supported capability.

6. Configure incident/action/threat-analytics email subscriptions only to your own training mailbox. Review alert correlation, suppression and tuning with an explicit scope and expiry. Document why a broad suppression can hide the next case.

## 4. Prove it

A healthy onboarded device, scoped group permissions and auditable feature/policy settings; simulation users submit the corresponding configuration worksheet.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** In the worksheet change a lab-only suppression to all devices. Identify the visibility loss without applying the change.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Restrict scope and expiry; show a before/after settings comparison and explain why notifications are not the alert engine. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map A01, A02, A03, A04, A05, A06, A09 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

Endpoint protection watches a computer for suspicious behaviour. Configure its rules and permissions before allowing it to take action. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Endpoint pilot](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-defender-endpoint) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ5.md) · [All days](../index.html)
