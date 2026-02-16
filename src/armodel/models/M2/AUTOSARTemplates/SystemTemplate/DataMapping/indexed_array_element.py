"""IndexedArrayElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)


class IndexedArrayElement(ARObject):
    """AUTOSAR IndexedArrayElement."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("application_array", None, False, False, any (ApplicationArray)),  # applicationArray
        ("implementation", None, False, False, any (ImplementationData)),  # implementation
        ("index", None, True, False, None),  # index
    ]

    def __init__(self) -> None:
        """Initialize IndexedArrayElement."""
        super().__init__()
        self.application_array: Optional[Any] = None
        self.implementation: Optional[Any] = None
        self.index: Optional[Integer] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert IndexedArrayElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "IndexedArrayElement":
        """Create IndexedArrayElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            IndexedArrayElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to IndexedArrayElement since parent returns ARObject
        return cast("IndexedArrayElement", obj)


class IndexedArrayElementBuilder:
    """Builder for IndexedArrayElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IndexedArrayElement = IndexedArrayElement()

    def build(self) -> IndexedArrayElement:
        """Build and return IndexedArrayElement object.

        Returns:
            IndexedArrayElement instance
        """
        # TODO: Add validation
        return self._obj
