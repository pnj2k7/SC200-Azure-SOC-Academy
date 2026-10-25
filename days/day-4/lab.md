# Lab 4: The missing telemetry

## 0. Before you start

**Access:** Azure-only custom-log path; optional Linux forwarder, test syslog/CEF sender; threat-intelligence connector permissions.

**Dependencies:** Day 3 learning and the relevant shared workspace/case packet. Read the access line: the next product may need a separate license.

**Time:** approximately 3 hours of practical work. **Safety boundary:** dedicated lab resources and fictional data only. **Evidence:** D04-setup, D04-proof, D04-fault, D04-cleanup plus the objective IDs mapped to this day.

If a required product is unavailable, use the bundled scenario cards, synthetic data and written designs. Label every proposed portal action Simulation/Design-only and leave live execution Pending. Do not treat a synthetic event as a real product alert.

## 1. Objective

A partner gateway and hospital application use different log formats. Bring both into the investigation with a traceable schema.

## 2. Timed segments

| Segment | Minutes | Outcome |
|---|---|---|
| Access, scope and prediction | 20 | Identity, permissions and expected result recorded |
| Build or investigate | 85 | Numbered steps completed |
| Prove and break/fix | 45 | Evidence and corrected state |
| Cleanup and report | 30 | Cost and closure record |

## 3. Steps

1. Run python scripts/make_sample_data.py on your machine to create data/events.json and queries/00-synthetic.kql with current UTC times. Upload the small JSON to Cloud Shell. Follow infra/README.md to post it to the DCR direct ingestion endpoint with a bearer token held only in memory.

2. Assign the sending identity Monitoring Metrics Publisher on the DCR, using an account permitted to assign roles. Use the DCR immutable ID, stream Custom-WardlightEvents and output WardlightEvents_CL. Expected: the API accepts the request; query the table after ingestion.

3. Query WardlightEvents_CL | summarize Rows=count() by Source, Action. Compare with data/answer-key.json. Inspect TimeGenerated type, Account, Device, IP, CorrelationId and whether sensitive data was excluded. Record DCR transformations; a custom table is not a built-in Defender table.

4. Optional live Linux track: install Syslog via AMA and CEF via AMA solutions, configure a supported forwarder with the connector instructions, associate the DCR, and send a benign logger message. Expected: Syslog for native messages; CommonSecurityLog for correctly parsed CEF. Check local listener, forwarding and facility/severity before portal queries.

5. Install an available threat-intelligence solution and ingest a lab indicator using the supported connector/API workflow in your tenant. Use documentation IP 203.0.113.50 with a short validity window, lab label and confidence; do not submit it to public feeds. Record the resulting TI table schema, which can change by connector generation.

6. Join the custom IP field to the available indicator field after inspecting getschema and validity fields. Without TI/CEF access, use the synthetic indicator/CEF cards in data/scenario-cards.json and label the output as simulation.

## 4. Prove it

The custom table contains the expected rows; demonstrate source, schema and ingestion path for Windows, syslog, CEF, cloud and TI.

Record the exact query/action, UTC interval, result and evidence reference. Ask a colleague to explain what the evidence establishes. If the result differs, diagnose permissions, feature availability, source collection, schema and time scope before broadening access or collecting more data.

## 5. Break it

**Controlled fault:** Use a wrong stream name in a single synthetic ingestion request, or map IP to an empty field in a saved query.

Predict the symptom first. Save the faulty result with the original configuration. Apply the fault only to a disposable lab copy or worksheet as specified. **Repair:** Correct stream/schema mapping, retain the error response without tokens, and re-run once. Do not rotate credentials to solve a field mismatch. Re-run the proof and record the root cause, symptom, diagnostic evidence and restored state. Never deliberately disable production protection.

## 6. Teardown

- Save only redacted evidence privately. Keep original event references and UTC times.
- Undo the day’s test changes, temporary role assignments, policies, messages, indicators or actions. Confirm the restored state; do not remove the shared workspace before later lessons.
- Disable temporary detection/automation rules and job schedules; turn off or delete optional workflows/compute when finished. Deallocate optional VMs; their disks can still bill.
- Review cleanup.md for tenant-level licenses, subscription plan settings and collection that a resource-group deletion will not remove. Record anything deliberately retained for the next day, owner and deletion date.

## 7. Cost line

Before starting, list each planned meter in templates/cost-ledger.csv: ingestion/retention, optional VM/disks, Logic Apps actions, licensed trial/capacity and any advanced scan/compute. Offline simulation creates no Azure resources. Use current regional prices; do not write zero just because credits may apply. After the lab record actual usage when available, currency, delay and remaining resources.

## 8. Evidence required

Complete templates/evidence-pack.md. Include scope/access, one successful outcome, the break/fix comparison, explanation in your own words and verified cleanup. Map C04, C06, C07 to evidence. Record Live verified, Simulation complete, Design-only or Pending per objective; one overall day checkbox cannot prove every subskill.

## 9. Wardlight connection

Different systems describe events differently. This lesson makes their records comparable, as if several departments agreed on the same incident form. In your final paragraph explain the business decision your evidence supports and what remains uncertain.

## Reading and next step

[Ingestion](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-portal) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)

[Daily notes](notes.md) · [Practice](../../practice/PQ4.md) · [All days](../index.html)
