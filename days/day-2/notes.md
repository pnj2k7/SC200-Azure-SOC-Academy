# Day 2 notes: Build the evidence room

## Start in plain language

A log is a timestamped record of something that happened. Sentinel brings selected records into one place so an analyst can investigate them.

## Words you will meet

Workspace: a container for collected records. Retention: how long records are kept. Ingestion: bringing records into the system.

## How the parts work together

A workspace is a query boundary. Retention, table plan and connector determine which evidence remains available. A daily cap can create visibility gaps and does not cover every billing meter.

## Apply it to Wardlight

Create the Sentinel workspace and capture the first harmless cloud control-plane change. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: The tag changed but the query returns nothing. What do you check before widening collection?

Reasoning: Confirm subscription diagnostics, destination workspace, UTC time window, ingestion delay and caller permissions. Inspect connector health before assuming an attack hid the event.

## Common mistake

Query a different workspace or change the time picker to five minutes before the tag operation.

Correction: Restore the workspace and a two-hour UTC window. Compare event time, ingestion time and portal time picker.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)
