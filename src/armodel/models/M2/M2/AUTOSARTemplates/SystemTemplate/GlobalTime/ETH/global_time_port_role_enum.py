"""GlobalTimePortRoleEnum enumeration."""

from enum import Enum


class GlobalTimePortRoleEnum(Enum):
    """AUTOSAR GlobalTimePortRoleEnum enumeration."""

    DYNAMIC = "dynamic"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    TIMESLAVE = "timeSlave"
