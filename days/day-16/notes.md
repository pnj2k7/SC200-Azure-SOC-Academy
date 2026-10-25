# Day 16 notes: Follow the historical trail

## Start in plain language

A relationship map shows how accounts, computers and files connect. Historical searches look further back, while summaries reduce detail to make some questions cheaper to answer.

## Words you will meet

Graph: a map of entities and their relationships. Data lake: storage and analysis capabilities for longer-term data. Summary: an aggregate that intentionally loses some detail.

## How the parts work together

Graphs expose relationships; they do not establish guilt. Historical jobs run asynchronously and promote results; summary rules materialize aggregates. Their cost, permissions and output semantics differ.

## Apply it to Wardlight

The same identity may have appeared weeks earlier. Compare graphs, historical jobs and summary tables. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Why can a summary table make an investigation impossible even while reducing query costs?

Reasoning: Aggregation can discard entity IDs and fine-grained timestamps. Preserve the investigation dimensions or maintain access to raw evidence.

## Common mistake

Aggregate away the Account field before attempting to link a summary result to the case identity.

Correction: Retain the grouping dimensions needed for investigation; compare query result schemas before scheduling the job.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Jobs](https://learn.microsoft.com/en-us/azure/sentinel/datalake/kql-jobs-summary-rules-search-jobs) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)
