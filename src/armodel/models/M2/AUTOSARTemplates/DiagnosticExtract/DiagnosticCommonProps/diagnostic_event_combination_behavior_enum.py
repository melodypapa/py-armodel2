"""AUTOSAR DiagnosticEventCombinationBehaviorEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 67)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticCommonProps.enums.json"""

from enum import Enum


class DiagnosticEventCombinationBehaviorEnum(Enum):
    """AUTOSAR DiagnosticEventCombinationBehaviorEnum enumeration."""

    EVENTCOMBINATIONONRETRIEVAL = "eventCombinationOnRetrieval"
    EVENTCOMBINATIONONSTORAGE = "eventCombinationOnStorage"
