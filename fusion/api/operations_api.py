# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from fusion.api_client import ApiClient


class OperationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_operation(self, id, **kwargs):  # noqa: E501
        """Gets a specific Operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Operation ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_operation_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_operation_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_operation_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets a specific Operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Operation ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_operation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_operation`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/operations/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_operation_by_id(self, id, **kwargs):  # noqa: E501
        """Gets a specific Operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Operation ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_operation_by_id_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_operation_by_id_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_operation_by_id_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets a specific Operation.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_operation_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The Operation ID (required)
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :return: Operation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'x_request_id', 'authorization', 'x_correlation_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_operation_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_operation_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/resources/operations/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Operation',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_operations(self, **kwargs):  # noqa: E501
        """Gets a list of Operations matching the criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_operations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str action: The action requested.
        :param str request_id: The request ID supplied with the request.
        :param str request_collection: Default to \\\"/\\\", valid values take the form \\\"/\\\", \\\"/tenants/<tname>\\\", or \\\"/tenants/<tname>/tenant-spaces/<tsname>\\\"
        :param str resource_kind: The kind of resource on which the Operation was performed.
        :param str resource_id: The ID of resource on which the Operation was performed.
        :param str status: The status of the Operation. Support for comma separated multiple status is deprecated, use IN list instead.
        :param str created_after:
        :param int created_at:
        :param int started_at:
        :param int ended_at:
        :param str filter: filter should use expression language for filtering
        :param str sort: Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \"sort=size-,name\")
        :param int limit:
        :param int offset:
        :return: OperationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_operations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_operations_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_operations_with_http_info(self, **kwargs):  # noqa: E501
        """Gets a list of Operations matching the criteria.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_operations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_request_id: The Request ID supplied with the request, used to perform operations idempotently.
        :param str authorization: Access token (in JWT format) required to use any API endpoint.
        :param str x_correlation_id: The Correlation ID provided will be added to log messages and can be used for support. The same Correlation ID may be used for separate requests, to track a higher level workflow.
        :param str action: The action requested.
        :param str request_id: The request ID supplied with the request.
        :param str request_collection: Default to \\\"/\\\", valid values take the form \\\"/\\\", \\\"/tenants/<tname>\\\", or \\\"/tenants/<tname>/tenant-spaces/<tsname>\\\"
        :param str resource_kind: The kind of resource on which the Operation was performed.
        :param str resource_id: The ID of resource on which the Operation was performed.
        :param str status: The status of the Operation. Support for comma separated multiple status is deprecated, use IN list instead.
        :param str created_after:
        :param int created_at:
        :param int started_at:
        :param int ended_at:
        :param str filter: filter should use expression language for filtering
        :param str sort: Returns the response items in the order specified. Set sort to the field(s) in the response by which to sort. Sorting can be performed on any of the fields in the response, and the items can be sorted in ascending or descending order by these fields. By default, the response items are sorted in ascending order. To sort in descending order, append the minus sign (-) to the field. A single request can be sorted on multiple fields. For example, you can sort all volumes from largest to smallest volume size, and then sort volumes of the same size in ascending order by volume name. To sort on multiple fields, list the fields as comma-separated values. (E.g. \"sort=size-,name\")
        :param int limit:
        :param int offset:
        :return: OperationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_request_id', 'authorization', 'x_correlation_id', 'action', 'request_id', 'request_collection', 'resource_kind', 'resource_id', 'status', 'created_after', 'created_at', 'started_at', 'ended_at', 'filter', 'sort', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_operations" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'action' in params:
            query_params.append(('action', params['action']))  # noqa: E501
        if 'request_id' in params:
            query_params.append(('request_id', params['request_id']))  # noqa: E501
        if 'request_collection' in params:
            query_params.append(('request_collection', params['request_collection']))  # noqa: E501
        if 'resource_kind' in params:
            query_params.append(('resource_kind', params['resource_kind']))  # noqa: E501
        if 'resource_id' in params:
            query_params.append(('resource_id', params['resource_id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'created_after' in params:
            query_params.append(('created_after', params['created_after']))  # noqa: E501
        if 'created_at' in params:
            query_params.append(('created_at', params['created_at']))  # noqa: E501
        if 'started_at' in params:
            query_params.append(('started_at', params['started_at']))  # noqa: E501
        if 'ended_at' in params:
            query_params.append(('ended_at', params['ended_at']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}
        if 'x_request_id' in params:
            header_params['X-Request-ID'] = params['x_request_id']  # noqa: E501
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501
        if 'x_correlation_id' in params:
            header_params['X-Correlation-ID'] = params['x_correlation_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['accessToken', 'oauth']  # noqa: E501

        return self.api_client.call_api(
            '/operations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='OperationList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
