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
from fusion.models.resource_metadata import ResourceMetadata  # noqa: F401,E501

class APIClient(ResourceMetadata):
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
        'issuer': 'str',
        'public_key': 'str',
        'last_key_update': 'float',
        'last_used': 'float',
        'creator_id': 'str'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'issuer': 'issuer',
        'public_key': 'public_key',
        'last_key_update': 'last_key_update',
        'last_used': 'last_used',
        'creator_id': 'creator_id'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, issuer=None, public_key=None, last_key_update=None, last_used=None, creator_id=None, *args, **kwargs):  # noqa: E501
        """APIClient - a model defined in Swagger"""  # noqa: E501
        self._issuer = None
        self._public_key = None
        self._last_key_update = None
        self._last_used = None
        self._creator_id = None
        self.discriminator = None
        self.issuer = issuer
        self.public_key = public_key
        self.last_key_update = last_key_update
        self.last_used = last_used
        self.creator_id = creator_id
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def issuer(self):
        """Gets the issuer of this APIClient.  # noqa: E501

        The name of API client  # noqa: E501

        :return: The issuer of this APIClient.  # noqa: E501
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this APIClient.

        The name of API client  # noqa: E501

        :param issuer: The issuer of this APIClient.  # noqa: E501
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")  # noqa: E501

        self._issuer = issuer

    @property
    def public_key(self):
        """Gets the public_key of this APIClient.  # noqa: E501

        Public key in PEM format associated with the API Client  # noqa: E501

        :return: The public_key of this APIClient.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this APIClient.

        Public key in PEM format associated with the API Client  # noqa: E501

        :param public_key: The public_key of this APIClient.  # noqa: E501
        :type: str
        """
        if public_key is None:
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def last_key_update(self):
        """Gets the last_key_update of this APIClient.  # noqa: E501

        The last time API client was updated  # noqa: E501

        :return: The last_key_update of this APIClient.  # noqa: E501
        :rtype: float
        """
        return self._last_key_update

    @last_key_update.setter
    def last_key_update(self, last_key_update):
        """Sets the last_key_update of this APIClient.

        The last time API client was updated  # noqa: E501

        :param last_key_update: The last_key_update of this APIClient.  # noqa: E501
        :type: float
        """
        if last_key_update is None:
            raise ValueError("Invalid value for `last_key_update`, must not be `None`")  # noqa: E501

        self._last_key_update = last_key_update

    @property
    def last_used(self):
        """Gets the last_used of this APIClient.  # noqa: E501

        The last time API client was used  # noqa: E501

        :return: The last_used of this APIClient.  # noqa: E501
        :rtype: float
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this APIClient.

        The last time API client was used  # noqa: E501

        :param last_used: The last_used of this APIClient.  # noqa: E501
        :type: float
        """
        if last_used is None:
            raise ValueError("Invalid value for `last_used`, must not be `None`")  # noqa: E501

        self._last_used = last_used

    @property
    def creator_id(self):
        """Gets the creator_id of this APIClient.  # noqa: E501

        The Id of Principal that created the API Client  # noqa: E501

        :return: The creator_id of this APIClient.  # noqa: E501
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this APIClient.

        The Id of Principal that created the API Client  # noqa: E501

        :param creator_id: The creator_id of this APIClient.  # noqa: E501
        :type: str
        """
        if creator_id is None:
            raise ValueError("Invalid value for `creator_id`, must not be `None`")  # noqa: E501

        self._creator_id = creator_id

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
        if issubclass(APIClient, dict):
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
        if not isinstance(other, APIClient):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
