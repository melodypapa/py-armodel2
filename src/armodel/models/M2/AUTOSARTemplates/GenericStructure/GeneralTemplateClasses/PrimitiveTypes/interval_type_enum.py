"""AUTOSAR IntervalTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 300)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 409)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class IntervalTypeEnum(AREnum):
    """AUTOSAR IntervalTypeEnum enumeration.

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

    CLOSED = "closed"
    OPEN = "open"
