"""AUTOSAR DiagnosticObdSupportEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 207)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticContribution.enums.json"""

from enum import Enum


class DiagnosticObdSupportEnum(Enum):
    """AUTOSAR DiagnosticObdSupportEnum enumeration."""

    MASTERECU = "masterEcu"
    NOOBDSUPPORT = "noObdSupport"
    PRIMARYECU = "primaryEcu"
    SECONDARYECU = "secondaryEcu"
