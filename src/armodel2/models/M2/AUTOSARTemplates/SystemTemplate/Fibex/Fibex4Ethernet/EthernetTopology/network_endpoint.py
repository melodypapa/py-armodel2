"""NetworkEndpoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 463)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    String,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.infrastructure_services import (
    InfrastructureServices,
)

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.SecureCommunication.ip_sec_config import (
        IPSecConfig,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class NetworkEndpoint(Identifiable):
    """AUTOSAR NetworkEndpoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    fully_qualified: Optional[String]
    infrastructure_services: Optional[InfrastructureServices]
    ip_sec_config: Optional[IPSecConfig]
    network_endpoints: list[NetworkEndpoint]
    priority: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize NetworkEndpoint."""
        super().__init__()
        self.fully_qualified: Optional[String] = None
        self.infrastructure_services: Optional[InfrastructureServices] = None
        self.ip_sec_config: Optional[IPSecConfig] = None
        self.network_endpoints: list[NetworkEndpoint] = []
        self.priority: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize NetworkEndpoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(NetworkEndpoint, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize fully_qualified
        if self.fully_qualified is not None:
            serialized = SerializationHelper.serialize_item(self.fully_qualified, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FULLY-QUALIFIED")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize infrastructure_services
        if self.infrastructure_services is not None:
            serialized = SerializationHelper.serialize_item(self.infrastructure_services, "InfrastructureServices")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INFRASTRUCTURE-SERVICES")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ip_sec_config
        if self.ip_sec_config is not None:
            serialized = SerializationHelper.serialize_item(self.ip_sec_config, "IPSecConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IP-SEC-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network_endpoints (list to container "NETWORK-ENDPOINTS")
        if self.network_endpoints:
            wrapper = ET.Element("NETWORK-ENDPOINTS")
            for item in self.network_endpoints:
                serialized = SerializationHelper.serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "NetworkEndpoint":
        """Deserialize XML element to NetworkEndpoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized NetworkEndpoint object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(NetworkEndpoint, cls).deserialize(element)

        # Parse fully_qualified
        child = SerializationHelper.find_child_element(element, "FULLY-QUALIFIED")
        if child is not None:
            fully_qualified_value = child.text
            obj.fully_qualified = fully_qualified_value

        # Parse infrastructure_services
        child = SerializationHelper.find_child_element(element, "INFRASTRUCTURE-SERVICES")
        if child is not None:
            infrastructure_services_value = SerializationHelper.deserialize_by_tag(child, "InfrastructureServices")
            obj.infrastructure_services = infrastructure_services_value

        # Parse ip_sec_config
        child = SerializationHelper.find_child_element(element, "IP-SEC-CONFIG")
        if child is not None:
            ip_sec_config_value = SerializationHelper.deserialize_by_tag(child, "IPSecConfig")
            obj.ip_sec_config = ip_sec_config_value

        # Parse network_endpoints (list from container "NETWORK-ENDPOINTS")
        obj.network_endpoints = []
        container = SerializationHelper.find_child_element(element, "NETWORK-ENDPOINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.network_endpoints.append(child_value)

        # Parse priority
        child = SerializationHelper.find_child_element(element, "PRIORITY")
        if child is not None:
            priority_value = child.text
            obj.priority = priority_value

        return obj



class NetworkEndpointBuilder(IdentifiableBuilder):
    """Builder for NetworkEndpoint with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: NetworkEndpoint = NetworkEndpoint()


    def with_fully_qualified(self, value: Optional[String]) -> "NetworkEndpointBuilder":
        """Set fully_qualified attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fully_qualified = value
        return self

    def with_infrastructure_services(self, value: Optional[InfrastructureServices]) -> "NetworkEndpointBuilder":
        """Set infrastructure_services attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.infrastructure_services = value
        return self

    def with_ip_sec_config(self, value: Optional[IPSecConfig]) -> "NetworkEndpointBuilder":
        """Set ip_sec_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ip_sec_config = value
        return self

    def with_network_endpoints(self, items: list[NetworkEndpoint]) -> "NetworkEndpointBuilder":
        """Set network_endpoints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.network_endpoints = list(items) if items else []
        return self

    def with_priority(self, value: Optional[PositiveInteger]) -> "NetworkEndpointBuilder":
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


    def add_network_endpoint(self, item: NetworkEndpoint) -> "NetworkEndpointBuilder":
        """Add a single item to network_endpoints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.network_endpoints.append(item)
        return self

    def clear_network_endpoints(self) -> "NetworkEndpointBuilder":
        """Clear all items from network_endpoints list.

        Returns:
            self for method chaining
        """
        self._obj.network_endpoints = []
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


    def build(self) -> NetworkEndpoint:
        """Build and return the NetworkEndpoint instance with validation."""
        self._validate_instance()
        pass
        return self._obj