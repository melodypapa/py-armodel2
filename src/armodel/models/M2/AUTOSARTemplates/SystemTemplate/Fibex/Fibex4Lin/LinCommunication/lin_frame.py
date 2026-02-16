"""LinFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)


class LinFrame(Frame):
    """AUTOSAR LinFrame."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize LinFrame."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinFrame":
        """Create LinFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinFrame since parent returns ARObject
        return cast("LinFrame", obj)


class LinFrameBuilder:
    """Builder for LinFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinFrame = LinFrame()

    def build(self) -> LinFrame:
        """Build and return LinFrame object.

        Returns:
            LinFrame instance
        """
        # TODO: Add validation
        return self._obj
