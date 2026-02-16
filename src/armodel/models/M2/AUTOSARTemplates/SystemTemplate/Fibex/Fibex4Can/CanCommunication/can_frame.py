"""CanFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)


class CanFrame(Frame):
    """AUTOSAR CanFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize CanFrame."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CanFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanFrame":
        """Create CanFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CanFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CanFrame since parent returns ARObject
        return cast("CanFrame", obj)


class CanFrameBuilder:
    """Builder for CanFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanFrame = CanFrame()

    def build(self) -> CanFrame:
        """Build and return CanFrame object.

        Returns:
            CanFrame instance
        """
        # TODO: Add validation
        return self._obj
