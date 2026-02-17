"""AUTOSAR DiagnosticAudienceEnum enumeration.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 754)

JSON Source: packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.enums.json"""

from enum import Enum


class DiagnosticAudienceEnum(Enum):
    """AUTOSAR DiagnosticAudienceEnum enumeration."""

    AFTERMARKET = "aftermarket"
    AFTERSALES = "afterSales"
    DEVELOPMENT = "development"
    MANUFACTURING = "manufacturing"
    SUPPLIER = "supplier"
