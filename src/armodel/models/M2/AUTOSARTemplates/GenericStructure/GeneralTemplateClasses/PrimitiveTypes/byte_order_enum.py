"""AUTOSAR ByteOrderEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 66)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 297)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 779)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ByteOrderEnum(AREnum):
    """AUTOSAR ByteOrderEnum enumeration.

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

    MOST_SIGNIFICANT_BYTE_FIRST = "mostSignificantByteFirst"
    MOST_SIGNIFICANT_BYTE_LAST = "mostSignificantByteLast"
    OPAQUE = "opaque"
