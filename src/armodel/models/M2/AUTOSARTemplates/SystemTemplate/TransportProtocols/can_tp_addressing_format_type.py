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

    EXTENDED = "EXTENDED"
    SYSTEM = "SYSTEM"
    AUTOSAR = "A-U-T-O-S-A-R"
    MIXED = "MIXED"
    MIXED29BIT = "MIXED29BIT"
    NORMALFIXED = "NORMALFIXED"
    STANDARD = "STANDARD"
