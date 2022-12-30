# fusion.VolumesApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_volume**](VolumesApi.md#create_volume) | **POST** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes | Creates a Volume.
[**delete_volume**](VolumesApi.md#delete_volume) | **DELETE** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name} | Eradicate a specific volume. Volume has to be destroyed before it can be eradicated.
[**get_volume**](VolumesApi.md#get_volume) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name} | Gets a specific Volume.
[**get_volume_by_id**](VolumesApi.md#get_volume_by_id) | **GET** /resources/volumes/{volume_id} | Gets a specific Volume.
[**get_volume_performance**](VolumesApi.md#get_volume_performance) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}/performance | (Provider) Gets performance metrics of a specific Volume.
[**get_volume_space**](VolumesApi.md#get_volume_space) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}/space | (Provider) Gets space metrics of a specific Volume.
[**list_volumes**](VolumesApi.md#list_volumes) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes | Gets a list of all Volumes.
[**query_volumes**](VolumesApi.md#query_volumes) | **GET** /resources/volumes | (Opt-in) Get all Volumes in the org. Provide a filter to search for specific volumes.
[**update_volume**](VolumesApi.md#update_volume) | **PATCH** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name} | Updates a Volume -- renaming, and resizing it; changing its Storage Class; changing its Placement Group; adding or removing host connections.

# **create_volume**
> Operation create_volume(body, tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Creates a Volume.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
body = fusion.VolumePost() # VolumePost | 
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Creates a Volume.
    api_response = api_instance.create_volume(body, tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->create_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VolumePost**](VolumePost.md)|  | 
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_volume**
> Operation delete_volume(tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Eradicate a specific volume. Volume has to be destroyed before it can be eradicated.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
volume_name = 'volume_name_example' # str | The Volume name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Eradicate a specific volume. Volume has to be destroyed before it can be eradicated.
    api_response = api_instance.delete_volume(tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->delete_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **volume_name** | **str**| The Volume name | 
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

# **get_volume**
> Volume get_volume(tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Volume.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
volume_name = 'volume_name_example' # str | The Volume name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Volume.
    api_response = api_instance.get_volume(tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->get_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **volume_name** | **str**| The Volume name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Volume**](Volume.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_by_id**
> Volume get_volume_by_id(volume_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Volume.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
volume_id = 'volume_id_example' # str | The Volume ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Volume.
    api_response = api_instance.get_volume_by_id(volume_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->get_volume_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volume_id** | **str**| The Volume ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Volume**](Volume.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_performance**
> Performance get_volume_performance(tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets performance metrics of a specific Volume.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
volume_name = 'volume_name_example' # str | The Volume name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets performance metrics of a specific Volume.
    api_response = api_instance.get_volume_performance(tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->get_volume_performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **volume_name** | **str**| The Volume name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Performance**](Performance.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_space**
> Space get_volume_space(tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Provider) Gets space metrics of a specific Volume.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
volume_name = 'volume_name_example' # str | The Volume name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Provider) Gets space metrics of a specific Volume.
    api_response = api_instance.get_volume_space(tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->get_volume_space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **volume_name** | **str**| The Volume name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Space**](Space.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_volumes**
> VolumeList list_volumes(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a list of all Volumes.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a list of all Volumes.
    api_response = api_instance.list_volumes(tenant_name, tenant_space_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->list_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**VolumeList**](VolumeList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_volumes**
> VolumeList query_volumes(filter=filter, sort=sort, limit=limit, offset=offset, id=id, name=name, display_name=display_name, serial_number=serial_number, size=size, created_at=created_at, tenant_space_id=tenant_space_id, tenant_id=tenant_id, storage_class_id=storage_class_id, placement_group_id=placement_group_id, protection_policy_id=protection_policy_id, array_id=array_id, source_volume_snapshot_id=source_volume_snapshot_id, iqn=iqn, destroyed=destroyed, time_remaining=time_remaining, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

(Opt-in) Get all Volumes in the org. Provide a filter to search for specific volumes.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
filter = 'filter_example' # str | filter should use expression language for filtering (optional)
sort = 'sort_example' # str | Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \"sort=size-,name\") (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
display_name = 'display_name_example' # str |  (optional)
serial_number = 'serial_number_example' # str |  (optional)
size = 789 # int |  (optional)
created_at = 789 # int |  (optional)
tenant_space_id = 'tenant_space_id_example' # str |  (optional)
tenant_id = 'tenant_id_example' # str |  (optional)
storage_class_id = 'storage_class_id_example' # str |  (optional)
placement_group_id = 'placement_group_id_example' # str |  (optional)
protection_policy_id = 'protection_policy_id_example' # str |  (optional)
array_id = 'array_id_example' # str |  (optional)
source_volume_snapshot_id = 'source_volume_snapshot_id_example' # str |  (optional)
iqn = 'iqn_example' # str |  (optional)
destroyed = true # bool |  (optional)
time_remaining = 789 # int |  (optional)
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # (Opt-in) Get all Volumes in the org. Provide a filter to search for specific volumes.
    api_response = api_instance.query_volumes(filter=filter, sort=sort, limit=limit, offset=offset, id=id, name=name, display_name=display_name, serial_number=serial_number, size=size, created_at=created_at, tenant_space_id=tenant_space_id, tenant_id=tenant_id, storage_class_id=storage_class_id, placement_group_id=placement_group_id, protection_policy_id=protection_policy_id, array_id=array_id, source_volume_snapshot_id=source_volume_snapshot_id, iqn=iqn, destroyed=destroyed, time_remaining=time_remaining, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->query_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| filter should use expression language for filtering | [optional] 
 **sort** | **str**| Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \&quot;sort&#x3D;size-,name\&quot;) | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **display_name** | **str**|  | [optional] 
 **serial_number** | **str**|  | [optional] 
 **size** | **int**|  | [optional] 
 **created_at** | **int**|  | [optional] 
 **tenant_space_id** | **str**|  | [optional] 
 **tenant_id** | **str**|  | [optional] 
 **storage_class_id** | **str**|  | [optional] 
 **placement_group_id** | **str**|  | [optional] 
 **protection_policy_id** | **str**|  | [optional] 
 **array_id** | **str**|  | [optional] 
 **source_volume_snapshot_id** | **str**|  | [optional] 
 **iqn** | **str**|  | [optional] 
 **destroyed** | **bool**|  | [optional] 
 **time_remaining** | **int**|  | [optional] 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**VolumeList**](VolumeList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_volume**
> Operation update_volume(body, tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Updates a Volume -- renaming, and resizing it; changing its Storage Class; changing its Placement Group; adding or removing host connections.

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
api_instance = fusion.VolumesApi(fusion.ApiClient(configuration))
body = fusion.VolumePatch() # VolumePatch | 
tenant_name = 'tenant_name_example' # str | The Tenant name
tenant_space_name = 'tenant_space_name_example' # str | The Tenant Space name
volume_name = 'volume_name_example' # str | The Volume name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Updates a Volume -- renaming, and resizing it; changing its Storage Class; changing its Placement Group; adding or removing host connections.
    api_response = api_instance.update_volume(body, tenant_name, tenant_space_name, volume_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->update_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VolumePatch**](VolumePatch.md)|  | 
 **tenant_name** | **str**| The Tenant name | 
 **tenant_space_name** | **str**| The Tenant Space name | 
 **volume_name** | **str**| The Volume name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

