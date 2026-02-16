"""FlexrayArTpChannel AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_ar_tp_connection import (
    FlexrayArTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class FlexrayArTpChannel(ARObject):
    """AUTOSAR FlexrayArTpChannel."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ack_type", None, False, False, FrArTpAckType),  # ackType
        ("cancellation", None, True, False, None),  # cancellation
        ("extended", None, True, False, None),  # extended
        ("max_ar", None, True, False, None),  # maxAr
        ("max_as", None, True, False, None),  # maxAs
        ("max_bs", None, True, False, None),  # maxBs
        ("max_fc_wait", None, True, False, None),  # maxFcWait
        ("maximum_message", None, False, False, MaximumMessageLengthType),  # maximumMessage
        ("max_retries", None, True, False, None),  # maxRetries
        ("minimum", None, True, False, None),  # minimum
        ("multicast", None, True, False, None),  # multicast
        ("n_pdus", None, False, True, NPdu),  # nPdus
        ("time_br", None, True, False, None),  # timeBr
        ("time_cs", None, True, False, None),  # timeCs
        ("timeout_ar", None, True, False, None),  # timeoutAr
        ("timeout_as", None, True, False, None),  # timeoutAs
        ("timeout_bs", None, True, False, None),  # timeoutBs
        ("timeout_cr", None, True, False, None),  # timeoutCr
        ("tp_connections", None, False, True, FlexrayArTpConnection),  # tpConnections
    ]

    def __init__(self) -> None:
        """Initialize FlexrayArTpChannel."""
        super().__init__()
        self.ack_type: Optional[FrArTpAckType] = None
        self.cancellation: Optional[Boolean] = None
        self.extended: Optional[Boolean] = None
        self.max_ar: Optional[Integer] = None
        self.max_as: Optional[Integer] = None
        self.max_bs: Optional[Integer] = None
        self.max_fc_wait: Optional[PositiveInteger] = None
        self.maximum_message: Optional[MaximumMessageLengthType] = None
        self.max_retries: Optional[Integer] = None
        self.minimum: Optional[TimeValue] = None
        self.multicast: Optional[Boolean] = None
        self.n_pdus: list[NPdu] = []
        self.time_br: Optional[TimeValue] = None
        self.time_cs: Optional[TimeValue] = None
        self.timeout_ar: Optional[TimeValue] = None
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.tp_connections: list[FlexrayArTpConnection] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert FlexrayArTpChannel to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayArTpChannel":
        """Create FlexrayArTpChannel from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            FlexrayArTpChannel instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to FlexrayArTpChannel since parent returns ARObject
        return cast("FlexrayArTpChannel", obj)


class FlexrayArTpChannelBuilder:
    """Builder for FlexrayArTpChannel."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlexrayArTpChannel = FlexrayArTpChannel()

    def build(self) -> FlexrayArTpChannel:
        """Build and return FlexrayArTpChannel object.

        Returns:
            FlexrayArTpChannel instance
        """
        # TODO: Add validation
        return self._obj
