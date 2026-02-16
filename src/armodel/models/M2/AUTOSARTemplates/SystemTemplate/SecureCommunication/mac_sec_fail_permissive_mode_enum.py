"""MacSecFailPermissiveModeEnum enumeration."""

from enum import Enum


class MacSecFailPermissiveModeEnum(Enum):
    """AUTOSAR MacSecFailPermissiveModeEnum enumeration."""

    NEVER = "never"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    TIMEOUT = "timeout"
