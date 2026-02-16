"""BswOperationInvokedEvent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_event import (
    BswEvent,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_client_server_entry import (
    BswModuleClientServerEntry,
)


class BswOperationInvokedEvent(BswEvent):
    """AUTOSAR BswOperationInvokedEvent."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("entry", None, False, False, BswModuleClientServerEntry),  # entry
    ]

    def __init__(self) -> None:
        """Initialize BswOperationInvokedEvent."""
        super().__init__()
        self.entry: Optional[BswModuleClientServerEntry] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswOperationInvokedEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswOperationInvokedEvent":
        """Create BswOperationInvokedEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswOperationInvokedEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswOperationInvokedEvent since parent returns ARObject
        return cast("BswOperationInvokedEvent", obj)


class BswOperationInvokedEventBuilder:
    """Builder for BswOperationInvokedEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswOperationInvokedEvent = BswOperationInvokedEvent()

    def build(self) -> BswOperationInvokedEvent:
        """Build and return BswOperationInvokedEvent object.

        Returns:
            BswOperationInvokedEvent instance
        """
        # TODO: Add validation
        return self._obj
