"""StreamFilterIpv4Address AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class StreamFilterIpv4Address(ARObject):
    """AUTOSAR StreamFilterIpv4Address."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STREAM-FILTER-IPV4-ADDRESS"


    ipv4_address: Optional[Ip4AddressString]
    _DESERIALIZE_DISPATCH = {
        "IPV4-ADDRESS": lambda obj, elem: setattr(obj, "ipv4_address", SerializationHelper.deserialize_by_tag(elem, "Ip4AddressString")),
    }


    def __init__(self) -> None:
        """Initialize StreamFilterIpv4Address."""
        super().__init__()
        self.ipv4_address: Optional[Ip4AddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterIpv4Address to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StreamFilterIpv4Address, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ipv4_address
        if self.ipv4_address is not None:
            serialized = SerializationHelper.serialize_item(self.ipv4_address, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterIpv4Address":
        """Deserialize XML element to StreamFilterIpv4Address object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterIpv4Address object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StreamFilterIpv4Address, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IPV4-ADDRESS":
                setattr(obj, "ipv4_address", SerializationHelper.deserialize_by_tag(child, "Ip4AddressString"))

        return obj



class StreamFilterIpv4AddressBuilder(BuilderBase):
    """Builder for StreamFilterIpv4Address with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StreamFilterIpv4Address = StreamFilterIpv4Address()


    def with_ipv4_address(self, value: Optional[Ip4AddressString]) -> "StreamFilterIpv4AddressBuilder":
        """Set ipv4_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv4_address = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ipv4Address",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> StreamFilterIpv4Address:
        """Build and return the StreamFilterIpv4Address instance with validation."""
        self._validate_instance()
        return self._obj