"""DoIpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 551)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_interface import (
    DoIpInterface,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class DoIpConfig(ARObject):
    """AUTOSAR DoIpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DO-IP-CONFIG"


    doip_interfaces: list[DoIpInterface]
    logic_address: Optional[DoIpLogicAddress]
    _DESERIALIZE_DISPATCH = {
        "DOIP-INTERFACES": lambda obj, elem: obj.doip_interfaces.append(SerializationHelper.deserialize_by_tag(elem, "DoIpInterface")),
        "LOGIC-ADDRESS": lambda obj, elem: setattr(obj, "logic_address", SerializationHelper.deserialize_by_tag(elem, "DoIpLogicAddress")),
    }


    def __init__(self) -> None:
        """Initialize DoIpConfig."""
        super().__init__()
        self.doip_interfaces: list[DoIpInterface] = []
        self.logic_address: Optional[DoIpLogicAddress] = None

    def serialize(self) -> ET.Element:
        """Serialize DoIpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize doip_interfaces (list to container "DOIP-INTERFACES")
        if self.doip_interfaces:
            wrapper = ET.Element("DOIP-INTERFACES")
            for item in self.doip_interfaces:
                serialized = SerializationHelper.serialize_item(item, "DoIpInterface")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize logic_address
        if self.logic_address is not None:
            serialized = SerializationHelper.serialize_item(self.logic_address, "DoIpLogicAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOGIC-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpConfig":
        """Deserialize XML element to DoIpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpConfig, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DOIP-INTERFACES":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.doip_interfaces.append(SerializationHelper.deserialize_by_tag(item_elem, "DoIpInterface"))
            elif tag == "LOGIC-ADDRESS":
                setattr(obj, "logic_address", SerializationHelper.deserialize_by_tag(child, "DoIpLogicAddress"))

        return obj



class DoIpConfigBuilder(BuilderBase):
    """Builder for DoIpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpConfig = DoIpConfig()


    def with_doip_interfaces(self, items: list[DoIpInterface]) -> "DoIpConfigBuilder":
        """Set doip_interfaces list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.doip_interfaces = list(items) if items else []
        return self

    def with_logic_address(self, value: Optional[DoIpLogicAddress]) -> "DoIpConfigBuilder":
        """Set logic_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.logic_address = value
        return self


    def add_doip_interface(self, item: DoIpInterface) -> "DoIpConfigBuilder":
        """Add a single item to doip_interfaces list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.doip_interfaces.append(item)
        return self

    def clear_doip_interfaces(self) -> "DoIpConfigBuilder":
        """Clear all items from doip_interfaces list.

        Returns:
            self for method chaining
        """
        self._obj.doip_interfaces = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "doipInterface",
        "logicAddress",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DoIpConfig:
        """Build and return the DoIpConfig instance with validation."""
        self._validate_instance()
        return self._obj