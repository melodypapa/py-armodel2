"""AUTOSAR AutoCollectEnum enumeration.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 399)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_ElementCollection.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class AutoCollectEnum(AREnum):
    """AUTOSAR AutoCollectEnum enumeration.

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

    REF_ALL = "REF-ALL"
    REF_NONE = "REF-NONE"
    REF_NON_STANDARD = "REF-NON-STANDARD"
