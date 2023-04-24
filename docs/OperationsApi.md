# fusion.OperationsApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_operation**](OperationsApi.md#get_operation) | **GET** /operations/{id} | Gets a specific Operation.
[**get_operation_by_id**](OperationsApi.md#get_operation_by_id) | **GET** /resources/operations/{id} | Gets a specific Operation.
[**list_operations**](OperationsApi.md#list_operations) | **GET** /operations | Gets a list of Operations matching the criteria.

# **get_operation**
> Operation get_operation(id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Operation.

### Example
```python
from __future__ import print_function
import time
import fusion
from fusion.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = fusion.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fusion.OperationsApi(fusion.ApiClient(configuration))
id = 'id_example' # str | The Operation ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Operation.
    api_response = api_instance.get_operation(id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_operation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Operation ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_operation_by_id**
> Operation get_operation_by_id(id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Operation.

### Example
```python
from __future__ import print_function
import time
import fusion
from fusion.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = fusion.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fusion.OperationsApi(fusion.ApiClient(configuration))
id = 'id_example' # str | The Operation ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Operation.
    api_response = api_instance.get_operation_by_id(id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->get_operation_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Operation ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations**
> OperationList list_operations(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, action=action, request_id=request_id, request_collection=request_collection, resource_kind=resource_kind, resource_id=resource_id, status=status, created_after=created_after, filter=filter, sort=sort, limit=limit, offset=offset)

Gets a list of Operations matching the criteria.

### Example
```python
from __future__ import print_function
import time
import fusion
from fusion.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = fusion.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = fusion.OperationsApi(fusion.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)
action = 'action_example' # str | The action requested. (optional)
request_id = 'request_id_example' # str | The request ID supplied with the request. (optional)
request_collection = 'request_collection_example' # str | Default to \\\"/\\\", valid values take the form \\\"/\\\", \\\"/tenants/<tname>\\\", or \\\"/tenants/<tname>/tenant-spaces/<tsname>\\\" (optional)
resource_kind = 'resource_kind_example' # str | The kind of resource on which the Operation was performed. (optional)
resource_id = 'resource_id_example' # str | The ID of resource on which the Operation was performed. (optional)
status = 'status_example' # str | The status of the Operation. Support for comma separated multiple status is deprecated, use IN list instead (optional)
created_after = 'created_after_example' # str |  (optional)
filter = 'filter_example' # str | filter should use expression language for filtering (optional)
sort = 'sort_example' # str | Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \"sort=size-,name\") (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)

try:
    # Gets a list of Operations matching the criteria.
    api_response = api_instance.list_operations(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, action=action, request_id=request_id, request_collection=request_collection, resource_kind=resource_kind, resource_id=resource_id, status=status, created_after=created_after, filter=filter, sort=sort, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OperationsApi->list_operations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 
 **action** | **str**| The action requested. | [optional] 
 **request_id** | **str**| The request ID supplied with the request. | [optional] 
 **request_collection** | **str**| Default to \\\&quot;/\\\&quot;, valid values take the form \\\&quot;/\\\&quot;, \\\&quot;/tenants/&lt;tname&gt;\\\&quot;, or \\\&quot;/tenants/&lt;tname&gt;/tenant-spaces/&lt;tsname&gt;\\\&quot; | [optional] 
 **resource_kind** | **str**| The kind of resource on which the Operation was performed. | [optional] 
 **resource_id** | **str**| The ID of resource on which the Operation was performed. | [optional] 
 **status** | **str**| The status of the Operation. Support for comma separated multiple status is deprecated, use IN list instead | [optional] 
 **created_after** | **str**|  | [optional] 
 **filter** | **str**| filter should use expression language for filtering | [optional] 
 **sort** | **str**| Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \&quot;sort&#x3D;size-,name\&quot;) | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 

### Return type

[**OperationList**](OperationList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

