"""UdpChecksumCalculationEnum enumeration."""

from enum import Enum


class UdpChecksumCalculationEnum(Enum):
    """AUTOSAR UdpChecksumCalculationEnum enumeration."""

    UDPCHECKSUMDISABLED = "udpChecksumDisabled"
    UDPCHECKSUMENABLED = "udpChecksumEnabled"
