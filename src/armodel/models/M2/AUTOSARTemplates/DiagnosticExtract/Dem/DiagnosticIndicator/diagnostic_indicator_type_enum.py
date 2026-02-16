"""DiagnosticIndicatorTypeEnum enumeration."""

from enum import Enum


class DiagnosticIndicatorTypeEnum(Enum):
    """AUTOSAR DiagnosticIndicatorTypeEnum enumeration."""

    AMBERWARNING = "amberWarning"
    MALFUNCTION = "malfunction"
    PROTECTLAMP = "protectLamp"
    REDSTOPLAMP = "redStopLamp"
    WARNING = "warning"
