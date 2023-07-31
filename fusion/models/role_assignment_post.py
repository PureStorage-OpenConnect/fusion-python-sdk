# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RoleAssignmentPost(object):
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
        'scope': 'str',
        'principal': 'str'
    }

    attribute_map = {
        'scope': 'scope',
        'principal': 'principal'
    }

    def __init__(self, scope=None, principal=None):  # noqa: E501
        """RoleAssignmentPost - a model defined in Swagger"""  # noqa: E501
        self._scope = None
        self._principal = None
        self.discriminator = None
        self.scope = scope
        self.principal = principal

    @property
    def scope(self):
        """Gets the scope of this RoleAssignmentPost.  # noqa: E501

        The fully-qualified resource path (self_link) to scope the Role Assignment to.  # noqa: E501

        :return: The scope of this RoleAssignmentPost.  # noqa: E501
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this RoleAssignmentPost.

        The fully-qualified resource path (self_link) to scope the Role Assignment to.  # noqa: E501

        :param scope: The scope of this RoleAssignmentPost.  # noqa: E501
        :type: str
        """
        if scope is None:
            raise ValueError("Invalid value for `scope`, must not be `None`")  # noqa: E501

        self._scope = scope

    @property
    def principal(self):
        """Gets the principal of this RoleAssignmentPost.  # noqa: E501

        The unique ID of the principal (User or API Client) to assign to the role.  # noqa: E501

        :return: The principal of this RoleAssignmentPost.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this RoleAssignmentPost.

        The unique ID of the principal (User or API Client) to assign to the role.  # noqa: E501

        :param principal: The principal of this RoleAssignmentPost.  # noqa: E501
        :type: str
        """
        if principal is None:
            raise ValueError("Invalid value for `principal`, must not be `None`")  # noqa: E501

        self._principal = principal

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
        if issubclass(RoleAssignmentPost, dict):
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
        if not isinstance(other, RoleAssignmentPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
