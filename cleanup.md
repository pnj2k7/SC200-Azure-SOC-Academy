# Cleanup and cost closure

Use only your dedicated training scope. Read and complete this list before any group deletion; it includes settings outside the resource group. Deleting evidence is irreversible, so preserve only the redacted records your training policy requires first. Do not delete any shared or production resource.

## End of each session

1. Export the redacted evidence, update the matrix and ledger and list deliberately retained resources with owner and removal date.
2. Disable lab detection/automation rules, playbook triggers, job schedules and optional compute sessions that are no longer required.
3. Undo temporary messages, indicators, device isolation, group assignments and policy changes; verify restored state.
4. Deallocate optional VMs. Disks, public IPs and other resources may still bill; record them explicitly.

## Final teardown

1. Stop data sources/forwarding and remove the lab subscription Activity diagnostic setting or policy assignment/remediation created for the course. This may sit outside the resource group.
2. Disable Sentinel automation rules, playbooks, KQL/notebook jobs, Summary rules and any separately provisioned compute. Verify schedules are disabled, not simply hidden.
3. Remove temporary Azure role grants, app grants/secrets, managed-identity assignments and client integrations created for the lab. Preserve recovery access.
4. Offboard the disposable endpoint using the supported product process if retaining the machine. Undo ASR/policy settings, temporary device group rules and notification subscriptions.
5. Remove lab-only Purview cases/searches and exports under retention policy; undo test SaaS/Entra actions and delete disposable mail/files only after recording evidence.
6. Disable any Defender for Cloud plan enabled solely for the lab and check subscription/resource overrides. Review tenant-level trial renewal and licensed capacity separately. Deleting the group does not cancel a Microsoft 365 subscription or AI capacity elsewhere.
7. In the Azure portal select rg-wardlight-sc200. Verify the subscription, tags and complete resource list. If every listed resource is dedicated to the course and evidence is preserved, delete the group using the portal confirmation. Do not use a broad scripted deletion.
8. Check resources in every region used, source diagnostics/policies, workspaces, Logic Apps, disks, storage, networking and compute. Confirm the group is absent and inspect any retained items separately.
9. Revisit Cost Management after billing data catches up and check for continuing meters. Keep the budget alert active until closure. A zero forecast alone does not prove all resources are gone.

## Closure record

Record UTC time, owner, scope, what was removed, what was retained, license/renewal status, measured cost and the date of the follow-up billing check. A second person should verify closure for corporate delivery.
