"""AUTOSAR DiagnosticRecordTriggerEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 191)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticFreezeFrame.enums.json"""

from enum import Enum


class DiagnosticRecordTriggerEnum(Enum):
    """AUTOSAR DiagnosticRecordTriggerEnum enumeration."""

    CONFIRMED = "confirmed"
    TESTFAILEDTHISOPERATIONCYCLE = "testFailedThisOperationCycle"
    TESTPASSED = "testPassed"
