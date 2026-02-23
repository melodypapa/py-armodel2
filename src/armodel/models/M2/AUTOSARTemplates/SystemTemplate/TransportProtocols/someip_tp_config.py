"""SomeipTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 619)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import TpConfigBuilder
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_channel import (
    SomeipTpChannel,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.someip_tp_connection import (
    SomeipTpConnection,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class SomeipTpConfig(TpConfig):
    """AUTOSAR SomeipTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tp_channels: list[SomeipTpChannel]
    tp_connections: list[SomeipTpConnection]
    def __init__(self) -> None:
        """Initialize SomeipTpConfig."""
        super().__init__()
        self.tp_channels: list[SomeipTpChannel] = []
        self.tp_connections: list[SomeipTpConnection] = []

    def serialize(self) -> ET.Element:
        """Serialize SomeipTpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SomeipTpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_channels (list to container "TP-CHANNELS")
        if self.tp_channels:
            wrapper = ET.Element("TP-CHANNELS")
            for item in self.tp_channels:
                serialized = SerializationHelper.serialize_item(item, "SomeipTpChannel")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_connections (list to container "TP-CONNECTIONS")
        if self.tp_connections:
            wrapper = ET.Element("TP-CONNECTIONS")
            for item in self.tp_connections:
                serialized = SerializationHelper.serialize_item(item, "SomeipTpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SomeipTpConfig":
        """Deserialize XML element to SomeipTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SomeipTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SomeipTpConfig, cls).deserialize(element)

        # Parse tp_channels (list from container "TP-CHANNELS")
        obj.tp_channels = []
        container = SerializationHelper.find_child_element(element, "TP-CHANNELS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_channels.append(child_value)

        # Parse tp_connections (list from container "TP-CONNECTIONS")
        obj.tp_connections = []
        container = SerializationHelper.find_child_element(element, "TP-CONNECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.tp_connections.append(child_value)

        return obj



class SomeipTpConfigBuilder(TpConfigBuilder):
    """Builder for SomeipTpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SomeipTpConfig = SomeipTpConfig()


    def with_tp_channels(self, items: list[SomeipTpChannel]) -> "SomeipTpConfigBuilder":
        """Set tp_channels list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_channels = list(items) if items else []
        return self

    def with_tp_connections(self, items: list[SomeipTpConnection]) -> "SomeipTpConfigBuilder":
        """Set tp_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = list(items) if items else []
        return self


    def add_tp_channel(self, item: SomeipTpChannel) -> "SomeipTpConfigBuilder":
        """Add a single item to tp_channels list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_channels.append(item)
        return self

    def clear_tp_channels(self) -> "SomeipTpConfigBuilder":
        """Clear all items from tp_channels list.

        Returns:
            self for method chaining
        """
        self._obj.tp_channels = []
        return self

    def add_tp_connection(self, item: SomeipTpConnection) -> "SomeipTpConfigBuilder":
        """Add a single item to tp_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_connections.append(item)
        return self

    def clear_tp_connections(self) -> "SomeipTpConfigBuilder":
        """Clear all items from tp_connections list.

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = []
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


    def build(self) -> SomeipTpConfig:
        """Build and return the SomeipTpConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj