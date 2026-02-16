"""CouplingElementEnum enumeration."""

from enum import Enum


class CouplingElementEnum(Enum):
    """AUTOSAR CouplingElementEnum enumeration."""

    HUB = "hub"
    ROUTER = "router"
    SWITCH = "switch"
