"""AUTOSAR DiagnosticHandleDDDIConfigurationEnum enumeration.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 128)

JSON Source: packages/M2_AUTOSARTemplates_DiagnosticExtract_Dcm_DiagnosticService_DynamicallyDefineData.enums.json"""

from enum import Enum


class DiagnosticHandleDDDIConfigurationEnum(Enum):
    """AUTOSAR DiagnosticHandleDDDIConfigurationEnum enumeration."""

    NONVOLATILE = "nonVolatile"
    VOLATILE = "volatile"
