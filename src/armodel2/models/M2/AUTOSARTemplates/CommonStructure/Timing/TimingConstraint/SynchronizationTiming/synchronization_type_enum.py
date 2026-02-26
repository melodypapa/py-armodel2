"""AUTOSAR SynchronizationTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 93)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingConstraint_SynchronizationTiming.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SynchronizationTypeEnum(AREnum):
    """AUTOSAR SynchronizationTypeEnum enumeration.

    This enum inherits from AREnum, which provides:
    - serialize(): XML serialization
    - deserialize(): XML deserialization with automatic member matching
    - Transparent equality comparison with string values
    """

    def __init__(self, value: str) -> None:
        """Initialize enum member.

        Args:
            value: The enum value as a string
        """
        self._value_ = value

    RESPONSE_IN = "RESPONSE-IN"
    STIMULUS_IN = "STIMULUS-IN"
