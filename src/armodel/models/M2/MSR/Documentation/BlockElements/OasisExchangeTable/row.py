"""Row AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TableSeparatorString,
)


class Row(Paginateable):
    """AUTOSAR Row."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("rowsep", None, True, False, None),  # rowsep
        ("valign", None, False, False, ValignEnum),  # valign
    ]

    def __init__(self) -> None:
        """Initialize Row."""
        super().__init__()
        self.rowsep: Optional[TableSeparatorString] = None
        self.valign: Optional[ValignEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Row to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Row":
        """Create Row from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Row instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Row since parent returns ARObject
        return cast("Row", obj)


class RowBuilder:
    """Builder for Row."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Row = Row()

    def build(self) -> Row:
        """Build and return Row object.

        Returns:
            Row instance
        """
        # TODO: Add validation
        return self._obj
