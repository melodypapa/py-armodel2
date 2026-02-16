"""DataSendCompletedEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
    VariableAccess,
)


class DataSendCompletedEvent(RTEEvent):
    """AUTOSAR DataSendCompletedEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("event_source", None, False, False, VariableAccess),  # eventSource
    ]

    def __init__(self) -> None:
        """Initialize DataSendCompletedEvent."""
        super().__init__()
        self.event_source: Optional[VariableAccess] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DataSendCompletedEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataSendCompletedEvent":
        """Create DataSendCompletedEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DataSendCompletedEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DataSendCompletedEvent since parent returns ARObject
        return cast("DataSendCompletedEvent", obj)


class DataSendCompletedEventBuilder:
    """Builder for DataSendCompletedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DataSendCompletedEvent = DataSendCompletedEvent()

    def build(self) -> DataSendCompletedEvent:
        """Build and return DataSendCompletedEvent object.

        Returns:
            DataSendCompletedEvent instance
        """
        # TODO: Add validation
        return self._obj
