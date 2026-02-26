"""AUTOSAR OperationCycleTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 761)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class OperationCycleTypeEnum(AREnum):
    """AUTOSAR OperationCycleTypeEnum enumeration.

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

    IGNITION = "IGNITION"
    OBD_DCY = "OBD-DCY"
    OTHER = "OTHER"
    POWER = "POWER"
    TIME = "TIME"
    WARMUP = "WARMUP"
