"""AUTOSAR IPsecModeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 575)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class IPsecModeEnum(Enum):
    """AUTOSAR IPsecModeEnum enumeration."""

    TRANSPORT = "transport"
    TUNNEL = "tunnel"
