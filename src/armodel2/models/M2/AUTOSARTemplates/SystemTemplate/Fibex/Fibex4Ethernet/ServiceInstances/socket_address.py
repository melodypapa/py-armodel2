"""SocketAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 452)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances import (
    UdpChecksumCalculationEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.IPv6HeaderFilterList.i_pv6_ext_header_filter_list import (
    IPv6ExtHeaderFilterList,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.TcpOptionFilterSet.tcp_option_filter_list import (
    TcpOptionFilterList,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
        StaticSocketConnection,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SocketAddress(Identifiable):
    """AUTOSAR SocketAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SOCKET-ADDRESS"


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
    _DESERIALIZE_DISPATCH = {
        "ALLOWED-I-PV6-EXT-REF": lambda obj, elem: setattr(obj, "allowed_i_pv6_ext_ref", ARRef.deserialize(elem)),
        "ALLOWED-TCP-REF": lambda obj, elem: setattr(obj, "allowed_tcp_ref", ARRef.deserialize(elem)),
        "APPLICATION-ENDPOINT-ENDPOINT": lambda obj, elem: setattr(obj, "application_endpoint_endpoint", SerializationHelper.deserialize_by_tag(elem, "ApplicationEndpoint")),
        "CONNECTOR-REF": lambda obj, elem: setattr(obj, "connector_ref", ARRef.deserialize(elem)),
        "DIFFERENTIATED": lambda obj, elem: setattr(obj, "differentiated", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "FLOW-LABEL": lambda obj, elem: setattr(obj, "flow_label", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "MULTICASTS": lambda obj, elem: obj.multicast_refs.append(ARRef.deserialize(elem)),
        "PATH-MTU": lambda obj, elem: setattr(obj, "path_mtu", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "PDU-COLLECTION": lambda obj, elem: setattr(obj, "pdu_collection", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "STATIC-SOCKETS": lambda obj, elem: obj.static_sockets.append(SerializationHelper.deserialize_by_tag(elem, "StaticSocketConnection")),
        "UDP-CHECKSUM": lambda obj, elem: setattr(obj, "udp_checksum", UdpChecksumCalculationEnum.deserialize(elem)),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ALLOWED-I-PV6-EXT-REF":
                setattr(obj, "allowed_i_pv6_ext_ref", ARRef.deserialize(child))
            elif tag == "ALLOWED-TCP-REF":
                setattr(obj, "allowed_tcp_ref", ARRef.deserialize(child))
            elif tag == "APPLICATION-ENDPOINT-ENDPOINT":
                setattr(obj, "application_endpoint_endpoint", SerializationHelper.deserialize_by_tag(child, "ApplicationEndpoint"))
            elif tag == "CONNECTOR-REF":
                setattr(obj, "connector_ref", ARRef.deserialize(child))
            elif tag == "DIFFERENTIATED":
                setattr(obj, "differentiated", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "FLOW-LABEL":
                setattr(obj, "flow_label", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "MULTICASTS":
                obj.multicast_refs.append(ARRef.deserialize(child))
            elif tag == "PATH-MTU":
                setattr(obj, "path_mtu", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "PDU-COLLECTION":
                setattr(obj, "pdu_collection", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "STATIC-SOCKETS":
                obj.static_sockets.append(SerializationHelper.deserialize_by_tag(child, "StaticSocketConnection"))
            elif tag == "UDP-CHECKSUM":
                setattr(obj, "udp_checksum", UdpChecksumCalculationEnum.deserialize(child))

        return obj



class SocketAddressBuilder(IdentifiableBuilder):
    """Builder for SocketAddress with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SocketAddress = SocketAddress()


    def with_allowed_i_pv6_ext(self, value: Optional[IPv6ExtHeaderFilterList]) -> "SocketAddressBuilder":
        """Set allowed_i_pv6_ext attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.allowed_i_pv6_ext = value
        return self

    def with_allowed_tcp(self, value: Optional[TcpOptionFilterList]) -> "SocketAddressBuilder":
        """Set allowed_tcp attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.allowed_tcp = value
        return self

    def with_application_endpoint_endpoint(self, value: Optional[ApplicationEndpoint]) -> "SocketAddressBuilder":
        """Set application_endpoint_endpoint attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.application_endpoint_endpoint = value
        return self

    def with_connector(self, value: Optional[any (EthernetCommunication)]) -> "SocketAddressBuilder":
        """Set connector attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.connector = value
        return self

    def with_differentiated(self, value: Optional[PositiveInteger]) -> "SocketAddressBuilder":
        """Set differentiated attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.differentiated = value
        return self

    def with_flow_label(self, value: Optional[PositiveInteger]) -> "SocketAddressBuilder":
        """Set flow_label attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.flow_label = value
        return self

    def with_multicasts(self, items: list[any (EthernetCommunication)]) -> "SocketAddressBuilder":
        """Set multicasts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.multicasts = list(items) if items else []
        return self

    def with_path_mtu(self, value: Optional[Boolean]) -> "SocketAddressBuilder":
        """Set path_mtu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.path_mtu = value
        return self

    def with_pdu_collection(self, value: Optional[TimeValue]) -> "SocketAddressBuilder":
        """Set pdu_collection attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.pdu_collection = value
        return self

    def with_static_sockets(self, items: list[StaticSocketConnection]) -> "SocketAddressBuilder":
        """Set static_sockets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.static_sockets = list(items) if items else []
        return self

    def with_udp_checksum(self, value: Optional[UdpChecksumCalculationEnum]) -> "SocketAddressBuilder":
        """Set udp_checksum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.udp_checksum = value
        return self


    def add_multicast(self, item: any (EthernetCommunication)) -> "SocketAddressBuilder":
        """Add a single item to multicasts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.multicasts.append(item)
        return self

    def clear_multicasts(self) -> "SocketAddressBuilder":
        """Clear all items from multicasts list.

        Returns:
            self for method chaining
        """
        self._obj.multicasts = []
        return self

    def add_static_socket(self, item: StaticSocketConnection) -> "SocketAddressBuilder":
        """Add a single item to static_sockets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.static_sockets.append(item)
        return self

    def clear_static_sockets(self) -> "SocketAddressBuilder":
        """Clear all items from static_sockets list.

        Returns:
            self for method chaining
        """
        self._obj.static_sockets = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> SocketAddress:
        """Build and return the SocketAddress instance with validation."""
        self._validate_instance()
        pass
        return self._obj