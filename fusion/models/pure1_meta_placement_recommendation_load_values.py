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

class Pure1MetaPlacementRecommendationLoadValues(object):
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
        'avg': 'list[Pure1MetaValue]',
        'blended_max': 'list[Pure1MetaValue]'
    }

    attribute_map = {
        'avg': 'avg',
        'blended_max': 'blended_max'
    }

    def __init__(self, avg=None, blended_max=None):  # noqa: E501
        """Pure1MetaPlacementRecommendationLoadValues - a model defined in Swagger"""  # noqa: E501
        self._avg = None
        self._blended_max = None
        self.discriminator = None
        if avg is not None:
            self.avg = avg
        if blended_max is not None:
            self.blended_max = blended_max

    @property
    def avg(self):
        """Gets the avg of this Pure1MetaPlacementRecommendationLoadValues.  # noqa: E501


        :return: The avg of this Pure1MetaPlacementRecommendationLoadValues.  # noqa: E501
        :rtype: list[Pure1MetaValue]
        """
        return self._avg

    @avg.setter
    def avg(self, avg):
        """Sets the avg of this Pure1MetaPlacementRecommendationLoadValues.


        :param avg: The avg of this Pure1MetaPlacementRecommendationLoadValues.  # noqa: E501
        :type: list[Pure1MetaValue]
        """

        self._avg = avg

    @property
    def blended_max(self):
        """Gets the blended_max of this Pure1MetaPlacementRecommendationLoadValues.  # noqa: E501


        :return: The blended_max of this Pure1MetaPlacementRecommendationLoadValues.  # noqa: E501
        :rtype: list[Pure1MetaValue]
        """
        return self._blended_max

    @blended_max.setter
    def blended_max(self, blended_max):
        """Sets the blended_max of this Pure1MetaPlacementRecommendationLoadValues.


        :param blended_max: The blended_max of this Pure1MetaPlacementRecommendationLoadValues.  # noqa: E501
        :type: list[Pure1MetaValue]
        """

        self._blended_max = blended_max

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
        if issubclass(Pure1MetaPlacementRecommendationLoadValues, dict):
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
        if not isinstance(other, Pure1MetaPlacementRecommendationLoadValues):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
