"""AUTOSAR MemorySectionType enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 146)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 417)

JSON Source: packages/M2_MSR_DataDictionary_AuxillaryObjects.enums.json"""

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
