"""CanFrameRxBehaviorEnum enumeration."""

from enum import Enum


class CanFrameRxBehaviorEnum(Enum):
    """AUTOSAR CanFrameRxBehaviorEnum enumeration."""

    ANY = "any"
    CAN20 = "can20"
    CANFD = "canFd"
