# Day 7 notes: Engineer a reliable detection

## Start in plain language

A detection is a repeatable test for a suspicious pattern. Like a smoke detector, it needs testing: sensitivity that is too high creates noise, while too low can miss danger.

## Words you will meet

KQL: a language for asking questions of records. Threshold: the point at which a pattern triggers a warning. False positive: a harmless event incorrectly treated as suspicious.

## How the parts work together

A detection includes data, query, schedule, grouping, entities and response context. NRT and ML are distinct rule families with eligibility limits. Tuning must preserve evidence of the behavior you intended to detect.

## Apply it to Wardlight

Turn the recurring failed-sign-in pattern into a tested signal, without flooding the SOC. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Why must XDR custom detection output preserve source event identifiers?

Reasoning: The detection service needs to associate results with real events and affected entities; a summarized query without required identifiers can be ineligible.

## Common mistake

Raise the threshold above the sample event count in a disabled copy of the rule. Predict the missed incident.

Correction: Restore the documented threshold and test both suspicious and benign sample accounts. Explain false-positive and false-negative consequences.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst) · [Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard)
