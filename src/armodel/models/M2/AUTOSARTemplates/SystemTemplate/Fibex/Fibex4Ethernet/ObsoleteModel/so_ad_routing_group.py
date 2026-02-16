"""SoAdRoutingGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)


class SoAdRoutingGroup(FibexElement):
    """AUTOSAR SoAdRoutingGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_group", None, False, False, EventGroupControlTypeEnum),  # eventGroup
    ]

    def __init__(self) -> None:
        """Initialize SoAdRoutingGroup."""
        super().__init__()
        self.event_group: Optional[EventGroupControlTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SoAdRoutingGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoAdRoutingGroup":
        """Create SoAdRoutingGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SoAdRoutingGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SoAdRoutingGroup since parent returns ARObject
        return cast("SoAdRoutingGroup", obj)


class SoAdRoutingGroupBuilder:
    """Builder for SoAdRoutingGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SoAdRoutingGroup = SoAdRoutingGroup()

    def build(self) -> SoAdRoutingGroup:
        """Build and return SoAdRoutingGroup object.

        Returns:
            SoAdRoutingGroup instance
        """
        # TODO: Add validation
        return self._obj
