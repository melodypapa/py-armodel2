"""AUTOSAR OperationCycleTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 761)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class OperationCycleTypeEnum(Enum):
    """AUTOSAR OperationCycleTypeEnum enumeration."""

    IGNITION = "ignition"
    OBDDCY = "obdDcy"
    OTHER = "other"
    POWER = "power"
    TIME = "time"
    WARMUP = "warmup"
