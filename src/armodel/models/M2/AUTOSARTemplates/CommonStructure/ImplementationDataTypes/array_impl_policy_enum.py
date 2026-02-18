"""AUTOSAR ArrayImplPolicyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 276)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class ArrayImplPolicyEnum(AREnum):
    """AUTOSAR ArrayImplPolicyEnum enumeration.

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

    PAYLOAD_AS_ARRAY = "payloadAsArray"
    PAYLOAD_AS_POINTER_TO_ARRAY = "payloadAsPointerToArray"
