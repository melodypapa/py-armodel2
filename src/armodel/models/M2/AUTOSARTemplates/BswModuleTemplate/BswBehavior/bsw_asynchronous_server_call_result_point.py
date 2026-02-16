"""BswAsynchronousServerCallResultPoint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_module_call_point import (
    BswModuleCallPoint,
)


class BswAsynchronousServerCallResultPoint(BswModuleCallPoint):
    """AUTOSAR BswAsynchronousServerCallResultPoint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("asynchronous", None, False, False, any (BswAsynchronous)),  # asynchronous
    ]

    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallResultPoint."""
        super().__init__()
        self.asynchronous: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswAsynchronousServerCallResultPoint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswAsynchronousServerCallResultPoint":
        """Create BswAsynchronousServerCallResultPoint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswAsynchronousServerCallResultPoint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswAsynchronousServerCallResultPoint since parent returns ARObject
        return cast("BswAsynchronousServerCallResultPoint", obj)


class BswAsynchronousServerCallResultPointBuilder:
    """Builder for BswAsynchronousServerCallResultPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallResultPoint = BswAsynchronousServerCallResultPoint()

    def build(self) -> BswAsynchronousServerCallResultPoint:
        """Build and return BswAsynchronousServerCallResultPoint object.

        Returns:
            BswAsynchronousServerCallResultPoint instance
        """
        # TODO: Add validation
        return self._obj
