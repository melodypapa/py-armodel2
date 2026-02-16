"""TransmissionModeDefinitionEnum enumeration."""

from enum import Enum


class TransmissionModeDefinitionEnum(Enum):
    """AUTOSAR TransmissionModeDefinitionEnum enumeration."""

    CYCLIC = "cyclic"
    CYCLICANDON = "cyclicAndOn"
    TRIGGERED = "triggered"
