# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from fusion.models.protection_policy_objective_type import ProtectionPolicyObjectiveType  # noqa: F401,E501

class RPO(ProtectionPolicyObjectiveType):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rpo': 'str'
    }
    if hasattr(ProtectionPolicyObjectiveType, "swagger_types"):
        swagger_types.update(ProtectionPolicyObjectiveType.swagger_types)

    attribute_map = {
        'rpo': 'rpo'
    }
    if hasattr(ProtectionPolicyObjectiveType, "attribute_map"):
        attribute_map.update(ProtectionPolicyObjectiveType.attribute_map)

    def __init__(self, rpo=None, *args, **kwargs):  # noqa: E501
        """RPO - a model defined in Swagger"""  # noqa: E501
        self._rpo = None
        self.discriminator = None
        self.rpo = rpo
        ProtectionPolicyObjectiveType.__init__(self, *args, **kwargs)

    @property
    def rpo(self):
        """Gets the rpo of this RPO.  # noqa: E501

        RPO (Recovery Point Objective) value. Format: only support subset of **Durations** format in https://en.wikipedia.org/wiki/ISO_8601. 1. The time designators(P,T,H,M,S) must be capital letters.  2. Only accepts whole numbers.  3. Leading zeroes are not required.  # noqa: E501

        :return: The rpo of this RPO.  # noqa: E501
        :rtype: str
        """
        return self._rpo

    @rpo.setter
    def rpo(self, rpo):
        """Sets the rpo of this RPO.

        RPO (Recovery Point Objective) value. Format: only support subset of **Durations** format in https://en.wikipedia.org/wiki/ISO_8601. 1. The time designators(P,T,H,M,S) must be capital letters.  2. Only accepts whole numbers.  3. Leading zeroes are not required.  # noqa: E501

        :param rpo: The rpo of this RPO.  # noqa: E501
        :type: str
        """
        if rpo is None:
            raise ValueError("Invalid value for `rpo`, must not be `None`")  # noqa: E501

        self._rpo = rpo

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(RPO, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RPO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
