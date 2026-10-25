# Lab 8: Automate with a brake

## 0. Before you start

**Access:** Sentinel Contributor; Logic Apps deployment rights; Sentinel Automation Contributor role assignment for the service; no email recipients beyond yourself.

**Dependencies:** Day 7 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D08-setup, D08-proof, D08-fault, D08-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

Tag and assign lab incidents automatically; make a reversible playbook visible in run history.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Create a disabled Sentinel automation rule scoped to the lab analytics rule. Trigger on incident creation, set an owner and add WL-Training tag. Set explicit execution order and expiry; ensure the rule cannot match real incidents.

2. Enable the scoped rule, generate a fresh Day 7 incident and inspect incident activity. Expected: owner/tag change with automation history, not a claim based on the rule being enabled.

3. Create a Consumption Logic App playbook in the lab group using a Microsoft Sentinel incident trigger. Add only a benign action such as composing the incident title; optionally add a lab comment with the supported Sentinel action. Do not configure external notifications or destructive containment.

4. Enable a system-assigned managed identity where supported, grant the minimum role needed for its chosen Sentinel action, and authorize the Sentinel service to run playbooks with Microsoft Sentinel Automation Contributor at the playbook group. Document trigger/action connection authentication separately.

5. Run the playbook manually on the lab incident; inspect trigger inputs, action outputs and run status. Then add it to the scoped automation rule if the trigger supports that workflow. Verify one run and check for duplicate loops.

6. Disable the automation rule and playbook after proof. Export a redacted design: trigger, filter, actions, identities, retry behavior, deduplication key, approval gate and rollback. A compose-only run does not prove incident write permissions.

## 4. Prove it

A real scoped owner/tag change and a successful harmless playbook run, with separate permission evidence for service and workflow identity.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Remove a required action permission in the design worksheet (or a dedicated disposable identity), then predict the exact failing stage.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Restore only the missing scoped permission and distinguish trigger authorization from action authorization. Check run logs before re-running. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map A10, A11 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

Automation gives routine tasks to a workflow. Begin with small reversible tasks, such as assigning a case, and keep important decisions under human control. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ8.md) · [All days](../index.html)
