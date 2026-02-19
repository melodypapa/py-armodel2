"""AUTOSAR TDEventFrameTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 68)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class TDEventFrameTypeEnum(AREnum):
    """AUTOSAR TDEventFrameTypeEnum enumeration.

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

    FRAME_QUEUED_FOR = "FRAME-QUEUED-FOR"
    FRAME_RECEIVED_BY_IFCORRESPONDING = "FRAME-RECEIVED-BY-IFCORRESPONDING"
    FRAME_TRANSMITTED_ON_BUS = "FRAME-TRANSMITTED-ON-BUS"
