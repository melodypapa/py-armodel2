"""AUTOSAR CycleRepetitionType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 425)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class CycleRepetitionType(AREnum):
    """AUTOSAR CycleRepetitionType enumeration.

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

    CYCLE_REPETITION1 = "CYCLE-REPETITION1"
    CYCLE_REPETITION10 = "CYCLE-REPETITION10"
    CYCLE_REPETITION16 = "CYCLE-REPETITION16"
    CYCLE_REPETITION2 = "CYCLE-REPETITION2"
    CYCLE_REPETITION20 = "CYCLE-REPETITION20"
    CYCLE_REPETITION32 = "CYCLE-REPETITION32"
    CYCLE_REPETITION4 = "CYCLE-REPETITION4"
    CYCLE_REPETITION40 = "CYCLE-REPETITION40"
    SYSTEM = "SYSTEM"
    AUTOSAR = "A-U-T-O-S-A-R"
    CYCLE_REPETITION5 = "CYCLE-REPETITION5"
    CYCLE_REPETITION50 = "CYCLE-REPETITION50"
    CYCLE_REPETITION64 = "CYCLE-REPETITION64"
    CYCLE_REPETITION8 = "CYCLE-REPETITION8"
