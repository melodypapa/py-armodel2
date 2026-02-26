"""AUTOSAR ArraySizeSemanticsEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 253)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ArraySizeSemanticsEnum(AREnum):
    """AUTOSAR ArraySizeSemanticsEnum enumeration.

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

    FIXED_SIZE = "FIXED-SIZE"
    VARIABLE_SIZE = "VARIABLE-SIZE"
