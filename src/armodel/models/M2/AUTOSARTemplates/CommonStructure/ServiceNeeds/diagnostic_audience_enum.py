"""DiagnosticAudienceEnum enumeration."""

from enum import Enum


class DiagnosticAudienceEnum(Enum):
    """AUTOSAR DiagnosticAudienceEnum enumeration."""

    AFTERMARKET = "aftermarket"
    AFTERSALES = "afterSales"
    DEVELOPMENT = "development"
    MANUFACTURING = "manufacturing"
    SUPPLIER = "supplier"
