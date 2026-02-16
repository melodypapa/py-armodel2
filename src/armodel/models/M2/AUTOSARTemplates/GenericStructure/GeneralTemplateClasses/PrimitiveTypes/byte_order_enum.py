"""ByteOrderEnum enumeration."""

from enum import Enum


class ByteOrderEnum(Enum):
    """AUTOSAR ByteOrderEnum enumeration."""

    MOSTSIGNIFICANTBYTEFIRST = "mostSignificantByteFirst"
    MOSTSIGNIFICANTBYTELAST = "mostSignificantByteLast"
    OPAQUE = "opaque"
