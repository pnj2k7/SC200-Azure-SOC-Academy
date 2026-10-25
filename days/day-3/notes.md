# Day 3 notes: Windows tells its story

## Start in plain language

A workstation can record successful and failed sign-ins, much like a reception access register. We choose which entries to collect so the register remains useful.

## Words you will meet

Agent: software that sends records. DCR: instructions telling the agent what to send and where. WEF: a Windows mechanism for forwarding records to a collector.

## How the parts work together

AMA transports selected events; DCRs control selection and destination. WEF aggregates Windows events before ingestion. Both need event generation at the source and a valid collection rule.

## Apply it to Wardlight

A reception workstation reports repeated failed logons. Collect useful Windows evidence without collecting everything. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Heartbeat is present but SecurityEvent is empty. Is AMA proven broken?

Reasoning: No. The VM can send heartbeat while Security auditing, event selection, workspace mapping or channel collection is wrong.

## Common mistake

Temporarily query EventID 4626 instead of 4625; for a live DCR fault use a duplicate training DCR only, never the sole collection path.

Correction: Correct the filter, rerun with a wider time window, and show why a healthy heartbeat alone does not prove Security-event delivery.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
