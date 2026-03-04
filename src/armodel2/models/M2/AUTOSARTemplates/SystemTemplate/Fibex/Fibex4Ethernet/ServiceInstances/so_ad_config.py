"""SoAdConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 451)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.socket_address import (
    SocketAddress,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.socket_connection import (
    SocketConnection,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SoAdConfig(ARObject):
    """AUTOSAR SoAdConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SO-AD-CONFIG"


    connections: list[SocketConnection]
    socket_addresses: list[SocketAddress]
    _DESERIALIZE_DISPATCH = {
        "CONNECTIONS": lambda obj, elem: obj.connections.append(SerializationHelper.deserialize_by_tag(elem, "SocketConnection")),
        "SOCKET-ADDRESSS": lambda obj, elem: obj.socket_addresses.append(SerializationHelper.deserialize_by_tag(elem, "SocketAddress")),
    }


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
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Serialize socket_addresses (list to container "SOCKET-ADDRESSS")
        if self.socket_addresses:
            wrapper = ET.Element("SOCKET-ADDRESSS")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "CONNECTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.connections.append(SerializationHelper.deserialize_by_tag(item_elem, "SocketConnection"))
            elif tag == "SOCKET-ADDRESSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.socket_addresses.append(SerializationHelper.deserialize_by_tag(item_elem, "SocketAddress"))

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

    def add_socket_address(self, item: SocketAddress) -> "SoAdConfigBuilder":
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


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "connection",
        "socketAddress",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SoAdConfig:
        """Build and return the SoAdConfig instance with validation."""
        self._validate_instance()
        return self._obj