"""SocketConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2057)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ObsoleteModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.describable import (
    Describable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    Identifier,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_connection_ipdu_identifier_set import (
    SocketConnectionIpduIdentifierSet,
)


class SocketConnection(Describable):
    """AUTOSAR SocketConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    client_ip_addr: Optional[Boolean]
    client_port: Optional[SocketAddress]
    client_port_from: Optional[Boolean]
    pdus: list[SocketConnectionIpduIdentifierSet]
    pdu_collection: Optional[TimeValue]
    runtime_ip: Optional[Any]
    runtime_port: Optional[Any]
    short_label: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize SocketConnection."""
        super().__init__()
        self.client_ip_addr: Optional[Boolean] = None
        self.client_port: Optional[SocketAddress] = None
        self.client_port_from: Optional[Boolean] = None
        self.pdus: list[SocketConnectionIpduIdentifierSet] = []
        self.pdu_collection: Optional[TimeValue] = None
        self.runtime_ip: Optional[Any] = None
        self.runtime_port: Optional[Any] = None
        self.short_label: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize SocketConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SocketConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize client_ip_addr
        if self.client_ip_addr is not None:
            serialized = ARObject._serialize_item(self.client_ip_addr, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-IP-ADDR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize client_port
        if self.client_port is not None:
            serialized = ARObject._serialize_item(self.client_port, "SocketAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize client_port_from
        if self.client_port_from is not None:
            serialized = ARObject._serialize_item(self.client_port_from, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CLIENT-PORT-FROM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdus (list to container "PDUS")
        if self.pdus:
            wrapper = ET.Element("PDUS")
            for item in self.pdus:
                serialized = ARObject._serialize_item(item, "SocketConnectionIpduIdentifierSet")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize pdu_collection
        if self.pdu_collection is not None:
            serialized = ARObject._serialize_item(self.pdu_collection, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PDU-COLLECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runtime_ip
        if self.runtime_ip is not None:
            serialized = ARObject._serialize_item(self.runtime_ip, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RUNTIME-IP")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize runtime_port
        if self.runtime_port is not None:
            serialized = ARObject._serialize_item(self.runtime_port, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RUNTIME-PORT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize short_label
        if self.short_label is not None:
            serialized = ARObject._serialize_item(self.short_label, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SHORT-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketConnection":
        """Deserialize XML element to SocketConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SocketConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SocketConnection, cls).deserialize(element)

        # Parse client_ip_addr
        child = ARObject._find_child_element(element, "CLIENT-IP-ADDR")
        if child is not None:
            client_ip_addr_value = child.text
            obj.client_ip_addr = client_ip_addr_value

        # Parse client_port
        child = ARObject._find_child_element(element, "CLIENT-PORT")
        if child is not None:
            client_port_value = ARObject._deserialize_by_tag(child, "SocketAddress")
            obj.client_port = client_port_value

        # Parse client_port_from
        child = ARObject._find_child_element(element, "CLIENT-PORT-FROM")
        if child is not None:
            client_port_from_value = child.text
            obj.client_port_from = client_port_from_value

        # Parse pdus (list from container "PDUS")
        obj.pdus = []
        container = ARObject._find_child_element(element, "PDUS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.pdus.append(child_value)

        # Parse pdu_collection
        child = ARObject._find_child_element(element, "PDU-COLLECTION")
        if child is not None:
            pdu_collection_value = child.text
            obj.pdu_collection = pdu_collection_value

        # Parse runtime_ip
        child = ARObject._find_child_element(element, "RUNTIME-IP")
        if child is not None:
            runtime_ip_value = child.text
            obj.runtime_ip = runtime_ip_value

        # Parse runtime_port
        child = ARObject._find_child_element(element, "RUNTIME-PORT")
        if child is not None:
            runtime_port_value = child.text
            obj.runtime_port = runtime_port_value

        # Parse short_label
        child = ARObject._find_child_element(element, "SHORT-LABEL")
        if child is not None:
            short_label_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.short_label = short_label_value

        return obj



class SocketConnectionBuilder:
    """Builder for SocketConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketConnection = SocketConnection()

    def build(self) -> SocketConnection:
        """Build and return SocketConnection object.

        Returns:
            SocketConnection instance
        """
        # TODO: Add validation
        return self._obj
