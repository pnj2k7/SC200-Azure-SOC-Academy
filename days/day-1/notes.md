# Day 1 notes: Open the SOC

## Start in plain language

A security operations centre is the team that checks warning signs and coordinates a response. Think of it as a hospital control room for digital services.

## Words you will meet

Tenant: an organisation’s identity directory. Subscription: the account that holds Azure resources and their bill. Role: permission to perform a defined set of actions.

## How the parts work together

A tenant is the identity directory; a subscription is a billing/resource boundary. Azure RBAC grants resource actions, while Defender and Purview apply their own permissions. Least privilege must work across all of them.

## Apply it to Wardlight

The hospital CFO approves a small security pilot. Establish identities, scope, and a spending trail before any telemetry flows. The technical result matters because the hospital needs a decision it can trust while continuing to serve patients. State what the evidence establishes before recommending an action.

## Worked reasoning

Question: Does a subscription budget stop a runaway ingestion pipeline?

Reasoning: No. It warns, and billing data can lag. Limit data sources, monitor usage, and stop chargeable resources yourself.

## Common mistake

In the written access matrix accidentally give the analyst Owner. Predict the extra powers; do not grant it in Azure.

Correction: Replace Owner with the required scoped Sentinel role, and explain how a Responder differs from Contributor.

## What the instructor demonstrates

Walk through the first two lab steps, point out the selected tenant/workspace and show a successful result. Explain one failure state and ask learners to predict its cause before correcting it. End by showing the evidence that would allow a colleague to reproduce the finding.

## Required reading

[Sentinel setup](https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard) · [Billing](https://learn.microsoft.com/en-us/azure/sentinel/billing)
