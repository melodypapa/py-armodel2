"""AUTOSAR CanTpAddressingFormatType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 609)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class CanTpAddressingFormatType(AREnum):
    """AUTOSAR CanTpAddressingFormatType enumeration.

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

    EXTENDED = "extended"
    SYSTEM = "System"
    AUTOSAR = "AUTOSAR"
    MIXED = "mixed"
    MIXED29BIT = "mixed29bit"
    NORMALFIXED = "normalfixed"
    STANDARD = "standard"
