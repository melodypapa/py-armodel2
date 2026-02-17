"""AUTOSAR DiagnosticSignificanceEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 187)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from enum import Enum


class DiagnosticSignificanceEnum(Enum):
    """AUTOSAR DiagnosticSignificanceEnum enumeration."""

    FAULT = "fault"
    OCCURENCE = "occurence"
