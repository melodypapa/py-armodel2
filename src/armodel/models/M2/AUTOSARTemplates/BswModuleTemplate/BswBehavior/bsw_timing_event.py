"""BswTimingEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_schedule_event import (
    BswScheduleEvent,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)


class BswTimingEvent(BswScheduleEvent):
    """AUTOSAR BswTimingEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("period", None, True, False, None),  # period
    ]

    def __init__(self) -> None:
        """Initialize BswTimingEvent."""
        super().__init__()
        self.period: Optional[TimeValue] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswTimingEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswTimingEvent":
        """Create BswTimingEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswTimingEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswTimingEvent since parent returns ARObject
        return cast("BswTimingEvent", obj)


class BswTimingEventBuilder:
    """Builder for BswTimingEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswTimingEvent = BswTimingEvent()

    def build(self) -> BswTimingEvent:
        """Build and return BswTimingEvent object.

        Returns:
            BswTimingEvent instance
        """
        # TODO: Add validation
        return self._obj
