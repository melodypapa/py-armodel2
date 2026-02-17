"""AUTOSAR MacSecFailPermissiveModeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 177)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class MacSecFailPermissiveModeEnum(Enum):
    """AUTOSAR MacSecFailPermissiveModeEnum enumeration."""

    NEVER = "never"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    TIMEOUT = "timeout"
