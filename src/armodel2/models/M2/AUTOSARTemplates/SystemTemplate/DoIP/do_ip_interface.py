"""DoIpInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 551)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_routing_activation import (
    DoIpRoutingActivation,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_tp_config import (
    DoIpTpConfig,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.socket_connection import (
    SocketConnection,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.static_socket_connection import (
    StaticSocketConnection,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DoIpInterface(Identifiable):
    """AUTOSAR DoIpInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DO-IP-INTERFACE"


    alive_check: Optional[TimeValue]
    doip_channel_ref: Optional[ARRef]
    doip_connection_refs: list[ARRef]
    do_ip_routings: list[DoIpRoutingActivation]
    general_inactivity: Optional[TimeValue]
    initial_inactivity: Optional[TimeValue]
    initial_vehicle: Optional[TimeValue]
    is_activation_line: Optional[Boolean]
    max_tester: Optional[PositiveInteger]
    socket_refs: list[ARRef]
    use_mac_address: Optional[Boolean]
    use_vehicle: Optional[Boolean]
    vehicle: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "ALIVE-CHECK": lambda obj, elem: setattr(obj, "alive_check", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "DOIP-CHANNEL-REF": lambda obj, elem: setattr(obj, "doip_channel_ref", ARRef.deserialize(elem)),
        "DOIP-CONNECTION-REFS": lambda obj, elem: obj.doip_connection_refs.append(ARRef.deserialize(elem)),
        "DO-IP-ROUTINGS": lambda obj, elem: obj.do_ip_routings.append(SerializationHelper.deserialize_by_tag(elem, "DoIpRoutingActivation")),
        "GENERAL-INACTIVITY": lambda obj, elem: setattr(obj, "general_inactivity", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "INITIAL-INACTIVITY": lambda obj, elem: setattr(obj, "initial_inactivity", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "INITIAL-VEHICLE": lambda obj, elem: setattr(obj, "initial_vehicle", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
        "IS-ACTIVATION-LINE": lambda obj, elem: setattr(obj, "is_activation_line", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "MAX-TESTER": lambda obj, elem: setattr(obj, "max_tester", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "SOCKET-REFS": lambda obj, elem: obj.socket_refs.append(ARRef.deserialize(elem)),
        "USE-MAC-ADDRESS": lambda obj, elem: setattr(obj, "use_mac_address", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "USE-VEHICLE": lambda obj, elem: setattr(obj, "use_vehicle", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "VEHICLE": lambda obj, elem: setattr(obj, "vehicle", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize DoIpInterface."""
        super().__init__()
        self.alive_check: Optional[TimeValue] = None
        self.doip_channel_ref: Optional[ARRef] = None
        self.doip_connection_refs: list[ARRef] = []
        self.do_ip_routings: list[DoIpRoutingActivation] = []
        self.general_inactivity: Optional[TimeValue] = None
        self.initial_inactivity: Optional[TimeValue] = None
        self.initial_vehicle: Optional[TimeValue] = None
        self.is_activation_line: Optional[Boolean] = None
        self.max_tester: Optional[PositiveInteger] = None
        self.socket_refs: list[ARRef] = []
        self.use_mac_address: Optional[Boolean] = None
        self.use_vehicle: Optional[Boolean] = None
        self.vehicle: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize DoIpInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize alive_check
        if self.alive_check is not None:
            serialized = SerializationHelper.serialize_item(self.alive_check, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ALIVE-CHECK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize doip_channel_ref
        if self.doip_channel_ref is not None:
            serialized = SerializationHelper.serialize_item(self.doip_channel_ref, "DoIpTpConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DOIP-CHANNEL-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize doip_connection_refs (list to container "DOIP-CONNECTION-REFS")
        if self.doip_connection_refs:
            wrapper = ET.Element("DOIP-CONNECTION-REFS")
            for item in self.doip_connection_refs:
                serialized = SerializationHelper.serialize_item(item, "SocketConnection")
                if serialized is not None:
                    child_elem = ET.Element("DOIP-CONNECTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize do_ip_routings (list to container "DO-IP-ROUTINGS")
        if self.do_ip_routings:
            wrapper = ET.Element("DO-IP-ROUTINGS")
            for item in self.do_ip_routings:
                serialized = SerializationHelper.serialize_item(item, "DoIpRoutingActivation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize general_inactivity
        if self.general_inactivity is not None:
            serialized = SerializationHelper.serialize_item(self.general_inactivity, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("GENERAL-INACTIVITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial_inactivity
        if self.initial_inactivity is not None:
            serialized = SerializationHelper.serialize_item(self.initial_inactivity, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-INACTIVITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial_vehicle
        if self.initial_vehicle is not None:
            serialized = SerializationHelper.serialize_item(self.initial_vehicle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-VEHICLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize is_activation_line
        if self.is_activation_line is not None:
            serialized = SerializationHelper.serialize_item(self.is_activation_line, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IS-ACTIVATION-LINE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize max_tester
        if self.max_tester is not None:
            serialized = SerializationHelper.serialize_item(self.max_tester, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-TESTER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize socket_refs (list to container "SOCKET-REFS")
        if self.socket_refs:
            wrapper = ET.Element("SOCKET-REFS")
            for item in self.socket_refs:
                serialized = SerializationHelper.serialize_item(item, "StaticSocketConnection")
                if serialized is not None:
                    child_elem = ET.Element("SOCKET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize use_mac_address
        if self.use_mac_address is not None:
            serialized = SerializationHelper.serialize_item(self.use_mac_address, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-MAC-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize use_vehicle
        if self.use_vehicle is not None:
            serialized = SerializationHelper.serialize_item(self.use_vehicle, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("USE-VEHICLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vehicle
        if self.vehicle is not None:
            serialized = SerializationHelper.serialize_item(self.vehicle, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VEHICLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpInterface":
        """Deserialize XML element to DoIpInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpInterface, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALIVE-CHECK":
                setattr(obj, "alive_check", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "DOIP-CHANNEL-REF":
                setattr(obj, "doip_channel_ref", ARRef.deserialize(child))
            elif tag == "DOIP-CONNECTION-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.doip_connection_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "SocketConnection"))
            elif tag == "DO-IP-ROUTINGS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.do_ip_routings.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpRoutingActivation"))
            elif tag == "GENERAL-INACTIVITY":
                setattr(obj, "general_inactivity", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "INITIAL-INACTIVITY":
                setattr(obj, "initial_inactivity", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "INITIAL-VEHICLE":
                setattr(obj, "initial_vehicle", SerializationHelper.deserialize_by_tag(child, "TimeValue"))
            elif tag == "IS-ACTIVATION-LINE":
                setattr(obj, "is_activation_line", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "MAX-TESTER":
                setattr(obj, "max_tester", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "SOCKET-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.socket_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "StaticSocketConnection"))
            elif tag == "USE-MAC-ADDRESS":
                setattr(obj, "use_mac_address", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "USE-VEHICLE":
                setattr(obj, "use_vehicle", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "VEHICLE":
                setattr(obj, "vehicle", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class DoIpInterfaceBuilder(IdentifiableBuilder):
    """Builder for DoIpInterface with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpInterface = DoIpInterface()


    def with_alive_check(self, value: Optional[TimeValue]) -> "DoIpInterfaceBuilder":
        """Set alive_check attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.alive_check = value
        return self

    def with_doip_channel(self, value: Optional[DoIpTpConfig]) -> "DoIpInterfaceBuilder":
        """Set doip_channel attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.doip_channel = value
        return self

    def with_doip_connections(self, items: list[SocketConnection]) -> "DoIpInterfaceBuilder":
        """Set doip_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.doip_connections = list(items) if items else []
        return self

    def with_do_ip_routings(self, items: list[DoIpRoutingActivation]) -> "DoIpInterfaceBuilder":
        """Set do_ip_routings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.do_ip_routings = list(items) if items else []
        return self

    def with_general_inactivity(self, value: Optional[TimeValue]) -> "DoIpInterfaceBuilder":
        """Set general_inactivity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.general_inactivity = value
        return self

    def with_initial_inactivity(self, value: Optional[TimeValue]) -> "DoIpInterfaceBuilder":
        """Set initial_inactivity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_inactivity = value
        return self

    def with_initial_vehicle(self, value: Optional[TimeValue]) -> "DoIpInterfaceBuilder":
        """Set initial_vehicle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.initial_vehicle = value
        return self

    def with_is_activation_line(self, value: Optional[Boolean]) -> "DoIpInterfaceBuilder":
        """Set is_activation_line attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.is_activation_line = value
        return self

    def with_max_tester(self, value: Optional[PositiveInteger]) -> "DoIpInterfaceBuilder":
        """Set max_tester attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_tester = value
        return self

    def with_sockets(self, items: list[StaticSocketConnection]) -> "DoIpInterfaceBuilder":
        """Set sockets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.sockets = list(items) if items else []
        return self

    def with_use_mac_address(self, value: Optional[Boolean]) -> "DoIpInterfaceBuilder":
        """Set use_mac_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_mac_address = value
        return self

    def with_use_vehicle(self, value: Optional[Boolean]) -> "DoIpInterfaceBuilder":
        """Set use_vehicle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.use_vehicle = value
        return self

    def with_vehicle(self, value: Optional[TimeValue]) -> "DoIpInterfaceBuilder":
        """Set vehicle attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vehicle = value
        return self


    def add_doip_connection(self, item: SocketConnection) -> "DoIpInterfaceBuilder":
        """Add a single item to doip_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.doip_connections.append(item)
        return self

    def clear_doip_connections(self) -> "DoIpInterfaceBuilder":
        """Clear all items from doip_connections list.

        Returns:
            self for method chaining
        """
        self._obj.doip_connections = []
        return self

    def add_do_ip_routing(self, item: DoIpRoutingActivation) -> "DoIpInterfaceBuilder":
        """Add a single item to do_ip_routings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.do_ip_routings.append(item)
        return self

    def clear_do_ip_routings(self) -> "DoIpInterfaceBuilder":
        """Clear all items from do_ip_routings list.

        Returns:
            self for method chaining
        """
        self._obj.do_ip_routings = []
        return self

    def add_socket(self, item: StaticSocketConnection) -> "DoIpInterfaceBuilder":
        """Add a single item to sockets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.sockets.append(item)
        return self

    def clear_sockets(self) -> "DoIpInterfaceBuilder":
        """Clear all items from sockets list.

        Returns:
            self for method chaining
        """
        self._obj.sockets = []
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


    def build(self) -> DoIpInterface:
        """Build and return the DoIpInterface instance with validation."""
        self._validate_instance()
        pass
        return self._obj