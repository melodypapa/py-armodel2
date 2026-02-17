"""AUTOSAR CanFrameTxBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 445)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanCommunication.enums.json"""

from enum import Enum


class CanFrameTxBehaviorEnum(Enum):
    """AUTOSAR CanFrameTxBehaviorEnum enumeration."""

    CAN20 = "can20"
    CANFD = "canFd"
