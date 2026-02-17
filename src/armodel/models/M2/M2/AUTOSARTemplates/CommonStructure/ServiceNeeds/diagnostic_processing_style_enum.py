"""AUTOSAR DiagnosticProcessingStyleEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 246)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 115)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 783)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class DiagnosticProcessingStyleEnum(Enum):
    """AUTOSAR DiagnosticProcessingStyleEnum enumeration."""

    PROCESSINGSTYLE = "processingStyle"
    PROCESSINGSTYLEERROR = "processingStyleError"
    PROCESSINGSTYLESYNCHRONOUS = "processingStyleSynchronous"
