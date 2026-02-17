"""AUTOSAR ByteOrderEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 66)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 297)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 779)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_PrimitiveTypes.enums.json"""

from enum import Enum


class ByteOrderEnum(Enum):
    """AUTOSAR ByteOrderEnum enumeration."""

    MOSTSIGNIFICANTBYTEFIRST = "mostSignificantByteFirst"
    MOSTSIGNIFICANTBYTELAST = "mostSignificantByteLast"
    OPAQUE = "opaque"
