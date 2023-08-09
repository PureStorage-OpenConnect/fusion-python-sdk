# Operation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The UUID of the operation. | 
**self_link** | **str** | The URI of the operation, e.g., /tenants/&lt;t&gt;/tenant-spaces/&lt;ts&gt;/volumes/&lt;v&gt;.  | 
**request** | [**OperationRequest**](OperationRequest.md) |  | [optional] 
**request_type** | **str** | Request type is a combination of action and resource kind, e.g., \&quot;CreateVolume\&quot;. | 
**request_id** | **str** | The request ID specified with the REST call (or system generated) used for idempotence when making API calls. Any name is valid. | 
**request_collection** | **str** | The URI of the request collection in which this operation was created. Valid values are \&quot;/\&quot;, \&quot;/&lt;tenants&gt;/&lt;t&gt;\&quot; or \&quot;/&lt;tenants&gt;/&lt;t&gt;/tenant-spaces&lt;ts&gt;\&quot;. | [optional] 
**state** | [**OperationState**](OperationState.md) |  | [optional] 
**result** | [**OperationResult**](OperationResult.md) |  | [optional] 
**status** | **str** | The latest status of the operation indicates if it is waiting (Pending), active (Running, Aborting) or complete (Succeeded, Failed). | 
**retry_in** | **int** | Recommended time to wait before getting the operation again to observe status change (polling interval). Unit is milliseconds, e.g., 100. | 
**error** | [**Error**](Error.md) |  | [optional] 
**created_at** | **int** | The time that the operation was created, in milliseconds since the Unix epoch. | 
**started_at** | **int** | The time that the operation was admitted, in milliseconds since the Unix epoch. | 
**ended_at** | **int** | The time that the operation ended with status Succeeded or Failed, in milliseconds since the Unix epoch. | 
**cancelation** | **str** | The cancelation status of the operation, one of five values. CancelNone means no cancelation has been requested or occured. CancelRequested means the user or system has requested to cancel the operation; it may or may not happen. CancelInProgress means the system has accepted the request to cancel and is trying to do so; once an operation is in Canceling status, it will fail. CancelSuccessful means an operation has failed with a CANCELED error code. CancelUnsuccessful means cancel was requested, but the system could not cancel the operation -- it may have failed with an error code other than CANCELED; or it may have succeeded. | 
**update_fields** | **dict(str, str)** | Key/value pairs of the fields this operation is updating, if it is an Update operation. E.g. destroyed:true or size:1048576. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

