"""CanTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 608)

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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols import (
    CanTpAddressingFormatType,
    NetworkTargetAddressType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Integer,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_address import (
    CanTpAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_channel import (
    CanTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.can_tp_node import (
    CanTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)


class CanTpConnection(TpConnection):
    """AUTOSAR CanTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    addressing: Optional[CanTpAddressingFormatType]
    cancellation: Optional[Boolean]
    can_tp_channel_ref: Optional[ARRef]
    data_pdu_ref: Optional[ARRef]
    flow_control_pdu_ref: Optional[ARRef]
    max_block_size: Optional[Integer]
    multicast_ref: Optional[ARRef]
    padding: Optional[Boolean]
    receiver_refs: list[ARRef]
    ta_type_type: Optional[NetworkTargetAddressType]
    timeout_br: Optional[TimeValue]
    timeout_bs: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    timeout_cs: Optional[TimeValue]
    tp_sdu_ref: Optional[ARRef]
    transmitter_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize CanTpConnection."""
        super().__init__()
        self.addressing: Optional[CanTpAddressingFormatType] = None
        self.cancellation: Optional[Boolean] = None
        self.can_tp_channel_ref: Optional[ARRef] = None
        self.data_pdu_ref: Optional[ARRef] = None
        self.flow_control_pdu_ref: Optional[ARRef] = None
        self.max_block_size: Optional[Integer] = None
        self.multicast_ref: Optional[ARRef] = None
        self.padding: Optional[Boolean] = None
        self.receiver_refs: list[ARRef] = []
        self.ta_type_type: Optional[NetworkTargetAddressType] = None
        self.timeout_br: Optional[TimeValue] = None
        self.timeout_bs: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.timeout_cs: Optional[TimeValue] = None
        self.tp_sdu_ref: Optional[ARRef] = None
        self.transmitter_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize CanTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CanTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize addressing
        if self.addressing is not None:
            serialized = SerializationHelper.serialize_item(self.addressing, "CanTpAddressingFormatType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDRESSING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize cancellation
        if self.cancellation is not None:
            serialized = SerializationHelper.serialize_item(self.cancellation, "Boolean")
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

        # Serialize can_tp_channel_ref
        if self.can_tp_channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.can_tp_channel_ref, "CanTpChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAN-TP-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize data_pdu_ref
        if self.data_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_pdu_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flow_control_pdu_ref
        if self.flow_control_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flow_control_pdu_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOW-CONTROL-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_block_size
        if self.max_block_size is not None:
            serialized = SerializationHelper.serialize_item(self.max_block_size, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-BLOCK-SIZE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize multicast_ref
        if self.multicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.multicast_ref, "CanTpAddress")
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

        # Serialize padding
        if self.padding is not None:
            serialized = SerializationHelper.serialize_item(self.padding, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PADDING")
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
                serialized = SerializationHelper.serialize_item(item, "CanTpNode")
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

        # Serialize ta_type_type
        if self.ta_type_type is not None:
            serialized = SerializationHelper.serialize_item(self.ta_type_type, "NetworkTargetAddressType")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TA-TYPE-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_br
        if self.timeout_br is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_br, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-BR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_bs
        if self.timeout_bs is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_bs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-BS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_cr
        if self.timeout_cr is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_cr, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-CR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize timeout_cs
        if self.timeout_cs is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_cs, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-CS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_sdu_ref
        if self.tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-SDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transmitter_ref
        if self.transmitter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transmitter_ref, "CanTpNode")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CanTpConnection":
        """Deserialize XML element to CanTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CanTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CanTpConnection, cls).deserialize(element)

        # Parse addressing
        child = SerializationHelper.find_child_element(element, "ADDRESSING")
        if child is not None:
            addressing_value = CanTpAddressingFormatType.deserialize(child)
            obj.addressing = addressing_value

        # Parse cancellation
        child = SerializationHelper.find_child_element(element, "CANCELLATION")
        if child is not None:
            cancellation_value = child.text
            obj.cancellation = cancellation_value

        # Parse can_tp_channel_ref
        child = SerializationHelper.find_child_element(element, "CAN-TP-CHANNEL-REF")
        if child is not None:
            can_tp_channel_ref_value = ARRef.deserialize(child)
            obj.can_tp_channel_ref = can_tp_channel_ref_value

        # Parse data_pdu_ref
        child = SerializationHelper.find_child_element(element, "DATA-PDU-REF")
        if child is not None:
            data_pdu_ref_value = ARRef.deserialize(child)
            obj.data_pdu_ref = data_pdu_ref_value

        # Parse flow_control_pdu_ref
        child = SerializationHelper.find_child_element(element, "FLOW-CONTROL-PDU-REF")
        if child is not None:
            flow_control_pdu_ref_value = ARRef.deserialize(child)
            obj.flow_control_pdu_ref = flow_control_pdu_ref_value

        # Parse max_block_size
        child = SerializationHelper.find_child_element(element, "MAX-BLOCK-SIZE")
        if child is not None:
            max_block_size_value = child.text
            obj.max_block_size = max_block_size_value

        # Parse multicast_ref
        child = SerializationHelper.find_child_element(element, "MULTICAST-REF")
        if child is not None:
            multicast_ref_value = ARRef.deserialize(child)
            obj.multicast_ref = multicast_ref_value

        # Parse padding
        child = SerializationHelper.find_child_element(element, "PADDING")
        if child is not None:
            padding_value = child.text
            obj.padding = padding_value

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

        # Parse ta_type_type
        child = SerializationHelper.find_child_element(element, "TA-TYPE-TYPE")
        if child is not None:
            ta_type_type_value = NetworkTargetAddressType.deserialize(child)
            obj.ta_type_type = ta_type_type_value

        # Parse timeout_br
        child = SerializationHelper.find_child_element(element, "TIMEOUT-BR")
        if child is not None:
            timeout_br_value = child.text
            obj.timeout_br = timeout_br_value

        # Parse timeout_bs
        child = SerializationHelper.find_child_element(element, "TIMEOUT-BS")
        if child is not None:
            timeout_bs_value = child.text
            obj.timeout_bs = timeout_bs_value

        # Parse timeout_cr
        child = SerializationHelper.find_child_element(element, "TIMEOUT-CR")
        if child is not None:
            timeout_cr_value = child.text
            obj.timeout_cr = timeout_cr_value

        # Parse timeout_cs
        child = SerializationHelper.find_child_element(element, "TIMEOUT-CS")
        if child is not None:
            timeout_cs_value = child.text
            obj.timeout_cs = timeout_cs_value

        # Parse tp_sdu_ref
        child = SerializationHelper.find_child_element(element, "TP-SDU-REF")
        if child is not None:
            tp_sdu_ref_value = ARRef.deserialize(child)
            obj.tp_sdu_ref = tp_sdu_ref_value

        # Parse transmitter_ref
        child = SerializationHelper.find_child_element(element, "TRANSMITTER-REF")
        if child is not None:
            transmitter_ref_value = ARRef.deserialize(child)
            obj.transmitter_ref = transmitter_ref_value

        return obj



class CanTpConnectionBuilder:
    """Builder for CanTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CanTpConnection = CanTpConnection()

    def build(self) -> CanTpConnection:
        """Build and return CanTpConnection object.

        Returns:
            CanTpConnection instance
        """
        # TODO: Add validation
        return self._obj
