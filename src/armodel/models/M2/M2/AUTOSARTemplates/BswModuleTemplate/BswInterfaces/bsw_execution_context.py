"""BswExecutionContext enumeration."""

from enum import Enum


class BswExecutionContext(Enum):
    """AUTOSAR BswExecutionContext enumeration."""

    HOOKINTERRUPTCAT1INTERRUPTCAT2 = "hookinterruptCat1interruptCat2"
    TASK = "task"
    UNSPECIFIED = "unspecified"
