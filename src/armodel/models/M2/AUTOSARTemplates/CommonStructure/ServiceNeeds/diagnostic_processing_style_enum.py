"""AUTOSAR DiagnosticProcessingStyleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 246)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 115)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 783)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticProcessingStyleEnum(AREnum):
    """AUTOSAR DiagnosticProcessingStyleEnum enumeration.

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

    PROCESSING_STYLE = "processingStyle"
    PROCESSING_STYLE_ERROR = "processingStyleError"
    PROCESSING_STYLE_SYNCHRONOUS = "processingStyleSynchronous"
