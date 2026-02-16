"""Item AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class Item(Paginateable):
    """AUTOSAR Item."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("item_contents", None, False, False, DocumentationBlock),  # itemContents
    ]

    def __init__(self) -> None:
        """Initialize Item."""
        super().__init__()
        self.item_contents: DocumentationBlock = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Item to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Item":
        """Create Item from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Item instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Item since parent returns ARObject
        return cast("Item", obj)


class ItemBuilder:
    """Builder for Item."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Item = Item()

    def build(self) -> Item:
        """Build and return Item object.

        Returns:
            Item instance
        """
        # TODO: Add validation
        return self._obj
