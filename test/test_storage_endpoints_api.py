# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.storage_endpoints_api import StorageEndpointsApi  # noqa: E501
from fusion.rest import ApiException


class TestStorageEndpointsApi(unittest.TestCase):
    """StorageEndpointsApi unit test stubs"""

    def setUp(self):
        self.api = StorageEndpointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_storage_endpoint(self):
        """Test case for create_storage_endpoint

        (Provider) Creates a Storage Endpoint.  # noqa: E501
        """
        pass

    def test_delete_storage_endpoint(self):
        """Test case for delete_storage_endpoint

        (Provider) Deletes a specific Storage Endpoint.  # noqa: E501
        """
        pass

    def test_get_storage_endpoint(self):
        """Test case for get_storage_endpoint

        (Provider) Gets a specific Storage Endpoint.  # noqa: E501
        """
        pass

    def test_get_storage_endpoint_by_id(self):
        """Test case for get_storage_endpoint_by_id

        (Provider) Gets a specific Storage Endpoint.  # noqa: E501
        """
        pass

    def test_list_storage_endpoints(self):
        """Test case for list_storage_endpoints

        (Provider) Gets a list of all Storage Endpoints.  # noqa: E501
        """
        pass

    def test_update_storage_endpoint(self):
        """Test case for update_storage_endpoint

        (Provider) Updates a Storage Endpoint.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
