# Day 6 notes: Investigate the workstation

## Start in plain language

An alert is a warning to investigate. A timeline helps explain what happened before and after the warning; containment limits further harm.

## Words you will meet

Isolation: restricting a device’s communication. Investigation package: collected diagnostic evidence. Remediation: removing the cause and restoring a safe state.

## How the parts work together

Investigation connects alerts to evidence. Automated investigation verdicts, disruption and analyst actions need separate verification. Containment trades business availability for risk reduction, so scope and rollback matter.

## Apply it to Wardlight

A benign simulation triggers a device alert. Build a timeline and contain the right entity. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Why is an isolation action marked submitted insufficient to close the case?

Reasoning: Submitted is not completed. Check the action outcome, device reachability/last seen, residual identity risk and recovery before closure.

## Common mistake

Use the wrong device name from the case packet in a draft containment request; do not execute it.

Correction: Cross-check DeviceId, account and UTC time against the incident; require the exact entity ID before acting.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Endpoint pilot](https://learn.microsoft.com/en-us/defender-xdr/pilot-deploy-defender-endpoint) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
