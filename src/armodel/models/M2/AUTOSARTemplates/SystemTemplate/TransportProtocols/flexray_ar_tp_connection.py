"""FlexrayArTpConnection AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_node import (
    FlexrayArTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class FlexrayArTpConnection(TpConnection):
    """AUTOSAR FlexrayArTpConnection."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("connection_prio", None, True, False, None),  # connectionPrio
        ("direct_tp_sdu", None, False, False, IPdu),  # directTpSdu
        ("multicast", None, False, False, TpAddress),  # multicast
        ("reversed_tp_sdu", None, False, False, IPdu),  # reversedTpSdu
        ("source", None, False, False, FlexrayArTpNode),  # source
        ("targets", None, False, True, FlexrayArTpNode),  # targets
    ]

    def __init__(self) -> None:
        """Initialize FlexrayArTpConnection."""
        super().__init__()
        self.connection_prio: Optional[Integer] = None
        self.direct_tp_sdu: Optional[IPdu] = None
        self.multicast: Optional[TpAddress] = None
        self.reversed_tp_sdu: Optional[IPdu] = None
        self.source: Optional[FlexrayArTpNode] = None
        self.targets: list[FlexrayArTpNode] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayArTpConnection to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpConnection":
        """Create FlexrayArTpConnection from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayArTpConnection instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayArTpConnection since parent returns ARObject
        return cast("FlexrayArTpConnection", obj)


class FlexrayArTpConnectionBuilder:
    """Builder for FlexrayArTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpConnection = FlexrayArTpConnection()

    def build(self) -> FlexrayArTpConnection:
        """Build and return FlexrayArTpConnection object.

        Returns:
            FlexrayArTpConnection instance
        """
        # TODO: Add validation
        return self._obj
