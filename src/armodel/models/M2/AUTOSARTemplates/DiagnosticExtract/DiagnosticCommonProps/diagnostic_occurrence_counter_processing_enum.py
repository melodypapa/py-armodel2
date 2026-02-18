"""AUTOSAR DiagnosticOccurrenceCounterProcessingEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 65)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticCommonProps.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticOccurrenceCounterProcessingEnum(AREnum):
    """AUTOSAR DiagnosticOccurrenceCounterProcessingEnum enumeration.

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

    CONFIRMED_DTC_BIT = "confirmedDtcBit"
    TEST_FAILED_BIT = "testFailedBit"
