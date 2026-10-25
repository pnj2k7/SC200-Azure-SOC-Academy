targetScope = 'resourceGroup'
@description('Use a region supported for Log Analytics and your intended lab services.')
param location string = resourceGroup().location
param workspaceName string = 'law-wardlight-soc'
param owner string = 'training'
var tags = { Module: 'SC200', Environment: 'Training', Owner: owner }
resource workspace 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: workspaceName
  location: location
  tags: tags
  properties: {
    sku: { name: 'PerGB2018' }
    retentionInDays: 90
    workspaceCapping: { dailyQuotaGb: json('0.1') }
    features: { enableLogAccessUsingOnlyResourcePermissions: false }
  }
}
resource sentinel 'Microsoft.SecurityInsights/onboardingStates@2024-03-01' = {
  name: 'default'
  scope: workspace
  properties: { customerManagedKey: false }
}
resource table 'Microsoft.OperationalInsights/workspaces/tables@2022-10-01' = {
  parent: workspace
  name: 'WardlightEvents_CL'
  properties: {
    plan: 'Analytics'
    retentionInDays: 90
    schema: {
      name: 'WardlightEvents_CL'
      columns: [
        { name: 'TimeGenerated', type: 'datetime' }
        { name: 'EventId', type: 'string' }
        { name: 'Source', type: 'string' }
        { name: 'Account', type: 'string' }
        { name: 'Device', type: 'string' }
        { name: 'IP', type: 'string' }
        { name: 'Action', type: 'string' }
        { name: 'Detail', type: 'string' }
        { name: 'CorrelationId', type: 'string' }
      ]
    }
  }
}
resource dcr 'Microsoft.Insights/dataCollectionRules@2023-03-11' = {
  name: 'dcr-wardlight-direct'
  location: location
  kind: 'Direct'
  tags: tags
  properties: {
    streamDeclarations: {
      'Custom-WardlightEvents': {
        columns: [
          { name: 'TimeGenerated', type: 'datetime' }
          { name: 'EventId', type: 'string' }
          { name: 'Source', type: 'string' }
          { name: 'Account', type: 'string' }
          { name: 'Device', type: 'string' }
          { name: 'IP', type: 'string' }
          { name: 'Action', type: 'string' }
          { name: 'Detail', type: 'string' }
          { name: 'CorrelationId', type: 'string' }
        ]
      }
    }
    destinations: { logAnalytics: [{ workspaceResourceId: workspace.id, name: 'socWorkspace' }] }
    dataFlows: [{ streams: ['Custom-WardlightEvents'], destinations: ['socWorkspace'], transformKql: 'source', outputStream: 'Custom-WardlightEvents_CL' }]
  }
  dependsOn: [table]
}
output workspaceResourceId string = workspace.id
output dcrResourceId string = dcr.id
output dcrImmutableId string = dcr.properties.immutableId
output logsIngestionEndpoint string = dcr.properties.endpoints.logsIngestion
