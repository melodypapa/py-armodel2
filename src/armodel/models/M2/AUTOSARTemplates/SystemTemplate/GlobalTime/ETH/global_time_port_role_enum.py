"""AUTOSAR GlobalTimePortRoleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 875)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime_ETH.enums.json"""

from enum import Enum


class GlobalTimePortRoleEnum(Enum):
    """AUTOSAR GlobalTimePortRoleEnum enumeration."""

    DYNAMIC = "dynamic"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    TIMESLAVE = "timeSlave"
