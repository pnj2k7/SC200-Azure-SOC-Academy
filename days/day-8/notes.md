# Day 8 notes: Automate with a brake

## Start in plain language

Automation gives routine tasks to a workflow. Begin with small reversible tasks, such as assigning a case, and keep important decisions under human control.

## Words you will meet

Playbook: an automated workflow. Managed identity: an identity used by a service rather than a person. Idempotency: repeating an action does not cause duplicate harm.

## How the parts work together

Automation rules orchestrate incident actions. Playbooks are Logic Apps workflows with independent identities and billing. Retries can duplicate actions, so idempotency and lab-only scope must be designed.

## Apply it to Wardlight

Tag and assign lab incidents automatically; make a reversible playbook visible in run history. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: The Sentinel rule ran but the playbook action failed with 403. Is Contributor on the analyst enough?

Reasoning: No. Check the Sentinel service permission to run the playbook, the workflow connection and the identity permission for the specific action.

## Common mistake

Remove a required action permission in the design worksheet (or a dedicated disposable identity), then predict the exact failing stage.

Correction: Restore only the missing scoped permission and distinguish trigger authorization from action authorization. Check run logs before re-running.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing) · [Official labs](https://github.com/MicrosoftLearning/SC-200T00A-Microsoft-Security-Operations-Analyst)
