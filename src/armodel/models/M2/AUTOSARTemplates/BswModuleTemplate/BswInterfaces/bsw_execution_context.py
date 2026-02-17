"""AUTOSAR BswExecutionContext enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 34)

JSON Source: packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.enums.json"""

from enum import Enum


class BswExecutionContext(Enum):
    """AUTOSAR BswExecutionContext enumeration."""

    HOOKINTERRUPTCAT1INTERRUPTCAT2 = "hookinterruptCat1interruptCat2"
    TASK = "task"
    UNSPECIFIED = "unspecified"
