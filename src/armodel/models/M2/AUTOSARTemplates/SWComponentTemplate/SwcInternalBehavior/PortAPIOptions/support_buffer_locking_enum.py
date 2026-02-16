"""SupportBufferLockingEnum enumeration."""

from enum import Enum


class SupportBufferLockingEnum(Enum):
    """AUTOSAR SupportBufferLockingEnum enumeration."""

    DOESNOTSUPPORTBUFFERLOCKING = "doesNotSupportBufferLocking"
    SUPPORTSBUFFERLOCKING = "supportsBufferLocking"
