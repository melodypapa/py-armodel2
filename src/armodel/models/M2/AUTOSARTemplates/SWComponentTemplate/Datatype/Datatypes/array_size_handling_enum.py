"""AUTOSAR ArraySizeHandlingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 253)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ArraySizeHandlingEnum(AREnum):
    """AUTOSAR ArraySizeHandlingEnum enumeration.

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

    ALL_INDICES_DIFFERENT_ARRAY_SIZE = "ALL-INDICES-DIFFERENT-ARRAY-SIZE"
    ALL_INDICES_SAME_ARRAY_SIZE = "ALL-INDICES-SAME-ARRAY-SIZE"
    SOFTWARE = "SOFTWARE"
    AUTOSA_RINHERITED_FROM_ARRAY = "A-U-T-O-S-A-RINHERITED-FROM-ARRAY"
