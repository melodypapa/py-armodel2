"""AUTOSAR IEEE1722TpAafNominalRateEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 643)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols_IEEE1722Tp_IEEE1722TpAv.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class IEEE1722TpAafNominalRateEnum(AREnum):
    """AUTOSAR IEEE1722TpAafNominalRateEnum enumeration.

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

    _16K_HZ = "_16K-HZ"
    _176_4K_HZ = "_176_4K-HZ"
    _192K_HZ = "_192K-HZ"
    _24K_HZ = "_24K-HZ"
    _32K_HZ = "_32K-HZ"
    _44_1K_HZ = "_44_1K-HZ"
    _48K_HZ = "_48K-HZ"
    SYSTEM = "SYSTEM"
    AUTOSAR_88_2K_HZ = "A-U-T-O-S-A-R_88_2K-HZ"
    _8K_HZ = "_8K-HZ"
    _96K_HZ = "_96K-HZ"
    USER = "USER"
