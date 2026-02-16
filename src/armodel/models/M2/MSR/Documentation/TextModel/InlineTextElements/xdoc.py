"""Xdoc AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.single_language_referrable import (
    SingleLanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    String,
)


class Xdoc(SingleLanguageReferrable):
    """AUTOSAR Xdoc."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("date", None, True, False, None),  # date
        ("number", None, True, False, None),  # number
        ("position", None, True, False, None),  # position
        ("publisher", None, True, False, None),  # publisher
        ("state", None, True, False, None),  # state
        ("url", None, False, False, any (Url)),  # url
    ]

    def __init__(self) -> None:
        """Initialize Xdoc."""
        super().__init__()
        self.date: Optional[DateTime] = None
        self.number: Optional[String] = None
        self.position: Optional[String] = None
        self.publisher: Optional[String] = None
        self.state: Optional[String] = None
        self.url: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert Xdoc to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Xdoc":
        """Create Xdoc from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            Xdoc instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to Xdoc since parent returns ARObject
        return cast("Xdoc", obj)


class XdocBuilder:
    """Builder for Xdoc."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Xdoc = Xdoc()

    def build(self) -> Xdoc:
        """Build and return Xdoc object.

        Returns:
            Xdoc instance
        """
        # TODO: Add validation
        return self._obj
