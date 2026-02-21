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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    direct_tp_sdu_ref: Optional[ARRef]
    multicast_ref: Optional[ARRef]
    receiver_refs: list[ARRef]
    reversed_tp_sdu_ref: Optional[ARRef]
    rx_pdu_pool_ref: Optional[ARRef]
    tp_connection_ref: Optional[ARRef]
    transmitter_ref: Optional[ARRef]
    tx_pdu_pool_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize FlexrayTpConnection."""
        super().__init__()
        self.bandwidth: Optional[Boolean] = None
        self.direct_tp_sdu_ref: Optional[ARRef] = None
        self.multicast_ref: Optional[ARRef] = None
        self.receiver_refs: list[ARRef] = []
        self.reversed_tp_sdu_ref: Optional[ARRef] = None
        self.rx_pdu_pool_ref: Optional[ARRef] = None
        self.tp_connection_ref: Optional[ARRef] = None
        self.transmitter_ref: Optional[ARRef] = None
        self.tx_pdu_pool_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bandwidth
        if self.bandwidth is not None:
            serialized = SerializationHelper.serialize_item(self.bandwidth, "Boolean")
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

        # Serialize direct_tp_sdu_ref
        if self.direct_tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.direct_tp_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECT-TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize multicast_ref
        if self.multicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.multicast_ref, "TpAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MULTICAST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize receiver_refs (list to container "RECEIVER-REFS")
        if self.receiver_refs:
            wrapper = ET.Element("RECEIVER-REFS")
            for item in self.receiver_refs:
                serialized = SerializationHelper.serialize_item(item, "FlexrayTpNode")
                if serialized is not None:
                    child_elem = ET.Element("RECEIVER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize reversed_tp_sdu_ref
        if self.reversed_tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.reversed_tp_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REVERSED-TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rx_pdu_pool_ref
        if self.rx_pdu_pool_ref is not None:
            serialized = SerializationHelper.serialize_item(self.rx_pdu_pool_ref, "FlexrayTpPduPool")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RX-PDU-POOL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_connection_ref
        if self.tp_connection_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_connection_ref, "FlexrayTpConnection")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-CONNECTION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmitter_ref
        if self.transmitter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transmitter_ref, "FlexrayTpNode")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSMITTER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tx_pdu_pool_ref
        if self.tx_pdu_pool_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tx_pdu_pool_ref, "FlexrayTpPduPool")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TX-PDU-POOL-REF")
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
        child = SerializationHelper.find_child_element(element, "BANDWIDTH")
        if child is not None:
            bandwidth_value = child.text
            obj.bandwidth = bandwidth_value

        # Parse direct_tp_sdu_ref
        child = SerializationHelper.find_child_element(element, "DIRECT-TP-SDU-REF")
        if child is not None:
            direct_tp_sdu_ref_value = ARRef.deserialize(child)
            obj.direct_tp_sdu_ref = direct_tp_sdu_ref_value

        # Parse multicast_ref
        child = SerializationHelper.find_child_element(element, "MULTICAST-REF")
        if child is not None:
            multicast_ref_value = ARRef.deserialize(child)
            obj.multicast_ref = multicast_ref_value

        # Parse receiver_refs (list from container "RECEIVER-REFS")
        obj.receiver_refs = []
        container = SerializationHelper.find_child_element(element, "RECEIVER-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.receiver_refs.append(child_value)

        # Parse reversed_tp_sdu_ref
        child = SerializationHelper.find_child_element(element, "REVERSED-TP-SDU-REF")
        if child is not None:
            reversed_tp_sdu_ref_value = ARRef.deserialize(child)
            obj.reversed_tp_sdu_ref = reversed_tp_sdu_ref_value

        # Parse rx_pdu_pool_ref
        child = SerializationHelper.find_child_element(element, "RX-PDU-POOL-REF")
        if child is not None:
            rx_pdu_pool_ref_value = ARRef.deserialize(child)
            obj.rx_pdu_pool_ref = rx_pdu_pool_ref_value

        # Parse tp_connection_ref
        child = SerializationHelper.find_child_element(element, "TP-CONNECTION-REF")
        if child is not None:
            tp_connection_ref_value = ARRef.deserialize(child)
            obj.tp_connection_ref = tp_connection_ref_value

        # Parse transmitter_ref
        child = SerializationHelper.find_child_element(element, "TRANSMITTER-REF")
        if child is not None:
            transmitter_ref_value = ARRef.deserialize(child)
            obj.transmitter_ref = transmitter_ref_value

        # Parse tx_pdu_pool_ref
        child = SerializationHelper.find_child_element(element, "TX-PDU-POOL-REF")
        if child is not None:
            tx_pdu_pool_ref_value = ARRef.deserialize(child)
            obj.tx_pdu_pool_ref = tx_pdu_pool_ref_value

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
