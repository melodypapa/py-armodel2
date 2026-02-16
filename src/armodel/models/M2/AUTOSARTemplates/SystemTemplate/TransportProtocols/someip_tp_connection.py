"""SomeipTpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
    SomeipTpChannel,
)


class SomeipTpConnection(ARObject):
    """AUTOSAR SomeipTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("tp_channel", None, False, False, SomeipTpChannel),  # tpChannel
        ("tp_sdu", None, False, False, PduTriggering),  # tpSdu
        ("transport_pdu", None, False, False, PduTriggering),  # transportPdu
    ]

    def __init__(self) -> None:
        """Initialize SomeipTpConnection."""
        super().__init__()
        self.tp_channel: Optional[SomeipTpChannel] = None
        self.tp_sdu: Optional[PduTriggering] = None
        self.transport_pdu: Optional[PduTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SomeipTpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpConnection":
        """Create SomeipTpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SomeipTpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SomeipTpConnection since parent returns ARObject
        return cast("SomeipTpConnection", obj)


class SomeipTpConnectionBuilder:
    """Builder for SomeipTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SomeipTpConnection = SomeipTpConnection()

    def build(self) -> SomeipTpConnection:
        """Build and return SomeipTpConnection object.

        Returns:
            SomeipTpConnection instance
        """
        # TODO: Add validation
        return self._obj
