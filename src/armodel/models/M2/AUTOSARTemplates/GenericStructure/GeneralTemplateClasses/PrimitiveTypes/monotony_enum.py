"""MonotonyEnum enumeration."""

from enum import Enum


class MonotonyEnum(Enum):
    """AUTOSAR MonotonyEnum enumeration."""

    DECREASINGINCREASING = "decreasingincreasing"
    MONOTONOUS = "monotonous"
    NOMONOTONY = "noMonotony"
    STRICTLYDECREASING = "strictlyDecreasing"
    STRICTLYINCREASING = "strictlyIncreasing"
    STRICTMONOTONOUS = "strictMonotonous"
