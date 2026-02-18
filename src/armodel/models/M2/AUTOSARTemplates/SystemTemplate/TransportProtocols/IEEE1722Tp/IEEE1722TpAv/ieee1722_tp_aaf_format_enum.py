"""AUTOSAR IEEE1722TpAafFormatEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 644)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class IEEE1722TpAafFormatEnum(AREnum):
    """AUTOSAR IEEE1722TpAafFormatEnum enumeration.

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

    AES3_32BIT = "aes3_32bit"
    FLOAT_32BITINT_16BITINT_24BITINT_32BIT = "float_32bitint_16bitint_24bitint_32bit"
    USER = "user"
