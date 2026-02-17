"""AUTOSAR RamBlockStatusControlEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 233)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 701)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_NvBlockComponent.enums.json"""

from enum import Enum


class RamBlockStatusControlEnum(Enum):
    """AUTOSAR RamBlockStatusControlEnum enumeration."""

    API = "api"
    NVRAMMANAGER = "nvRamManager"
