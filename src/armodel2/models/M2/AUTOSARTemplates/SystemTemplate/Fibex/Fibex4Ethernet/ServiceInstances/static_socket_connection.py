"""StaticSocketConnection AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 543)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    TcpRoleEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_con_i_pdu_identifier import (
    SoConIPduIdentifier,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
        SocketAddress,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class StaticSocketConnection(Identifiable):
    """AUTOSAR StaticSocketConnection."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STATIC-SOCKET-CONNECTION"


    i_pdu_identifier_refs: list[ARRef]
    remote_address_ref: Optional[ARRef]
    tcp_connect: Optional[TimeValue]
    tcp_role: Optional[TcpRoleEnum]
    _DESERIALIZE_DISPATCH = {
        "I-PDU-IDENTIFIER-REFS": lambda obj, elem: [obj.i_pdu_identifier_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "REMOTE-ADDRESS-REF": lambda obj, elem: setattr(obj, "remote_address_ref", ARRef.deserialize(elem)),
        "TCP-CONNECT": lambda obj, elem: setattr(obj, "tcp_connect", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "TCP-ROLE": lambda obj, elem: setattr(obj, "tcp_role", TcpRoleEnum.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "I-PDU-IDENTIFIER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.i_pdu_identifier_refs.append(ARRef.deserialize(item_elem))
            elif tag == "REMOTE-ADDRESS-REF":
                setattr(obj, "remote_address_ref", ARRef.deserialize(child))
            elif tag == "TCP-CONNECT":
                setattr(obj, "tcp_connect", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "TCP-ROLE":
                setattr(obj, "tcp_role", TcpRoleEnum.deserialize(child))

        return obj



class StaticSocketConnectionBuilder(IdentifiableBuilder):
    """Builder for StaticSocketConnection with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StaticSocketConnection = StaticSocketConnection()


    def with_i_pdu_identifiers(self, items: list[SoConIPduIdentifier]) -> "StaticSocketConnectionBuilder":
        """Set i_pdu_identifiers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers = list(items) if items else []
        return self

    def with_remote_address(self, value: Optional[SocketAddress]) -> "StaticSocketConnectionBuilder":
        """Set remote_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'remote_address' is required and cannot be None")
        self._obj.remote_address = value
        return self

    def with_tcp_connect(self, value: Optional[TimeValue]) -> "StaticSocketConnectionBuilder":
        """Set tcp_connect attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_connect' is required and cannot be None")
        self._obj.tcp_connect = value
        return self

    def with_tcp_role(self, value: Optional[TcpRoleEnum]) -> "StaticSocketConnectionBuilder":
        """Set tcp_role attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'tcp_role' is required and cannot be None")
        self._obj.tcp_role = value
        return self


    def add_i_pdu_identifier(self, item: SoConIPduIdentifier) -> "StaticSocketConnectionBuilder":
        """Add a single item to i_pdu_identifiers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers.append(item)
        return self

    def clear_i_pdu_identifiers(self) -> "StaticSocketConnectionBuilder":
        """Clear all items from i_pdu_identifiers list.

        Returns:
            self for method chaining
        """
        self._obj.i_pdu_identifiers = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "iPduIdentifier",
        "remoteAddress",
        "tcpConnect",
        "tcpRole",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> StaticSocketConnection:
        """Build and return the StaticSocketConnection instance with validation."""
        self._validate_instance()
        return self._obj