"""AUTOSAR DiagnosticEventCombinationBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 67)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticCommonProps.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DiagnosticEventCombinationBehaviorEnum(AREnum):
    """AUTOSAR DiagnosticEventCombinationBehaviorEnum enumeration.

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

    EVENT_COMBINATION_ON_RETRIEVAL = "EVENT-COMBINATION-ON-RETRIEVAL"
    EVENT_COMBINATION_ON_STORAGE = "EVENT-COMBINATION-ON-STORAGE"
