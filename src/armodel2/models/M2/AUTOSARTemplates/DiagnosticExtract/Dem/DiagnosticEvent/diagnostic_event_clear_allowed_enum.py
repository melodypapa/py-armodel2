"""AUTOSAR DiagnosticEventClearAllowedEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 167)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticEvent.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticEventClearAllowedEnum(AREnum):
    """AUTOSAR DiagnosticEventClearAllowedEnum enumeration.

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

    ALWAYS = "ALWAYS"
    REQUIRES_CALLBACK = "REQUIRES-CALLBACK"
    EXECUTION = "EXECUTION"
