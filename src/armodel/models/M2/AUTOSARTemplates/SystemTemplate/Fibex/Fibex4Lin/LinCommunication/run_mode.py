"""RunMode enumeration."""

from enum import Enum


class RunMode(Enum):
    """AUTOSAR RunMode enumeration."""

    RUNCONTINUOUS = "RunContinuous"
    RUNONCE = "runOnce"
