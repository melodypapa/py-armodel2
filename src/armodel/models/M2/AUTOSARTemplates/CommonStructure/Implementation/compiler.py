"""Compiler AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class Compiler(Identifiable):
    """AUTOSAR Compiler."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("name", None, True, False, None),  # name
        ("options", None, True, False, None),  # options
        ("vendor", None, True, False, None),  # vendor
        ("version", None, True, False, None),  # version
    ]

    def __init__(self) -> None:
        """Initialize Compiler."""
        super().__init__()
        self.name: Optional[String] = None
        self.options: Optional[String] = None
        self.vendor: Optional[String] = None
        self.version: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Compiler to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Compiler":
        """Create Compiler from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Compiler instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Compiler since parent returns ARObject
        return cast("Compiler", obj)


class CompilerBuilder:
    """Builder for Compiler."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Compiler = Compiler()

    def build(self) -> Compiler:
        """Build and return Compiler object.

        Returns:
            Compiler instance
        """
        # TODO: Add validation
        return self._obj
