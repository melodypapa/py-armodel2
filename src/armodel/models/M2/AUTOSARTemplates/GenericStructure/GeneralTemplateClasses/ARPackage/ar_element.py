"""ARElement AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.packageable_element import (
    PackageableElement,
)


class ARElement(PackageableElement):
    """AUTOSAR ARElement."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize ARElement."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ARElement to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARElement":
        """Create ARElement from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ARElement instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ARElement since parent returns ARObject
        return cast("ARElement", obj)


class ARElementBuilder:
    """Builder for ARElement."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARElement = ARElement()

    def build(self) -> ARElement:
        """Build and return ARElement object.

        Returns:
            ARElement instance
        """
        # TODO: Add validation
        return self._obj
