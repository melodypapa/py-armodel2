"""AUTOSAR DiagnosticClearDtcNotificationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 776)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class DiagnosticClearDtcNotificationEnum(Enum):
    """AUTOSAR DiagnosticClearDtcNotificationEnum enumeration."""

    FINISH = "finish"
    START = "start"
