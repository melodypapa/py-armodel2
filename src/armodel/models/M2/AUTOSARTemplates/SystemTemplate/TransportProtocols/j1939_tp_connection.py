"""J1939TpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 624)

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
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_node import (
    J1939TpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_pg import (
    J1939TpPg,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class J1939TpConnection(TpConnection):
    """AUTOSAR J1939TpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    broadcast: Optional[Boolean]
    buffer_ratio: Optional[PositiveInteger]
    cancellation: Optional[Boolean]
    data_pdu: Optional[NPdu]
    dynamic_bs: Optional[Boolean]
    flow_control_pdu: NPdu
    max_bs: Optional[PositiveInteger]
    max_exp_bs: Optional[PositiveInteger]
    receivers: list[J1939TpNode]
    retry: Optional[Boolean]
    tp_pgs: list[J1939TpPg]
    transmitter: Optional[J1939TpNode]
    def __init__(self) -> None:
        """Initialize J1939TpConnection."""
        super().__init__()
        self.broadcast: Optional[Boolean] = None
        self.buffer_ratio: Optional[PositiveInteger] = None
        self.cancellation: Optional[Boolean] = None
        self.data_pdu: Optional[NPdu] = None
        self.dynamic_bs: Optional[Boolean] = None
        self.flow_control_pdu: NPdu = None
        self.max_bs: Optional[PositiveInteger] = None
        self.max_exp_bs: Optional[PositiveInteger] = None
        self.receivers: list[J1939TpNode] = []
        self.retry: Optional[Boolean] = None
        self.tp_pgs: list[J1939TpPg] = []
        self.transmitter: Optional[J1939TpNode] = None
    def serialize(self) -> ET.Element:
        """Serialize J1939TpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939TpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize broadcast
        if self.broadcast is not None:
            serialized = ARObject._serialize_item(self.broadcast, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BROADCAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize buffer_ratio
        if self.buffer_ratio is not None:
            serialized = ARObject._serialize_item(self.buffer_ratio, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BUFFER-RATIO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cancellation
        if self.cancellation is not None:
            serialized = ARObject._serialize_item(self.cancellation, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CANCELLATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_pdu
        if self.data_pdu is not None:
            serialized = ARObject._serialize_item(self.data_pdu, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize dynamic_bs
        if self.dynamic_bs is not None:
            serialized = ARObject._serialize_item(self.dynamic_bs, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flow_control_pdu
        if self.flow_control_pdu is not None:
            serialized = ARObject._serialize_item(self.flow_control_pdu, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOW-CONTROL-PDU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_bs
        if self.max_bs is not None:
            serialized = ARObject._serialize_item(self.max_bs, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_exp_bs
        if self.max_exp_bs is not None:
            serialized = ARObject._serialize_item(self.max_exp_bs, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-EXP-BS")
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
                serialized = ARObject._serialize_item(item, "J1939TpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize retry
        if self.retry is not None:
            serialized = ARObject._serialize_item(self.retry, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RETRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_pgs (list to container "TP-PGS")
        if self.tp_pgs:
            wrapper = ET.Element("TP-PGS")
            for item in self.tp_pgs:
                serialized = ARObject._serialize_item(item, "J1939TpPg")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transmitter
        if self.transmitter is not None:
            serialized = ARObject._serialize_item(self.transmitter, "J1939TpNode")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpConnection":
        """Deserialize XML element to J1939TpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939TpConnection, cls).deserialize(element)

        # Parse broadcast
        child = ARObject._find_child_element(element, "BROADCAST")
        if child is not None:
            broadcast_value = child.text
            obj.broadcast = broadcast_value

        # Parse buffer_ratio
        child = ARObject._find_child_element(element, "BUFFER-RATIO")
        if child is not None:
            buffer_ratio_value = child.text
            obj.buffer_ratio = buffer_ratio_value

        # Parse cancellation
        child = ARObject._find_child_element(element, "CANCELLATION")
        if child is not None:
            cancellation_value = child.text
            obj.cancellation = cancellation_value

        # Parse data_pdu
        child = ARObject._find_child_element(element, "DATA-PDU")
        if child is not None:
            data_pdu_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.data_pdu = data_pdu_value

        # Parse dynamic_bs
        child = ARObject._find_child_element(element, "DYNAMIC-BS")
        if child is not None:
            dynamic_bs_value = child.text
            obj.dynamic_bs = dynamic_bs_value

        # Parse flow_control_pdu
        child = ARObject._find_child_element(element, "FLOW-CONTROL-PDU")
        if child is not None:
            flow_control_pdu_value = ARObject._deserialize_by_tag(child, "NPdu")
            obj.flow_control_pdu = flow_control_pdu_value

        # Parse max_bs
        child = ARObject._find_child_element(element, "MAX-BS")
        if child is not None:
            max_bs_value = child.text
            obj.max_bs = max_bs_value

        # Parse max_exp_bs
        child = ARObject._find_child_element(element, "MAX-EXP-BS")
        if child is not None:
            max_exp_bs_value = child.text
            obj.max_exp_bs = max_exp_bs_value

        # Parse receivers (list from container "RECEIVERS")
        obj.receivers = []
        container = ARObject._find_child_element(element, "RECEIVERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.receivers.append(child_value)

        # Parse retry
        child = ARObject._find_child_element(element, "RETRY")
        if child is not None:
            retry_value = child.text
            obj.retry = retry_value

        # Parse tp_pgs (list from container "TP-PGS")
        obj.tp_pgs = []
        container = ARObject._find_child_element(element, "TP-PGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_pgs.append(child_value)

        # Parse transmitter
        child = ARObject._find_child_element(element, "TRANSMITTER")
        if child is not None:
            transmitter_value = ARObject._deserialize_by_tag(child, "J1939TpNode")
            obj.transmitter = transmitter_value

        return obj



class J1939TpConnectionBuilder:
    """Builder for J1939TpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: J1939TpConnection = J1939TpConnection()

    def build(self) -> J1939TpConnection:
        """Build and return J1939TpConnection object.

        Returns:
            J1939TpConnection instance
        """
        # TODO: Add validation
        return self._obj
