"""ReentrancyLevelEnum enumeration."""

from enum import Enum


class ReentrancyLevelEnum(Enum):
    """AUTOSAR ReentrancyLevelEnum enumeration."""

    MULTICOREREENTRANTON = "multicoreReentranton"
    NONREENTRANT = "nonReentrant"
    SINGLECOREREENTRANT = "singleCoreReentrant"
