"""AUTOSAR SynchronizationTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 93)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationTiming.enums.json"""

from enum import Enum


class SynchronizationTypeEnum(Enum):
    """AUTOSAR SynchronizationTypeEnum enumeration."""

    RESPONSEIN = "responseIn"
    STIMULUSIN = "stimulusIn"
