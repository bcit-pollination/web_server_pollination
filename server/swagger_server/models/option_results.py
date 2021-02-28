# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.option import Option  # noqa: F401,E501
from swagger_server import util


class OptionResults(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, option: Option=None, total_votes_for: float=None, vote_proportion_percent: float=None):  # noqa: E501
        """OptionResults - a model defined in Swagger

        :param option: The option of this OptionResults.  # noqa: E501
        :type option: Option
        :param total_votes_for: The total_votes_for of this OptionResults.  # noqa: E501
        :type total_votes_for: float
        :param vote_proportion_percent: The vote_proportion_percent of this OptionResults.  # noqa: E501
        :type vote_proportion_percent: float
        """
        self.swagger_types = {
            'option': Option,
            'total_votes_for': float,
            'vote_proportion_percent': float
        }

        self.attribute_map = {
            'option': 'option',
            'total_votes_for': 'total_votes_for',
            'vote_proportion_percent': 'vote_proportion_percent'
        }
        self._option = option
        self._total_votes_for = total_votes_for
        self._vote_proportion_percent = vote_proportion_percent

    @classmethod
    def from_dict(cls, dikt) -> 'OptionResults':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The option_results of this OptionResults.  # noqa: E501
        :rtype: OptionResults
        """
        return util.deserialize_model(dikt, cls)

    @property
    def option(self) -> Option:
        """Gets the option of this OptionResults.


        :return: The option of this OptionResults.
        :rtype: Option
        """
        return self._option

    @option.setter
    def option(self, option: Option):
        """Sets the option of this OptionResults.


        :param option: The option of this OptionResults.
        :type option: Option
        """
        if option is None:
            raise ValueError("Invalid value for `option`, must not be `None`")  # noqa: E501

        self._option = option

    @property
    def total_votes_for(self) -> float:
        """Gets the total_votes_for of this OptionResults.

        The total number of votes cast for this option. A float  # noqa: E501

        :return: The total_votes_for of this OptionResults.
        :rtype: float
        """
        return self._total_votes_for

    @total_votes_for.setter
    def total_votes_for(self, total_votes_for: float):
        """Sets the total_votes_for of this OptionResults.

        The total number of votes cast for this option. A float  # noqa: E501

        :param total_votes_for: The total_votes_for of this OptionResults.
        :type total_votes_for: float
        """
        if total_votes_for is None:
            raise ValueError("Invalid value for `total_votes_for`, must not be `None`")  # noqa: E501

        self._total_votes_for = total_votes_for

    @property
    def vote_proportion_percent(self) -> float:
        """Gets the vote_proportion_percent of this OptionResults.

        The voting proportion for this option, in percents. A float  # noqa: E501

        :return: The vote_proportion_percent of this OptionResults.
        :rtype: float
        """
        return self._vote_proportion_percent

    @vote_proportion_percent.setter
    def vote_proportion_percent(self, vote_proportion_percent: float):
        """Sets the vote_proportion_percent of this OptionResults.

        The voting proportion for this option, in percents. A float  # noqa: E501

        :param vote_proportion_percent: The vote_proportion_percent of this OptionResults.
        :type vote_proportion_percent: float
        """
        if vote_proportion_percent is None:
            raise ValueError("Invalid value for `vote_proportion_percent`, must not be `None`")  # noqa: E501

        self._vote_proportion_percent = vote_proportion_percent
