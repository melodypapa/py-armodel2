"""PackageableElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ElementCollection.collectable_element import (
    CollectableElement,
)


class PackageableElement(CollectableElement):
    """AUTOSAR PackageableElement."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize PackageableElement."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PackageableElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PackageableElement":
        """Create PackageableElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PackageableElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PackageableElement since parent returns ARObject
        return cast("PackageableElement", obj)


class PackageableElementBuilder:
    """Builder for PackageableElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PackageableElement = PackageableElement()

    def build(self) -> PackageableElement:
        """Build and return PackageableElement object.

        Returns:
            PackageableElement instance
        """
        # TODO: Add validation
        return self._obj
