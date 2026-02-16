"""HandleTimeoutEnum enumeration."""

from enum import Enum


class HandleTimeoutEnum(Enum):
    """AUTOSAR HandleTimeoutEnum enumeration."""

    NONE = "none"
    REPLACE = "replace"
    REPLACEBYTIMEOUTSUBSTITUTIONVALUE = "replaceByTimeoutSubstitutionValue"
