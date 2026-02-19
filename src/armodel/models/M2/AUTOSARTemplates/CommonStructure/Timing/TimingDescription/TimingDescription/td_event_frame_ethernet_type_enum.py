"""AUTOSAR TDEventFrameEthernetTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 70)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class TDEventFrameEthernetTypeEnum(AREnum):
    """AUTOSAR TDEventFrameEthernetTypeEnum enumeration.

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

    # Note: 1 duplicate literal(s) found and removed: frameEthernet
    FRAME_ETHERNET_TRANSMISSION = "FRAME-ETHERNET-TRANSMISSION"
    FRAME_ETHERNET = "FRAME-ETHERNET"
    FRAME_ETHERNET_SENT_ON_BUS = "FRAME-ETHERNET-SENT-ON-BUS"
