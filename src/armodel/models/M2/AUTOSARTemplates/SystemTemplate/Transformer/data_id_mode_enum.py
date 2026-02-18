"""AUTOSAR DataIdModeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 807)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DataIdModeEnum(AREnum):
    """AUTOSAR DataIdModeEnum enumeration.

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

    ALL16_BIT = "all16Bit"
    ALTERNATING8_BITCOUNTER = "alternating8Bitcounter"
    LOWER12_BIT = "lower12Bit"
    LOWER8_BITARE = "lower8Bitare"
