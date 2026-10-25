# Lab 1: Open the SOC

## 0. Before you start

**Access:** Azure subscription; Entra tenant; subscription Contributor for deployment; Owner or User Access Administrator only for role assignment.

**Dependencies:** Getting started and account inventory.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D01-setup, D01-proof, D01-fault, D01-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

The hospital CFO approves a small security pilot. Establish identities, scope, and a spending trail before any telemetry flows.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Open portal.azure.com. Record the selected tenant and subscription IDs privately. Use a dedicated training tenant and fictional identities only. Enable MFA for the administrator; keep a separate recovery method. Expected: a fresh sign-in requests MFA.

2. Create a named analyst account in Entra ID. At the lab resource-group scope assign Microsoft Sentinel Reader initially; use Microsoft Sentinel Responder for later incident work and Contributor for rule creation. Record which identity assigns roles. Expected: analyst has no subscription-wide Owner permission.

3. In Cost Management, select the intended subscription and create a monthly budget in your billing currency. Choose an amount you can afford and actual/forecast email thresholds, for example 50%, 80%, 100%. Record the scope and recipients. Expected: budget is visible; this is an alert, not a spending cap.

4. Fill templates/access-matrix.csv for platform, analyst, endpoint operator, Purview investigator, and automation identity. Separate Azure RBAC from Defender unified RBAC, Entra roles and Purview role groups. Test the analyst in a private browser window.

5. Read getting-started.md and inventory the licenses actually available. Mark each day Live, Simulation, or Pending in templates/progress.csv. Do not activate expiring trials until the related teaching block begins.

## 4. Prove it

An analyst can read the lab scope but cannot grant roles; MFA and budget details are documented.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** In the written access matrix accidentally give the analyst Owner. Predict the extra powers; do not grant it in Azure.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Replace Owner with the required scoped Sentinel role, and explain how a Responder differs from Contributor. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map B01 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

A security operations centre is the team that checks warning signs and coordinates a response. Think of it as a hospital control room for digital services. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)

[Daily notes](notes.md) · [Practice](../../practice/PQ1.md) · [All days](../index.html)
