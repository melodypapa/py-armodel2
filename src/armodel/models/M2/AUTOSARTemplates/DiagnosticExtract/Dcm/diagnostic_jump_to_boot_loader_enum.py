"""AUTOSAR DiagnosticJumpToBootLoaderEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 74)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm.enums.json"""

from enum import Enum


class DiagnosticJumpToBootLoaderEnum(Enum):
    """AUTOSAR DiagnosticJumpToBootLoaderEnum enumeration."""

    SEND = "send"
    SYSTEMSUPPLIERBOOT = "systemSupplierBoot"
