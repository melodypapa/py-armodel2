"""AUTOSAR DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 129)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineData.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum(AREnum):
    """AUTOSAR DiagnosticDynamicallyDefineDataIdentifierSubfunctionEnum enumeration.

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

    CLEAR_DYNAMICALLY_DEFINE_DATA_IDENTIFIER = "CLEAR-DYNAMICALLY-DEFINE-DATA-IDENTIFIER"
    DEFINE_BY_IDENTIFIER = "DEFINE-BY-IDENTIFIER"
    DEFINE_BY_MEMORY_ADDRESS = "DEFINE-BY-MEMORY-ADDRESS"
