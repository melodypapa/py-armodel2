"""AUTOSAR MacSecRoleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 177)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SecureCommunication.enums.json"""

from enum import Enum


class MacSecRoleEnum(Enum):
    """AUTOSAR MacSecRoleEnum enumeration."""

    KEYSERVER = "keyServer"
    PEER = "peer"
