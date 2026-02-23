"""SoAdConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 451)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.socket_connection import (
    SocketConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SoAdConfig(ARObject):
    """AUTOSAR SoAdConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    connections: list[SocketConnection]
    socket_addresses: list[SocketAddress]
    def __init__(self) -> None:
        """Initialize SoAdConfig."""
        super().__init__()
        self.connections: list[SocketConnection] = []
        self.socket_addresses: list[SocketAddress] = []

    def serialize(self) -> ET.Element:
        """Serialize SoAdConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SoAdConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize connections (list to container "CONNECTIONS")
        if self.connections:
            wrapper = ET.Element("CONNECTIONS")
            for item in self.connections:
                serialized = SerializationHelper.serialize_item(item, "SocketConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize socket_addresses (list to container "SOCKET-ADDRESSES")
        if self.socket_addresses:
            wrapper = ET.Element("SOCKET-ADDRESSES")
            for item in self.socket_addresses:
                serialized = SerializationHelper.serialize_item(item, "SocketAddress")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SoAdConfig":
        """Deserialize XML element to SoAdConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SoAdConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SoAdConfig, cls).deserialize(element)

        # Parse connections (list from container "CONNECTIONS")
        obj.connections = []
        container = SerializationHelper.find_child_element(element, "CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.connections.append(child_value)

        # Parse socket_addresses (list from container "SOCKET-ADDRESSES")
        obj.socket_addresses = []
        container = SerializationHelper.find_child_element(element, "SOCKET-ADDRESSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.socket_addresses.append(child_value)

        return obj



class SoAdConfigBuilder(BuilderBase):
    """Builder for SoAdConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SoAdConfig = SoAdConfig()


    def with_connections(self, items: list[SocketConnection]) -> "SoAdConfigBuilder":
        """Set connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.connections = list(items) if items else []
        return self

    def with_socket_addresses(self, items: list[SocketAddress]) -> "SoAdConfigBuilder":
        """Set socket_addresses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.socket_addresses = list(items) if items else []
        return self


    def add_connection(self, item: SocketConnection) -> "SoAdConfigBuilder":
        """Add a single item to connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.connections.append(item)
        return self

    def clear_connections(self) -> "SoAdConfigBuilder":
        """Clear all items from connections list.

        Returns:
            self for method chaining
        """
        self._obj.connections = []
        return self

    def add_socket_addresse(self, item: SocketAddress) -> "SoAdConfigBuilder":
        """Add a single item to socket_addresses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.socket_addresses.append(item)
        return self

    def clear_socket_addresses(self) -> "SoAdConfigBuilder":
        """Clear all items from socket_addresses list.

        Returns:
            self for method chaining
        """
        self._obj.socket_addresses = []
        return self



    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> SoAdConfig:
        """Build and return the SoAdConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj