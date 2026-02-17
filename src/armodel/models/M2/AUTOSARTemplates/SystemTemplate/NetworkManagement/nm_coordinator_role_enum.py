"""AUTOSAR NmCoordinatorRoleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 676)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.enums.json"""

from enum import Enum


class NmCoordinatorRoleEnum(Enum):
    """AUTOSAR NmCoordinatorRoleEnum enumeration."""

    ACTIVE = "Active"
    PASSIVE = "Passive"
