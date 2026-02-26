"""AUTOSAR IEEE1722TpRvfPixelFormatEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 650)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class IEEE1722TpRvfPixelFormatEnum(AREnum):
    """AUTOSAR IEEE1722TpRvfPixelFormatEnum enumeration.

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

    _4_1_1 = "_4_1_1"
