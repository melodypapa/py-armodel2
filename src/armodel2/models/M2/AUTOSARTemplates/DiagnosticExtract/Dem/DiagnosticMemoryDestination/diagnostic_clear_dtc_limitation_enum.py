"""AUTOSAR DiagnosticClearDtcLimitationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 183)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticMemoryDestination.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticClearDtcLimitationEnum(AREnum):
    """AUTOSAR DiagnosticClearDtcLimitationEnum enumeration.

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

    ALL_SUPPORTED_DTCS = "ALL-SUPPORTED-DTCS"
    CLEAR_ALL_DTCS = "CLEAR-ALL-DTCS"
