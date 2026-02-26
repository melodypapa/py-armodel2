"""AUTOSAR EthernetPhysicalLayerTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 111)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class EthernetPhysicalLayerTypeEnum(AREnum):
    """AUTOSAR EthernetPhysicalLayerTypeEnum enumeration.

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

    _1000_BASE_T = "_1000-B-A-S-E_-T"
    _1000_BASE_T1 = "_1000-B-A-S-E_-T1"
    _100_BASE_T1 = "_100-B-A-S-E_-T1"
    _100_BASE_TX = "_100-B-A-S-E_-T-X"
    _10_BASE_T1_S = "_10-B-A-S-E_-T1-S"
    I_EEE802_11_P = "I-E-E-E802_11-P"
