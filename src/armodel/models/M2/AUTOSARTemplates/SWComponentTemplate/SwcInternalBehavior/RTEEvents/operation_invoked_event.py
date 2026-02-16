"""OperationInvokedEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.RTEEvents.rte_event import (
    RTEEvent,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class OperationInvokedEvent(RTEEvent):
    """AUTOSAR OperationInvokedEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation_instance_ref", None, False, False, ClientServerOperation),  # operationInstanceRef
    ]

    def __init__(self) -> None:
        """Initialize OperationInvokedEvent."""
        super().__init__()
        self.operation_instance_ref: Optional[ClientServerOperation] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert OperationInvokedEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "OperationInvokedEvent":
        """Create OperationInvokedEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            OperationInvokedEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to OperationInvokedEvent since parent returns ARObject
        return cast("OperationInvokedEvent", obj)


class OperationInvokedEventBuilder:
    """Builder for OperationInvokedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OperationInvokedEvent = OperationInvokedEvent()

    def build(self) -> OperationInvokedEvent:
        """Build and return OperationInvokedEvent object.

        Returns:
            OperationInvokedEvent instance
        """
        # TODO: Add validation
        return self._obj
