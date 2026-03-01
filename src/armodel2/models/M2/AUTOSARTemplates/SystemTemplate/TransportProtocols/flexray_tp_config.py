"""FlexrayTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 592)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import TpConfigBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_connection import (
    FlexrayTpConnection,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_ecu import (
    FlexrayTpEcu,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_node import (
    FlexrayTpNode,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.flexray_tp_pdu_pool import (
    FlexrayTpPduPool,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class FlexrayTpConfig(TpConfig):
    """AUTOSAR FlexrayTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "FLEXRAY-TP-CONFIG"


    pdu_pools: list[FlexrayTpPduPool]
    tp_addresses: list[TpAddress]
    tp_connections: list[FlexrayTpConnection]
    tp_ecus: list[FlexrayTpEcu]
    tp_nodes: list[FlexrayTpNode]
    _DESERIALIZE_DISPATCH = {
        "PDU-POOLS": lambda obj, elem: obj.pdu_pools.append(SerializationHelper.deserialize_by_tag(elem, "FlexrayTpPduPool")),
        "TP-ADDRESSES": lambda obj, elem: obj.tp_addresses.append(SerializationHelper.deserialize_by_tag(elem, "TpAddress")),
        "TP-CONNECTIONS": lambda obj, elem: obj.tp_connections.append(SerializationHelper.deserialize_by_tag(elem, "FlexrayTpConnection")),
        "TP-ECUS": lambda obj, elem: obj.tp_ecus.append(SerializationHelper.deserialize_by_tag(elem, "FlexrayTpEcu")),
        "TP-NODES": lambda obj, elem: obj.tp_nodes.append(SerializationHelper.deserialize_by_tag(elem, "FlexrayTpNode")),
    }


    def __init__(self) -> None:
        """Initialize FlexrayTpConfig."""
        super().__init__()
        self.pdu_pools: list[FlexrayTpPduPool] = []
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[FlexrayTpConnection] = []
        self.tp_ecus: list[FlexrayTpEcu] = []
        self.tp_nodes: list[FlexrayTpNode] = []

    def serialize(self) -> ET.Element:
        """Serialize FlexrayTpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(FlexrayTpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize pdu_pools (list to container "PDU-POOLS")
        if self.pdu_pools:
            wrapper = ET.Element("PDU-POOLS")
            for item in self.pdu_pools:
                serialized = SerializationHelper.serialize_item(item, "FlexrayTpPduPool")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

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
                serialized = SerializationHelper.serialize_item(item, "FlexrayTpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_ecus (list to container "TP-ECUS")
        if self.tp_ecus:
            wrapper = ET.Element("TP-ECUS")
            for item in self.tp_ecus:
                serialized = SerializationHelper.serialize_item(item, "FlexrayTpEcu")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_nodes (list to container "TP-NODES")
        if self.tp_nodes:
            wrapper = ET.Element("TP-NODES")
            for item in self.tp_nodes:
                serialized = SerializationHelper.serialize_item(item, "FlexrayTpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "FlexrayTpConfig":
        """Deserialize XML element to FlexrayTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized FlexrayTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(FlexrayTpConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "PDU-POOLS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.pdu_pools.append(SerializationHelper.deserialize_by_tag(item_elem, "FlexrayTpPduPool"))
            elif tag == "TP-ADDRESSES":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.tp_addresses.append(SerializationHelper.deserialize_by_tag(item_elem, "TpAddress"))
            elif tag == "TP-CONNECTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.tp_connections.append(SerializationHelper.deserialize_by_tag(item_elem, "FlexrayTpConnection"))
            elif tag == "TP-ECUS":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.tp_ecus.append(SerializationHelper.deserialize_by_tag(item_elem, "FlexrayTpEcu"))
            elif tag == "TP-NODES":
                # Iterate through wrapper children
                for item_elem in child:
                    item_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    obj.tp_nodes.append(SerializationHelper.deserialize_by_tag(item_elem, "FlexrayTpNode"))

        return obj



class FlexrayTpConfigBuilder(TpConfigBuilder):
    """Builder for FlexrayTpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: FlexrayTpConfig = FlexrayTpConfig()


    def with_pdu_pools(self, items: list[FlexrayTpPduPool]) -> "FlexrayTpConfigBuilder":
        """Set pdu_pools list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.pdu_pools = list(items) if items else []
        return self

    def with_tp_addresses(self, items: list[TpAddress]) -> "FlexrayTpConfigBuilder":
        """Set tp_addresses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses = list(items) if items else []
        return self

    def with_tp_connections(self, items: list[FlexrayTpConnection]) -> "FlexrayTpConfigBuilder":
        """Set tp_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = list(items) if items else []
        return self

    def with_tp_ecus(self, items: list[FlexrayTpEcu]) -> "FlexrayTpConfigBuilder":
        """Set tp_ecus list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_ecus = list(items) if items else []
        return self

    def with_tp_nodes(self, items: list[FlexrayTpNode]) -> "FlexrayTpConfigBuilder":
        """Set tp_nodes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_nodes = list(items) if items else []
        return self


    def add_pdu_pool(self, item: FlexrayTpPduPool) -> "FlexrayTpConfigBuilder":
        """Add a single item to pdu_pools list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.pdu_pools.append(item)
        return self

    def clear_pdu_pools(self) -> "FlexrayTpConfigBuilder":
        """Clear all items from pdu_pools list.

        Returns:
            self for method chaining
        """
        self._obj.pdu_pools = []
        return self

    def add_tp_address(self, item: TpAddress) -> "FlexrayTpConfigBuilder":
        """Add a single item to tp_addresses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses.append(item)
        return self

    def clear_tp_addresses(self) -> "FlexrayTpConfigBuilder":
        """Clear all items from tp_addresses list.

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses = []
        return self

    def add_tp_connection(self, item: FlexrayTpConnection) -> "FlexrayTpConfigBuilder":
        """Add a single item to tp_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_connections.append(item)
        return self

    def clear_tp_connections(self) -> "FlexrayTpConfigBuilder":
        """Clear all items from tp_connections list.

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = []
        return self

    def add_tp_ecu(self, item: FlexrayTpEcu) -> "FlexrayTpConfigBuilder":
        """Add a single item to tp_ecus list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_ecus.append(item)
        return self

    def clear_tp_ecus(self) -> "FlexrayTpConfigBuilder":
        """Clear all items from tp_ecus list.

        Returns:
            self for method chaining
        """
        self._obj.tp_ecus = []
        return self

    def add_tp_node(self, item: FlexrayTpNode) -> "FlexrayTpConfigBuilder":
        """Add a single item to tp_nodes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_nodes.append(item)
        return self

    def clear_tp_nodes(self) -> "FlexrayTpConfigBuilder":
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


    def build(self) -> FlexrayTpConfig:
        """Build and return the FlexrayTpConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj