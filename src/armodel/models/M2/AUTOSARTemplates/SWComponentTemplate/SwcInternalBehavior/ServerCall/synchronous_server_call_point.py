"""SynchronousServerCallPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.ServerCall.server_call_point import (
    ServerCallPoint,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area_nesting_order import (
    ExclusiveAreaNestingOrder,
)


class SynchronousServerCallPoint(ServerCallPoint):
    """AUTOSAR SynchronousServerCallPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("called_from", None, False, False, ExclusiveAreaNestingOrder),  # calledFrom
    ]

    def __init__(self) -> None:
        """Initialize SynchronousServerCallPoint."""
        super().__init__()
        self.called_from: Optional[ExclusiveAreaNestingOrder] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SynchronousServerCallPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SynchronousServerCallPoint":
        """Create SynchronousServerCallPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SynchronousServerCallPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SynchronousServerCallPoint since parent returns ARObject
        return cast("SynchronousServerCallPoint", obj)


class SynchronousServerCallPointBuilder:
    """Builder for SynchronousServerCallPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SynchronousServerCallPoint = SynchronousServerCallPoint()

    def build(self) -> SynchronousServerCallPoint:
        """Build and return SynchronousServerCallPoint object.

        Returns:
            SynchronousServerCallPoint instance
        """
        # TODO: Add validation
        return self._obj
