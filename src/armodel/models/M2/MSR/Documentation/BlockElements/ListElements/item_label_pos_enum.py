"""AUTOSAR ItemLabelPosEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 297)

JSON Source: packages/M2_MSR_Documentation_BlockElements_ListElements.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ItemLabelPosEnum(AREnum):
    """AUTOSAR ItemLabelPosEnum enumeration.

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

    NEWLINE = "newline"
    NEWLINE_IF_NECESSARY = "newlineIfNecessary"
    NO_NEWLINE = "noNewline"
