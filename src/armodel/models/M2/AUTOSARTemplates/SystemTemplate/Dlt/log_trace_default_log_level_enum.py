"""AUTOSAR LogTraceDefaultLogLevelEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 723)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Dlt.enums.json"""

from enum import Enum


class LogTraceDefaultLogLevelEnum(Enum):
    """AUTOSAR LogTraceDefaultLogLevelEnum enumeration."""

    DEBUG = "debug"
    ERROR = "error"
    FATALINFO = "fatalinfo"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    VERBOSE = "verbose"
    WARN = "warn"
