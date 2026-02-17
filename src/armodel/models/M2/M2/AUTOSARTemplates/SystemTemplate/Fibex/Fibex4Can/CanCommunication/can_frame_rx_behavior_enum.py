"""AUTOSAR CanFrameRxBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 444)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.enums.json"""

from enum import Enum


class CanFrameRxBehaviorEnum(Enum):
    """AUTOSAR CanFrameRxBehaviorEnum enumeration."""

    ANY = "any"
    CAN20 = "can20"
    CANFD = "canFd"
