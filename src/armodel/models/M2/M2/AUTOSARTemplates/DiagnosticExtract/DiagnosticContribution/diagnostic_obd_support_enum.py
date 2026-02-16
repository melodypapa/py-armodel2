"""DiagnosticObdSupportEnum enumeration."""

from enum import Enum


class DiagnosticObdSupportEnum(Enum):
    """AUTOSAR DiagnosticObdSupportEnum enumeration."""

    MASTERECU = "masterEcu"
    NOOBDSUPPORT = "noObdSupport"
    PRIMARYECU = "primaryEcu"
    SECONDARYECU = "secondaryEcu"
