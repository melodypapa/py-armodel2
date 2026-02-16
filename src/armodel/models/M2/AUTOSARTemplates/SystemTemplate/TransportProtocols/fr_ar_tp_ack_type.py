"""FrArTpAckType enumeration."""

from enum import Enum


class FrArTpAckType(Enum):
    """AUTOSAR FrArTpAckType enumeration."""

    ACKWITHOUTRT = "ackWithoutRt"
    ACKWITHRT = "ackWithRt"
    NOACK = "noAck"
