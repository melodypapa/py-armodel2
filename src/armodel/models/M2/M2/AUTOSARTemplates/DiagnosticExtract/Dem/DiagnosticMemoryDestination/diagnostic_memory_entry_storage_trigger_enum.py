"""AUTOSAR DiagnosticMemoryEntryStorageTriggerEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 183)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.enums.json"""

from enum import Enum


class DiagnosticMemoryEntryStorageTriggerEnum(Enum):
    """AUTOSAR DiagnosticMemoryEntryStorageTriggerEnum enumeration."""

    CONFIRMED = "confirmed"
    FDCTHRESHOLD = "fdcThreshold"
    TESTFAILED = "testFailed"
