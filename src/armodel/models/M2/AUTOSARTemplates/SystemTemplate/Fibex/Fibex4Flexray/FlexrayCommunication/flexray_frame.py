"""FlexrayFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.frame import (
    Frame,
)


class FlexrayFrame(Frame):
    """AUTOSAR FlexrayFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize FlexrayFrame."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayFrame":
        """Create FlexrayFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayFrame since parent returns ARObject
        return cast("FlexrayFrame", obj)


class FlexrayFrameBuilder:
    """Builder for FlexrayFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayFrame = FlexrayFrame()

    def build(self) -> FlexrayFrame:
        """Build and return FlexrayFrame object.

        Returns:
            FlexrayFrame instance
        """
        # TODO: Add validation
        return self._obj
