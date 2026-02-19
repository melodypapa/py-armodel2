"""AUTOSAR SeverityEnum enumeration.

References:
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 87)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_StandardizationTemplate_DataExchangePoint.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SeverityEnum(AREnum):
    """AUTOSAR SeverityEnum enumeration.

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

    ERRORINFO = "ERRORINFO"
    WARNING = "WARNING"
