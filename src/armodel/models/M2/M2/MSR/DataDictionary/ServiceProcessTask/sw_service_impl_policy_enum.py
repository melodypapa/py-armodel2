"""AUTOSAR SwServiceImplPolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 36)

JSON Source: packages/M2_MSR_DataDictionary_ServiceProcessTask.enums.json"""

from enum import Enum


class SwServiceImplPolicyEnum(Enum):
    """AUTOSAR SwServiceImplPolicyEnum enumeration."""

    INLINEINLINECONDITIONALINLINEIN = "inlineinlineConditionalinlineIn"
    STANDARD = "standard"
