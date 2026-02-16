"""LabeledList AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.indent_sample import (
    IndentSample,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_item import (
    LabeledItem,
)


class LabeledList(Paginateable):
    """AUTOSAR LabeledList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("indent_sample", None, False, False, IndentSample),  # indentSample
        ("labeled_item_label", None, False, False, LabeledItem),  # labeledItemLabel
    ]

    def __init__(self) -> None:
        """Initialize LabeledList."""
        super().__init__()
        self.indent_sample: Optional[IndentSample] = None
        self.labeled_item_label: LabeledItem = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LabeledList to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LabeledList":
        """Create LabeledList from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LabeledList instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LabeledList since parent returns ARObject
        return cast("LabeledList", obj)


class LabeledListBuilder:
    """Builder for LabeledList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LabeledList = LabeledList()

    def build(self) -> LabeledList:
        """Build and return LabeledList object.

        Returns:
            LabeledList instance
        """
        # TODO: Add validation
        return self._obj
