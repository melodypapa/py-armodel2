"""AUTOSAR MonotonyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 408)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class MonotonyEnum(AREnum):
    """AUTOSAR MonotonyEnum enumeration.

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

    DECREASINGINCREASING = "DECREASINGINCREASING"
    MONOTONOUS = "MONOTONOUS"
    NO_MONOTONY = "NO-MONOTONY"
    STRICTLY_DECREASING = "STRICTLY-DECREASING"
    STRICTLY_INCREASING = "STRICTLY-INCREASING"
    STRICT_MONOTONOUS = "STRICT-MONOTONOUS"
