# Array

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apartment_id** | **str** | Apartment identifier of Array. Return value of purearray list | 
**hardware_type** | [**HardwareTypeRef**](HardwareTypeRef.md) |  | [optional] 
**region** | [**RegionRef**](RegionRef.md) |  | [optional] 
**availability_zone** | [**AvailabilityZoneRef**](AvailabilityZoneRef.md) |  | 
**appliance_id** | **str** | The Appliance id of the array. | 
**host_name** | **str** | The host name of the array. This should resolve to the management address of the array. If DNS is not available, provide the management address directly. | 
**maintenance_mode** | **bool** | The flag to indicate whether the array is ready to use or not. True if not ready. | [optional] 
**unavailable_mode** | **bool** | The flag to indicate whether the array is unavaialble/unhealthy. True if unavailable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

