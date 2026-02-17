"""AUTOSAR DataFilterTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 182)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 394)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Filter.enums.json"""

from enum import Enum


class DataFilterTypeEnum(Enum):
    """AUTOSAR DataFilterTypeEnum enumeration."""

    ALWAYS = "always"
    MASKEDNEWDIFFERSMASKEDOLD = "maskedNewDiffersMaskedOld"
    MASKEDNEWDIFFERSX = "maskedNewDiffersX"
    MASKEDNEWEQUALSX = "maskedNewEqualsX"
    NEVER = "never"
    NEWISOUTSIDE = "newIsOutside"
    NEWISWITHINMINONEEVERYN = "newIsWithinminoneEveryN"
