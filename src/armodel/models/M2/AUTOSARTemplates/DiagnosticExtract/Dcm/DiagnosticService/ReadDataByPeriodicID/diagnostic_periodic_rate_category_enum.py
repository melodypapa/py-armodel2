"""AUTOSAR DiagnosticPeriodicRateCategoryEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 131)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_ReadDataByPeriodicID.enums.json"""

from enum import Enum


class DiagnosticPeriodicRateCategoryEnum(Enum):
    """AUTOSAR DiagnosticPeriodicRateCategoryEnum enumeration."""

    PERIODICRATEFAST = "periodicRateFast"
    PERIODICRATEMEDIUM = "periodicRateMedium"
    PERIODICRATESLOW = "periodicRateSlow"
