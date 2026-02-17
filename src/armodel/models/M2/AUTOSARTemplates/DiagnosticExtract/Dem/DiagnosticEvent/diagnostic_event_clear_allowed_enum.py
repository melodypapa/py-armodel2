"""AUTOSAR DiagnosticEventClearAllowedEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 167)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.enums.json"""

from enum import Enum


class DiagnosticEventClearAllowedEnum(Enum):
    """AUTOSAR DiagnosticEventClearAllowedEnum enumeration."""

    ALWAYS = "always"
    REQUIRESCALLBACK = "requiresCallback"
    EXECUTION = "Execution"
