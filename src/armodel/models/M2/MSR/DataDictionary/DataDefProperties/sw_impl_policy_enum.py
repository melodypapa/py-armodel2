"""SwImplPolicyEnum enumeration."""

from enum import Enum


class SwImplPolicyEnum(Enum):
    """AUTOSAR SwImplPolicyEnum enumeration."""

    CONST = "const"
    BASIC = "Basic"
    AUTOSAR = "AUTOSAR"
    FIXED = "fixed"
    MEASUREMENTPOINT = "measurementPoint"
    QUEUED = "queued"
    STANDARD = "standard"
