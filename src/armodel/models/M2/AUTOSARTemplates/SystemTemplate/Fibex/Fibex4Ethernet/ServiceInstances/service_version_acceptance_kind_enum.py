"""ServiceVersionAcceptanceKindEnum enumeration."""

from enum import Enum


class ServiceVersionAcceptanceKindEnum(Enum):
    """AUTOSAR ServiceVersionAcceptanceKindEnum enumeration."""

    EXACTORANYMINOR = "exactOrAnyMinor"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    MINIMUMMINOR = "minimumMinor"
