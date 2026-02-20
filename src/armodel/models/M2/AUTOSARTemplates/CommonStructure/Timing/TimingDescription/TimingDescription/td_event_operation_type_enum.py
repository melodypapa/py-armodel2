"""AUTOSAR TDEventOperationTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 56)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class TDEventOperationTypeEnum(AREnum):
    """AUTOSAR TDEventOperationTypeEnum enumeration.

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

    OPERATION_CALLED = "OPERATION-CALLED"
    OPERATION_CALL_RECEIVED = "OPERATION-CALL-RECEIVED"
    OPERATION_CALL_RESPONSE_RECEIVED = "OPERATION-CALL-RESPONSE-RECEIVED"
    OPERATION_CALL = "OPERATION-CALL"
