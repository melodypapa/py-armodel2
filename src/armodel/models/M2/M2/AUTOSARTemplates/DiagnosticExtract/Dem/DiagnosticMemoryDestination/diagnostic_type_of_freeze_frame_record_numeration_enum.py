"""AUTOSAR DiagnosticTypeOfFreezeFrameRecordNumerationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 184)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.enums.json"""

from enum import Enum


class DiagnosticTypeOfFreezeFrameRecordNumerationEnum(Enum):
    """AUTOSAR DiagnosticTypeOfFreezeFrameRecordNumerationEnum enumeration."""

    CALCULATED = "calculated"
    CONFIGURED = "configured"
