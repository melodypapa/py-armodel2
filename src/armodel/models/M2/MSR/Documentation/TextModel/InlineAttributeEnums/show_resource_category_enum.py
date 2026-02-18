"""AUTOSAR ShowResourceCategoryEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 323)

JSON Source: packages/M2_MSR_Documentation_TextModel_InlineAttributeEnums.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ShowResourceCategoryEnum(AREnum):
    """AUTOSAR ShowResourceCategoryEnum enumeration.

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

    NO_SHOW_CATEGORY = "noShowCategory"
    SHOW_CATEGORY = "showCategory"
