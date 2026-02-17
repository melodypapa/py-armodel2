"""AUTOSAR FrArTpAckType enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 604)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.enums.json"""

from enum import Enum


class FrArTpAckType(Enum):
    """AUTOSAR FrArTpAckType enumeration."""

    ACKWITHOUTRT = "ackWithoutRt"
    ACKWITHRT = "ackWithRt"
    NOACK = "noAck"
