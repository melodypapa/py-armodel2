"""TriggerMode enumeration."""

from enum import Enum


class TriggerMode(Enum):
    """AUTOSAR TriggerMode enumeration."""

    DYNAMICPARTTRIGGER = "dynamicPartTrigger"
    NONE = "none"
    STATICORDYNAMICPARTTRIGGER = "staticOrDynamicPartTrigger"
    STATICPARTTRIGGER = "staticPartTrigger"
