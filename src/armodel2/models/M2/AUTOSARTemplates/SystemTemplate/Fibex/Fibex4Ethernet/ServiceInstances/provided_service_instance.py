"""ProvidedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1000)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 485)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import (
    AbstractServiceInstance,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.abstract_service_instance import AbstractServiceInstanceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.event_handler import (
    EventHandler,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ProvidedServiceInstance(AbstractServiceInstance):
    """AUTOSAR ProvidedServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PROVIDED-SERVICE-INSTANCE"


    allowed_service_refs: list[ARRef]
    auto_available: Optional[Boolean]
    event_handlers: list[EventHandler]
    instance: Optional[PositiveInteger]
    load_balancing: Optional[PositiveInteger]
    local_unicast: ApplicationEndpoint
    minor_version: Optional[PositiveInteger]
    priority: Optional[PositiveInteger]
    remote_multicast_refs: list[ARRef]
    remote_unicast_refs: list[ARRef]
    sd_server_config: Optional[Any]
    sd_server_timer_ref: Optional[Any]
    service_identifier: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "ALLOWED-SERVICES": lambda obj, elem: obj.allowed_service_refs.append(ARRef.deserialize(elem)),
        "AUTO-AVAILABLE": lambda obj, elem: setattr(obj, "auto_available", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "EVENT-HANDLERS": lambda obj, elem: obj.event_handlers.append(SerializationHelper.deserialize_by_tag(elem, "EventHandler")),
        "INSTANCE": lambda obj, elem: setattr(obj, "instance", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "LOAD-BALANCING": lambda obj, elem: setattr(obj, "load_balancing", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "LOCAL-UNICAST": lambda obj, elem: setattr(obj, "local_unicast", SerializationHelper.deserialize_by_tag(elem, "ApplicationEndpoint")),
        "MINOR-VERSION": lambda obj, elem: setattr(obj, "minor_version", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "PRIORITY": lambda obj, elem: setattr(obj, "priority", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "REMOTE-MULTICASTS": lambda obj, elem: obj.remote_multicast_refs.append(ARRef.deserialize(elem)),
        "REMOTE-UNICASTS": lambda obj, elem: obj.remote_unicast_refs.append(ARRef.deserialize(elem)),
        "SD-SERVER-CONFIG": lambda obj, elem: setattr(obj, "sd_server_config", SerializationHelper.deserialize_by_tag(elem, "any (SdServerConfig)")),
        "SD-SERVER-TIMER-REF": lambda obj, elem: setattr(obj, "sd_server_timer_ref", ARRef.deserialize(elem)),
        "SERVICE-IDENTIFIER": lambda obj, elem: setattr(obj, "service_identifier", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize ProvidedServiceInstance."""
        super().__init__()
        self.allowed_service_refs: list[ARRef] = []
        self.auto_available: Optional[Boolean] = None
        self.event_handlers: list[EventHandler] = []
        self.instance: Optional[PositiveInteger] = None
        self.load_balancing: Optional[PositiveInteger] = None
        self.local_unicast: ApplicationEndpoint = None
        self.minor_version: Optional[PositiveInteger] = None
        self.priority: Optional[PositiveInteger] = None
        self.remote_multicast_refs: list[ARRef] = []
        self.remote_unicast_refs: list[ARRef] = []
        self.sd_server_config: Optional[Any] = None
        self.sd_server_timer_ref: Optional[Any] = None
        self.service_identifier: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize ProvidedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ProvidedServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize allowed_service_refs (list to container "ALLOWED-SERVICE-REFS")
        if self.allowed_service_refs:
            wrapper = ET.Element("ALLOWED-SERVICE-REFS")
            for item in self.allowed_service_refs:
                serialized = SerializationHelper.serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("ALLOWED-SERVICE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize auto_available
        if self.auto_available is not None:
            serialized = SerializationHelper.serialize_item(self.auto_available, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-AVAILABLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize event_handlers (list to container "EVENT-HANDLERS")
        if self.event_handlers:
            wrapper = ET.Element("EVENT-HANDLERS")
            for item in self.event_handlers:
                serialized = SerializationHelper.serialize_item(item, "EventHandler")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize instance
        if self.instance is not None:
            serialized = SerializationHelper.serialize_item(self.instance, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize load_balancing
        if self.load_balancing is not None:
            serialized = SerializationHelper.serialize_item(self.load_balancing, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOAD-BALANCING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize local_unicast
        if self.local_unicast is not None:
            serialized = SerializationHelper.serialize_item(self.local_unicast, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOCAL-UNICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize minor_version
        if self.minor_version is not None:
            serialized = SerializationHelper.serialize_item(self.minor_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MINOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize priority
        if self.priority is not None:
            serialized = SerializationHelper.serialize_item(self.priority, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PRIORITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remote_multicast_refs (list to container "REMOTE-MULTICAST-REFS")
        if self.remote_multicast_refs:
            wrapper = ET.Element("REMOTE-MULTICAST-REFS")
            for item in self.remote_multicast_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("REMOTE-MULTICAST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize remote_unicast_refs (list to container "REMOTE-UNICAST-REFS")
        if self.remote_unicast_refs:
            wrapper = ET.Element("REMOTE-UNICAST-REFS")
            for item in self.remote_unicast_refs:
                serialized = SerializationHelper.serialize_item(item, "ApplicationEndpoint")
                if serialized is not None:
                    child_elem = ET.Element("REMOTE-UNICAST-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sd_server_config
        if self.sd_server_config is not None:
            serialized = SerializationHelper.serialize_item(self.sd_server_config, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-SERVER-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd_server_timer_ref
        if self.sd_server_timer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sd_server_timer_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-SERVER-TIMER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize service_identifier
        if self.service_identifier is not None:
            serialized = SerializationHelper.serialize_item(self.service_identifier, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-IDENTIFIER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ProvidedServiceInstance":
        """Deserialize XML element to ProvidedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ProvidedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ProvidedServiceInstance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "ALLOWED-SERVICES":
                obj.allowed_service_refs.append(ARRef.deserialize(child))
            elif tag == "AUTO-AVAILABLE":
                setattr(obj, "auto_available", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "EVENT-HANDLERS":
                obj.event_handlers.append(SerializationHelper.deserialize_by_tag(child, "EventHandler"))
            elif tag == "INSTANCE":
                setattr(obj, "instance", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "LOAD-BALANCING":
                setattr(obj, "load_balancing", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "LOCAL-UNICAST":
                setattr(obj, "local_unicast", SerializationHelper.deserialize_by_tag(child, "ApplicationEndpoint"))
            elif tag == "MINOR-VERSION":
                setattr(obj, "minor_version", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "PRIORITY":
                setattr(obj, "priority", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "REMOTE-MULTICASTS":
                obj.remote_multicast_refs.append(ARRef.deserialize(child))
            elif tag == "REMOTE-UNICASTS":
                obj.remote_unicast_refs.append(ARRef.deserialize(child))
            elif tag == "SD-SERVER-CONFIG":
                setattr(obj, "sd_server_config", SerializationHelper.deserialize_by_tag(child, "any (SdServerConfig)"))
            elif tag == "SD-SERVER-TIMER-REF":
                setattr(obj, "sd_server_timer_ref", ARRef.deserialize(child))
            elif tag == "SERVICE-IDENTIFIER":
                setattr(obj, "service_identifier", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class ProvidedServiceInstanceBuilder(AbstractServiceInstanceBuilder):
    """Builder for ProvidedServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ProvidedServiceInstance = ProvidedServiceInstance()


    def with_allowed_services(self, items: list[NetworkEndpoint]) -> "ProvidedServiceInstanceBuilder":
        """Set allowed_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.allowed_services = list(items) if items else []
        return self

    def with_auto_available(self, value: Optional[Boolean]) -> "ProvidedServiceInstanceBuilder":
        """Set auto_available attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.auto_available = value
        return self

    def with_event_handlers(self, items: list[EventHandler]) -> "ProvidedServiceInstanceBuilder":
        """Set event_handlers list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.event_handlers = list(items) if items else []
        return self

    def with_instance(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set instance attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.instance = value
        return self

    def with_load_balancing(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set load_balancing attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.load_balancing = value
        return self

    def with_local_unicast(self, value: ApplicationEndpoint) -> "ProvidedServiceInstanceBuilder":
        """Set local_unicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.local_unicast = value
        return self

    def with_minor_version(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set minor_version attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.minor_version = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set priority attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.priority = value
        return self

    def with_remote_multicasts(self, items: list[ApplicationEndpoint]) -> "ProvidedServiceInstanceBuilder":
        """Set remote_multicasts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.remote_multicasts = list(items) if items else []
        return self

    def with_remote_unicasts(self, items: list[ApplicationEndpoint]) -> "ProvidedServiceInstanceBuilder":
        """Set remote_unicasts list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.remote_unicasts = list(items) if items else []
        return self

    def with_sd_server_config(self, value: Optional[any (SdServerConfig)]) -> "ProvidedServiceInstanceBuilder":
        """Set sd_server_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_server_config = value
        return self

    def with_sd_server_timer(self, value: Optional[any (SomeipSdServer)]) -> "ProvidedServiceInstanceBuilder":
        """Set sd_server_timer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_server_timer = value
        return self

    def with_service_identifier(self, value: Optional[PositiveInteger]) -> "ProvidedServiceInstanceBuilder":
        """Set service_identifier attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.service_identifier = value
        return self


    def add_allowed_service(self, item: NetworkEndpoint) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to allowed_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.allowed_services.append(item)
        return self

    def clear_allowed_services(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from allowed_services list.

        Returns:
            self for method chaining
        """
        self._obj.allowed_services = []
        return self

    def add_event_handler(self, item: EventHandler) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to event_handlers list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.event_handlers.append(item)
        return self

    def clear_event_handlers(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from event_handlers list.

        Returns:
            self for method chaining
        """
        self._obj.event_handlers = []
        return self

    def add_remote_multicast(self, item: ApplicationEndpoint) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to remote_multicasts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.remote_multicasts.append(item)
        return self

    def clear_remote_multicasts(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from remote_multicasts list.

        Returns:
            self for method chaining
        """
        self._obj.remote_multicasts = []
        return self

    def add_remote_unicast(self, item: ApplicationEndpoint) -> "ProvidedServiceInstanceBuilder":
        """Add a single item to remote_unicasts list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.remote_unicasts.append(item)
        return self

    def clear_remote_unicasts(self) -> "ProvidedServiceInstanceBuilder":
        """Clear all items from remote_unicasts list.

        Returns:
            self for method chaining
        """
        self._obj.remote_unicasts = []
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


    def build(self) -> ProvidedServiceInstance:
        """Build and return the ProvidedServiceInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj