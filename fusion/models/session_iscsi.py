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

class SessionIscsi(object):
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
        'initiator_iqn': 'str',
        'target_iqn': 'str',
        'initiator_portal': 'str',
        'target_discovery_address': 'str',
        'target_portal': 'str'
    }

    attribute_map = {
        'initiator_iqn': 'initiator_iqn',
        'target_iqn': 'target_iqn',
        'initiator_portal': 'initiator_portal',
        'target_discovery_address': 'target_discovery_address',
        'target_portal': 'target_portal'
    }

    def __init__(self, initiator_iqn=None, target_iqn=None, initiator_portal=None, target_discovery_address=None, target_portal=None):  # noqa: E501
        """SessionIscsi - a model defined in Swagger"""  # noqa: E501
        self._initiator_iqn = None
        self._target_iqn = None
        self._initiator_portal = None
        self._target_discovery_address = None
        self._target_portal = None
        self.discriminator = None
        if initiator_iqn is not None:
            self.initiator_iqn = initiator_iqn
        if target_iqn is not None:
            self.target_iqn = target_iqn
        if initiator_portal is not None:
            self.initiator_portal = initiator_portal
        if target_discovery_address is not None:
            self.target_discovery_address = target_discovery_address
        if target_portal is not None:
            self.target_portal = target_portal

    @property
    def initiator_iqn(self):
        """Gets the initiator_iqn of this SessionIscsi.  # noqa: E501

        The iSCSI Qualified Name of the Initiator.  # noqa: E501

        :return: The initiator_iqn of this SessionIscsi.  # noqa: E501
        :rtype: str
        """
        return self._initiator_iqn

    @initiator_iqn.setter
    def initiator_iqn(self, initiator_iqn):
        """Sets the initiator_iqn of this SessionIscsi.

        The iSCSI Qualified Name of the Initiator.  # noqa: E501

        :param initiator_iqn: The initiator_iqn of this SessionIscsi.  # noqa: E501
        :type: str
        """

        self._initiator_iqn = initiator_iqn

    @property
    def target_iqn(self):
        """Gets the target_iqn of this SessionIscsi.  # noqa: E501

        The iSCSI Qualified Name of the Target.  # noqa: E501

        :return: The target_iqn of this SessionIscsi.  # noqa: E501
        :rtype: str
        """
        return self._target_iqn

    @target_iqn.setter
    def target_iqn(self, target_iqn):
        """Sets the target_iqn of this SessionIscsi.

        The iSCSI Qualified Name of the Target.  # noqa: E501

        :param target_iqn: The target_iqn of this SessionIscsi.  # noqa: E501
        :type: str
        """

        self._target_iqn = target_iqn

    @property
    def initiator_portal(self):
        """Gets the initiator_portal of this SessionIscsi.  # noqa: E501

        TCP/IP network address and tcp port number of the iSCSI Initiator.  # noqa: E501

        :return: The initiator_portal of this SessionIscsi.  # noqa: E501
        :rtype: str
        """
        return self._initiator_portal

    @initiator_portal.setter
    def initiator_portal(self, initiator_portal):
        """Sets the initiator_portal of this SessionIscsi.

        TCP/IP network address and tcp port number of the iSCSI Initiator.  # noqa: E501

        :param initiator_portal: The initiator_portal of this SessionIscsi.  # noqa: E501
        :type: str
        """

        self._initiator_portal = initiator_portal

    @property
    def target_discovery_address(self):
        """Gets the target_discovery_address of this SessionIscsi.  # noqa: E501

        The iSCSI Discovery Login IP for this session.  # noqa: E501

        :return: The target_discovery_address of this SessionIscsi.  # noqa: E501
        :rtype: str
        """
        return self._target_discovery_address

    @target_discovery_address.setter
    def target_discovery_address(self, target_discovery_address):
        """Sets the target_discovery_address of this SessionIscsi.

        The iSCSI Discovery Login IP for this session.  # noqa: E501

        :param target_discovery_address: The target_discovery_address of this SessionIscsi.  # noqa: E501
        :type: str
        """

        self._target_discovery_address = target_discovery_address

    @property
    def target_portal(self):
        """Gets the target_portal of this SessionIscsi.  # noqa: E501

        TCP/IP network address and tcp port number of the iSCSI Target.  # noqa: E501

        :return: The target_portal of this SessionIscsi.  # noqa: E501
        :rtype: str
        """
        return self._target_portal

    @target_portal.setter
    def target_portal(self, target_portal):
        """Sets the target_portal of this SessionIscsi.

        TCP/IP network address and tcp port number of the iSCSI Target.  # noqa: E501

        :param target_portal: The target_portal of this SessionIscsi.  # noqa: E501
        :type: str
        """

        self._target_portal = target_portal

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
        if issubclass(SessionIscsi, dict):
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
        if not isinstance(other, SessionIscsi):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
