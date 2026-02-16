"""DiagnosticEventClearAllowedEnum enumeration."""

from enum import Enum


class DiagnosticEventClearAllowedEnum(Enum):
    """AUTOSAR DiagnosticEventClearAllowedEnum enumeration."""

    ALWAYS = "always"
    REQUIRESCALLBACK = "requiresCallback"
    EXECUTION = "Execution"
