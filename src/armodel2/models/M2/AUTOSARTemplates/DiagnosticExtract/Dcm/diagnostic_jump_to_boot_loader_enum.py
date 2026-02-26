"""AUTOSAR DiagnosticJumpToBootLoaderEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 74)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticJumpToBootLoaderEnum(AREnum):
    """AUTOSAR DiagnosticJumpToBootLoaderEnum enumeration.

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

    SEND = "SEND"
    SYSTEM_SUPPLIER_BOOT = "SYSTEM-SUPPLIER-BOOT"
