"""AUTOSAR IPsecHeaderTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 576)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class IPsecHeaderTypeEnum(Enum):
    """AUTOSAR IPsecHeaderTypeEnum enumeration."""

    AH = "ah"
    ESP = "esp"
    NONE = "none"
