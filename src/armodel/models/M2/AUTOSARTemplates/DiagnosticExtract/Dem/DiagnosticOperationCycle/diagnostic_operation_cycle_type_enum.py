"""DiagnosticOperationCycleTypeEnum enumeration."""

from enum import Enum


class DiagnosticOperationCycleTypeEnum(Enum):
    """AUTOSAR DiagnosticOperationCycleTypeEnum enumeration."""

    IGNITION = "ignition"
    OBDDRIVINGCYCLE = "obdDrivingCycle"
    WARMUP = "warmup"
