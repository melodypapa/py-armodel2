"""AUTOSAR DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 183)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from enum import Enum


class DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum(Enum):
    """AUTOSAR DiagnosticStatusBitHandlingTestFailedSinceLastClearEnum enumeration."""

    STATUSBITAGINGANDDISPLACEMENT = "statusBitAgingAndDisplacement"
    STATUSBITNORMAL = "statusBitNormal"
