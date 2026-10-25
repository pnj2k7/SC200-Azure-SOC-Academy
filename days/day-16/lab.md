# Lab 16: Follow the historical trail

## 0. Before you start

**Access:** Sentinel data lake and graph availability/entitlement plus scoped roles for live advanced path; otherwise offline graph and job designs.

**Dependencies:** Day 15 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D16-setup, D16-proof, D16-fault, D16-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

The same identity may have appeared weeks earlier. Compare graphs, historical jobs and summary tables.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. From the case packet identify nodes (account, device, IP, app, file) and evidence-backed edges. Open artefacts/attack-map.html and compare event sequence with the blast-radius questions. Do not infer every nearby node is compromised.

2. In available XDR hunting graph/blast-radius and Sentinel Graph experiences, choose the case entity, constrain time and inspect relationship evidence. Save the query/filter and explain one uncertain edge. Where unavailable complete the supplied graph worksheet and mark live feature Pending.

3. Before enabling a data lake, read the linked jobs/billing guidance and check region, entitlement and cost. For the live path open Microsoft Sentinel > Data lake exploration > Jobs, create a bounded one-time KQL job for the lab account, choose supported source/destination and review scan estimate.

4. Run only a small bounded job, inspect status/errors and destination results, then disable/delete any schedule. Contrast this asynchronous historical query with an interactive Analytics query; record data period and source tier.

5. Create a supported Summary rule for an eligible lab table using a bounded aggregation such as counts by Account and time bin. Record output-table schema, bin size, late-data behavior, schedule and permissions. Verify materialized output; avoid submitting the interactive query as proof of summary-rule execution.

6. If advanced features are unavailable, submit separate KQL-job and Summary-rule designs: source tier, query, target table, schedule, expected sample counts, cost and validation. Compare with search jobs and explain when each is suitable.

## 4. Prove it

Evidence-backed entity graph plus verified job/summary output, or explicitly labelled designs with reproducible expected results.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Aggregate away the Account field before attempting to link a summary result to the case identity.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Retain the grouping dimensions needed for investigation; compare query result schemas before scheduling the job. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map H05, H06, I02, I03 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

A relationship map shows how accounts, computers and files connect. Historical searches look further back, while summaries reduce detail to make some questions cheaper to answer. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Jobs](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs-summary-rules-search-jobs) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)

[Daily notes](notes.md) · [Practice](../../practice/PQ16.md) · [All days](../index.html)
