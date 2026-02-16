"""FlexrayTpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_connection import (
    FlexrayTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_node import (
    FlexrayTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_pdu_pool import (
    FlexrayTpPduPool,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayTpConnection(TpConnection):
    """AUTOSAR FlexrayTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("bandwidth", None, True, False, None),  # bandwidth
        ("direct_tp_sdu", None, False, False, IPdu),  # directTpSdu
        ("multicast", None, False, False, TpAddress),  # multicast
        ("receivers", None, False, True, FlexrayTpNode),  # receivers
        ("reversed_tp_sdu", None, False, False, IPdu),  # reversedTpSdu
        ("rx_pdu_pool", None, False, False, FlexrayTpPduPool),  # rxPduPool
        ("tp_connection", None, False, False, FlexrayTpConnection),  # tpConnection
        ("transmitter", None, False, False, FlexrayTpNode),  # transmitter
        ("tx_pdu_pool", None, False, False, FlexrayTpPduPool),  # txPduPool
    ]

    def __init__(self) -> None:
        """Initialize FlexrayTpConnection."""
        super().__init__()
        self.bandwidth: Optional[Boolean] = None
        self.direct_tp_sdu: Optional[IPdu] = None
        self.multicast: Optional[TpAddress] = None
        self.receivers: list[FlexrayTpNode] = []
        self.reversed_tp_sdu: Optional[IPdu] = None
        self.rx_pdu_pool: Optional[FlexrayTpPduPool] = None
        self.tp_connection: Optional[FlexrayTpConnection] = None
        self.transmitter: Optional[FlexrayTpNode] = None
        self.tx_pdu_pool: Optional[FlexrayTpPduPool] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayTpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConnection":
        """Create FlexrayTpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayTpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayTpConnection since parent returns ARObject
        return cast("FlexrayTpConnection", obj)


class FlexrayTpConnectionBuilder:
    """Builder for FlexrayTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayTpConnection = FlexrayTpConnection()

    def build(self) -> FlexrayTpConnection:
        """Build and return FlexrayTpConnection object.

        Returns:
            FlexrayTpConnection instance
        """
        # TODO: Add validation
        return self._obj
