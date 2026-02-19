"""AUTOSAR HandleTimeoutEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 174)

JSON Source: packages/M2_AUTOSARTemplates_SWComponentTemplate_Communication.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class HandleTimeoutEnum(AREnum):
    """AUTOSAR HandleTimeoutEnum enumeration.

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

    NONE = "NONE"
    REPLACE = "REPLACE"
    REPLACE_BY_TIMEOUT_SUBSTITUTION_VALUE = "REPLACE-BY-TIMEOUT-SUBSTITUTION-VALUE"
