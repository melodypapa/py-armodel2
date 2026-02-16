"""DiagnosticUdsSeverityEnum enumeration."""

from enum import Enum


class DiagnosticUdsSeverityEnum(Enum):
    """AUTOSAR DiagnosticUdsSeverityEnum enumeration."""

    CHECKATNEXTHALT = "checkAtNextHalt"
    IMMEDIATELY = "immediately"
    MAINTENANCEONLY = "maintenanceOnly"
    NOSEVERITY = "noSeverity"
