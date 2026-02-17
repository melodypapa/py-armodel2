"""AUTOSAR SecurityEventReportingModeEnum enumeration.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 35)

JSON Source: packages/M2_AUTOSARTemplates_SecurityExtractTemplate.enums.json"""

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
