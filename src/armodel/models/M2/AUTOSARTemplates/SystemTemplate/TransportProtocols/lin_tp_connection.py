"""LinTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 615)

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
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.i_pdu import (
    IPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_node import (
    LinTpNode,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.n_pdu import (
    NPdu,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)


class LinTpConnection(TpConnection):
    """AUTOSAR LinTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_pdu_ref: Optional[ARRef]
    flow_control_ref: Optional[ARRef]
    lin_tp_n_sdu_ref: Optional[ARRef]
    multicast_ref: Optional[ARRef]
    receiver_refs: list[ARRef]
    timeout_as: Optional[TimeValue]
    timeout_cr: Optional[TimeValue]
    timeout_cs: Optional[TimeValue]
    transmitter_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize LinTpConnection."""
        super().__init__()
        self.data_pdu_ref: Optional[ARRef] = None
        self.flow_control_ref: Optional[ARRef] = None
        self.lin_tp_n_sdu_ref: Optional[ARRef] = None
        self.multicast_ref: Optional[ARRef] = None
        self.receiver_refs: list[ARRef] = []
        self.timeout_as: Optional[TimeValue] = None
        self.timeout_cr: Optional[TimeValue] = None
        self.timeout_cs: Optional[TimeValue] = None
        self.transmitter_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize LinTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

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

        # Serialize flow_control_ref
        if self.flow_control_ref is not None:
            serialized = SerializationHelper.serialize_item(self.flow_control_ref, "NPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOW-CONTROL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_tp_n_sdu_ref
        if self.lin_tp_n_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.lin_tp_n_sdu_ref, "IPdu")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIN-TP-N-SDU-REF")
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
                serialized = SerializationHelper.serialize_item(item, "LinTpNode")
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

        # Serialize timeout_as
        if self.timeout_as is not None:
            serialized = SerializationHelper.serialize_item(self.timeout_as, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TIMEOUT-AS")
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

        # Serialize transmitter_ref
        if self.transmitter_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transmitter_ref, "LinTpNode")
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
    def deserialize(cls, element: ET.Element) -> "LinTpConnection":
        """Deserialize XML element to LinTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinTpConnection, cls).deserialize(element)

        # Parse data_pdu_ref
        child = SerializationHelper.find_child_element(element, "DATA-PDU-REF")
        if child is not None:
            data_pdu_ref_value = ARRef.deserialize(child)
            obj.data_pdu_ref = data_pdu_ref_value

        # Parse flow_control_ref
        child = SerializationHelper.find_child_element(element, "FLOW-CONTROL-REF")
        if child is not None:
            flow_control_ref_value = ARRef.deserialize(child)
            obj.flow_control_ref = flow_control_ref_value

        # Parse lin_tp_n_sdu_ref
        child = SerializationHelper.find_child_element(element, "LIN-TP-N-SDU-REF")
        if child is not None:
            lin_tp_n_sdu_ref_value = ARRef.deserialize(child)
            obj.lin_tp_n_sdu_ref = lin_tp_n_sdu_ref_value

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

        # Parse timeout_as
        child = SerializationHelper.find_child_element(element, "TIMEOUT-AS")
        if child is not None:
            timeout_as_value = child.text
            obj.timeout_as = timeout_as_value

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

        # Parse transmitter_ref
        child = SerializationHelper.find_child_element(element, "TRANSMITTER-REF")
        if child is not None:
            transmitter_ref_value = ARRef.deserialize(child)
            obj.transmitter_ref = transmitter_ref_value

        return obj



class LinTpConnectionBuilder:
    """Builder for LinTpConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinTpConnection = LinTpConnection()

    def build(self) -> LinTpConnection:
        """Build and return LinTpConnection object.

        Returns:
            LinTpConnection instance
        """
        # TODO: Add validation
        return self._obj
