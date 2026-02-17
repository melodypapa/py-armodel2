"""AUTOSAR DiagnosticMonitorUpdateKindEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 798)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class DiagnosticMonitorUpdateKindEnum(Enum):
    """AUTOSAR DiagnosticMonitorUpdateKindEnum enumeration."""

    ALWAYS = "always"
    STEADY = "steady"
