from werkzeug.exceptions import Unauthorized

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
import src.db.mysql_interface as db
from src.constants_enums.obj_keys import LoginKeys
from src.auth.jwt import generate_token
from src.auth.password_hashing import hash_password


def login(body):  # noqa: E501
    """Login user

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse200
    """
    password_hash_tuple = db.
    uid_tuple = db.get_uid_with_credentials(body[LoginKeys.EMAIL], hash_password(body[LoginKeys.PASSWORD]))
    if uid_tuple is None:
        raise Unauthorized("Incorrect credentials")
    return InlineResponse200(generate_token(uid_tuple[0]))
