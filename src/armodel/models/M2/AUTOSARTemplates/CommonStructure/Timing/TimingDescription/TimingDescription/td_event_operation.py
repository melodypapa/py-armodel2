"""TDEventOperation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)


class TDEventOperation(TDEventVfbPort):
    """AUTOSAR TDEventOperation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("operation", None, False, False, ClientServerOperation),  # operation
        ("td_event", None, False, False, TDEventOperationTypeEnum),  # tdEvent
    ]

    def __init__(self) -> None:
        """Initialize TDEventOperation."""
        super().__init__()
        self.operation: Optional[ClientServerOperation] = None
        self.td_event: Optional[TDEventOperationTypeEnum] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert TDEventOperation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventOperation":
        """Create TDEventOperation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            TDEventOperation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to TDEventOperation since parent returns ARObject
        return cast("TDEventOperation", obj)


class TDEventOperationBuilder:
    """Builder for TDEventOperation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventOperation = TDEventOperation()

    def build(self) -> TDEventOperation:
        """Build and return TDEventOperation object.

        Returns:
            TDEventOperation instance
        """
        # TODO: Add validation
        return self._obj
