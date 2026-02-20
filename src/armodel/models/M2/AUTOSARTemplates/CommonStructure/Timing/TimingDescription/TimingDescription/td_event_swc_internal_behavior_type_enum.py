"""AUTOSAR TDEventSwcInternalBehaviorTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 62)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class TDEventSwcInternalBehaviorTypeEnum(AREnum):
    """AUTOSAR TDEventSwcInternalBehaviorTypeEnum enumeration.

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

    # Note: 1 duplicate literal(s) found and removed: runnableEntity
    RUNNABLE_ENTITY = "RUNNABLE-ENTITY"
    RUNNABLE_ENTITY_TERMINATED = "RUNNABLE-ENTITY-TERMINATED"
    RUNNABLE_ENTITY_VARIABLE_ACCESS = "RUNNABLE-ENTITY-VARIABLE-ACCESS"
