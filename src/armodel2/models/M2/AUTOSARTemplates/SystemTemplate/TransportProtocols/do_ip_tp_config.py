"""DoIpTpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 555)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_TransportProtocols.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import (
    TpConfig,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.tp_config import TpConfigBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DiagnosticConnection.do_ip_tp_connection import (
    DoIpTpConnection,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DoIpTpConfig(TpConfig):
    """AUTOSAR DoIpTpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DO-IP-TP-CONFIG"


    do_ip_logic_address_addresses: list[DoIpLogicAddress]
    tp_connections: list[DoIpTpConnection]
    _DESERIALIZE_DISPATCH = {
        "DO-IP-LOGIC-ADDRESS-ADDRESSS": lambda obj, elem: obj.do_ip_logic_address_addresses.append(SerializationHelper.deserialize_by_tag(elem, "DoIpLogicAddress")),
        "TP-CONNECTIONS": lambda obj, elem: obj.tp_connections.append(SerializationHelper.deserialize_by_tag(elem, "DoIpTpConnection")),
    }


    def __init__(self) -> None:
        """Initialize DoIpTpConfig."""
        super().__init__()
        self.do_ip_logic_address_addresses: list[DoIpLogicAddress] = []
        self.tp_connections: list[DoIpTpConnection] = []

    def serialize(self) -> ET.Element:
        """Serialize DoIpTpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpTpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize do_ip_logic_address_addresses (list to container "DO-IP-LOGIC-ADDRESS-ADDRESSS")
        if self.do_ip_logic_address_addresses:
            wrapper = ET.Element("DO-IP-LOGIC-ADDRESS-ADDRESSS")
            for item in self.do_ip_logic_address_addresses:
                serialized = SerializationHelper.serialize_item(item, "DoIpLogicAddress")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize tp_connections (list to container "TP-CONNECTIONS")
        if self.tp_connections:
            wrapper = ET.Element("TP-CONNECTIONS")
            for item in self.tp_connections:
                serialized = SerializationHelper.serialize_item(item, "DoIpTpConnection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpTpConfig":
        """Deserialize XML element to DoIpTpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpTpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpTpConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DO-IP-LOGIC-ADDRESS-ADDRESSS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.do_ip_logic_address_addresses.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpLogicAddress"))
            elif tag == "TP-CONNECTIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.tp_connections.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpTpConnection"))

        return obj



class DoIpTpConfigBuilder(TpConfigBuilder):
    """Builder for DoIpTpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpTpConfig = DoIpTpConfig()


    def with_do_ip_logic_address_addresses(self, items: list[DoIpLogicAddress]) -> "DoIpTpConfigBuilder":
        """Set do_ip_logic_address_addresses list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.do_ip_logic_address_addresses = list(items) if items else []
        return self

    def with_tp_connections(self, items: list[DoIpTpConnection]) -> "DoIpTpConfigBuilder":
        """Set tp_connections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = list(items) if items else []
        return self


    def add_do_ip_logic_address_address(self, item: DoIpLogicAddress) -> "DoIpTpConfigBuilder":
        """Add a single item to do_ip_logic_address_addresses list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.do_ip_logic_address_addresses.append(item)
        return self

    def clear_do_ip_logic_address_addresses(self) -> "DoIpTpConfigBuilder":
        """Clear all items from do_ip_logic_address_addresses list.

        Returns:
            self for method chaining
        """
        self._obj.do_ip_logic_address_addresses = []
        return self

    def add_tp_connection(self, item: DoIpTpConnection) -> "DoIpTpConfigBuilder":
        """Add a single item to tp_connections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.tp_connections.append(item)
        return self

    def clear_tp_connections(self) -> "DoIpTpConfigBuilder":
        """Clear all items from tp_connections list.

        Returns:
            self for method chaining
        """
        self._obj.tp_connections = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "doIpLogicAddressAddress",
        "tpConnection",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DoIpTpConfig:
        """Build and return the DoIpTpConfig instance with validation."""
        self._validate_instance()
        return self._obj