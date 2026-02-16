"""EventObdReadinessGroup AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)


class EventObdReadinessGroup(ARObject):
    """AUTOSAR EventObdReadinessGroup."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_obd", None, True, False, None),  # eventObd
    ]

    def __init__(self) -> None:
        """Initialize EventObdReadinessGroup."""
        super().__init__()
        self.event_obd: Optional[NameToken] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert EventObdReadinessGroup to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EventObdReadinessGroup":
        """Create EventObdReadinessGroup from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            EventObdReadinessGroup instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to EventObdReadinessGroup since parent returns ARObject
        return cast("EventObdReadinessGroup", obj)


class EventObdReadinessGroupBuilder:
    """Builder for EventObdReadinessGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EventObdReadinessGroup = EventObdReadinessGroup()

    def build(self) -> EventObdReadinessGroup:
        """Build and return EventObdReadinessGroup object.

        Returns:
            EventObdReadinessGroup instance
        """
        # TODO: Add validation
        return self._obj
