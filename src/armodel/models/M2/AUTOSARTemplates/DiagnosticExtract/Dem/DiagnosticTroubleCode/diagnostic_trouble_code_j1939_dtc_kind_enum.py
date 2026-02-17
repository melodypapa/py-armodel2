"""AUTOSAR DiagnosticTroubleCodeJ1939DtcKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 221)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from enum import Enum


class DiagnosticTroubleCodeJ1939DtcKindEnum(Enum):
    """AUTOSAR DiagnosticTroubleCodeJ1939DtcKindEnum enumeration."""

    SERVICEONLY = "serviceOnly"
    STANDARD = "standard"
