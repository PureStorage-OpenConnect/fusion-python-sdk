# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class StorageEndpointCbsAzureIscsi(object):
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
        'storage_endpoint_collection_identity': 'str',
        'load_balancer': 'str',
        'load_balancer_addresses': 'list[str]'
    }

    attribute_map = {
        'storage_endpoint_collection_identity': 'storage_endpoint_collection_identity',
        'load_balancer': 'load_balancer',
        'load_balancer_addresses': 'load_balancer_addresses'
    }

    def __init__(self, storage_endpoint_collection_identity=None, load_balancer=None, load_balancer_addresses=None):  # noqa: E501
        """StorageEndpointCbsAzureIscsi - a model defined in Swagger"""  # noqa: E501
        self._storage_endpoint_collection_identity = None
        self._load_balancer = None
        self._load_balancer_addresses = None
        self.discriminator = None
        if storage_endpoint_collection_identity is not None:
            self.storage_endpoint_collection_identity = storage_endpoint_collection_identity
        if load_balancer is not None:
            self.load_balancer = load_balancer
        if load_balancer_addresses is not None:
            self.load_balancer_addresses = load_balancer_addresses

    @property
    def storage_endpoint_collection_identity(self):
        """Gets the storage_endpoint_collection_identity of this StorageEndpointCbsAzureIscsi.  # noqa: E501

        The Storage Endpoint Collection Identity which belongs to the Azure entities.  # noqa: E501

        :return: The storage_endpoint_collection_identity of this StorageEndpointCbsAzureIscsi.  # noqa: E501
        :rtype: str
        """
        return self._storage_endpoint_collection_identity

    @storage_endpoint_collection_identity.setter
    def storage_endpoint_collection_identity(self, storage_endpoint_collection_identity):
        """Sets the storage_endpoint_collection_identity of this StorageEndpointCbsAzureIscsi.

        The Storage Endpoint Collection Identity which belongs to the Azure entities.  # noqa: E501

        :param storage_endpoint_collection_identity: The storage_endpoint_collection_identity of this StorageEndpointCbsAzureIscsi.  # noqa: E501
        :type: str
        """

        self._storage_endpoint_collection_identity = storage_endpoint_collection_identity

    @property
    def load_balancer(self):
        """Gets the load_balancer of this StorageEndpointCbsAzureIscsi.  # noqa: E501

        The Load Balancer id which gives permissions to CBS array appliations to modify the Load Balancer.  # noqa: E501

        :return: The load_balancer of this StorageEndpointCbsAzureIscsi.  # noqa: E501
        :rtype: str
        """
        return self._load_balancer

    @load_balancer.setter
    def load_balancer(self, load_balancer):
        """Sets the load_balancer of this StorageEndpointCbsAzureIscsi.

        The Load Balancer id which gives permissions to CBS array appliations to modify the Load Balancer.  # noqa: E501

        :param load_balancer: The load_balancer of this StorageEndpointCbsAzureIscsi.  # noqa: E501
        :type: str
        """

        self._load_balancer = load_balancer

    @property
    def load_balancer_addresses(self):
        """Gets the load_balancer_addresses of this StorageEndpointCbsAzureIscsi.  # noqa: E501


        :return: The load_balancer_addresses of this StorageEndpointCbsAzureIscsi.  # noqa: E501
        :rtype: list[str]
        """
        return self._load_balancer_addresses

    @load_balancer_addresses.setter
    def load_balancer_addresses(self, load_balancer_addresses):
        """Sets the load_balancer_addresses of this StorageEndpointCbsAzureIscsi.


        :param load_balancer_addresses: The load_balancer_addresses of this StorageEndpointCbsAzureIscsi.  # noqa: E501
        :type: list[str]
        """

        self._load_balancer_addresses = load_balancer_addresses

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
        if issubclass(StorageEndpointCbsAzureIscsi, dict):
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
        if not isinstance(other, StorageEndpointCbsAzureIscsi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
