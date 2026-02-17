"""AUTOSAR DiagnosticUdsSeverityEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 187)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticTroubleCode.enums.json"""

from enum import Enum


class DiagnosticUdsSeverityEnum(Enum):
    """AUTOSAR DiagnosticUdsSeverityEnum enumeration."""

    CHECKATNEXTHALT = "checkAtNextHalt"
    IMMEDIATELY = "immediately"
    MAINTENANCEONLY = "maintenanceOnly"
    NOSEVERITY = "noSeverity"
