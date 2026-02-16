"""DoIpTpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)


class DoIpTpConnection(TpConnection):
    """AUTOSAR DoIpTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("do_ip_source", None, False, False, DoIpLogicAddress),  # doIpSource
        ("do_ip_target", None, False, False, DoIpLogicAddress),  # doIpTarget
        ("tp_sdu", None, False, False, PduTriggering),  # tpSdu
    ]

    def __init__(self) -> None:
        """Initialize DoIpTpConnection."""
        super().__init__()
        self.do_ip_source: Optional[DoIpLogicAddress] = None
        self.do_ip_target: Optional[DoIpLogicAddress] = None
        self.tp_sdu: Optional[PduTriggering] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert DoIpTpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpTpConnection":
        """Create DoIpTpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            DoIpTpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to DoIpTpConnection since parent returns ARObject
        return cast("DoIpTpConnection", obj)


class DoIpTpConnectionBuilder:
    """Builder for DoIpTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DoIpTpConnection = DoIpTpConnection()

    def build(self) -> DoIpTpConnection:
        """Build and return DoIpTpConnection object.

        Returns:
            DoIpTpConnection instance
        """
        # TODO: Add validation
        return self._obj
