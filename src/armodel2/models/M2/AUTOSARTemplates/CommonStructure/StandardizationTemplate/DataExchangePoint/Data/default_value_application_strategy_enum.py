"""AUTOSAR DefaultValueApplicationStrategyEnum enumeration.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 112)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint_Data.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class DefaultValueApplicationStrategyEnum(AREnum):
    """AUTOSAR DefaultValueApplicationStrategyEnum enumeration.

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

    FURTHER = "FURTHER"
    DEFAULT_IF_UNDEFINED = "DEFAULT-IF-UNDEFINED"
