"""DataFilterTypeEnum enumeration."""

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
