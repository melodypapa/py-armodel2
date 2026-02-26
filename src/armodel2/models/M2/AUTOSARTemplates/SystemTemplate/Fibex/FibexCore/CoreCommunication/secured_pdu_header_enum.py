"""AUTOSAR SecuredPduHeaderEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 368)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class SecuredPduHeaderEnum(AREnum):
    """AUTOSAR SecuredPduHeaderEnum enumeration.

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

    NO_HEADER = "NO-HEADER"
    SYSTEM = "SYSTEM"
    AUTOSA_RSECURED_PDU_HEADER08_BIT = "A-U-T-O-S-A-RSECURED-PDU-HEADER08-BIT"
    SECURED_PDU_HEADER16_BIT = "SECURED-PDU-HEADER16-BIT"
    SECURED_PDU_HEADER32_BIT = "SECURED-PDU-HEADER32-BIT"
