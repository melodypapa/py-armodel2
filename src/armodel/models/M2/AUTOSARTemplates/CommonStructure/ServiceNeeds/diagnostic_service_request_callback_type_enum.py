"""AUTOSAR DiagnosticServiceRequestCallbackTypeEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 779)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class DiagnosticServiceRequestCallbackTypeEnum(Enum):
    """AUTOSAR DiagnosticServiceRequestCallbackTypeEnum enumeration."""

    # Note: 1 duplicate literal(s) found and removed: requestCallback
    REQUESTCALLBACK = "requestCallback"
