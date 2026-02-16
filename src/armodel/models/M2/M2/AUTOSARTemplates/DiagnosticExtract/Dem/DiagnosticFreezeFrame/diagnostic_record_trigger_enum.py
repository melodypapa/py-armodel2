"""DiagnosticRecordTriggerEnum enumeration."""

from enum import Enum


class DiagnosticRecordTriggerEnum(Enum):
    """AUTOSAR DiagnosticRecordTriggerEnum enumeration."""

    CONFIRMED = "confirmed"
    TESTFAILEDTHISOPERATIONCYCLE = "testFailedThisOperationCycle"
    TESTPASSED = "testPassed"
