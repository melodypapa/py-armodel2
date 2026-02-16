"""SpecificationDocumentScope AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchange.document_element_scope import (
    DocumentElementScope,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.DocumentationOnM1.documentation import (
    Documentation,
)


class SpecificationDocumentScope(SpecElementReference):
    """AUTOSAR SpecificationDocumentScope."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("custom_documentation", None, False, False, Documentation),  # customDocumentation
        ("documents", None, False, True, DocumentElementScope),  # documents
    ]

    def __init__(self) -> None:
        """Initialize SpecificationDocumentScope."""
        super().__init__()
        self.custom_documentation: Optional[Documentation] = None
        self.documents: list[DocumentElementScope] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SpecificationDocumentScope to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SpecificationDocumentScope":
        """Create SpecificationDocumentScope from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SpecificationDocumentScope instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SpecificationDocumentScope since parent returns ARObject
        return cast("SpecificationDocumentScope", obj)


class SpecificationDocumentScopeBuilder:
    """Builder for SpecificationDocumentScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SpecificationDocumentScope = SpecificationDocumentScope()

    def build(self) -> SpecificationDocumentScope:
        """Build and return SpecificationDocumentScope object.

        Returns:
            SpecificationDocumentScope instance
        """
        # TODO: Add validation
        return self._obj
