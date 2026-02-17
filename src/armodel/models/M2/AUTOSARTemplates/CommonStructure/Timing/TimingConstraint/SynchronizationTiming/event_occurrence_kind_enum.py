"""AUTOSAR EventOccurrenceKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 93)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationTiming.enums.json"""

from enum import Enum


class EventOccurrenceKindEnum(Enum):
    """AUTOSAR EventOccurrenceKindEnum enumeration."""

    MULTIPLEOCCURRENCES = "multipleOccurrences"
    SINGLEOCCURRENCEINDICATES = "singleOccurrenceIndicates"
