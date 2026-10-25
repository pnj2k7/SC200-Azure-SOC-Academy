# Day 4 notes: The missing telemetry

## Start in plain language

Different systems describe events differently. This lesson makes their records comparable, as if several departments agreed on the same incident form.

## Words you will meet

Schema: the names and types of fields. CEF: a common security-message format. Indicator: a known clue, such as an IP address, that deserves investigation.

## How the parts work together

Source logs, collection transport, transformations and destination schemas are separate failure points. TI matches require field normalization, indicator freshness and context; a match alone is not a verdict.

## Apply it to Wardlight

A partner gateway and hospital application use different log formats. Bring both into the investigation with a traceable schema. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Why can a successful HTTP ingestion response coexist with an empty investigation result?

Reasoning: Delivery is asynchronous; the query can target the wrong table/window, or transformations can filter rows. Check the DCR, stream, timestamps and ingestion errors.

## Common mistake

Use a wrong stream name in a single synthetic ingestion request, or map IP to an empty field in a saved query.

Correction: Correct stream/schema mapping, retain the error response without tokens, and re-run once. Do not rotate credentials to solve a field mismatch.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Ingestion](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-portal) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
