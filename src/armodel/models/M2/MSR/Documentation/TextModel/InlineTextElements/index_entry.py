"""IndexEntry AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Superscript,
)


class IndexEntry(ARObject):
    """AUTOSAR IndexEntry."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("sub", None, True, False, None),  # sub
        ("sup", None, True, False, None),  # sup
    ]

    def __init__(self) -> None:
        """Initialize IndexEntry."""
        super().__init__()
        self.sub: Superscript = None
        self.sup: Superscript = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IndexEntry to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndexEntry":
        """Create IndexEntry from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IndexEntry instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IndexEntry since parent returns ARObject
        return cast("IndexEntry", obj)


class IndexEntryBuilder:
    """Builder for IndexEntry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndexEntry = IndexEntry()

    def build(self) -> IndexEntry:
        """Build and return IndexEntry object.

        Returns:
            IndexEntry instance
        """
        # TODO: Add validation
        return self._obj
