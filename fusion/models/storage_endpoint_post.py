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
from fusion.models.resource_post import ResourcePost  # noqa: F401,E501

class StorageEndpointPost(ResourcePost):
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
        'endpoint_type': 'str',
        'iscsi': 'StorageEndpointIscsiPost',
        'cbs_azure_iscsi': 'StorageEndpointCbsAzureIscsiPost'
    }
    if hasattr(ResourcePost, "swagger_types"):
        swagger_types.update(ResourcePost.swagger_types)

    attribute_map = {
        'endpoint_type': 'endpoint_type',
        'iscsi': 'iscsi',
        'cbs_azure_iscsi': 'cbs_azure_iscsi'
    }
    if hasattr(ResourcePost, "attribute_map"):
        attribute_map.update(ResourcePost.attribute_map)

    def __init__(self, endpoint_type=None, iscsi=None, cbs_azure_iscsi=None, *args, **kwargs):  # noqa: E501
        """StorageEndpointPost - a model defined in Swagger"""  # noqa: E501
        self._endpoint_type = None
        self._iscsi = None
        self._cbs_azure_iscsi = None
        self.discriminator = None
        self.endpoint_type = endpoint_type
        if iscsi is not None:
            self.iscsi = iscsi
        if cbs_azure_iscsi is not None:
            self.cbs_azure_iscsi = cbs_azure_iscsi
        ResourcePost.__init__(self, *args, **kwargs)

    @property
    def endpoint_type(self):
        """Gets the endpoint_type of this StorageEndpointPost.  # noqa: E501

        The endpoint type.  # noqa: E501

        :return: The endpoint_type of this StorageEndpointPost.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """Sets the endpoint_type of this StorageEndpointPost.

        The endpoint type.  # noqa: E501

        :param endpoint_type: The endpoint_type of this StorageEndpointPost.  # noqa: E501
        :type: str
        """
        if endpoint_type is None:
            raise ValueError("Invalid value for `endpoint_type`, must not be `None`")  # noqa: E501
        allowed_values = ["iscsi", "cbs-azure-iscsi"]  # noqa: E501
        if endpoint_type not in allowed_values:
            raise ValueError(
                "Invalid value for `endpoint_type` ({0}), must be one of {1}"  # noqa: E501
                .format(endpoint_type, allowed_values)
            )

        self._endpoint_type = endpoint_type

    @property
    def iscsi(self):
        """Gets the iscsi of this StorageEndpointPost.  # noqa: E501


        :return: The iscsi of this StorageEndpointPost.  # noqa: E501
        :rtype: StorageEndpointIscsiPost
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """Sets the iscsi of this StorageEndpointPost.


        :param iscsi: The iscsi of this StorageEndpointPost.  # noqa: E501
        :type: StorageEndpointIscsiPost
        """

        self._iscsi = iscsi

    @property
    def cbs_azure_iscsi(self):
        """Gets the cbs_azure_iscsi of this StorageEndpointPost.  # noqa: E501


        :return: The cbs_azure_iscsi of this StorageEndpointPost.  # noqa: E501
        :rtype: StorageEndpointCbsAzureIscsiPost
        """
        return self._cbs_azure_iscsi

    @cbs_azure_iscsi.setter
    def cbs_azure_iscsi(self, cbs_azure_iscsi):
        """Sets the cbs_azure_iscsi of this StorageEndpointPost.


        :param cbs_azure_iscsi: The cbs_azure_iscsi of this StorageEndpointPost.  # noqa: E501
        :type: StorageEndpointCbsAzureIscsiPost
        """

        self._cbs_azure_iscsi = cbs_azure_iscsi

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
        if issubclass(StorageEndpointPost, dict):
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
        if not isinstance(other, StorageEndpointPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
