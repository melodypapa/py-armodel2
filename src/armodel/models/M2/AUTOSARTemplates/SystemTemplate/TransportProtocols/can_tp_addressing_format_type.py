"""CanTpAddressingFormatType enumeration."""

from enum import Enum


class CanTpAddressingFormatType(Enum):
    """AUTOSAR CanTpAddressingFormatType enumeration."""

    EXTENDED = "extended"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    MIXED = "mixed"
    MIXED29BIT = "mixed29bit"
    NORMALFIXED = "normalfixed"
    STANDARD = "standard"
