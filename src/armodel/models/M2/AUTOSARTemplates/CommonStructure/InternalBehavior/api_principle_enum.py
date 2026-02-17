"""AUTOSAR ApiPrincipleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 83)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 556)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.enums.json"""

from enum import Enum


class ApiPrincipleEnum(Enum):
    """AUTOSAR ApiPrincipleEnum enumeration."""

    COMMON = "common"
    PEREXECUTABLEMODULE = "perExecutableModule"
