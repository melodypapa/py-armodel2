"""StaticSocketConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 543)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    TcpRoleEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
        SocketAddress,
    )



class StaticSocketConnection(Identifiable):
    """AUTOSAR StaticSocketConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    i_pdu_identifier_refs: list[ARRef]
    remote_address_ref: Optional[ARRef]
    tcp_connect: Optional[TimeValue]
    tcp_role: Optional[TcpRoleEnum]
    def __init__(self) -> None:
        """Initialize StaticSocketConnection."""
        super().__init__()
        self.i_pdu_identifier_refs: list[ARRef] = []
        self.remote_address_ref: Optional[ARRef] = None
        self.tcp_connect: Optional[TimeValue] = None
        self.tcp_role: Optional[TcpRoleEnum] = None

    def serialize(self) -> ET.Element:
        """Serialize StaticSocketConnection to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StaticSocketConnection, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize i_pdu_identifier_refs (list to container "I-PDU-IDENTIFIER-REFS")
        if self.i_pdu_identifier_refs:
            wrapper = ET.Element("I-PDU-IDENTIFIER-REFS")
            for item in self.i_pdu_identifier_refs:
                serialized = SerializationHelper.serialize_item(item, "SoConIPduIdentifier")
                if serialized is not None:
                    child_elem = ET.Element("I-PDU-IDENTIFIER-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize remote_address_ref
        if self.remote_address_ref is not None:
            serialized = SerializationHelper.serialize_item(self.remote_address_ref, "SocketAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMOTE-ADDRESS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_connect
        if self.tcp_connect is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_connect, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-CONNECT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tcp_role
        if self.tcp_role is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_role, "TcpRoleEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StaticSocketConnection":
        """Deserialize XML element to StaticSocketConnection object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StaticSocketConnection object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StaticSocketConnection, cls).deserialize(element)

        # Parse i_pdu_identifier_refs (list from container "I-PDU-IDENTIFIER-REFS")
        obj.i_pdu_identifier_refs = []
        container = SerializationHelper.find_child_element(element, "I-PDU-IDENTIFIER-REFS")
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
                    obj.i_pdu_identifier_refs.append(child_value)

        # Parse remote_address_ref
        child = SerializationHelper.find_child_element(element, "REMOTE-ADDRESS-REF")
        if child is not None:
            remote_address_ref_value = ARRef.deserialize(child)
            obj.remote_address_ref = remote_address_ref_value

        # Parse tcp_connect
        child = SerializationHelper.find_child_element(element, "TCP-CONNECT")
        if child is not None:
            tcp_connect_value = child.text
            obj.tcp_connect = tcp_connect_value

        # Parse tcp_role
        child = SerializationHelper.find_child_element(element, "TCP-ROLE")
        if child is not None:
            tcp_role_value = TcpRoleEnum.deserialize(child)
            obj.tcp_role = tcp_role_value

        return obj



class StaticSocketConnectionBuilder:
    """Builder for StaticSocketConnection."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: StaticSocketConnection = StaticSocketConnection()

    def build(self) -> StaticSocketConnection:
        """Build and return StaticSocketConnection object.

        Returns:
            StaticSocketConnection instance
        """
        # TODO: Add validation
        return self._obj
