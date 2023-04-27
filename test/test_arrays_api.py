# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.arrays_api import ArraysApi  # noqa: E501
from fusion.rest import ApiException


class TestArraysApi(unittest.TestCase):
    """ArraysApi unit test stubs"""

    def setUp(self):
        self.api = ArraysApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_array(self):
        """Test case for create_array

        (Provider) Registers an array into Pure Fusion.  # noqa: E501
        """
        pass

    def test_delete_array(self):
        """Test case for delete_array

        Deregister a specific array.  # noqa: E501
        """
        pass

    def test_get_array(self):
        """Test case for get_array

        (Provider) Gets a specific Array.  # noqa: E501
        """
        pass

    def test_get_array_by_id(self):
        """Test case for get_array_by_id

        (Provider) Gets a specific Array.  # noqa: E501
        """
        pass

    def test_get_array_performance(self):
        """Test case for get_array_performance

        (Provider) Gets performance metrics of a specific Array.  # noqa: E501
        """
        pass

    def test_get_array_space(self):
        """Test case for get_array_space

        (Provider) Gets performance metrics of a specific Array.  # noqa: E501
        """
        pass

    def test_list_arrays(self):
        """Test case for list_arrays

        (Provider) Gets a list of all arrays registered to Pure Fusion.  # noqa: E501
        """
        pass

    def test_update_array(self):
        """Test case for update_array

        Updates a specific array.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
