"""AUTOSAR TriggerMode enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 408)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class TriggerMode(Enum):
    """AUTOSAR TriggerMode enumeration."""

    DYNAMICPARTTRIGGER = "dynamicPartTrigger"
    NONE = "none"
    STATICORDYNAMICPARTTRIGGER = "staticOrDynamicPartTrigger"
    STATICPARTTRIGGER = "staticPartTrigger"
