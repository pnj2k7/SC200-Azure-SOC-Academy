# Getting started

## Understand the commitment

Plan 18 learning days of approximately 4–5 hours each plus a review. A corporate team can deliver two days a week over nine weeks; a self-paced learner may split a day across several evenings. Allow more time if Azure and Microsoft 365 are new to you. This is security operations training, not a general replacement for an introductory Azure course.

The story uses invented people, devices and documents. You will assemble an evidence collection system, test detection and response, investigate an incident and dismantle the lab. Begin with the plain-language notes; the commands become meaningful after you understand their purpose.

## Access paths

| Path | What you need | What it proves |
|---|---|---|
| Offline simulation | Extracted repository; browser; optional Python 3 | Reasoning, synthetic queries, timelines, notebook analysis and written designs |
| Azure core | Dedicated tenant/subscription, deployment/role permissions and a cost owner | Sentinel, workspace, custom telemetry, Activity logs, analytics, workbook and optional Logic Apps |
| Endpoint | Defender for Endpoint investigation entitlement and a supported isolated device | Onboarding, policy/settings, timelines and device actions |
| Email, identity, SaaS | Relevant Defender for Office 365, Cloud Apps, Identity and Entra entitlements; Exchange/AD prerequisites as applicable | Cross-product investigation and permitted remediation |
| Data investigations | Purview Audit/eDiscovery and relevant policy/alert licenses and roles | Audit, Content search, data-related investigation |
| Advanced platform and AI | Region/tenant support, relevant Sentinel lake/graph/notebook and Copilot entitlements or capacity | Live historical jobs, summaries, graphs, MCP and AI workflows |

Do not assume a Microsoft 365 developer tenant, E5 trial, free Azure credit or Copilot capacity will be available. Check the actual product offer and renewal terms. Group Days 5–13 together if a short licensed trial is used. Mark missing access Pending and complete the simulation exercise rather than buying licenses automatically.

## Before Day 1

1. Identify the training sponsor, instructor/security owner, billing owner and learners. Agree a maximum acceptable budget and escalation contact in your billing currency.
2. Choose a dedicated subscription and training tenant. Confirm ownership and recovery access. Use a separate analyst account with MFA. Do not weaken organisation-wide access policies to make a lab work.
3. Confirm a supported region for the planned services and data residency. Record the chosen region once; advanced features may have a different availability footprint. Examples use southeastasia only as a starting value.
4. Install a current browser. Python 3 is optional for offline analysis and required to run bundled generation/check scripts; Azure Cloud Shell Bash can run deployment commands without local Azure tools.
5. Open the access matrix and progress template. Inventory licenses, actual service enablement and expiry dates before activating trials. Choose the path for each lesson.
6. Read cleanup.md and create a private evidence directory outside the public repository. Decide what screenshots may be retained and for how long.

## Cost controls

No fixed total price or zero-cost promise is made. Offline reading is local; cloud ingestion, VMs/disks, retention, Logic Apps, connectors, lake scans/storage, notebook compute and AI capacity can incur separate charges. Use current regional prices and write estimates before starting each resource. Budget alerts and workspace caps do not guarantee a hard spending ceiling. Check measured costs after each session and after billing has caught up.

Create only the lab resource group, use tags Module=SC200, Environment=Training, Owner=your-training-id and Day=n, collect tiny samples and avoid commitment tiers. Deallocate optional VMs when idle; disks and other services may still bill. Disable workflows and schedules after proof. Never enable all Defender for Cloud plans by default.

## Evidence rules

Record timestamp, workspace/tenant context, action/result and explanation. Redact identifiers where required; never record passwords, access tokens, onboarding packages or personal health data. Label each artifact Live, Simulation or Design-only. Keep live completion Pending where the capability has not been executed. A screenshot of a configuration is not proof that the configuration works.

## First ten minutes

Open scenario/organisation.html, review the architecture, read Day 1 notes, copy the templates to your private working folder and complete the access inventory. If you have no Azure account yet, start in Simulation mode; do not deploy anything on someone else’s subscription.
