"""AUTOSAR TransferPropertyEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 327)

JSON Source: packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.enums.json"""

from enum import Enum


class TransferPropertyEnum(Enum):
    """AUTOSAR TransferPropertyEnum enumeration."""

    PENDING = "pending"
    TRIGGERED = "triggered"
    TRIGGEREDONCHANGE = "triggeredOnChange"
    TRIGGEREDONCHANGE = "triggeredOnChange"
    TRIGGEREDWITHOUT = "triggeredWithout"
    REPETITION = "Repetition"
