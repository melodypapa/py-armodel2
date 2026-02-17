"""AUTOSAR ArgumentDirectionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 40)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 104)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1999)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.enums.json"""

from enum import Enum


class ArgumentDirectionEnum(Enum):
    """AUTOSAR ArgumentDirectionEnum enumeration."""

    ININOUTOUT = "ininoutout"
