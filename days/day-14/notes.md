# Day 14 notes: Make the SOC observable

## Start in plain language

A dashboard is useful only when its numbers have a clear meaning. A quiet chart could mean there were no events, or that collection stopped working.

## Words you will meet

Workbook: a dashboard of queries and charts. Collection health: whether expected records arrive. Cost forecast: an estimate, not a guaranteed bill.

## How the parts work together

Operational dashboards must reveal missing telemetry, not hide it behind totals. Retention choices trade historical visibility against cost; every optimization needs a detection-impact check.

## Apply it to Wardlight

The CFO asks whether detection is working and what the data costs. Build an honest dashboard. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: A source volume chart is flat. What additional panel helps decide if this is healthy?

Reasoning: Last event/ingestion time, connector health and expected source activity, alongside detection execution and incident outcomes.

## Common mistake

Set a workbook panel to an unrelated workspace or to a period before ingestion.

Correction: Correct the query scope/time parameter and compare with a direct Logs query. Record how a convincing chart can be wrong.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing) · [Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard)
