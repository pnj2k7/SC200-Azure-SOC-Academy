# Day 13 notes: Run the incident bridge

## Start in plain language

A case connects the warnings, evidence, decisions and people responsible. It should let a colleague understand what is confirmed, what is uncertain and what happens next.

## Words you will meet

Incident: related security events that require investigation. Correlation: connecting evidence. UTC: a shared time standard used to compare events from different locations.

## How the parts work together

An incident is a coordinated investigation with business decisions, not just a pile of alerts. A case records hypotheses, evidence, actions and ownership while the team tests the attack story.

## Apply it to Wardlight

Join the invoice, identity, endpoint and data signals into a case the hospital can act on. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Two alerts share an IP. Is that enough to declare lateral movement?

Reasoning: No. NAT/proxies and shared infrastructure create coincidences. Seek host, identity, process/session and time evidence supporting the movement.

## Common mistake

The packet gives one device’s timestamp in local time. Build the draft timeline without normalizing it and identify the contradiction.

Correction: Normalize to UTC, retain original timezone and event IDs, then re-evaluate causality. Temporal proximity alone does not prove lateral movement.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
