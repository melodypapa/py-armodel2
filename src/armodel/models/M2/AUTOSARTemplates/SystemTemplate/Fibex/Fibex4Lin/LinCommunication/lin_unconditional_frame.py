"""LinUnconditionalFrame AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinUnconditionalFrame(LinFrame):
    """AUTOSAR LinUnconditionalFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize LinUnconditionalFrame."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert LinUnconditionalFrame to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinUnconditionalFrame":
        """Create LinUnconditionalFrame from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            LinUnconditionalFrame instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to LinUnconditionalFrame since parent returns ARObject
        return cast("LinUnconditionalFrame", obj)


class LinUnconditionalFrameBuilder:
    """Builder for LinUnconditionalFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinUnconditionalFrame = LinUnconditionalFrame()

    def build(self) -> LinUnconditionalFrame:
        """Build and return LinUnconditionalFrame object.

        Returns:
            LinUnconditionalFrame instance
        """
        # TODO: Add validation
        return self._obj
