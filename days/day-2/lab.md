# Lab 2: Build the evidence room

## 0. Before you start

**Access:** Day 1 complete; Azure deployment permissions; Sentinel onboarding permission. Azure-only live path.

**Dependencies:** Day 1 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D02-setup, D02-proof, D02-fault, D02-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

Create the Sentinel workspace and capture the first harmless cloud control-plane change.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Open Azure Cloud Shell in Bash. Upload infra/main.bicep. Select the subscription with az account set --subscription YOUR_ID, then check az account show. Use the commands in infra/README.md; run what-if before deployment. Expected: only the dedicated resource group receives resources.

2. Deploy the workspace, Sentinel onboarding, custom table and direct-ingestion DCR using main.bicep. Record outputs locally. This does not deploy VMs, subscription diagnostic settings, role grants, or tenant products. Expected: law-wardlight-soc and WardlightEvents_CL exist.

3. Open security.microsoft.com, select Settings > Microsoft Sentinel > Workspaces, and verify the workspace. If onboarding is not automatic, follow the official onboarding guide linked below. Record the portal and workspace you actually used.

4. In Sentinel Content hub install Azure Activity. Open its connector and configure subscription Activity Logs through diagnostic settings or the connector Azure Policy workflow. Select only the lab subscription and target workspace. Policy assignment and remediation require additional rights; record the managed identity and scope.

5. Change the lab resource-group tag Drill=Day2. In Logs query AzureActivity | where TimeGenerated > ago(2h) | take 20. Allow delivery time before retrying. Expected: a successful tag/resource write with your caller and resource ID; absence is a connector problem to diagnose, not proof of no activity.

6. Review table retention and available Analytics, lake and XDR tiers. Save a retention design for 30-day hot investigation and longer historical hunting; choose live settings based on your budget and supported minimums. Do not enable the data lake yet. Record each table plan and retention explicitly.

## 4. Prove it

A real Activity event is searchable, and the correct tenant/workspace and retention plan are recorded.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Query a different workspace or change the time picker to five minutes before the tag operation.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Restore the workspace and a two-hour UTC window. Compare event time, ingestion time and portal time picker. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map B02, C05 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

A log is a timestamped record of something that happened. Sentinel brings selected records into one place so an analyst can investigate them. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)

[Daily notes](notes.md) · [Practice](../../practice/PQ2.md) · [All days](../index.html)
