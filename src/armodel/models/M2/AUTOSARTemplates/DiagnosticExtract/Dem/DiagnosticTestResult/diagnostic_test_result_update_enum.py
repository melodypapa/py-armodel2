"""AUTOSAR DiagnosticTestResultUpdateEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 205)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTestResult.enums.json"""

from enum import Enum


class DiagnosticTestResultUpdateEnum(Enum):
    """AUTOSAR DiagnosticTestResultUpdateEnum enumeration."""

    ALWAYS = "always"
    STEADY = "steady"
