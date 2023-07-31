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
from fusion.models.protection_policy_objective_type import ProtectionPolicyObjectiveType  # noqa: E501
from fusion.rest import ApiException


class TestProtectionPolicyObjectiveType(unittest.TestCase):
    """ProtectionPolicyObjectiveType unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProtectionPolicyObjectiveType(self):
        """Test ProtectionPolicyObjectiveType"""
        # FIXME: construct object with mandatory attributes with example values
        # model = fusion.models.protection_policy_objective_type.ProtectionPolicyObjectiveType()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
