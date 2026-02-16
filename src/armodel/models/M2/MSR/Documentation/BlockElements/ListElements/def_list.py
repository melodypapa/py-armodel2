"""DefList AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.def_item import (
    DefItem,
)


class DefList(Paginateable):
    """AUTOSAR DefList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("def_item", None, False, False, DefItem),  # defItem
    ]

    def __init__(self) -> None:
        """Initialize DefList."""
        super().__init__()
        self.def_item: DefItem = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DefList to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefList":
        """Create DefList from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DefList instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DefList since parent returns ARObject
        return cast("DefList", obj)


class DefListBuilder:
    """Builder for DefList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefList = DefList()

    def build(self) -> DefList:
        """Build and return DefList object.

        Returns:
            DefList instance
        """
        # TODO: Add validation
        return self._obj
