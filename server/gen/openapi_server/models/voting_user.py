# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.user import User
from openapi_server.models.voting_token import VotingToken
from openapi_server.models.voting_user_all_of import VotingUserAllOf
from openapi_server import util

from openapi_server.models.user import User  # noqa: E501
from openapi_server.models.voting_token import VotingToken  # noqa: E501
from openapi_server.models.voting_user_all_of import VotingUserAllOf  # noqa: E501

class VotingUser(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, first_name=None, last_name=None, email=None, dob=None, voting_token=None, user_org_id=None):  # noqa: E501
        """VotingUser - a model defined in OpenAPI

        :param id: The id of this VotingUser.  # noqa: E501
        :type id: int
        :param first_name: The first_name of this VotingUser.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this VotingUser.  # noqa: E501
        :type last_name: str
        :param email: The email of this VotingUser.  # noqa: E501
        :type email: str
        :param dob: The dob of this VotingUser.  # noqa: E501
        :type dob: date
        :param voting_token: The voting_token of this VotingUser.  # noqa: E501
        :type voting_token: str
        :param user_org_id: The user_org_id of this VotingUser.  # noqa: E501
        :type user_org_id: str
        """
        self.openapi_types = {
            'id': int,
            'first_name': str,
            'last_name': str,
            'email': str,
            'dob': date,
            'voting_token': str,
            'user_org_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'dob': 'dob',
            'voting_token': 'voting_token',
            'user_org_id': 'user_org_id'
        }

        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._dob = dob
        self._voting_token = voting_token
        self._user_org_id = user_org_id

    @classmethod
    def from_dict(cls, dikt) -> 'VotingUser':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The voting_user of this VotingUser.  # noqa: E501
        :rtype: VotingUser
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this VotingUser.


        :return: The id of this VotingUser.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VotingUser.


        :param id: The id of this VotingUser.
        :type id: int
        """

        self._id = id

    @property
    def first_name(self):
        """Gets the first_name of this VotingUser.


        :return: The first_name of this VotingUser.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this VotingUser.


        :param first_name: The first_name of this VotingUser.
        :type first_name: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this VotingUser.


        :return: The last_name of this VotingUser.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this VotingUser.


        :param last_name: The last_name of this VotingUser.
        :type last_name: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this VotingUser.


        :return: The email of this VotingUser.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this VotingUser.


        :param email: The email of this VotingUser.
        :type email: str
        """

        self._email = email

    @property
    def dob(self):
        """Gets the dob of this VotingUser.


        :return: The dob of this VotingUser.
        :rtype: date
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """Sets the dob of this VotingUser.


        :param dob: The dob of this VotingUser.
        :type dob: date
        """

        self._dob = dob

    @property
    def voting_token(self):
        """Gets the voting_token of this VotingUser.


        :return: The voting_token of this VotingUser.
        :rtype: str
        """
        return self._voting_token

    @voting_token.setter
    def voting_token(self, voting_token):
        """Sets the voting_token of this VotingUser.


        :param voting_token: The voting_token of this VotingUser.
        :type voting_token: str
        """

        self._voting_token = voting_token

    @property
    def user_org_id(self):
        """Gets the user_org_id of this VotingUser.

        The ID of the user within the organization (School id, Driver License, etc...)  # noqa: E501

        :return: The user_org_id of this VotingUser.
        :rtype: str
        """
        return self._user_org_id

    @user_org_id.setter
    def user_org_id(self, user_org_id):
        """Sets the user_org_id of this VotingUser.

        The ID of the user within the organization (School id, Driver License, etc...)  # noqa: E501

        :param user_org_id: The user_org_id of this VotingUser.
        :type user_org_id: str
        """

        self._user_org_id = user_org_id
