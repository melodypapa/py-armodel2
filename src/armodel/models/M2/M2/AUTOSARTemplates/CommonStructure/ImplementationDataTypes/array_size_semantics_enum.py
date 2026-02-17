"""AUTOSAR ArraySizeSemanticsEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 42)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 253)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ImplementationDataTypes.enums.json"""

from enum import Enum


class ArraySizeSemanticsEnum(Enum):
    """AUTOSAR ArraySizeSemanticsEnum enumeration."""

    FIXEDSIZE = "fixedSize"
    VARIABLESIZE = "variableSize"
