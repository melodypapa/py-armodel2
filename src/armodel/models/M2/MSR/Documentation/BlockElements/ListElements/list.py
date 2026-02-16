"""List AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.item import (
    Item,
)


class List(Paginateable):
    """AUTOSAR List."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("item", None, False, False, Item),  # item
        ("type", None, False, False, ListEnum),  # type
    ]

    def __init__(self) -> None:
        """Initialize List."""
        super().__init__()
        self.item: Item = None
        self.type: Optional[ListEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert List to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "List":
        """Create List from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            List instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to List since parent returns ARObject
        return cast("List", obj)


class ListBuilder:
    """Builder for List."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: List = List()

    def build(self) -> List:
        """Build and return List object.

        Returns:
            List instance
        """
        # TODO: Add validation
        return self._obj
