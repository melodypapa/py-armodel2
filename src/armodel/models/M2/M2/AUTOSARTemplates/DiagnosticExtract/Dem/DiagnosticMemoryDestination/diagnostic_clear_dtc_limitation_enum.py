"""AUTOSAR DiagnosticClearDtcLimitationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 183)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.enums.json"""

from enum import Enum


class DiagnosticClearDtcLimitationEnum(Enum):
    """AUTOSAR DiagnosticClearDtcLimitationEnum enumeration."""

    ALLSUPPORTEDDTCS = "allSupportedDtcs"
    CLEARALLDTCS = "clearAllDtcs"
