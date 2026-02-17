"""AUTOSAR DiagnosticConnectedIndicatorBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 168)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.enums.json"""

from enum import Enum


class DiagnosticConnectedIndicatorBehaviorEnum(Enum):
    """AUTOSAR DiagnosticConnectedIndicatorBehaviorEnum enumeration."""

    BLINKMODE = "blinkMode"
    BLINKORCONTINUOUSONMODE = "blinkOrContinuousOnMode"
    CONTINUOUSONMODE = "continuousOnMode"
    FASTFLASHINGMODE = "fastFlashingMode"
    SLOWFLASHINGMODE = "slowFlashingMode"
