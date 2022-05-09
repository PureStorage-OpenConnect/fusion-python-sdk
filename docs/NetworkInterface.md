# NetworkInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | [**RegionRef**](RegionRef.md) |  | [optional] 
**availability_zone** | [**AvailabilityZoneRef**](AvailabilityZoneRef.md) |  | [optional] 
**array** | [**ArrayRef**](ArrayRef.md) |  | [optional] 
**interface_type** | **str** | The interface type. | 
**eth** | [**NetworkInterfaceEth**](NetworkInterfaceEth.md) |  | [optional] 
**services** | **list[str]** | The services provided by this Network Interface. | [optional] 
**enabled** | **bool** | True if interface is in use. | 
**network_interface_group** | [**NetworkInterfaceGroupRef**](NetworkInterfaceGroupRef.md) |  | [optional] 
**max_speed** | **int** | Configured speed of this Network Interface. Typically this is the maximum speed of the port or bond represented by the Network Interface. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

