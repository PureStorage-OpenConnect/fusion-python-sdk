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
from fusion.api.storage_classes_api import StorageClassesApi  # noqa: E501
from fusion.rest import ApiException


class TestStorageClassesApi(unittest.TestCase):
    """StorageClassesApi unit test stubs"""

    def setUp(self):
        self.api = StorageClassesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_storage_class(self):
        """Test case for create_storage_class

        (Provider) Creates a Storage Class.  # noqa: E501
        """
        pass

    def test_delete_storage_class(self):
        """Test case for delete_storage_class

        Deletes a Storage Class.  # noqa: E501
        """
        pass

    def test_get_storage_class(self):
        """Test case for get_storage_class

        Gets a specific Storage Class.  # noqa: E501
        """
        pass

    def test_get_storage_class_by_id(self):
        """Test case for get_storage_class_by_id

        Gets a specific Storage Class.  # noqa: E501
        """
        pass

    def test_list_storage_classes(self):
        """Test case for list_storage_classes

        Gets a list of all Storage Classes.  # noqa: E501
        """
        pass

    def test_update_storage_class(self):
        """Test case for update_storage_class

        Updates a Storage Class.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
