"""AUTOSAR DependencyUsageEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 132)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Implementation.enums.json"""

from enum import Enum


class DependencyUsageEnum(Enum):
    """AUTOSAR DependencyUsageEnum enumeration."""

    BUILD = "build"
    CODEGENERATION = "codegeneration"
    COMPILE = "compile"
    EXECUTE = "execute"
    LINK = "link"
