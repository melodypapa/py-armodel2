"""AUTOSAR DiagnosticOccurrenceCounterProcessingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 65)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticCommonProps.enums.json"""

from enum import Enum


class DiagnosticOccurrenceCounterProcessingEnum(Enum):
    """AUTOSAR DiagnosticOccurrenceCounterProcessingEnum enumeration."""

    CONFIRMEDDTCBIT = "confirmedDtcBit"
    TESTFAILEDBIT = "testFailedBit"
