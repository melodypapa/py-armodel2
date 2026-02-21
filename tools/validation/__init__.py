"""XSD validation module for comparing JSON class definitions against AUTOSAR XSD schema."""

from tools.validation.models import (
    Discrepancy,
    DiscrepancySeverity,
    JSONClass,
    JSONMember,
    XSDComplexType,
    XSDMember,
)

__all__ = [
    "Discrepancy",
    "DiscrepancySeverity",
    "JSONClass",
    "JSONMember",
    "XSDComplexType",
    "XSDMember",
]