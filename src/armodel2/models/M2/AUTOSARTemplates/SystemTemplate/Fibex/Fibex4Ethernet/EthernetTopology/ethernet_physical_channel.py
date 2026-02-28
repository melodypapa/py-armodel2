"""EthernetPhysicalChannel AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 314)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 105)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import (
    PhysicalChannel,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.physical_channel import PhysicalChannelBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.network_endpoint import (
    NetworkEndpoint,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.so_ad_config import (
    SoAdConfig,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.vlan_config import (
    VlanConfig,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthernetPhysicalChannel(PhysicalChannel):
    """AUTOSAR EthernetPhysicalChannel."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETHERNET-PHYSICAL-CHANNEL"


    network_endpoints: list[NetworkEndpoint]
    so_ad_config: Optional[SoAdConfig]
    vlan: Optional[VlanConfig]
    _DESERIALIZE_DISPATCH = {
        "NETWORK-ENDPOINTS": lambda obj, elem: obj.network_endpoints.append(NetworkEndpoint.deserialize(elem)),
        "SO-AD-CONFIG": lambda obj, elem: setattr(obj, "so_ad_config", SoAdConfig.deserialize(elem)),
        "VLAN": lambda obj, elem: setattr(obj, "vlan", VlanConfig.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize EthernetPhysicalChannel."""
        super().__init__()
        self.network_endpoints: list[NetworkEndpoint] = []
        self.so_ad_config: Optional[SoAdConfig] = None
        self.vlan: Optional[VlanConfig] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetPhysicalChannel to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetPhysicalChannel, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize network_endpoints (list to container "NETWORK-ENDPOINTS")
        if self.network_endpoints:
            wrapper = ET.Element("NETWORK-ENDPOINTS")
            for item in self.network_endpoints:
                serialized = SerializationHelper.serialize_item(item, "NetworkEndpoint")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize so_ad_config
        if self.so_ad_config is not None:
            serialized = SerializationHelper.serialize_item(self.so_ad_config, "SoAdConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SO-AD-CONFIG")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vlan
        if self.vlan is not None:
            serialized = SerializationHelper.serialize_item(self.vlan, "VlanConfig")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VLAN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetPhysicalChannel":
        """Deserialize XML element to EthernetPhysicalChannel object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetPhysicalChannel object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetPhysicalChannel, cls).deserialize(element)

        # Parse network_endpoints (list from container "NETWORK-ENDPOINTS")
        obj.network_endpoints = []
        container = SerializationHelper.find_child_element(element, "NETWORK-ENDPOINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.network_endpoints.append(child_value)

        # Parse so_ad_config
        child = SerializationHelper.find_child_element(element, "SO-AD-CONFIG")
        if child is not None:
            so_ad_config_value = SerializationHelper.deserialize_by_tag(child, "SoAdConfig")
            obj.so_ad_config = so_ad_config_value

        # Parse vlan
        child = SerializationHelper.find_child_element(element, "VLAN")
        if child is not None:
            vlan_value = SerializationHelper.deserialize_by_tag(child, "VlanConfig")
            obj.vlan = vlan_value

        return obj



class EthernetPhysicalChannelBuilder(PhysicalChannelBuilder):
    """Builder for EthernetPhysicalChannel with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthernetPhysicalChannel = EthernetPhysicalChannel()


    def with_network_endpoints(self, items: list[NetworkEndpoint]) -> "EthernetPhysicalChannelBuilder":
        """Set network_endpoints list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.network_endpoints = list(items) if items else []
        return self

    def with_so_ad_config(self, value: Optional[SoAdConfig]) -> "EthernetPhysicalChannelBuilder":
        """Set so_ad_config attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.so_ad_config = value
        return self

    def with_vlan(self, value: Optional[VlanConfig]) -> "EthernetPhysicalChannelBuilder":
        """Set vlan attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.vlan = value
        return self


    def add_network_endpoint(self, item: NetworkEndpoint) -> "EthernetPhysicalChannelBuilder":
        """Add a single item to network_endpoints list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.network_endpoints.append(item)
        return self

    def clear_network_endpoints(self) -> "EthernetPhysicalChannelBuilder":
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


    def build(self) -> EthernetPhysicalChannel:
        """Build and return the EthernetPhysicalChannel instance with validation."""
        self._validate_instance()
        pass
        return self._obj