"""TransformerHardErrorEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class TransformerHardErrorEvent(RTEEvent):
    """AUTOSAR TransformerHardErrorEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation", None, False, False, ClientServerOperation),  # operation
        ("required_trigger", None, False, False, Trigger),  # requiredTrigger
    ]

    def __init__(self) -> None:
        """Initialize TransformerHardErrorEvent."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.required_trigger: Optional[Trigger] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TransformerHardErrorEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformerHardErrorEvent":
        """Create TransformerHardErrorEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TransformerHardErrorEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TransformerHardErrorEvent since parent returns ARObject
        return cast("TransformerHardErrorEvent", obj)


class TransformerHardErrorEventBuilder:
    """Builder for TransformerHardErrorEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformerHardErrorEvent = TransformerHardErrorEvent()

    def build(self) -> TransformerHardErrorEvent:
        """Build and return TransformerHardErrorEvent object.

        Returns:
            TransformerHardErrorEvent instance
        """
        # TODO: Add validation
        return self._obj
