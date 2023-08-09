# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.storage_services_api import StorageServicesApi  # noqa: E501
from fusion.rest import ApiException


class TestStorageServicesApi(unittest.TestCase):
    """StorageServicesApi unit test stubs"""

    def setUp(self):
        self.api = StorageServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_storage_service(self):
        """Test case for create_storage_service

        (Provider) Creates a Storage Service.  # noqa: E501
        """
        pass

    def test_delete_storage_service(self):
        """Test case for delete_storage_service

        (Provider) Deletes a Storage Service.  # noqa: E501
        """
        pass

    def test_get_storage_service(self):
        """Test case for get_storage_service

        Gets a specific Storage Service.  # noqa: E501
        """
        pass

    def test_get_storage_service_by_id(self):
        """Test case for get_storage_service_by_id

        Gets a specific Storage Service.  # noqa: E501
        """
        pass

    def test_list_storage_services(self):
        """Test case for list_storage_services

        Gets a list of all Storage Services.  # noqa: E501
        """
        pass

    def test_update_storage_service(self):
        """Test case for update_storage_service

        (Provider) Updates a Storage Service.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
