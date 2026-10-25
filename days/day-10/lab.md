# Lab 10: Identity crosses the perimeter

## 0. Before you start

**Access:** Entra ID risk investigation entitlement (often P2), Defender for Cloud Apps; optional Defender for Identity with supported AD sensor lab. Licensed or simulation.

**Dependencies:** Day 9 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D10-setup, D10-proof, D10-fault, D10-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

A receptionist account appears in a SaaS alert and an identity alert. Decide what to revoke and why.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Open CASE-IDENTITY. Map account object ID, UPN, session, device and IP. In live Entra inspect sign-in and audit logs for a known test account, including authentication details, Conditional Access result and risk where licensed.

2. Investigate the account entity and any Cloud Apps alert. Inspect app activity, OAuth application permissions, app governance/risk context and affected files. A sanctioned app can still be abused through an excessive permission grant.

3. For a disposable compromised account case choose remediation based on the evidence: revoke sessions, reset credentials and review authentication methods; disable the account only with a recovery plan. Record which action affects sessions, tokens and future sign-ins; verify actual results.

4. In Cloud Apps inspect available session/access policy controls and consent governance actions. For the lab, review rather than revoke a real business application. In the packet propose a scoped consent/app action, owner notification and reauthorization plan.

5. For Defender for Identity use the supported AD sensor lab if available; inspect a sample identity alert, source/destination host and lateral-movement path. Without AD/sensors complete CASE-IDENTITY-AD and mark sensor deployment and live response Pending.

6. Join identity, SaaS and endpoint evidence by stable IDs and UTC interval. Identify a benign travel explanation and test it against MFA, device and token evidence before classifying the case.

## 4. Prove it

An identity/SaaS response plan with distinct Entra, Cloud Apps and on-premises Identity evidence and rollback.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Join on display name instead of object ID in the packet, merging two people with the same name.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Use object ID or normalized UPN with tenant context; document any remaining ambiguity and exclude the false entity link. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map E04, E05, E06 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

An attacker may use a valid account or a connected business application. Changing a password can help, but the investigation also needs to check active access and application permissions. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ10.md) · [All days](../index.html)
