"""AUTOSAR DiagnosticInhibitionMaskEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 216)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Fim.enums.json"""

from enum import Enum


class DiagnosticInhibitionMaskEnum(Enum):
    """AUTOSAR DiagnosticInhibitionMaskEnum enumeration."""

    LASTFAILED = "lastFailed"
    NOTTESTED = "notTested"
    TESTED = "tested"
    TESTEDANDFAILED = "testedAndFailed"
