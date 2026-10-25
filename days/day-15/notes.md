# Day 15 notes: Hunt beyond the alert

## Start in plain language

Hunting starts with a question, such as whether an account behaved unusually, even when no alert has appeared. A good hunt tests both suspicious and harmless explanations.

## Words you will meet

Hypothesis: a statement to test. Baseline: normal behaviour used for comparison. Query scope: the data, people and period included in a search.

## How the parts work together

Hunting begins with a question, while detection operationalizes a repeatedly useful signal. KQL syntax travels across services, but schemas and custom-detection requirements do not.

## Apply it to Wardlight

There is no new alert, but the threat report suggests a suspicious process and a reused identity. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: A hunt returns zero rows. What does it prove?

Reasoning: Only that the query found no matches in its data/window/scope. Verify coverage and query assumptions before claiming the behavior never occurred.

## Common mistake

Replace a case-insensitive comparison with a case-sensitive exact match that drops a known variant in the synthetic query.

Correction: Normalize the relevant field or use the appropriate operator; test the counterexample and explain the performance/precision tradeoff.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
