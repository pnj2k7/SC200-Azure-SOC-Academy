# Day 9 notes: The suspicious invoice

## Start in plain language

An email’s visible sender name can be misleading. Investigators examine delivery and authentication records and then check what the recipient actually did.

## Words you will meet

Message ID: a reference to an individual email. Authentication: checks of the sending system. Quarantine: holding a message away from the recipient.

## How the parts work together

Email investigation crosses delivery, authentication and post-delivery actions. A malicious verdict supports remediation, while blast radius depends on who received, clicked or executed the payload.

## Apply it to Wardlight

A fake supplier invoice reaches a fictional employee. Follow email evidence into the cross-product incident. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Does delivery of a suspicious message prove the recipient is compromised?

Reasoning: No. Correlate click, authentication and endpoint activity; record what is known and what remains unproven.

## Common mistake

Search using the sender display name alone and compare with the supplied forged display name.

Correction: Use immutable message identifiers, actual sender/authentication details and recipient/time boundaries; avoid treating display names as identity proof.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
