"""AUTOSAR CanAddressingModeType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 443)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class CanAddressingModeType(AREnum):
    """AUTOSAR CanAddressingModeType enumeration.

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

    EXTENDED = "EXTENDED"
    STANDARD = "STANDARD"
