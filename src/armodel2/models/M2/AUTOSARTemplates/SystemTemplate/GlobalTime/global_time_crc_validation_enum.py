"""AUTOSAR GlobalTimeCrcValidationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 880)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_GlobalTime.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class GlobalTimeCrcValidationEnum(AREnum):
    """AUTOSAR GlobalTimeCrcValidationEnum enumeration.

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

    CRC_IGNORED = "CRC-IGNORED"
    CRC_NOT_VALIDATED = "CRC-NOT-VALIDATED"
    CRC_OPTIONAL = "CRC-OPTIONAL"
    CRC_VALIDATED = "CRC-VALIDATED"
