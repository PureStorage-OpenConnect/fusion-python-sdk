# fusion.VolumesApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_volume**](VolumesApi.md#create_volume) | **POST** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes | Creates a Volume.
[**delete_volume**](VolumesApi.md#delete_volume) | **DELETE** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name} | Eradicate a specific volume.
[**get_volume**](VolumesApi.md#get_volume) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name} | Gets a specific Volume.
[**get_volume_by_id**](VolumesApi.md#get_volume_by_id) | **GET** /resources/volumes/{volume_id} | Gets a specific Volume.
[**get_volume_performance**](VolumesApi.md#get_volume_performance) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}/performance | (Provider) Gets performance metrics of a specific Volume.
[**get_volume_space**](VolumesApi.md#get_volume_space) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes/{volume_name}/space | (Provider) Gets space metrics of a specific Volume.
[**list_volumes**](VolumesApi.md#list_volumes) | **GET** /tenants/{tenant_name}/tenant-spaces/{tenant_space_name}/volumes | Gets a list of all Volumes.
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

Eradicate a specific volume.

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
    # Eradicate a specific volume.
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

