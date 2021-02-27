import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util
from src.auth.jwt import *
from src.db.mysql_interface import *


def login(body=None):  # noqa: E501
    """Login user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()  # noqa: E501

    uid = get_uid_with_credentials(body['email'], body['password'])
    return generate_token(uid) if uid else 'Not Authorized', 401


def logout():  # noqa: E501
    """Login user

     # noqa: E501


    :rtype: None
    """

    # Remove some server session information
    return 'do some magic!'
