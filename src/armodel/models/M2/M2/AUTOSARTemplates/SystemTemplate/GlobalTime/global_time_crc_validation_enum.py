"""GlobalTimeCrcValidationEnum enumeration."""

from enum import Enum


class GlobalTimeCrcValidationEnum(Enum):
    """AUTOSAR GlobalTimeCrcValidationEnum enumeration."""

    CRCIGNORED = "crcIgnored"
    CRCNOTVALIDATED = "crcNotValidated"
    CRCOPTIONAL = "crcOptional"
    CRCVALIDATED = "crcValidated"
