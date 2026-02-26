"""AUTOSAR TransformerClassEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 200)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 765)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class TransformerClassEnum(AREnum):
    """AUTOSAR TransformerClassEnum enumeration.

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

    CUSTOM = "CUSTOM"
    SAFETY = "SAFETY"
    SECURITY = "SECURITY"
    SERIALIZER = "SERIALIZER"
