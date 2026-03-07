"""UdpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 154)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class UdpProps(ARObject):
    """AUTOSAR UdpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "UDP-PROPS"


    udp_ttl: Optional[PositiveInteger]
    _DESERIALIZE_DISPATCH = {
        "UDP-TTL": lambda obj, elem: setattr(obj, "udp_ttl", SerializationHelper.deserialize_by_tag(elem, "PositiveInteger")),
    }


    def __init__(self) -> None:
        """Initialize UdpProps."""
        super().__init__()
        self.udp_ttl: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize UdpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(UdpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize udp_ttl
        if self.udp_ttl is not None:
            serialized = SerializationHelper.serialize_item(self.udp_ttl, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDP-TTL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "UdpProps":
        """Deserialize XML element to UdpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized UdpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(UdpProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "UDP-TTL":
                setattr(obj, "udp_ttl", SerializationHelper.deserialize_by_tag(child, "PositiveInteger"))

        return obj



class UdpPropsBuilder(BuilderBase):
    """Builder for UdpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: UdpProps = UdpProps()


    def with_udp_ttl(self, value: Optional[PositiveInteger]) -> "UdpPropsBuilder":
        """Set udp_ttl attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'udp_ttl' is required and cannot be None")
        self._obj.udp_ttl = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "udpTtl",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> UdpProps:
        """Build and return the UdpProps instance with validation."""
        self._validate_instance()
        return self._obj