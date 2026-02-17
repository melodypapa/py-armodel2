"""AUTOSAR BswInterruptCategory enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 76)

JSON Source: packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.enums.json"""

from enum import Enum


class BswInterruptCategory(Enum):
    """AUTOSAR BswInterruptCategory enumeration."""

    CAT1 = "cat1"
    CAT2INTERRUPTENTITY = "cat2InterruptEntity"
