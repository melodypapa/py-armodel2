"""EventGroupControlTypeEnum enumeration."""

from enum import Enum


class EventGroupControlTypeEnum(Enum):
    """AUTOSAR EventGroupControlTypeEnum enumeration."""

    ACTIVATIONAND = "activationAnd"
    ACTIVATIONMULTICAST = "activationMulticast"
    ACTIVATIONUNICAST = "activationUnicast"
    TRIGGERUNICAST = "triggerUnicast"
