"""DataWriteCompletedEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class DataWriteCompletedEvent(RTEEvent):
    """AUTOSAR DataWriteCompletedEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_source", None, False, False, VariableAccess),  # eventSource
    ]

    def __init__(self) -> None:
        """Initialize DataWriteCompletedEvent."""
        super().__init__()
        self.event_source: Optional[VariableAccess] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataWriteCompletedEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataWriteCompletedEvent":
        """Create DataWriteCompletedEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataWriteCompletedEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataWriteCompletedEvent since parent returns ARObject
        return cast("DataWriteCompletedEvent", obj)


class DataWriteCompletedEventBuilder:
    """Builder for DataWriteCompletedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataWriteCompletedEvent = DataWriteCompletedEvent()

    def build(self) -> DataWriteCompletedEvent:
        """Build and return DataWriteCompletedEvent object.

        Returns:
            DataWriteCompletedEvent instance
        """
        # TODO: Add validation
        return self._obj
