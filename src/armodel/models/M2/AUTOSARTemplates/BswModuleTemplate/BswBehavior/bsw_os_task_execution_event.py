"""BswOsTaskExecutionEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)


class BswOsTaskExecutionEvent(BswScheduleEvent):
    """AUTOSAR BswOsTaskExecutionEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
    ]

    def __init__(self) -> None:
        """Initialize BswOsTaskExecutionEvent."""
        super().__init__()

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswOsTaskExecutionEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswOsTaskExecutionEvent":
        """Create BswOsTaskExecutionEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswOsTaskExecutionEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswOsTaskExecutionEvent since parent returns ARObject
        return cast("BswOsTaskExecutionEvent", obj)


class BswOsTaskExecutionEventBuilder:
    """Builder for BswOsTaskExecutionEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswOsTaskExecutionEvent = BswOsTaskExecutionEvent()

    def build(self) -> BswOsTaskExecutionEvent:
        """Build and return BswOsTaskExecutionEvent object.

        Returns:
            BswOsTaskExecutionEvent instance
        """
        # TODO: Add validation
        return self._obj
