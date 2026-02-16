"""SecurityEventReportingModeEnum enumeration."""

from enum import Enum


class SecurityEventReportingModeEnum(Enum):
    """AUTOSAR SecurityEventReportingModeEnum enumeration."""

    BRIEF = "brief"
    BRIEFBYPASSING = "briefBypassing"
    DETAILED = "detailed"
    SECURITY = "Security"
    AUTOSAR = "AUTOSAR"
    DETAILEDBYPASSING = "detailedBypassing"
    OFF = "off"
