"""SoftwareContext AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)


class SoftwareContext(ARObject):
    """AUTOSAR SoftwareContext."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("input", None, True, False, None),  # input
        ("state", None, True, False, None),  # state
    ]

    def __init__(self) -> None:
        """Initialize SoftwareContext."""
        super().__init__()
        self.input: Optional[String] = None
        self.state: Optional[String] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SoftwareContext to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoftwareContext":
        """Create SoftwareContext from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SoftwareContext instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SoftwareContext since parent returns ARObject
        return cast("SoftwareContext", obj)


class SoftwareContextBuilder:
    """Builder for SoftwareContext."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoftwareContext = SoftwareContext()

    def build(self) -> SoftwareContext:
        """Build and return SoftwareContext object.

        Returns:
            SoftwareContext instance
        """
        # TODO: Add validation
        return self._obj
