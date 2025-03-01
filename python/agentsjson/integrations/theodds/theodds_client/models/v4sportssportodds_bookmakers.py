# coding: utf-8

"""
    The Odds API

    To access the API, get a free API key from https://the-odds-api.com  # noqa: E501

    OpenAPI spec version: 4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class V4sportssportoddsBookmakers(object):
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
        'key': 'str',
        'title': 'str',
        'last_update': 'datetime',
        'markets': 'list[V4sportssportoddsMarkets]',
        'link': 'str',
        'sid': 'str'
    }

    attribute_map = {
        'key': 'key',
        'title': 'title',
        'last_update': 'last_update',
        'markets': 'markets',
        'link': 'link',
        'sid': 'sid'
    }

    def __init__(self, key=None, title=None, last_update=None, markets=None, link=None, sid=None):  # noqa: E501
        """V4sportssportoddsBookmakers - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._title = None
        self._last_update = None
        self._markets = None
        self._link = None
        self._sid = None
        self.discriminator = None
        if key is not None:
            self.key = key
        if title is not None:
            self.title = title
        if last_update is not None:
            self.last_update = last_update
        if markets is not None:
            self.markets = markets
        if link is not None:
            self.link = link
        if sid is not None:
            self.sid = sid

    @property
    def key(self):
        """Gets the key of this V4sportssportoddsBookmakers.  # noqa: E501

        A unique slug (key) of the bookmaker  # noqa: E501

        :return: The key of this V4sportssportoddsBookmakers.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V4sportssportoddsBookmakers.

        A unique slug (key) of the bookmaker  # noqa: E501

        :param key: The key of this V4sportssportoddsBookmakers.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def title(self):
        """Gets the title of this V4sportssportoddsBookmakers.  # noqa: E501

        A formatted title of the bookmaker  # noqa: E501

        :return: The title of this V4sportssportoddsBookmakers.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this V4sportssportoddsBookmakers.

        A formatted title of the bookmaker  # noqa: E501

        :param title: The title of this V4sportssportoddsBookmakers.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def last_update(self):
        """Gets the last_update of this V4sportssportoddsBookmakers.  # noqa: E501

        A timestamp of when the bookmaker's odds were last read. Will be an integer if dateFormat=unix, otherwise it will be a string  # noqa: E501

        :return: The last_update of this V4sportssportoddsBookmakers.  # noqa: E501
        :rtype: datetime
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this V4sportssportoddsBookmakers.

        A timestamp of when the bookmaker's odds were last read. Will be an integer if dateFormat=unix, otherwise it will be a string  # noqa: E501

        :param last_update: The last_update of this V4sportssportoddsBookmakers.  # noqa: E501
        :type: datetime
        """

        self._last_update = last_update

    @property
    def markets(self):
        """Gets the markets of this V4sportssportoddsBookmakers.  # noqa: E501

        The included market depends on the specified 'markets' GET param. NOTE Allow for the addition of new market types in future.  # noqa: E501

        :return: The markets of this V4sportssportoddsBookmakers.  # noqa: E501
        :rtype: list[V4sportssportoddsMarkets]
        """
        return self._markets

    @markets.setter
    def markets(self, markets):
        """Sets the markets of this V4sportssportoddsBookmakers.

        The included market depends on the specified 'markets' GET param. NOTE Allow for the addition of new market types in future.  # noqa: E501

        :param markets: The markets of this V4sportssportoddsBookmakers.  # noqa: E501
        :type: list[V4sportssportoddsMarkets]
        """

        self._markets = markets

    @property
    def link(self):
        """Gets the link of this V4sportssportoddsBookmakers.  # noqa: E501

        Link to the event on the bookmaker's website if available. This field is included when providing the query parameter includeLinks=true  # noqa: E501

        :return: The link of this V4sportssportoddsBookmakers.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this V4sportssportoddsBookmakers.

        Link to the event on the bookmaker's website if available. This field is included when providing the query parameter includeLinks=true  # noqa: E501

        :param link: The link of this V4sportssportoddsBookmakers.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def sid(self):
        """Gets the sid of this V4sportssportoddsBookmakers.  # noqa: E501

        The bookmaker's id of the event if available. This field is included when providing the query parameter includeSids=true  # noqa: E501

        :return: The sid of this V4sportssportoddsBookmakers.  # noqa: E501
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """Sets the sid of this V4sportssportoddsBookmakers.

        The bookmaker's id of the event if available. This field is included when providing the query parameter includeSids=true  # noqa: E501

        :param sid: The sid of this V4sportssportoddsBookmakers.  # noqa: E501
        :type: str
        """

        self._sid = sid

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
        if issubclass(V4sportssportoddsBookmakers, dict):
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
        if not isinstance(other, V4sportssportoddsBookmakers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
