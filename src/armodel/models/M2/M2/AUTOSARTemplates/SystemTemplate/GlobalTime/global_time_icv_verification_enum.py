"""GlobalTimeIcvVerificationEnum enumeration."""

from enum import Enum


class GlobalTimeIcvVerificationEnum(Enum):
    """AUTOSAR GlobalTimeIcvVerificationEnum enumeration."""

    ICVIGNORED = "icvIgnored"
    ICVNOTVERIFIED = "icvNotVerified"
    ICVOPTIONAL = "icvOptional"
    ICVVERIFIED = "icvVerified"
