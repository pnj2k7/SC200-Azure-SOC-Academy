# Day 11 notes: Find the data trail

## Start in plain language

Finding a file and proving that someone downloaded it are different tasks. Use the right record for each question and collect only the information the investigation needs.

## Words you will meet

Audit: a history of recorded actions. eDiscovery: authorised searching and preservation of business information. DLP: controls designed to reduce inappropriate disclosure.

## How the parts work together

Purview investigation has privacy and authorization boundaries. Audit answers what happened, content search finds material, Graph logs show API requests, and alert context guides response. None substitutes for the others.

## Apply it to Wardlight

A fictional export might contain patient identifiers. Investigate audit, content, Graph and Purview signals without touching real records. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: A content search finds a sensitive marker. What additional evidence supports an exfiltration claim?

Reasoning: A relevant access/download/share event tied to the actor and file, corroborating session/app context and an authorized interpretation of the event.

## Common mistake

Use a Content search hit as proof the user downloaded the file.

Correction: Obtain the corresponding audit action and correlate actor/object/time; the search hit proves content presence, not the download.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
