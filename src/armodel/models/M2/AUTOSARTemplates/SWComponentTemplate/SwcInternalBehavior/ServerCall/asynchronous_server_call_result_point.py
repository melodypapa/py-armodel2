"""AsynchronousServerCallResultPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)


class AsynchronousServerCallResultPoint(AbstractAccessPoint):
    """AUTOSAR AsynchronousServerCallResultPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("asynchronous_server", None, False, False, any (AsynchronousServer)),  # asynchronousServer
    ]

    def __init__(self) -> None:
        """Initialize AsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous_server: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert AsynchronousServerCallResultPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AsynchronousServerCallResultPoint":
        """Create AsynchronousServerCallResultPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            AsynchronousServerCallResultPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to AsynchronousServerCallResultPoint since parent returns ARObject
        return cast("AsynchronousServerCallResultPoint", obj)


class AsynchronousServerCallResultPointBuilder:
    """Builder for AsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AsynchronousServerCallResultPoint = AsynchronousServerCallResultPoint()

    def build(self) -> AsynchronousServerCallResultPoint:
        """Build and return AsynchronousServerCallResultPoint object.

        Returns:
            AsynchronousServerCallResultPoint instance
        """
        # TODO: Add validation
        return self._obj
