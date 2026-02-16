"""MaximumMessageLengthType enumeration."""

from enum import Enum


class MaximumMessageLengthType(Enum):
    """AUTOSAR MaximumMessageLengthType enumeration."""

    I4GLENGTH = "I4glength"
    ISO = "iso"
    ISO6 = "iso6"
    ROUTE = "route"
