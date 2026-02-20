"""AUTOSAR SendIndicationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 903)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SendIndicationEnum(AREnum):
    """AUTOSAR SendIndicationEnum enumeration.

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

    ANY_SEND_OPERATION = "ANY-SEND-OPERATION"
    NONE = "NONE"
