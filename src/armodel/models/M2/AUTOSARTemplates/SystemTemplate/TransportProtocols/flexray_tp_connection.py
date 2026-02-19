"""FlexrayTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 594)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.tp_connection import (
    TpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bandwidth: Optional[Boolean]
    direct_tp_sdu: Optional[IPdu]
    multicast: Optional[TpAddress]
    receivers: list[FlexrayTpNode]
    reversed_tp_sdu: Optional[IPdu]
    rx_pdu_pool: Optional[FlexrayTpPduPool]
    tp_connection: Optional[FlexrayTpConnection]
    transmitter: Optional[FlexrayTpNode]
    tx_pdu_pool: Optional[FlexrayTpPduPool]
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
    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bandwidth
        if self.bandwidth is not None:
            serialized = ARObject._serialize_item(self.bandwidth, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BANDWIDTH")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize direct_tp_sdu
        if self.direct_tp_sdu is not None:
            serialized = ARObject._serialize_item(self.direct_tp_sdu, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECT-TP-SDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize multicast
        if self.multicast is not None:
            serialized = ARObject._serialize_item(self.multicast, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize receivers (list to container "RECEIVERS")
        if self.receivers:
            wrapper = ET.Element("RECEIVERS")
            for item in self.receivers:
                serialized = ARObject._serialize_item(item, "FlexrayTpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reversed_tp_sdu
        if self.reversed_tp_sdu is not None:
            serialized = ARObject._serialize_item(self.reversed_tp_sdu, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REVERSED-TP-SDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_pdu_pool
        if self.rx_pdu_pool is not None:
            serialized = ARObject._serialize_item(self.rx_pdu_pool, "FlexrayTpPduPool")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-PDU-POOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_connection
        if self.tp_connection is not None:
            serialized = ARObject._serialize_item(self.tp_connection, "FlexrayTpConnection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-CONNECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmitter
        if self.transmitter is not None:
            serialized = ARObject._serialize_item(self.transmitter, "FlexrayTpNode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMITTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tx_pdu_pool
        if self.tx_pdu_pool is not None:
            serialized = ARObject._serialize_item(self.tx_pdu_pool, "FlexrayTpPduPool")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TX-PDU-POOL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConnection":
        """Deserialize XML element to FlexrayTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpConnection, cls).deserialize(element)

        # Parse bandwidth
        child = ARObject._find_child_element(element, "BANDWIDTH")
        if child is not None:
            bandwidth_value = child.text
            obj.bandwidth = bandwidth_value

        # Parse direct_tp_sdu
        child = ARObject._find_child_element(element, "DIRECT-TP-SDU")
        if child is not None:
            direct_tp_sdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.direct_tp_sdu = direct_tp_sdu_value

        # Parse multicast
        child = ARObject._find_child_element(element, "MULTICAST")
        if child is not None:
            multicast_value = ARObject._deserialize_by_tag(child, "TpAddress")
            obj.multicast = multicast_value

        # Parse receivers (list from container "RECEIVERS")
        obj.receivers = []
        container = ARObject._find_child_element(element, "RECEIVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.receivers.append(child_value)

        # Parse reversed_tp_sdu
        child = ARObject._find_child_element(element, "REVERSED-TP-SDU")
        if child is not None:
            reversed_tp_sdu_value = ARObject._deserialize_by_tag(child, "IPdu")
            obj.reversed_tp_sdu = reversed_tp_sdu_value

        # Parse rx_pdu_pool
        child = ARObject._find_child_element(element, "RX-PDU-POOL")
        if child is not None:
            rx_pdu_pool_value = ARObject._deserialize_by_tag(child, "FlexrayTpPduPool")
            obj.rx_pdu_pool = rx_pdu_pool_value

        # Parse tp_connection
        child = ARObject._find_child_element(element, "TP-CONNECTION")
        if child is not None:
            tp_connection_value = ARObject._deserialize_by_tag(child, "FlexrayTpConnection")
            obj.tp_connection = tp_connection_value

        # Parse transmitter
        child = ARObject._find_child_element(element, "TRANSMITTER")
        if child is not None:
            transmitter_value = ARObject._deserialize_by_tag(child, "FlexrayTpNode")
            obj.transmitter = transmitter_value

        # Parse tx_pdu_pool
        child = ARObject._find_child_element(element, "TX-PDU-POOL")
        if child is not None:
            tx_pdu_pool_value = ARObject._deserialize_by_tag(child, "FlexrayTpPduPool")
            obj.tx_pdu_pool = tx_pdu_pool_value

        return obj



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
