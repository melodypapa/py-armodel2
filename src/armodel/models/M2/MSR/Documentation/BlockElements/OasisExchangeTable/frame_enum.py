"""FrameEnum enumeration."""

from enum import Enum


class FrameEnum(Enum):
    """AUTOSAR FrameEnum enumeration."""

    ALL = "all"
    BOTTOM = "bottom"
    NONE = "none"
    SIDES = "sides"
    TOP = "top"
    TOPBOT = "topbot"
