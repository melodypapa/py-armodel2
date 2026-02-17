"""AUTOSAR TDEventTriggerTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 59)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from enum import Enum


class TDEventTriggerTypeEnum(Enum):
    """AUTOSAR TDEventTriggerTypeEnum enumeration."""

    TRIGGERACTIVATED = "triggerActivated"
    TRIGGERRELEASED = "triggerReleased"
