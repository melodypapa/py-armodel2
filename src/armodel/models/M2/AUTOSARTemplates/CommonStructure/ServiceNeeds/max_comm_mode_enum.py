"""AUTOSAR MaxCommModeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 233)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 711)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class MaxCommModeEnum(Enum):
    """AUTOSAR MaxCommModeEnum enumeration."""

    FULL = "full"
    NONE = "none"
    SILENT = "silent"
