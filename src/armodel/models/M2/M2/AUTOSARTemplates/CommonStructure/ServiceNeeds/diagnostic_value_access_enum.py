"""DiagnosticValueAccessEnum enumeration."""

from enum import Enum


class DiagnosticValueAccessEnum(Enum):
    """AUTOSAR DiagnosticValueAccessEnum enumeration."""

    INFORMATION = "information"
    READWRITE = "readWrite"
    WRITEONLY = "writeOnly"
