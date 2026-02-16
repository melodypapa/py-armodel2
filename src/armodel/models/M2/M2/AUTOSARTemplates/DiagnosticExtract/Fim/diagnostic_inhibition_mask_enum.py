"""DiagnosticInhibitionMaskEnum enumeration."""

from enum import Enum


class DiagnosticInhibitionMaskEnum(Enum):
    """AUTOSAR DiagnosticInhibitionMaskEnum enumeration."""

    LASTFAILED = "lastFailed"
    NOTTESTED = "notTested"
    TESTED = "tested"
    TESTEDANDFAILED = "testedAndFailed"
