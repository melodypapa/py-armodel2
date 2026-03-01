"""J1939TpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 623)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import TpConfigBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_connection import (
    J1939TpConnection,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.j1939_tp_node import (
    J1939TpNode,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939TpConfig(TpConfig):
    """AUTOSAR J1939TpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "J1939-TP-CONFIG"


    tp_addresses: list[TpAddress]
    tp_connections: list[J1939TpConnection]
    tp_nodes: list[J1939TpNode]
    _DESERIALIZE_DISPATCH = {
        "TP-ADDRESSES": lambda obj, elem: obj.tp_addresses.append(SerializationHelper.deserialize_by_tag(elem, "TpAddress")),
        "TP-CONNECTIONS": lambda obj, elem: obj.tp_connections.append(SerializationHelper.deserialize_by_tag(elem, "J1939TpConnection")),
        "TP-NODES": lambda obj, elem: obj.tp_nodes.append(SerializationHelper.deserialize_by_tag(elem, "J1939TpNode")),
    }


    def __init__(self) -> None:
        """Initialize J1939TpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[J1939TpConnection] = []
        self.tp_nodes: list[J1939TpNode] = []

    def serialize(self) -> ET.Element:
        """Serialize J1939TpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939TpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_addresses (list to container "TP-ADDRESSES")
        if self.tp_addresses:
            wrapper = ET.Element("TP-ADDRESSES")
            for item in self.tp_addresses:
                serialized = SerializationHelper.serialize_item(item, "TpAddress")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_connections (list to container "TP-CONNECTIONS")
        if self.tp_connections:
            wrapper = ET.Element("TP-CONNECTIONS")
            for item in self.tp_connections:
                serialized = SerializationHelper.serialize_item(item, "J1939TpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_nodes (list to container "TP-NODES")
        if self.tp_nodes:
            wrapper = ET.Element("TP-NODES")
            for item in self.tp_nodes:
                serialized = SerializationHelper.serialize_item(item, "J1939TpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939TpConfig":
        """Deserialize XML element to J1939TpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939TpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939TpConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "TP-ADDRESSES":
                obj.tp_addresses.append(SerializationHelper.deserialize_by_tag(child, "TpAddress"))
            elif tag == "TP-CONNECTIONS":
                obj.tp_connections.append(SerializationHelper.deserialize_by_tag(child, "J1939TpConnection"))
            elif tag == "TP-NODES":
                obj.tp_nodes.append(SerializationHelper.deserialize_by_tag(child, "J1939TpNode"))

        return obj



class J1939TpConfigBuilder(TpConfigBuilder):
    """Builder for J1939TpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939TpConfig = J1939TpConfig()


    def with_tp_addresses(self, items: list[TpAddress]) -> "J1939TpConfigBuilder":
        """Set tp_addresses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses = list(items) if items else []
        return self

    def with_tp_connections(self, items: list[J1939TpConnection]) -> "J1939TpConfigBuilder":
        """Set tp_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = list(items) if items else []
        return self

    def with_tp_nodes(self, items: list[J1939TpNode]) -> "J1939TpConfigBuilder":
        """Set tp_nodes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_nodes = list(items) if items else []
        return self


    def add_tp_address(self, item: TpAddress) -> "J1939TpConfigBuilder":
        """Add a single item to tp_addresses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses.append(item)
        return self

    def clear_tp_addresses(self) -> "J1939TpConfigBuilder":
        """Clear all items from tp_addresses list.

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses = []
        return self

    def add_tp_connection(self, item: J1939TpConnection) -> "J1939TpConfigBuilder":
        """Add a single item to tp_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_connections.append(item)
        return self

    def clear_tp_connections(self) -> "J1939TpConfigBuilder":
        """Clear all items from tp_connections list.

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = []
        return self

    def add_tp_node(self, item: J1939TpNode) -> "J1939TpConfigBuilder":
        """Add a single item to tp_nodes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_nodes.append(item)
        return self

    def clear_tp_nodes(self) -> "J1939TpConfigBuilder":
        """Clear all items from tp_nodes list.

        Returns:
            self for method chaining
        """
        self._obj.tp_nodes = []
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


    def build(self) -> J1939TpConfig:
        """Build and return the J1939TpConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj