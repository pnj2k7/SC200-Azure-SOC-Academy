# Lab 9: The suspicious invoice

## 0. Before you start

**Access:** Defender for Office 365 appropriate investigation entitlement, Exchange Online lab mailbox and scoped response roles; otherwise CASE-MAIL simulation.

**Dependencies:** Day 8 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D09-setup, D09-proof, D09-fault, D09-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

A fake supplier invoice reaches a fictional employee. Follow email evidence into the cross-product incident.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Use only a Microsoft-provided safe email tutorial available in your tenant or an innocuous internal lab message. Do not send credential-harvesting links or messages to real recipients. If no safe tutorial exists use CASE-MAIL in the packet.

2. Open Email & collaboration investigation/Explorer or the available email entity view. Search by the lab recipient, UTC interval and NetworkMessageId. Inspect sender, authentication, URLs, attachment verdict and delivery location.

3. Follow URL clicks and associated user/device entities where telemetry is available. Distinguish message delivery, user click, process execution and successful compromise. Save a chronological evidence table with confidence for each claim.

4. In a disposable mailbox inspect available remediation actions and permissions. Quarantine or soft-delete only the known lab message if supported, then verify the action outcome and recovery. Otherwise write the exact proposed action and approval requirement.

5. Inspect automatic attack disruption evidence if present in the supported tutorial. Record the triggering signals, affected entities, action state and rollback; absence of disruption in a single-source test is not a failure to configure it.

6. Create the CASE-MAIL response note linking email ID, account and endpoint case. Recommend one preventive control and one tuning change with a reason tied to the evidence.

## 4. Prove it

A trace from message to entity and verified remediation outcome, or a simulation report that preserves the distinction between suspicion and compromise.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Search using the sender display name alone and compare with the supplied forged display name.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Use immutable message identifiers, actual sender/authentication details and recipient/time boundaries; avoid treating display names as identity proof. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map E01 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

An email’s visible sender name can be misleading. Investigators examine delivery and authentication records and then check what the recipient actually did. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ9.md) · [All days](../index.html)
