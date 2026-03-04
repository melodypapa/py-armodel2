"""StreamFilterMACAddress AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 137)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MacAddressString,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class StreamFilterMACAddress(ARObject):
    """AUTOSAR StreamFilterMACAddress."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "STREAM-FILTER-M-A-C-ADDRESS"


    mac_address_string: Optional[MacAddressString]
    _DESERIALIZE_DISPATCH = {
        "MAC-ADDRESS-STRING": lambda obj, elem: setattr(obj, "mac_address_string", SerializationHelper.deserialize_by_tag(elem, "MacAddressString")),
    }


    def __init__(self) -> None:
        """Initialize StreamFilterMACAddress."""
        super().__init__()
        self.mac_address_string: Optional[MacAddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize StreamFilterMACAddress to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(StreamFilterMACAddress, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mac_address_string
        if self.mac_address_string is not None:
            serialized = SerializationHelper.serialize_item(self.mac_address_string, "MacAddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAC-ADDRESS-STRING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "StreamFilterMACAddress":
        """Deserialize XML element to StreamFilterMACAddress object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized StreamFilterMACAddress object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(StreamFilterMACAddress, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "MAC-ADDRESS-STRING":
                setattr(obj, "mac_address_string", SerializationHelper.deserialize_by_tag(child, "MacAddressString"))

        return obj



class StreamFilterMACAddressBuilder(BuilderBase):
    """Builder for StreamFilterMACAddress with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: StreamFilterMACAddress = StreamFilterMACAddress()


    def with_mac_address_string(self, value: Optional[MacAddressString]) -> "StreamFilterMACAddressBuilder":
        """Set mac_address_string attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.mac_address_string = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "macAddressString",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> StreamFilterMACAddress:
        """Build and return the StreamFilterMACAddress instance with validation."""
        self._validate_instance()
        return self._obj