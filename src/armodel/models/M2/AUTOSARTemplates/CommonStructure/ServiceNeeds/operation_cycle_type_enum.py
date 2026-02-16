"""OperationCycleTypeEnum enumeration."""

from enum import Enum


class OperationCycleTypeEnum(Enum):
    """AUTOSAR OperationCycleTypeEnum enumeration."""

    IGNITION = "ignition"
    OBDDCY = "obdDcy"
    OTHER = "other"
    POWER = "power"
    TIME = "time"
    WARMUP = "warmup"
