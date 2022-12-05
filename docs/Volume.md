# Volume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** | The size of the volume | [optional] 
**tenant** | [**TenantRef**](TenantRef.md) |  | 
**tenant_space** | [**TenantSpaceRef**](TenantSpaceRef.md) |  | 
**storage_class** | [**StorageClassRef**](StorageClassRef.md) |  | 
**protection_policy** | [**ProtectionPolicyRef**](ProtectionPolicyRef.md) |  | [optional] 
**placement_group** | [**PlacementGroupRef**](PlacementGroupRef.md) |  | [optional] 
**array** | [**ArrayRef**](ArrayRef.md) |  | [optional] 
**created_at** | **int** |  | [optional] 
**source_volume_snapshot** | [**VolumeSnapshotRef**](VolumeSnapshotRef.md) |  | [optional] 
**host_access_policies** | [**list[HostAccessPolicyRef]**](HostAccessPolicyRef.md) |  | [optional] 
**serial_number** | **str** | Volume Serial Numbers, aka LUN Serial Numbers. This will be visible to initiators that connect to the volume. | 
**target** | [**Target**](Target.md) |  | [optional] 
**time_remaining** | **int** | The amount of time left until the destroyed volume is permanently eradicated. Measured in milliseconds. Before the time_remaining period has elapsed, the destroyed volume can be recovered by setting destroyed&#x3D;false. | [optional] 
**destroyed** | **bool** | True if the volume has been destroyed and is pending eradication. The time_remaining value displays the amount of time left until the destroyed volume is permanently eradicated. Before the time_remaining period has elapsed, the destroyed volume can be recovered by setting destroyed&#x3D;false. Once the time_remaining period has elapsed, the volume is permanently eradicated and can no longer be recovered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

