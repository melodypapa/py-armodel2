"""NvBlockNeedsReliabilityEnum enumeration."""

from enum import Enum


class NvBlockNeedsReliabilityEnum(Enum):
    """AUTOSAR NvBlockNeedsReliabilityEnum enumeration."""

    ERRORCORRECTION = "errorCorrection"
    ERRORDETECTION = "errorDetection"
    NOPROTECTION = "noProtection"
