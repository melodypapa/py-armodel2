"""DiagnosticMemoryEntryStorageTriggerEnum enumeration."""

from enum import Enum


class DiagnosticMemoryEntryStorageTriggerEnum(Enum):
    """AUTOSAR DiagnosticMemoryEntryStorageTriggerEnum enumeration."""

    CONFIRMED = "confirmed"
    FDCTHRESHOLD = "fdcThreshold"
    TESTFAILED = "testFailed"
