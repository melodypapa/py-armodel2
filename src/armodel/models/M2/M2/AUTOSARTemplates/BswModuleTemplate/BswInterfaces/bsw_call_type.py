"""BswCallType enumeration."""

from enum import Enum


class BswCallType(Enum):
    """AUTOSAR BswCallType enumeration."""

    CALLBACK = "callback"
    CALLOUTINTERRUPT = "calloutinterrupt"
    REGULAR = "regular"
    SCHEDULED = "scheduled"
