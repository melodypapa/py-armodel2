"""AUTOSAR ProgramminglanguageEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 621)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Implementation.enums.json"""

from enum import Enum


class ProgramminglanguageEnum(Enum):
    """AUTOSAR ProgramminglanguageEnum enumeration."""

    C = "c"
    CPP = "cpp"
    JAVA = "java"
