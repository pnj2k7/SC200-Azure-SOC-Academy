# Deploy the Azure core

This reviewable template creates only a Log Analytics workspace, Sentinel onboarding, a custom Analytics table and a direct-ingestion DCR. It does not create Microsoft 365 licenses, endpoint sensors, Windows/Linux VMs, role grants, Activity diagnostics, lake/graph/AI resources or a complete corporate SOC. Treat it as a lab starter and run what-if first. The 0.1 GB daily quota is a lab guardrail, not a guaranteed spending ceiling; caps can interrupt collection and do not apply to all meters.

## Deploy from Azure Cloud Shell Bash

Upload main.bicep. Replace the subscription ID and training owner; choose a supported region after checking organisational data residency and service availability.

```bash
az account set --subscription YOUR_SUBSCRIPTION_ID
az account show --query '{name:name,id:id,tenantId:tenantId}' -o table
az group create --name rg-wardlight-sc200 --location southeastasia --tags Module=SC200 Environment=Training Owner=YOUR_TRAINING_ID
az deployment group what-if --resource-group rg-wardlight-sc200 --template-file main.bicep --parameters owner=YOUR_TRAINING_ID
az deployment group create --resource-group rg-wardlight-sc200 --name wardlight-core --template-file main.bicep --parameters owner=YOUR_TRAINING_ID
az deployment group show --resource-group rg-wardlight-sc200 --name wardlight-core --query properties.outputs
```

Contributor can deploy resources but cannot normally assign roles. Owner/User Access Administrator or another suitably authorised identity must grant role assignments. Record the separate assignment step. Provider registration, regional support and tenant policy can affect deployment; inspect the deployment error instead of broadening permissions blindly.

## Ingest the synthetic JSON

Generate fresh samples on your machine with `python scripts/make_sample_data.py`, then upload data/events.json to Cloud Shell. Copy the deployment outputs into the variables below; use the signed-in user’s object ID for a training user, or the approved service-principal object ID for that identity. Do not commit output containing credentials or tokens.

```bash
DCR_RESOURCE_ID='PASTE_DCR_RESOURCE_ID'
DCR_IMMUTABLE_ID='PASTE_DCR_IMMUTABLE_ID'
INGESTION_ENDPOINT='PASTE_LOGS_INGESTION_ENDPOINT'
SENDER_OBJECT_ID='PASTE_SENDER_OBJECT_ID'
az role assignment create --assignee-object-id "$SENDER_OBJECT_ID" --assignee-principal-type User --role 'Monitoring Metrics Publisher' --scope "$DCR_RESOURCE_ID"
```

If using a service principal, use the appropriate principal type and authorised authentication flow instead. Allow role propagation. The following sends a small synthetic batch; the token is held in a shell variable and not printed.

```bash
LAB_TOKEN=$(az account get-access-token --resource https://monitor.azure.com/ --query accessToken -o tsv)
curl --fail-with-body --request POST "${INGESTION_ENDPOINT%/}/dataCollectionRules/${DCR_IMMUTABLE_ID}/streams/Custom-WardlightEvents?api-version=2023-01-01" --header "Authorization: Bearer $LAB_TOKEN" --header 'Content-Type: application/json' --data-binary @events.json
unset LAB_TOKEN
```

A successful response can have an empty body. Allow ingestion time and query `WardlightEvents_CL | summarize count() by Source, Action`. A 403 suggests permissions/token audience; a 400 suggests stream/schema/payload; an empty query may be time, destination, transformation or delivery delay. Do not paste bearer tokens into evidence. Run the same batch only once when testing baseline counts; repeated ingestion duplicates events unless your query deduplicates EventId.

## More collection

Follow Days 2–4 for Activity diagnostics, AMA/DCR, optional WEF, Syslog/CEF and TI. Those sources are deliberately configured and tested individually. Main.bicep uses a DCR direct ingestion endpoint; a separate DCE may still be required for private networking or other collection designs outside this lab scope.

## Validation boundary

No live Azure deployment is claimed by the course files. Run Bicep compilation, Azure what-if and the deployed proof in your own isolated subscription before corporate use. Product availability and policies can change. Review cleanup.md before removing anything.
