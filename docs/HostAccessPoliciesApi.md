# fusion.HostAccessPoliciesApi

All URIs are relative to *https://api.pure1.purestorage.com/fusion/api/1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_host_access_policy**](HostAccessPoliciesApi.md#create_host_access_policy) | **POST** /host-access-policies | Creates a Host Access Policy.
[**delete_host_access_policy**](HostAccessPoliciesApi.md#delete_host_access_policy) | **DELETE** /host-access-policies/{host_access_policy_name} | Deletes a specific host access policy.
[**get_host_access_policy**](HostAccessPoliciesApi.md#get_host_access_policy) | **GET** /host-access-policies/{host_access_policy_name} | Gets a specific Host Access Policy.
[**get_host_access_policy_by_id**](HostAccessPoliciesApi.md#get_host_access_policy_by_id) | **GET** /resources/host-access-policies/{host_access_policy_id} | Gets a specific Host Access Policy.
[**list_host_access_policies**](HostAccessPoliciesApi.md#list_host_access_policies) | **GET** /host-access-policies | Gets a list of all Host Access Policies.

# **create_host_access_policy**
> Operation create_host_access_policy(body, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Creates a Host Access Policy.

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
api_instance = fusion.HostAccessPoliciesApi(fusion.ApiClient(configuration))
body = fusion.HostAccessPoliciesPost() # HostAccessPoliciesPost | 
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Creates a Host Access Policy.
    api_response = api_instance.create_host_access_policy(body, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostAccessPoliciesApi->create_host_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**HostAccessPoliciesPost**](HostAccessPoliciesPost.md)|  | 
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

# **delete_host_access_policy**
> Operation delete_host_access_policy(host_access_policy_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Deletes a specific host access policy.

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
api_instance = fusion.HostAccessPoliciesApi(fusion.ApiClient(configuration))
host_access_policy_name = 'host_access_policy_name_example' # str | The Host policy name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Deletes a specific host access policy.
    api_response = api_instance.delete_host_access_policy(host_access_policy_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostAccessPoliciesApi->delete_host_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_access_policy_name** | **str**| The Host policy name | 
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

# **get_host_access_policy**
> HostAccessPolicy get_host_access_policy(host_access_policy_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Host Access Policy.

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
api_instance = fusion.HostAccessPoliciesApi(fusion.ApiClient(configuration))
host_access_policy_name = 'host_access_policy_name_example' # str | The Host policy name
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Host Access Policy.
    api_response = api_instance.get_host_access_policy(host_access_policy_name, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostAccessPoliciesApi->get_host_access_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_access_policy_name** | **str**| The Host policy name | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**HostAccessPolicy**](HostAccessPolicy.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_host_access_policy_by_id**
> HostAccessPolicy get_host_access_policy_by_id(host_access_policy_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a specific Host Access Policy.

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
api_instance = fusion.HostAccessPoliciesApi(fusion.ApiClient(configuration))
host_access_policy_id = 'host_access_policy_id_example' # str | The Host policy ID
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a specific Host Access Policy.
    api_response = api_instance.get_host_access_policy_by_id(host_access_policy_id, x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostAccessPoliciesApi->get_host_access_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_access_policy_id** | **str**| The Host policy ID | 
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**HostAccessPolicy**](HostAccessPolicy.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_host_access_policies**
> HostAccessPolicyList list_host_access_policies(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)

Gets a list of all Host Access Policies.

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
api_instance = fusion.HostAccessPoliciesApi(fusion.ApiClient(configuration))
x_request_id = 'x_request_id_example' # str | The Request ID supplied with the request, used to perform operations idempotently. (optional)
authorization = 'authorization_example' # str | Access token (in JWT format) required to use any API endpoint. (optional)
x_correlation_id = 'x_correlation_id_example' # str | The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. (optional)

try:
    # Gets a list of all Host Access Policies.
    api_response = api_instance.list_host_access_policies(x_request_id=x_request_id, authorization=authorization, x_correlation_id=x_correlation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostAccessPoliciesApi->list_host_access_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_request_id** | **str**| The Request ID supplied with the request, used to perform operations idempotently. | [optional] 
 **authorization** | **str**| Access token (in JWT format) required to use any API endpoint. | [optional] 
 **x_correlation_id** | **str**| The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow. | [optional] 

### Return type

[**HostAccessPolicyList**](HostAccessPolicyList.md)

### Authorization

[accessToken](../README.md#accessToken), [oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

