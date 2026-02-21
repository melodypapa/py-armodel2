"""SocketAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 452)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    UdpChecksumCalculationEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_list import (
    IPv6ExtHeaderFilterList,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
        StaticSocketConnection,
    )



class SocketAddress(Identifiable):
    """AUTOSAR SocketAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    allowed_i_pv6_ext_ref: Optional[ARRef]
    allowed_tcp_ref: Optional[ARRef]
    application_endpoint_endpoint: Optional[ApplicationEndpoint]
    connector_ref: Optional[Any]
    differentiated: Optional[PositiveInteger]
    flow_label: Optional[PositiveInteger]
    multicast_refs: list[Any]
    path_mtu: Optional[Boolean]
    pdu_collection: Optional[TimeValue]
    static_sockets: list[StaticSocketConnection]
    udp_checksum: Optional[UdpChecksumCalculationEnum]
    def __init__(self) -> None:
        """Initialize SocketAddress."""
        super().__init__()
        self.allowed_i_pv6_ext_ref: Optional[ARRef] = None
        self.allowed_tcp_ref: Optional[ARRef] = None
        self.application_endpoint_endpoint: Optional[ApplicationEndpoint] = None
        self.connector_ref: Optional[Any] = None
        self.differentiated: Optional[PositiveInteger] = None
        self.flow_label: Optional[PositiveInteger] = None
        self.multicast_refs: list[Any] = []
        self.path_mtu: Optional[Boolean] = None
        self.pdu_collection: Optional[TimeValue] = None
        self.static_sockets: list[StaticSocketConnection] = []
        self.udp_checksum: Optional[UdpChecksumCalculationEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize SocketAddress to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SocketAddress, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_i_pv6_ext_ref
        if self.allowed_i_pv6_ext_ref is not None:
            serialized = SerializationHelper.serialize_item(self.allowed_i_pv6_ext_ref, "IPv6ExtHeaderFilterList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOWED-I-PV6-EXT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize allowed_tcp_ref
        if self.allowed_tcp_ref is not None:
            serialized = SerializationHelper.serialize_item(self.allowed_tcp_ref, "TcpOptionFilterList")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALLOWED-TCP-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize application_endpoint_endpoint
        if self.application_endpoint_endpoint is not None:
            serialized = SerializationHelper.serialize_item(self.application_endpoint_endpoint, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION-ENDPOINT-ENDPOINT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize connector_ref
        if self.connector_ref is not None:
            serialized = SerializationHelper.serialize_item(self.connector_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize differentiated
        if self.differentiated is not None:
            serialized = SerializationHelper.serialize_item(self.differentiated, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIFFERENTIATED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize flow_label
        if self.flow_label is not None:
            serialized = SerializationHelper.serialize_item(self.flow_label, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FLOW-LABEL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize multicast_refs (list to container "MULTICAST-REFS")
        if self.multicast_refs:
            wrapper = ET.Element("MULTICAST-REFS")
            for item in self.multicast_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("MULTICAST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize path_mtu
        if self.path_mtu is not None:
            serialized = SerializationHelper.serialize_item(self.path_mtu, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATH-MTU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize pdu_collection
        if self.pdu_collection is not None:
            serialized = SerializationHelper.serialize_item(self.pdu_collection, "TimeValue")
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

        # Serialize static_sockets (list to container "STATIC-SOCKETS")
        if self.static_sockets:
            wrapper = ET.Element("STATIC-SOCKETS")
            for item in self.static_sockets:
                serialized = SerializationHelper.serialize_item(item, "StaticSocketConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize udp_checksum
        if self.udp_checksum is not None:
            serialized = SerializationHelper.serialize_item(self.udp_checksum, "UdpChecksumCalculationEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDP-CHECKSUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SocketAddress":
        """Deserialize XML element to SocketAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SocketAddress object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SocketAddress, cls).deserialize(element)

        # Parse allowed_i_pv6_ext_ref
        child = SerializationHelper.find_child_element(element, "ALLOWED-I-PV6-EXT-REF")
        if child is not None:
            allowed_i_pv6_ext_ref_value = ARRef.deserialize(child)
            obj.allowed_i_pv6_ext_ref = allowed_i_pv6_ext_ref_value

        # Parse allowed_tcp_ref
        child = SerializationHelper.find_child_element(element, "ALLOWED-TCP-REF")
        if child is not None:
            allowed_tcp_ref_value = ARRef.deserialize(child)
            obj.allowed_tcp_ref = allowed_tcp_ref_value

        # Parse application_endpoint_endpoint
        child = SerializationHelper.find_child_element(element, "APPLICATION-ENDPOINT-ENDPOINT")
        if child is not None:
            application_endpoint_endpoint_value = SerializationHelper.deserialize_by_tag(child, "ApplicationEndpoint")
            obj.application_endpoint_endpoint = application_endpoint_endpoint_value

        # Parse connector_ref
        child = SerializationHelper.find_child_element(element, "CONNECTOR-REF")
        if child is not None:
            connector_ref_value = ARRef.deserialize(child)
            obj.connector_ref = connector_ref_value

        # Parse differentiated
        child = SerializationHelper.find_child_element(element, "DIFFERENTIATED")
        if child is not None:
            differentiated_value = child.text
            obj.differentiated = differentiated_value

        # Parse flow_label
        child = SerializationHelper.find_child_element(element, "FLOW-LABEL")
        if child is not None:
            flow_label_value = child.text
            obj.flow_label = flow_label_value

        # Parse multicast_refs (list from container "MULTICAST-REFS")
        obj.multicast_refs = []
        container = SerializationHelper.find_child_element(element, "MULTICAST-REFS")
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
                    obj.multicast_refs.append(child_value)

        # Parse path_mtu
        child = SerializationHelper.find_child_element(element, "PATH-MTU")
        if child is not None:
            path_mtu_value = child.text
            obj.path_mtu = path_mtu_value

        # Parse pdu_collection
        child = SerializationHelper.find_child_element(element, "PDU-COLLECTION")
        if child is not None:
            pdu_collection_value = child.text
            obj.pdu_collection = pdu_collection_value

        # Parse static_sockets (list from container "STATIC-SOCKETS")
        obj.static_sockets = []
        container = SerializationHelper.find_child_element(element, "STATIC-SOCKETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.static_sockets.append(child_value)

        # Parse udp_checksum
        child = SerializationHelper.find_child_element(element, "UDP-CHECKSUM")
        if child is not None:
            udp_checksum_value = UdpChecksumCalculationEnum.deserialize(child)
            obj.udp_checksum = udp_checksum_value

        return obj



class SocketAddressBuilder:
    """Builder for SocketAddress."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SocketAddress = SocketAddress()

    def build(self) -> SocketAddress:
        """Build and return SocketAddress object.

        Returns:
            SocketAddress instance
        """
        # TODO: Add validation
        return self._obj
