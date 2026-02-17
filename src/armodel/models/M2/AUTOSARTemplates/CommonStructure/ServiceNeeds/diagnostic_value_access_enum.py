"""AUTOSAR DiagnosticValueAccessEnum enumeration.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 246)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 114)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 782)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class DiagnosticValueAccessEnum(Enum):
    """AUTOSAR DiagnosticValueAccessEnum enumeration."""

    INFORMATION = "information"
    READWRITE = "readWrite"
    WRITEONLY = "writeOnly"
