"""AUTOSAR StandardNameEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 169)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 314)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 26)

JSON Source: packages/M2_AUTOSARTemplates_GenericStructure_DocumentationOnM1.enums.json"""

from enum import Enum


class StandardNameEnum(Enum):
    """AUTOSAR StandardNameEnum enumeration."""

    AP = "AP"
    CP = "CP"
    FO = "FO"
    TA = "TA"
    TC = "TC"
