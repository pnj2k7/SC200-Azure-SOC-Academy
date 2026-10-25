# Day 5 notes: Protect the reception desk

## Start in plain language

Endpoint protection watches a computer for suspicious behaviour. Configure its rules and permissions before allowing it to take action.

## Words you will meet

Endpoint: a laptop, desktop or server. ASR: rules that reduce opportunities for attack. Audit mode: observe what would be blocked without blocking it.

## How the parts work together

Protection policy, detection, notification and automated response have different controls. ASR audit mode measures impact before enforcement; entitlement and device support can change the available settings.

## Apply it to Wardlight

Prepare endpoint controls and safe automation settings before the first endpoint case. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Should an ASR rule be put into block mode across the hospital on first use?

Reasoning: Pilot in audit mode on a scoped group, review operational impact and exceptions, then deploy under change control with rollback.

## Common mistake

In the worksheet change a lab-only suppression to all devices. Identify the visibility loss without applying the change.

Correction: Restrict scope and expiry; show a before/after settings comparison and explain why notifications are not the alert engine.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Endpoint pilot](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-defender-endpoint) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
