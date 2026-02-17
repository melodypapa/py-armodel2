"""AUTOSAR IPsecDpdActionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 577)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class IPsecDpdActionEnum(Enum):
    """AUTOSAR IPsecDpdActionEnum enumeration."""

    CLEAR = "clear"
    RESTART = "restart"
