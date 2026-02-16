"""DiagnosticProcessingStyleEnum enumeration."""

from enum import Enum


class DiagnosticProcessingStyleEnum(Enum):
    """AUTOSAR DiagnosticProcessingStyleEnum enumeration."""

    PROCESSINGSTYLE = "processingStyle"
    PROCESSINGSTYLEERROR = "processingStyleError"
    PROCESSINGSTYLESYNCHRONOUS = "processingStyleSynchronous"
