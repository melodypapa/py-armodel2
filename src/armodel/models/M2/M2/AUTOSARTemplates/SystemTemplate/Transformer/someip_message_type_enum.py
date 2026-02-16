"""SOMEIPMessageTypeEnum enumeration."""

from enum import Enum


class SOMEIPMessageTypeEnum(Enum):
    """AUTOSAR SOMEIPMessageTypeEnum enumeration."""

    NOTIFICATION = "notification"
    REQUEST = "request"
    REQUESTNORETURN = "requestNoReturn"
    RESPONSE = "response"
