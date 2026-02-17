"""AUTOSAR ReentrancyLevelEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 73)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.enums.json"""

from enum import Enum


class ReentrancyLevelEnum(Enum):
    """AUTOSAR ReentrancyLevelEnum enumeration."""

    MULTICOREREENTRANTON = "multicoreReentranton"
    NONREENTRANT = "nonReentrant"
    SINGLECOREREENTRANT = "singleCoreReentrant"
