"""MemorySectionType enumeration."""

from enum import Enum


class MemorySectionType(Enum):
    """AUTOSAR MemorySectionType enumeration."""

    CALIBRATIONVARIABLES = "calibrationVariables"
    CALPRM = "calprm"
    CODE = "code"
    CONFIGDATA = "configData"
    CONST = "const"
    EXCLUDEFROMFLASHTIMEIN = "excludeFromFlashtimein"
    VAR = "var"
