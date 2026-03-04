"""LinTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 614)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import TpConfigBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_connection import (
    LinTpConnection,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.lin_tp_node import (
    LinTpNode,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_address import (
    TpAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class LinTpConfig(TpConfig):
    """AUTOSAR LinTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "LIN-TP-CONFIG"


    tp_addresses: list[TpAddress]
    tp_connections: list[LinTpConnection]
    tp_nodes: list[LinTpNode]
    _DESERIALIZE_DISPATCH = {
        "TP-ADDRESSS": lambda obj, elem: obj.tp_addresses.append(SerializationHelper.deserialize_by_tag(elem, "TpAddress")),
        "TP-CONNECTIONS": lambda obj, elem: obj.tp_connections.append(SerializationHelper.deserialize_by_tag(elem, "LinTpConnection")),
        "TP-NODES": lambda obj, elem: obj.tp_nodes.append(SerializationHelper.deserialize_by_tag(elem, "LinTpNode")),
    }


    def __init__(self) -> None:
        """Initialize LinTpConfig."""
        super().__init__()
        self.tp_addresses: list[TpAddress] = []
        self.tp_connections: list[LinTpConnection] = []
        self.tp_nodes: list[LinTpNode] = []

    def serialize(self) -> ET.Element:
        """Serialize LinTpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(LinTpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tp_addresses (list to container "TP-ADDRESSS")
        if self.tp_addresses:
            wrapper = ET.Element("TP-ADDRESSS")
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
                serialized = SerializationHelper.serialize_item(item, "LinTpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_nodes (list to container "TP-NODES")
        if self.tp_nodes:
            wrapper = ET.Element("TP-NODES")
            for item in self.tp_nodes:
                serialized = SerializationHelper.serialize_item(item, "LinTpNode")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinTpConfig":
        """Deserialize XML element to LinTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(LinTpConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TP-ADDRESSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tp_addresses.append(SerializationHelper.deserialize_by_tag(item_elem, "TpAddress"))
            elif tag == "TP-CONNECTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tp_connections.append(SerializationHelper.deserialize_by_tag(item_elem, "LinTpConnection"))
            elif tag == "TP-NODES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tp_nodes.append(SerializationHelper.deserialize_by_tag(item_elem, "LinTpNode"))

        return obj



class LinTpConfigBuilder(TpConfigBuilder):
    """Builder for LinTpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: LinTpConfig = LinTpConfig()


    def with_tp_addresses(self, items: list[TpAddress]) -> "LinTpConfigBuilder":
        """Set tp_addresses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses = list(items) if items else []
        return self

    def with_tp_connections(self, items: list[LinTpConnection]) -> "LinTpConfigBuilder":
        """Set tp_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = list(items) if items else []
        return self

    def with_tp_nodes(self, items: list[LinTpNode]) -> "LinTpConfigBuilder":
        """Set tp_nodes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_nodes = list(items) if items else []
        return self


    def add_tp_address(self, item: TpAddress) -> "LinTpConfigBuilder":
        """Add a single item to tp_addresses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses.append(item)
        return self

    def clear_tp_addresses(self) -> "LinTpConfigBuilder":
        """Clear all items from tp_addresses list.

        Returns:
            self for method chaining
        """
        self._obj.tp_addresses = []
        return self

    def add_tp_connection(self, item: LinTpConnection) -> "LinTpConfigBuilder":
        """Add a single item to tp_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_connections.append(item)
        return self

    def clear_tp_connections(self) -> "LinTpConfigBuilder":
        """Clear all items from tp_connections list.

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = []
        return self

    def add_tp_node(self, item: LinTpNode) -> "LinTpConfigBuilder":
        """Add a single item to tp_nodes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_nodes.append(item)
        return self

    def clear_tp_nodes(self) -> "LinTpConfigBuilder":
        """Clear all items from tp_nodes list.

        Returns:
            self for method chaining
        """
        self._obj.tp_nodes = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tpAddress",
        "tpConnection",
        "tpNode",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> LinTpConfig:
        """Build and return the LinTpConfig instance with validation."""
        self._validate_instance()
        return self._obj