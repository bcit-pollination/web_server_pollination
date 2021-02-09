# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.option import Option  # noqa: F401,E501
from swagger_server import util


class Question(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, election_id: int=None, max_selection_count: int=None, options: List[Option]=None):  # noqa: E501
        """Question - a model defined in Swagger

        :param election_id: The election_id of this Question.  # noqa: E501
        :type election_id: int
        :param max_selection_count: The max_selection_count of this Question.  # noqa: E501
        :type max_selection_count: int
        :param options: The options of this Question.  # noqa: E501
        :type options: List[Option]
        """
        self.swagger_types = {
            'election_id': int,
            'max_selection_count': int,
            'options': List[Option]
        }

        self.attribute_map = {
            'election_id': 'election_id',
            'max_selection_count': 'max_selection_count',
            'options': 'options'
        }
        self._election_id = election_id
        self._max_selection_count = max_selection_count
        self._options = options

    @classmethod
    def from_dict(cls, dikt) -> 'Question':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The question of this Question.  # noqa: E501
        :rtype: Question
        """
        return util.deserialize_model(dikt, cls)

    @property
    def election_id(self) -> int:
        """Gets the election_id of this Question.

        The id of the parent election  # noqa: E501

        :return: The election_id of this Question.
        :rtype: int
        """
        return self._election_id

    @election_id.setter
    def election_id(self, election_id: int):
        """Sets the election_id of this Question.

        The id of the parent election  # noqa: E501

        :param election_id: The election_id of this Question.
        :type election_id: int
        """

        self._election_id = election_id

    @property
    def max_selection_count(self) -> int:
        """Gets the max_selection_count of this Question.

        How many of the given question options can the user select. Must be >= 1  # noqa: E501

        :return: The max_selection_count of this Question.
        :rtype: int
        """
        return self._max_selection_count

    @max_selection_count.setter
    def max_selection_count(self, max_selection_count: int):
        """Sets the max_selection_count of this Question.

        How many of the given question options can the user select. Must be >= 1  # noqa: E501

        :param max_selection_count: The max_selection_count of this Question.
        :type max_selection_count: int
        """

        self._max_selection_count = max_selection_count

    @property
    def options(self) -> List[Option]:
        """Gets the options of this Question.

        The options given  # noqa: E501

        :return: The options of this Question.
        :rtype: List[Option]
        """
        return self._options

    @options.setter
    def options(self, options: List[Option]):
        """Sets the options of this Question.

        The options given  # noqa: E501

        :param options: The options of this Question.
        :type options: List[Option]
        """

        self._options = options
