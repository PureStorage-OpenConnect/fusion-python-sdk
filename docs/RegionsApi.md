# fusion.RegionsApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_region**](RegionsApi.md#create_region) | **POST** /regions | Creates a Region.
[**delete_region**](RegionsApi.md#delete_region) | **DELETE** /regions/{region_name} | Deletes a specific Region.
[**get_region**](RegionsApi.md#get_region) | **GET** /regions/{region_name} | Gets a specific Region.
[**get_region_by_id**](RegionsApi.md#get_region_by_id) | **GET** /resources/regions/{region_id} | Gets a specific Region.
[**list_regions**](RegionsApi.md#list_regions) | **GET** /regions | Gets a list of all Regions.
[**query_regions**](RegionsApi.md#query_regions) | **GET** /resources/regions | Get all Regions in the org. Provide a filter to search for specific Regions.
[**update_region**](RegionsApi.md#update_region) | **PATCH** /regions/{region_name} | Updates a Region.

# **create_region**
> Operation create_region(body, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Creates a Region.

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
api_instance = fusion.RegionsApi(fusion.ApiClient(configuration))
body = fusion.RegionPost() # RegionPost | 
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Creates a Region.
    api_response = api_instance.create_region(body, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->create_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegionPost**](RegionPost.md)|  | 
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

# **delete_region**
> Operation delete_region(region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Deletes a specific Region.

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
api_instance = fusion.RegionsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Deletes a specific Region.
    api_response = api_instance.delete_region(region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->delete_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
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

# **get_region**
> Region get_region(region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Region.

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
api_instance = fusion.RegionsApi(fusion.ApiClient(configuration))
region_name = 'region_name_example' # str | The Region name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Region.
    api_response = api_instance.get_region(region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->get_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| The Region name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_region_by_id**
> Region get_region_by_id(region_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Region.

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
api_instance = fusion.RegionsApi(fusion.ApiClient(configuration))
region_id = 'region_id_example' # str | The Region ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Region.
    api_response = api_instance.get_region_by_id(region_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->get_region_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_id** | **str**| The Region ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**Region**](Region.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_regions**
> RegionList list_regions(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, filter=filter, sort=sort, limit=limit, offset=offset, id=id, name=name, display_name=display_name)

Gets a list of all Regions.

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
api_instance = fusion.RegionsApi(fusion.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)
filter = 'filter_example' # str | filter should use expression language for filtering (optional)
sort = 'sort_example' # str | Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \"sort=size-,name\") (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
display_name = 'display_name_example' # str |  (optional)

try:
    # Gets a list of all Regions.
    api_response = api_instance.list_regions(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id, filter=filter, sort=sort, limit=limit, offset=offset, id=id, name=name, display_name=display_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->list_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 
 **filter** | **str**| filter should use expression language for filtering | [optional] 
 **sort** | **str**| Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \&quot;sort&#x3D;size-,name\&quot;) | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **display_name** | **str**|  | [optional] 

### Return type

[**RegionList**](RegionList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_regions**
> RegionList query_regions(filter=filter, sort=sort, limit=limit, offset=offset, id=id, name=name, display_name=display_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Get all Regions in the org. Provide a filter to search for specific Regions.

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
api_instance = fusion.RegionsApi(fusion.ApiClient(configuration))
filter = 'filter_example' # str | filter should use expression language for filtering (optional)
sort = 'sort_example' # str | Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \"sort=size-,name\") (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
display_name = 'display_name_example' # str |  (optional)
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Get all Regions in the org. Provide a filter to search for specific Regions.
    api_response = api_instance.query_regions(filter=filter, sort=sort, limit=limit, offset=offset, id=id, name=name, display_name=display_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->query_regions: %s\n" % e)
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
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**RegionList**](RegionList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_region**
> Operation update_region(body, region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Updates a Region.

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
api_instance = fusion.RegionsApi(fusion.ApiClient(configuration))
body = fusion.RegionPatch() # RegionPatch | 
region_name = 'region_name_example' # str | The Region name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Updates a Region.
    api_response = api_instance.update_region(body, region_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->update_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegionPatch**](RegionPatch.md)|  | 
 **region_name** | **str**| The Region name | 
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

