# Day 12 notes: Defend the cloud workload

## Start in plain language

A weak door lock and evidence that someone entered are different findings. Cloud security tools report both weaknesses and suspicious activity; the response must distinguish them.

## Words you will meet

Workload: an application and its supporting resources. Posture: how securely a system is configured. Sample alert: a training record that does not prove a real attack.

## How the parts work together

Defender for Cloud workload protection detects threats; posture management prioritizes weaknesses. Both matter, but incident classification must follow evidence and resource context.

## Apply it to Wardlight

A workload protection alert points to the application server. Separate a posture weakness from an active incident. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Can a higher secure score prove that yesterday’s workload incident is remediated?

Reasoning: No. Verify the incident actions and residual compromise independently; secure score measures posture recommendations.

## Common mistake

Treat the secure-score recommendation as proof of a successful intrusion in the draft incident report.

Correction: Separate exposure from observed behavior; identify the missing telemetry and revise the confidence level.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)
