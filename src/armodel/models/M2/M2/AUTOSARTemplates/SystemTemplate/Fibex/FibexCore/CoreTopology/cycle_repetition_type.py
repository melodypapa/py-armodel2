"""AUTOSAR CycleRepetitionType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 425)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreTopology.enums.json"""

from enum import Enum


class CycleRepetitionType(Enum):
    """AUTOSAR CycleRepetitionType enumeration."""

    CYCLEREPETITION1 = "cycleRepetition1"
    CYCLEREPETITION10 = "cycleRepetition10"
    CYCLEREPETITION16 = "cycleRepetition16"
    CYCLEREPETITION2 = "cycleRepetition2"
    CYCLEREPETITION20 = "cycleRepetition20"
    CYCLEREPETITION32 = "cycleRepetition32"
    CYCLEREPETITION4 = "cycleRepetition4"
    CYCLEREPETITION40 = "cycleRepetition40"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    CYCLEREPETITION5 = "cycleRepetition5"
    CYCLEREPETITION50 = "cycleRepetition50"
    CYCLEREPETITION64 = "cycleRepetition64"
    CYCLEREPETITION8 = "cycleRepetition8"
