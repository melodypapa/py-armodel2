"""SomeipTpConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 620)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreCommunication.pdu_triggering import (
    PduTriggering,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
    SomeipTpChannel,
)


class SomeipTpConnection(ARObject):
    """AUTOSAR SomeipTpConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_channel_ref: Optional[ARRef]
    tp_sdu_ref: Optional[ARRef]
    transport_pdu_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SomeipTpConnection."""
        super().__init__()
        self.tp_channel_ref: Optional[ARRef] = None
        self.tp_sdu_ref: Optional[ARRef] = None
        self.transport_pdu_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SomeipTpConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipTpConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_channel_ref
        if self.tp_channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_channel_ref, "SomeipTpChannel")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_sdu_ref
        if self.tp_sdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tp_sdu_ref, "PduTriggering")
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

        # Serialize transport_pdu_ref
        if self.transport_pdu_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transport_pdu_ref, "PduTriggering")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSPORT-PDU-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpConnection":
        """Deserialize XML element to SomeipTpConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipTpConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipTpConnection, cls).deserialize(element)

        # Parse tp_channel_ref
        child = SerializationHelper.find_child_element(element, "TP-CHANNEL-REF")
        if child is not None:
            tp_channel_ref_value = ARRef.deserialize(child)
            obj.tp_channel_ref = tp_channel_ref_value

        # Parse tp_sdu_ref
        child = SerializationHelper.find_child_element(element, "TP-SDU-REF")
        if child is not None:
            tp_sdu_ref_value = ARRef.deserialize(child)
            obj.tp_sdu_ref = tp_sdu_ref_value

        # Parse transport_pdu_ref
        child = SerializationHelper.find_child_element(element, "TRANSPORT-PDU-REF")
        if child is not None:
            transport_pdu_ref_value = ARRef.deserialize(child)
            obj.transport_pdu_ref = transport_pdu_ref_value

        return obj



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
