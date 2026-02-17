"""AUTOSAR OsTaskPreemptabilityEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 209)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_RteEventToOsTaskMapping.enums.json"""

from enum import Enum


class OsTaskPreemptabilityEnum(Enum):
    """AUTOSAR OsTaskPreemptabilityEnum enumeration."""

    FULL = "full"
    NONE = "none"
