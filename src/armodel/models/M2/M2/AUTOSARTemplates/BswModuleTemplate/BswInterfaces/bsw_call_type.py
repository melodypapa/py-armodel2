"""AUTOSAR BswCallType enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 36)

JSON Source: packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.enums.json"""

from enum import Enum


class BswCallType(Enum):
    """AUTOSAR BswCallType enumeration."""

    CALLBACK = "callback"
    CALLOUTINTERRUPT = "calloutinterrupt"
    REGULAR = "regular"
    SCHEDULED = "scheduled"
