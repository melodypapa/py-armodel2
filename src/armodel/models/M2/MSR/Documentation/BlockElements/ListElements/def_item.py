"""DefItem AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class DefItem(Paginateable):
    """AUTOSAR DefItem."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("def_", 'DEF', False, False, DocumentationBlock),  # def
        ("help_entry", None, True, False, None),  # helpEntry
    ]

    def __init__(self) -> None:
        """Initialize DefItem."""
        super().__init__()
        self.def_: DocumentationBlock = None
        self.help_entry: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DefItem to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DefItem":
        """Create DefItem from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DefItem instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DefItem since parent returns ARObject
        return cast("DefItem", obj)


class DefItemBuilder:
    """Builder for DefItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefItem = DefItem()

    def build(self) -> DefItem:
        """Build and return DefItem object.

        Returns:
            DefItem instance
        """
        # TODO: Add validation
        return self._obj
