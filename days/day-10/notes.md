# Day 10 notes: Identity crosses the perimeter

## Start in plain language

An attacker may use a valid account or a connected business application. Changing a password can help, but the investigation also needs to check active access and application permissions.

## Words you will meet

Session: an ongoing signed-in interaction. Token: a digital access credential. OAuth consent: permission for an application to act within an agreed scope.

## How the parts work together

Entra Identity Protection, Defender for Identity and Cloud Apps see different parts of an attack. Session revocation is not a guarantee that every access token disappears instantly; verify behavior and residual access.

## Apply it to Wardlight

A receptionist account appears in a SaaS alert and an identity alert. Decide what to revoke and why. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Why does resetting a password alone leave an incomplete SaaS response?

Reasoning: Investigate existing sessions, authentication methods, OAuth grants and app permissions. Some access can persist independently of the old password.

## Common mistake

Join on display name instead of object ID in the packet, merging two people with the same name.

Correction: Use object ID or normalized UPN with tenant context; document any remaining ambiguity and exclude the false entity link.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
