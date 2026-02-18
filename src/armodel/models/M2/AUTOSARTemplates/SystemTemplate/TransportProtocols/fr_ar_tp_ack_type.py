"""AUTOSAR FrArTpAckType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 604)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.enums.json"""

from __future__ import annotations

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes.ar_enum import AREnum

class FrArTpAckType(AREnum):
    """AUTOSAR FrArTpAckType enumeration.

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

    ACK_WITHOUT_RT = "ackWithoutRt"
    ACK_WITH_RT = "ackWithRt"
    NO_ACK = "noAck"
