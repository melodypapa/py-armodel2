"""DataIdModeEnum enumeration."""

from enum import Enum


class DataIdModeEnum(Enum):
    """AUTOSAR DataIdModeEnum enumeration."""

    ALL16BIT = "all16Bit"
    ALTERNATING8BITCOUNTER = "alternating8Bitcounter"
    LOWER12BIT = "lower12Bit"
    LOWER8BITARE = "lower8Bitare"
