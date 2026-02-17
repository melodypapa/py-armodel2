"""AUTOSAR SOMEIPMessageTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 779)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.enums.json"""

from enum import Enum


class SOMEIPMessageTypeEnum(Enum):
    """AUTOSAR SOMEIPMessageTypeEnum enumeration."""

    NOTIFICATION = "notification"
    REQUEST = "request"
    REQUESTNORETURN = "requestNoReturn"
    RESPONSE = "response"
