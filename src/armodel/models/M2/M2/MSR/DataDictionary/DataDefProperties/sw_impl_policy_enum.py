"""AUTOSAR SwImplPolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 342)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 336)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2065)

JSON Source: packages/M2_MSR_DataDictionary_DataDefProperties.enums.json"""

from enum import Enum


class SwImplPolicyEnum(Enum):
    """AUTOSAR SwImplPolicyEnum enumeration."""

    CONST = "const"
    BASIC = "Basic"
    AUTOSAR = "AUTOSAR"
    FIXED = "fixed"
    MEASUREMENTPOINT = "measurementPoint"
    QUEUED = "queued"
    STANDARD = "standard"
