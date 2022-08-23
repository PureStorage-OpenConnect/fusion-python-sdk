# PlacementRecommendationPost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placement_group_link** | **str** | Deprecated. Use placement_group instead. The link to the placement group that we would like to generate a placement recommendation report on | [optional] 
**placement_group** | **str** | Placement Group you would like to generate a placement recommendation report on. For placement of new placement group, leave this blank, and instead fill in simulated_placement | [optional] 
**tenant** | **str** | Tenant that Placement Group belongs to. For placement of new placement group, enter Tenant where the Placement Group would have been created in | 
**tenant_space** | **str** | Tenant Space that Placement Group belongs to. For placement of new placement group, enter TenantSpace where Placement Group would have been created in | 
**placement_engine** | [**PlacementEngine**](PlacementEngine.md) |  | [optional] 
**simulated_placement** | [**SimulatedPlacementPost**](SimulatedPlacementPost.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

