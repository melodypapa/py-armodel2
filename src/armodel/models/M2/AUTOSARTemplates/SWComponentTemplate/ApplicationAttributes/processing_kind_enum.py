"""ProcessingKindEnum enumeration."""

from enum import Enum


class ProcessingKindEnum(Enum):
    """AUTOSAR ProcessingKindEnum enumeration."""

    FILTERED = "filtered"
    NONE = "none"
    RAW = "raw"
