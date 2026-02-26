"""AUTOSAR DataLimitKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 153)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_ApplicationAttributes.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DataLimitKindEnum(AREnum):
    """AUTOSAR DataLimitKindEnum enumeration.

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

    MAX = "MAX"
    SOFTWARE = "SOFTWARE"
    AUTOSAR = "A-U-T-O-S-A-R"
    MIN = "MIN"
    NONE = "NONE"
