"""ConsumedServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 980)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 500)

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
    AnyServiceInstanceId,
    AnyVersionString,
    Boolean,
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.application_endpoint import (
    ApplicationEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_sd_client_service_instance_config import (
    SomeipSdClientServiceInstanceConfig,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.someip_service_version import (
    SomeipServiceVersion,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ConsumedServiceInstance(AbstractServiceInstance):
    """AUTOSAR ConsumedServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "CONSUMED-SERVICE-INSTANCE"


    allowed_service_refs: list[ARRef]
    auto_require: Optional[Boolean]
    blocklisteds: list[SomeipServiceVersion]
    consumed_event_group_refs: list[ARRef]
    event_multicast_ref: Optional[ARRef]
    instance: Optional[AnyServiceInstanceId]
    local_unicast: ApplicationEndpoint
    minor_version: Optional[AnyVersionString]
    provided_service_ref: Optional[Any]
    remote_unicast: ApplicationEndpoint
    sd_client_config: Optional[Any]
    sd_client_timer_ref: Optional[ARRef]
    service_identifier: Optional[PositiveInteger]
    version_driven: Optional[Any]
    _DESERIALIZE_DISPATCH = {
        "ALLOWED-SERVICES": lambda obj, elem: obj.allowed_service_refs.append(ARRef.deserialize(elem)),
        "AUTO-REQUIRE": lambda obj, elem: setattr(obj, "auto_require", SerializationHelper.deserialize_by_tag(elem, "Boolean")),
        "BLOCKLISTEDS": lambda obj, elem: obj.blocklisteds.append(SerializationHelper.deserialize_by_tag(elem, "SomeipServiceVersion")),
        "CONSUMED-EVENT-GROUPS": lambda obj, elem: obj.consumed_event_group_refs.append(ARRef.deserialize(elem)),
        "EVENT-MULTICAST-REF": lambda obj, elem: setattr(obj, "event_multicast_ref", ARRef.deserialize(elem)),
        "INSTANCE": lambda obj, elem: setattr(obj, "instance", SerializationHelper.deserialize_by_tag(elem, "AnyServiceInstanceId")),
        "LOCAL-UNICAST": lambda obj, elem: setattr(obj, "local_unicast", SerializationHelper.deserialize_by_tag(elem, "ApplicationEndpoint")),
        "MINOR-VERSION": lambda obj, elem: setattr(obj, "minor_version", SerializationHelper.deserialize_by_tag(elem, "AnyVersionString")),
        "PROVIDED-SERVICE-REF": lambda obj, elem: setattr(obj, "provided_service_ref", ARRef.deserialize(elem)),
        "REMOTE-UNICAST": lambda obj, elem: setattr(obj, "remote_unicast", SerializationHelper.deserialize_by_tag(elem, "ApplicationEndpoint")),
        "SD-CLIENT-CONFIG": lambda obj, elem: setattr(obj, "sd_client_config", SerializationHelper.deserialize_by_tag(elem, "any (SdClientConfig)")),
        "SD-CLIENT-TIMER-REF": lambda obj, elem: setattr(obj, "sd_client_timer_ref", ARRef.deserialize(elem)),
        "SERVICE-IDENTIFIER": lambda obj, elem: setattr(obj, "service_identifier", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
        "VERSION-DRIVEN": lambda obj, elem: setattr(obj, "version_driven", SerializationHelper.deserialize_by_tag(elem, "any (ServiceVersion)")),
    }


    def __init__(self) -> None:
        """Initialize ConsumedServiceInstance."""
        super().__init__()
        self.allowed_service_refs: list[ARRef] = []
        self.auto_require: Optional[Boolean] = None
        self.blocklisteds: list[SomeipServiceVersion] = []
        self.consumed_event_group_refs: list[ARRef] = []
        self.event_multicast_ref: Optional[ARRef] = None
        self.instance: Optional[AnyServiceInstanceId] = None
        self.local_unicast: ApplicationEndpoint = None
        self.minor_version: Optional[AnyVersionString] = None
        self.provided_service_ref: Optional[Any] = None
        self.remote_unicast: ApplicationEndpoint = None
        self.sd_client_config: Optional[Any] = None
        self.sd_client_timer_ref: Optional[ARRef] = None
        self.service_identifier: Optional[PositiveInteger] = None
        self.version_driven: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ConsumedServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ConsumedServiceInstance, self).serialize()

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

        # Serialize auto_require
        if self.auto_require is not None:
            serialized = SerializationHelper.serialize_item(self.auto_require, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-REQUIRE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize blocklisteds (list to container "BLOCKLISTEDS")
        if self.blocklisteds:
            wrapper = ET.Element("BLOCKLISTEDS")
            for item in self.blocklisteds:
                serialized = SerializationHelper.serialize_item(item, "SomeipServiceVersion")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize consumed_event_group_refs (list to container "CONSUMED-EVENT-GROUP-REFS")
        if self.consumed_event_group_refs:
            wrapper = ET.Element("CONSUMED-EVENT-GROUP-REFS")
            for item in self.consumed_event_group_refs:
                serialized = SerializationHelper.serialize_item(item, "ConsumedEventGroup")
                if serialized is not None:
                    child_elem = ET.Element("CONSUMED-EVENT-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize event_multicast_ref
        if self.event_multicast_ref is not None:
            serialized = SerializationHelper.serialize_item(self.event_multicast_ref, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EVENT-MULTICAST-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize instance
        if self.instance is not None:
            serialized = SerializationHelper.serialize_item(self.instance, "AnyServiceInstanceId")
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
            serialized = SerializationHelper.serialize_item(self.minor_version, "AnyVersionString")
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

        # Serialize provided_service_ref
        if self.provided_service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provided_service_ref, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize remote_unicast
        if self.remote_unicast is not None:
            serialized = SerializationHelper.serialize_item(self.remote_unicast, "ApplicationEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REMOTE-UNICAST")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd_client_config
        if self.sd_client_config is not None:
            serialized = SerializationHelper.serialize_item(self.sd_client_config, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-CLIENT-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sd_client_timer_ref
        if self.sd_client_timer_ref is not None:
            serialized = SerializationHelper.serialize_item(self.sd_client_timer_ref, "SomeipSdClientServiceInstanceConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SD-CLIENT-TIMER-REF")
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

        # Serialize version_driven
        if self.version_driven is not None:
            serialized = SerializationHelper.serialize_item(self.version_driven, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VERSION-DRIVEN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ConsumedServiceInstance":
        """Deserialize XML element to ConsumedServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ConsumedServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ConsumedServiceInstance, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ALLOWED-SERVICES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.allowed_service_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "NetworkEndpoint"))
            elif tag == "AUTO-REQUIRE":
                setattr(obj, "auto_require", SerializationHelper.deserialize_by_tag(child, "Boolean"))
            elif tag == "BLOCKLISTEDS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.blocklisteds.append(SerializationHelper.deserialize_by_tag(item_elem, "SomeipServiceVersion"))
            elif tag == "CONSUMED-EVENT-GROUPS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.consumed_event_group_refs.append(SerializationHelper.deserialize_by_tag(item_elem, "ConsumedEventGroup"))
            elif tag == "EVENT-MULTICAST-REF":
                setattr(obj, "event_multicast_ref", ARRef.deserialize(child))
            elif tag == "INSTANCE":
                setattr(obj, "instance", SerializationHelper.deserialize_by_tag(child, "AnyServiceInstanceId"))
            elif tag == "LOCAL-UNICAST":
                setattr(obj, "local_unicast", SerializationHelper.deserialize_by_tag(child, "ApplicationEndpoint"))
            elif tag == "MINOR-VERSION":
                setattr(obj, "minor_version", SerializationHelper.deserialize_by_tag(child, "AnyVersionString"))
            elif tag == "PROVIDED-SERVICE-REF":
                setattr(obj, "provided_service_ref", ARRef.deserialize(child))
            elif tag == "REMOTE-UNICAST":
                setattr(obj, "remote_unicast", SerializationHelper.deserialize_by_tag(child, "ApplicationEndpoint"))
            elif tag == "SD-CLIENT-CONFIG":
                setattr(obj, "sd_client_config", SerializationHelper.deserialize_by_tag(child, "any (SdClientConfig)"))
            elif tag == "SD-CLIENT-TIMER-REF":
                setattr(obj, "sd_client_timer_ref", ARRef.deserialize(child))
            elif tag == "SERVICE-IDENTIFIER":
                setattr(obj, "service_identifier", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))
            elif tag == "VERSION-DRIVEN":
                setattr(obj, "version_driven", SerializationHelper.deserialize_by_tag(child, "any (ServiceVersion)"))

        return obj



class ConsumedServiceInstanceBuilder(AbstractServiceInstanceBuilder):
    """Builder for ConsumedServiceInstance with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ConsumedServiceInstance = ConsumedServiceInstance()


    def with_allowed_services(self, items: list[NetworkEndpoint]) -> "ConsumedServiceInstanceBuilder":
        """Set allowed_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.allowed_services = list(items) if items else []
        return self

    def with_auto_require(self, value: Optional[Boolean]) -> "ConsumedServiceInstanceBuilder":
        """Set auto_require attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.auto_require = value
        return self

    def with_blocklisteds(self, items: list[SomeipServiceVersion]) -> "ConsumedServiceInstanceBuilder":
        """Set blocklisteds list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.blocklisteds = list(items) if items else []
        return self

    def with_consumed_event_groups(self, items: list[ConsumedEventGroup]) -> "ConsumedServiceInstanceBuilder":
        """Set consumed_event_groups list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups = list(items) if items else []
        return self

    def with_event_multicast(self, value: Optional[ApplicationEndpoint]) -> "ConsumedServiceInstanceBuilder":
        """Set event_multicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.event_multicast = value
        return self

    def with_instance(self, value: Optional[AnyServiceInstanceId]) -> "ConsumedServiceInstanceBuilder":
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

    def with_local_unicast(self, value: ApplicationEndpoint) -> "ConsumedServiceInstanceBuilder":
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

    def with_minor_version(self, value: Optional[AnyVersionString]) -> "ConsumedServiceInstanceBuilder":
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

    def with_provided_service(self, value: Optional[any (ProvidedService)]) -> "ConsumedServiceInstanceBuilder":
        """Set provided_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.provided_service = value
        return self

    def with_remote_unicast(self, value: ApplicationEndpoint) -> "ConsumedServiceInstanceBuilder":
        """Set remote_unicast attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not False:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.remote_unicast = value
        return self

    def with_sd_client_config(self, value: Optional[any (SdClientConfig)]) -> "ConsumedServiceInstanceBuilder":
        """Set sd_client_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_client_config = value
        return self

    def with_sd_client_timer(self, value: Optional[SomeipSdClientServiceInstanceConfig]) -> "ConsumedServiceInstanceBuilder":
        """Set sd_client_timer attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.sd_client_timer = value
        return self

    def with_service_identifier(self, value: Optional[PositiveInteger]) -> "ConsumedServiceInstanceBuilder":
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

    def with_version_driven(self, value: Optional[any (ServiceVersion)]) -> "ConsumedServiceInstanceBuilder":
        """Set version_driven attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.version_driven = value
        return self


    def add_allowed_service(self, item: NetworkEndpoint) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to allowed_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.allowed_services.append(item)
        return self

    def clear_allowed_services(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from allowed_services list.

        Returns:
            self for method chaining
        """
        self._obj.allowed_services = []
        return self

    def add_blocklisted(self, item: SomeipServiceVersion) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to blocklisteds list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.blocklisteds.append(item)
        return self

    def clear_blocklisteds(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from blocklisteds list.

        Returns:
            self for method chaining
        """
        self._obj.blocklisteds = []
        return self

    def add_consumed_event_group(self, item: ConsumedEventGroup) -> "ConsumedServiceInstanceBuilder":
        """Add a single item to consumed_event_groups list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups.append(item)
        return self

    def clear_consumed_event_groups(self) -> "ConsumedServiceInstanceBuilder":
        """Clear all items from consumed_event_groups list.

        Returns:
            self for method chaining
        """
        self._obj.consumed_event_groups = []
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


    def build(self) -> ConsumedServiceInstance:
        """Build and return the ConsumedServiceInstance instance with validation."""
        self._validate_instance()
        pass
        return self._obj