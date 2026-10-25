# Wardlight Hospitals: the training scenario

Wardlight is a fictional private hospital group with sites in Colombo and Kandy. Its reception staff use Microsoft 365 and supported Windows devices; a patient-portal pilot runs in Azure. An external laboratory sends operational messages through a gateway. All data and identities in this course are synthetic.

## The incident

A supplier invoice appears in a reception mailbox. A staff account then records failed sign-ins, a process starts on a workstation and an export file is accessed. The hospital manager wants facts, not an assumption that every warning is an attack. One noisy service-account pattern and a misleading claim are deliberately included.

## The people

- Hospital manager: protects continuity of patient services and approves business-impacting response.
- Incident lead: owns severity, decisions, escalation and closure.
- Analyst: collects evidence, tests explanations and recommends action.
- Platform engineer: configures scoped collection, detection and workflows.
- Data owner/privacy lead: authorises content searches and evidence handling.
- Billing owner: checks spending and closes resources/trials.

## Requirements

1. Every confirmed finding must cite evidence and UTC time.
2. Production services and real employee/patient data are outside the lab.
3. Containment must have a clear target, business impact, approval and rollback.
4. Routine automation is scoped to lab incidents and independently verified.
5. Costs, permissions and incomplete capabilities remain visible.
6. A second analyst must be able to reproduce the final report.

## Numbered architecture

1. Tenant, scoped identities and billing guardrails.
2. Sentinel workspace and retention decisions.
3. Windows source, AMA/DCR and optional WEF collector.
4. Syslog/CEF gateway, custom application records and indicators.
5. Endpoint protection and response.
6. Scheduled/custom detections and anomaly/ATT&CK review.
7. Scoped automation rule and harmless Logic App.
8. Email, identity, SaaS and data investigations.
9. Cloud workload protection evidence.
10. Cross-product case, timeline and operational workbook.
11. Hunting, entity relationships and historical analysis.
12. Validated notebook/AI assistance, capstone and teardown.

[Open the architecture](architecture.svg). Solid flow in the diagram represents the teaching sequence; product-to-product integration must be configured and licensed separately. The custom table is a synthetic lab source and does not populate built-in Defender tables.

## Naming

Resource group: rg-wardlight-sc200. Workspace: law-wardlight-soc. Custom table: WardlightEvents_CL. Analyst: analyst-lab. Device: WL-RECEPTION-01. Test person: maya@wardlight.example. Test IP: 203.0.113.50. The .example domain and documentation IP range are intentionally non-production.
