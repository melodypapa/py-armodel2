"""BswAsynchronousServerCallReturnsEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)


class BswAsynchronousServerCallReturnsEvent(BswScheduleEvent):
    """AUTOSAR BswAsynchronousServerCallReturnsEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_source", None, False, False, any (BswAsynchronous)),  # eventSource
    ]

    def __init__(self) -> None:
        """Initialize BswAsynchronousServerCallReturnsEvent."""
        super().__init__()
        self.event_source: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswAsynchronousServerCallReturnsEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswAsynchronousServerCallReturnsEvent":
        """Create BswAsynchronousServerCallReturnsEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswAsynchronousServerCallReturnsEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswAsynchronousServerCallReturnsEvent since parent returns ARObject
        return cast("BswAsynchronousServerCallReturnsEvent", obj)


class BswAsynchronousServerCallReturnsEventBuilder:
    """Builder for BswAsynchronousServerCallReturnsEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswAsynchronousServerCallReturnsEvent = BswAsynchronousServerCallReturnsEvent()

    def build(self) -> BswAsynchronousServerCallReturnsEvent:
        """Build and return BswAsynchronousServerCallReturnsEvent object.

        Returns:
            BswAsynchronousServerCallReturnsEvent instance
        """
        # TODO: Add validation
        return self._obj
