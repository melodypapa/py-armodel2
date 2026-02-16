"""DocumentElementScope AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.DataExchangePoint.Common.spec_element_reference import (
    SpecElementReference,
)


class DocumentElementScope(SpecElementReference):
    """AUTOSAR DocumentElementScope."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("custom_document", None, False, False, any (TraceableElement)),  # customDocument
        ("tailorings", None, False, True, any (DataFormatElement)),  # tailorings
    ]

    def __init__(self) -> None:
        """Initialize DocumentElementScope."""
        super().__init__()
        self.custom_document: Optional[Any] = None
        self.tailorings: list[Any] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DocumentElementScope to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentElementScope":
        """Create DocumentElementScope from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DocumentElementScope instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DocumentElementScope since parent returns ARObject
        return cast("DocumentElementScope", obj)


class DocumentElementScopeBuilder:
    """Builder for DocumentElementScope."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentElementScope = DocumentElementScope()

    def build(self) -> DocumentElementScope:
        """Build and return DocumentElementScope object.

        Returns:
            DocumentElementScope instance
        """
        # TODO: Add validation
        return self._obj
