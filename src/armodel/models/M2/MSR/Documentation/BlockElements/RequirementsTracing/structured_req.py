"""StructuredReq AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)


class StructuredReq(Paginateable):
    """AUTOSAR StructuredReq."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("applies_tos", None, False, True, StandardNameEnum),  # appliesTos
        ("conflicts", None, False, False, DocumentationBlock),  # conflicts
        ("date", None, True, False, None),  # date
        ("dependencies", None, False, False, DocumentationBlock),  # dependencies
        ("description", None, False, False, DocumentationBlock),  # description
        ("importance", None, True, False, None),  # importance
        ("issued_by", None, True, False, None),  # issuedBy
        ("rationale", None, False, False, DocumentationBlock),  # rationale
        ("remark", None, False, False, DocumentationBlock),  # remark
        ("supporting", None, False, False, DocumentationBlock),  # supporting
        ("tested_items", None, False, True, Traceable),  # testedItems
        ("type", None, True, False, None),  # type
        ("use_case", None, False, False, DocumentationBlock),  # useCase
    ]

    def __init__(self) -> None:
        """Initialize StructuredReq."""
        super().__init__()
        self.applies_tos: list[StandardNameEnum] = []
        self.conflicts: Optional[DocumentationBlock] = None
        self.date: DateTime = None
        self.dependencies: Optional[DocumentationBlock] = None
        self.description: Optional[DocumentationBlock] = None
        self.importance: String = None
        self.issued_by: String = None
        self.rationale: Optional[DocumentationBlock] = None
        self.remark: Optional[DocumentationBlock] = None
        self.supporting: Optional[DocumentationBlock] = None
        self.tested_items: list[Traceable] = []
        self.type: String = None
        self.use_case: Optional[DocumentationBlock] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert StructuredReq to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StructuredReq":
        """Create StructuredReq from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            StructuredReq instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to StructuredReq since parent returns ARObject
        return cast("StructuredReq", obj)


class StructuredReqBuilder:
    """Builder for StructuredReq."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StructuredReq = StructuredReq()

    def build(self) -> StructuredReq:
        """Build and return StructuredReq object.

        Returns:
            StructuredReq instance
        """
        # TODO: Add validation
        return self._obj
