"""DataLimitKindEnum enumeration."""

from enum import Enum


class DataLimitKindEnum(Enum):
    """AUTOSAR DataLimitKindEnum enumeration."""

    MAX = "max"
    SOFTWARE = "Software"
    AUTOSAR = "AUTOSAR"
    MIN = "min"
    NONE = "none"
