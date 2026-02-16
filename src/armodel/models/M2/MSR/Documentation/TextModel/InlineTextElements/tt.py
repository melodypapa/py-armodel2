"""Tt AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)


class Tt(ARObject):
    """AUTOSAR Tt."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("term", None, True, False, None),  # term
        ("tex_render", None, True, False, None),  # texRender
        ("type", None, True, False, None),  # type
    ]

    def __init__(self) -> None:
        """Initialize Tt."""
        super().__init__()
        self.term: String = None
        self.tex_render: Optional[String] = None
        self.type: NameToken = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Tt to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Tt":
        """Create Tt from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Tt instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Tt since parent returns ARObject
        return cast("Tt", obj)


class TtBuilder:
    """Builder for Tt."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Tt = Tt()

    def build(self) -> Tt:
        """Build and return Tt object.

        Returns:
            Tt instance
        """
        # TODO: Add validation
        return self._obj
