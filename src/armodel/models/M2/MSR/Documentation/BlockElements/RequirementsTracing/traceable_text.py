"""TraceableText AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class TraceableText(Paginateable):
    """AUTOSAR TraceableText."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("text", None, False, False, DocumentationBlock),  # text
    ]

    def __init__(self) -> None:
        """Initialize TraceableText."""
        super().__init__()
        self.text: DocumentationBlock = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TraceableText to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TraceableText":
        """Create TraceableText from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TraceableText instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TraceableText since parent returns ARObject
        return cast("TraceableText", obj)


class TraceableTextBuilder:
    """Builder for TraceableText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TraceableText = TraceableText()

    def build(self) -> TraceableText:
        """Build and return TraceableText object.

        Returns:
            TraceableText instance
        """
        # TODO: Add validation
        return self._obj
