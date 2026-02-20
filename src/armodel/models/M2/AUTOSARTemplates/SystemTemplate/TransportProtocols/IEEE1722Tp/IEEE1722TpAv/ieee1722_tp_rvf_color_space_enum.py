"""AUTOSAR IEEE1722TpRvfColorSpaceEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 652)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class IEEE1722TpRvfColorSpaceEnum(AREnum):
    """AUTOSAR IEEE1722TpRvfColorSpaceEnum enumeration.

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

    BT_REC_601 = "BT_REC_601"
    BT_REC_709 = "BT_REC_709"
    GRAYSCALE = "GRAYSCALE"
    ITU_BT_2020 = "ITU_BT_2020"
    USER = "USER"
    XYZ = "XYZ"
    YCBCR = "YCBCR"
    YCGCO = "YCGCO"
    YCM = "YCM"
