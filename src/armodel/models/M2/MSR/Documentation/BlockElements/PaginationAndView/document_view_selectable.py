"""DocumentViewSelectable AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameTokens,
)
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.view_tokens import (
    ViewTokens,
)


class DocumentViewSelectable(ARObject):
    """AUTOSAR DocumentViewSelectable."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("si", None, True, False, None),  # si
        ("view", None, True, False, None),  # view
    ]

    def __init__(self) -> None:
        """Initialize DocumentViewSelectable."""
        super().__init__()
        self.si: NameTokens = None
        self.view: Optional[ViewTokens] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DocumentViewSelectable to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DocumentViewSelectable":
        """Create DocumentViewSelectable from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DocumentViewSelectable instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DocumentViewSelectable since parent returns ARObject
        return cast("DocumentViewSelectable", obj)


class DocumentViewSelectableBuilder:
    """Builder for DocumentViewSelectable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DocumentViewSelectable = DocumentViewSelectable()

    def build(self) -> DocumentViewSelectable:
        """Build and return DocumentViewSelectable object.

        Returns:
            DocumentViewSelectable instance
        """
        # TODO: Add validation
        return self._obj
