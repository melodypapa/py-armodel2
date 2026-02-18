"""AUTOSAR CycleRepetitionType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 425)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

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

    CYCLE_REPETITION1 = "cycleRepetition1"
    CYCLE_REPETITION10 = "cycleRepetition10"
    CYCLE_REPETITION16 = "cycleRepetition16"
    CYCLE_REPETITION2 = "cycleRepetition2"
    CYCLE_REPETITION20 = "cycleRepetition20"
    CYCLE_REPETITION32 = "cycleRepetition32"
    CYCLE_REPETITION4 = "cycleRepetition4"
    CYCLE_REPETITION40 = "cycleRepetition40"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    CYCLE_REPETITION5 = "cycleRepetition5"
    CYCLE_REPETITION50 = "cycleRepetition50"
    CYCLE_REPETITION64 = "cycleRepetition64"
    CYCLE_REPETITION8 = "cycleRepetition8"
