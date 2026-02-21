"""Data models for XSD validation tool."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class DiscrepancyType(Enum):
    """Types of discrepancies between JSON and XSD definitions."""

    MISSING_XSD_TYPE = "missing_xsd_type"
    MISSING_MEMBER = "missing_member"
    EXTRA_MEMBER = "extra_member"
    TYPE_MISMATCH = "type_mismatch"
    MULTIPLICITY_MISMATCH = "multiplicity_mismatch"
    REF_KIND_MISMATCH = "ref_kind_mismatch"


class DiscrepancySeverity(Enum):
    """Severity levels for discrepancies."""

    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class XSDMember:
    """Represents a member from XSD schema."""

    xsd_name: str  # "AUTO-COLLECT"
    qualified_name: str  # "Collection.autoCollect"
    json_name: str  # "autoCollect"
    type_name: str  # "AR:AUTO-COLLECT-ENUM"
    min_occurs: int  # 0
    max_occurs: str  # "1" or "unbounded" or "-1"
    multiplicity: str  # "0..1", "*", "1"
    is_reference: bool  # True if ref/iref/tref
    reference_kind: Optional[str]  # "ref", "iref", "tref", "attribute"
    is_attribute: bool  # True if XML attribute (not element)


@dataclass
class XSDComplexType:
    """Represents a complexType from XSD schema."""

    xsd_name: str  # "COLLECTION"
    qualified_name: str  # "Collection"
    members: Dict[str, XSDMember] = field(default_factory=dict)  # Own members only
    all_members: Dict[str, XSDMember] = field(default_factory=dict)  # All members including inherited
    base_types: List[str] = field(default_factory=list)


@dataclass
class JSONMember:
    """Represents a member from JSON class definition."""

    type: str
    multiplicity: str
    kind: str  # "attribute", "ref", "iref", "tref", "xml_attribute"
    is_ref: bool
    note: Optional[str] = None


@dataclass
class JSONClass:
    """Represents a class from JSON definition."""

    name: str
    package: str
    is_abstract: bool
    atp_type: Optional[str]
    parent: Optional[str]
    bases: List[str]
    children: List[str]
    subclasses: List[str]
    attributes: Dict[str, JSONMember] = field(default_factory=dict)


@dataclass
class Discrepancy:
    """Represents a discrepancy between JSON and XSD."""

    discrepancy_type: DiscrepancyType
    severity: DiscrepancySeverity
    class_name: str
    member_name: Optional[str]  # None for class-level issues
    message: str
    details: Dict[str, str] = field(default_factory=dict)

    def __str__(self) -> str:
        """String representation for display."""
        if self.member_name:
            return f"[{self.class_name}.{self.member_name}] {self.discrepancy_type.value}: {self.message}"
        return f"[{self.class_name}] {self.discrepancy_type.value}: {self.message}"