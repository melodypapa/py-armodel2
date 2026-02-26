"""ApplicationEndpoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 457)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.tls_crypto_service_mapping import (
    TlsCryptoServiceMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.transport_protocol_configuration import (
    TransportProtocolConfiguration,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ApplicationEndpoint(Identifiable):
    """AUTOSAR ApplicationEndpoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    consumed_services: list[Any]
    max_number_of: Optional[PositiveInteger]
    network_endpoint_endpoint_ref: Optional[ARRef]
    priority: Optional[PositiveInteger]
    provided_services: list[Any]
    tls_crypto_service_ref: Optional[ARRef]
    tp_configuration_configuration: Optional[TransportProtocolConfiguration]
    def __init__(self) -> None:
        """Initialize ApplicationEndpoint."""
        super().__init__()
        self.consumed_services: list[Any] = []
        self.max_number_of: Optional[PositiveInteger] = None
        self.network_endpoint_endpoint_ref: Optional[ARRef] = None
        self.priority: Optional[PositiveInteger] = None
        self.provided_services: list[Any] = []
        self.tls_crypto_service_ref: Optional[ARRef] = None
        self.tp_configuration_configuration: Optional[TransportProtocolConfiguration] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationEndpoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationEndpoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize consumed_services (list to container "CONSUMED-SERVICES")
        if self.consumed_services:
            wrapper = ET.Element("CONSUMED-SERVICES")
            for item in self.consumed_services:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize max_number_of
        if self.max_number_of is not None:
            serialized = SerializationHelper.serialize_item(self.max_number_of, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAX-NUMBER-OF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_endpoint_endpoint_ref
        if self.network_endpoint_endpoint_ref is not None:
            serialized = SerializationHelper.serialize_item(self.network_endpoint_endpoint_ref, "NetworkEndpoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK-ENDPOINT-ENDPOINT-REF")
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

        # Serialize provided_services (list to container "PROVIDED-SERVICES")
        if self.provided_services:
            wrapper = ET.Element("PROVIDED-SERVICES")
            for item in self.provided_services:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tls_crypto_service_ref
        if self.tls_crypto_service_ref is not None:
            serialized = SerializationHelper.serialize_item(self.tls_crypto_service_ref, "TlsCryptoServiceMapping")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TLS-CRYPTO-SERVICE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize tp_configuration_configuration
        if self.tp_configuration_configuration is not None:
            serialized = SerializationHelper.serialize_item(self.tp_configuration_configuration, "TransportProtocolConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TP-CONFIGURATION-CONFIGURATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationEndpoint":
        """Deserialize XML element to ApplicationEndpoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationEndpoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationEndpoint, cls).deserialize(element)

        # Parse consumed_services (list from container "CONSUMED-SERVICES")
        obj.consumed_services = []
        container = SerializationHelper.find_child_element(element, "CONSUMED-SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.consumed_services.append(child_value)

        # Parse max_number_of
        child = SerializationHelper.find_child_element(element, "MAX-NUMBER-OF")
        if child is not None:
            max_number_of_value = child.text
            obj.max_number_of = max_number_of_value

        # Parse network_endpoint_endpoint_ref
        child = SerializationHelper.find_child_element(element, "NETWORK-ENDPOINT-ENDPOINT-REF")
        if child is not None:
            network_endpoint_endpoint_ref_value = ARRef.deserialize(child)
            obj.network_endpoint_endpoint_ref = network_endpoint_endpoint_ref_value

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        # Parse provided_services (list from container "PROVIDED-SERVICES")
        obj.provided_services = []
        container = SerializationHelper.find_child_element(element, "PROVIDED-SERVICES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.provided_services.append(child_value)

        # Parse tls_crypto_service_ref
        child = SerializationHelper.find_child_element(element, "TLS-CRYPTO-SERVICE-REF")
        if child is not None:
            tls_crypto_service_ref_value = ARRef.deserialize(child)
            obj.tls_crypto_service_ref = tls_crypto_service_ref_value

        # Parse tp_configuration_configuration
        child = SerializationHelper.find_child_element(element, "TP-CONFIGURATION-CONFIGURATION")
        if child is not None:
            tp_configuration_configuration_value = SerializationHelper.deserialize_by_tag(child, "TransportProtocolConfiguration")
            obj.tp_configuration_configuration = tp_configuration_configuration_value

        return obj



class ApplicationEndpointBuilder(IdentifiableBuilder):
    """Builder for ApplicationEndpoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ApplicationEndpoint = ApplicationEndpoint()


    def with_consumed_services(self, items: list[any (ConsumedService)]) -> "ApplicationEndpointBuilder":
        """Set consumed_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.consumed_services = list(items) if items else []
        return self

    def with_max_number_of(self, value: Optional[PositiveInteger]) -> "ApplicationEndpointBuilder":
        """Set max_number_of attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.max_number_of = value
        return self

    def with_network_endpoint_endpoint(self, value: Optional[NetworkEndpoint]) -> "ApplicationEndpointBuilder":
        """Set network_endpoint_endpoint attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.network_endpoint_endpoint = value
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "ApplicationEndpointBuilder":
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

    def with_provided_services(self, items: list[any (ProvidedService)]) -> "ApplicationEndpointBuilder":
        """Set provided_services list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_services = list(items) if items else []
        return self

    def with_tls_crypto_service(self, value: Optional[TlsCryptoServiceMapping]) -> "ApplicationEndpointBuilder":
        """Set tls_crypto_service attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tls_crypto_service = value
        return self

    def with_tp_configuration_configuration(self, value: Optional[TransportProtocolConfiguration]) -> "ApplicationEndpointBuilder":
        """Set tp_configuration_configuration attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tp_configuration_configuration = value
        return self


    def add_consumed_service(self, item: any (ConsumedService)) -> "ApplicationEndpointBuilder":
        """Add a single item to consumed_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.consumed_services.append(item)
        return self

    def clear_consumed_services(self) -> "ApplicationEndpointBuilder":
        """Clear all items from consumed_services list.

        Returns:
            self for method chaining
        """
        self._obj.consumed_services = []
        return self

    def add_provided_service(self, item: any (ProvidedService)) -> "ApplicationEndpointBuilder":
        """Add a single item to provided_services list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_services.append(item)
        return self

    def clear_provided_services(self) -> "ApplicationEndpointBuilder":
        """Clear all items from provided_services list.

        Returns:
            self for method chaining
        """
        self._obj.provided_services = []
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


    def build(self) -> ApplicationEndpoint:
        """Build and return the ApplicationEndpoint instance with validation."""
        self._validate_instance()
        pass
        return self._obj