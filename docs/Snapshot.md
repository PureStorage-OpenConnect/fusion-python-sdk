# Snapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**TenantRef**](TenantRef.md) |  | 
**tenant_space** | [**TenantSpaceRef**](TenantSpaceRef.md) |  | 
**volume_snapshots_link** | **str** | The URI of volume snapshots in the snapshot. | 
**protection_policy** | [**ProtectionPolicyRef**](ProtectionPolicyRef.md) |  | [optional] 
**time_remaining** | **int** | Unimplemented - The amount of time left until the destroyed snapshot is permanently eradicated. Measured in milliseconds. Before the time_remaining period has elapsed, the destroyed snapshot can be recovered by setting destroyed&#x3D;false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

