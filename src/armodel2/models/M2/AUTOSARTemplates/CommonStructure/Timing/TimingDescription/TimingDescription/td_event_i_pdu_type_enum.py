"""AUTOSAR TDEventIPduTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 67)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from __future__ import annotations

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class TDEventIPduTypeEnum(AREnum):
    """AUTOSAR TDEventIPduTypeEnum enumeration.

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

    I_PDU_RECEIVED_BY = "I-PDU-RECEIVED-BY"
    COM = "C-O-M"
    I_PDU_SENT_TO_IFSPECIFIC = "I-PDU-SENT-TO-IFSPECIFIC"
