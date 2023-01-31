# PlacementRecommendation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant** | [**TenantRef**](TenantRef.md) |  | [optional] 
**tenant_space** | [**TenantSpaceRef**](TenantSpaceRef.md) |  | [optional] 
**placement_engine** | [**PlacementEngine**](PlacementEngine.md) |  | [optional] 
**placement_group_id** | **str** | If not empty, this is the Placement Group ID for which the placement recommendation was made | [optional] 
**placement_group** | [**PlacementGroupRef**](PlacementGroupRef.md) |  | [optional] 
**simulated_placement** | [**SimulatedPlacement**](SimulatedPlacement.md) |  | [optional] 
**included_arrays** | [**list[PlacementRecommendationIncludedArray]**](PlacementRecommendationIncludedArray.md) | A JSON array of Arrays that the Placement Group can be placed/migrated to | [optional] 
**excluded_arrays** | [**list[PlacementRecommendationExcludedArray]**](PlacementRecommendationExcludedArray.md) | A JSON array of Arrays that the Placement Group cannot be placed on | [optional] 
**target_arrays** | [**list[ArrayRef]**](ArrayRef.md) | If present, this is the list of arrays that was provided when requesting the placement recommendation report to consider for placement recommendations | [optional] 
**time_remaining** | **int** | Number of milliseconds left before this Placement Recommendation report is deleted | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

