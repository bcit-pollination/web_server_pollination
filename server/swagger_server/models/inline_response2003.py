# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.org_user import OrgUser  # noqa: F401,E501
from swagger_server import util


class InlineResponse2003(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, users: List[OrgUser]=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger

        :param users: The users of this InlineResponse2003.  # noqa: E501
        :type users: List[OrgUser]
        """
        self.swagger_types = {
            'users': List[OrgUser]
        }

        self.attribute_map = {
            'users': 'users'
        }
        self._users = users

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2003':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_3 of this InlineResponse2003.  # noqa: E501
        :rtype: InlineResponse2003
        """
        return util.deserialize_model(dikt, cls)

    @property
    def users(self) -> List[OrgUser]:
        """Gets the users of this InlineResponse2003.

        An array of all users subscribed to vote  # noqa: E501

        :return: The users of this InlineResponse2003.
        :rtype: List[OrgUser]
        """
        return self._users

    @users.setter
    def users(self, users: List[OrgUser]):
        """Sets the users of this InlineResponse2003.

        An array of all users subscribed to vote  # noqa: E501

        :param users: The users of this InlineResponse2003.
        :type users: List[OrgUser]
        """

        self._users = users
