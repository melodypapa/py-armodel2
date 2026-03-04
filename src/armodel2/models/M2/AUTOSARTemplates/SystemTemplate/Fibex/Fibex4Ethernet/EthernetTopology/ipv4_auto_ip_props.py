"""Ipv4AutoIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 147)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Ipv4AutoIpProps(ARObject):
    """AUTOSAR Ipv4AutoIpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IPV4-AUTO-IP-PROPS"


    tcp_ip_auto_ip_init: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "TCP-IP-AUTO-IP-INIT": lambda obj, elem: setattr(obj, "tcp_ip_auto_ip_init", SerializationHelper.deserialize_by_tag(elem, "TimeValue")),
    }


    def __init__(self) -> None:
        """Initialize Ipv4AutoIpProps."""
        super().__init__()
        self.tcp_ip_auto_ip_init: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4AutoIpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv4AutoIpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_ip_auto_ip_init
        if self.tcp_ip_auto_ip_init is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_ip_auto_ip_init, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-IP-AUTO-IP-INIT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4AutoIpProps":
        """Deserialize XML element to Ipv4AutoIpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4AutoIpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv4AutoIpProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "TCP-IP-AUTO-IP-INIT":
                setattr(obj, "tcp_ip_auto_ip_init", SerializationHelper.deserialize_by_tag(child, "TimeValue"))

        return obj



class Ipv4AutoIpPropsBuilder(BuilderBase):
    """Builder for Ipv4AutoIpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv4AutoIpProps = Ipv4AutoIpProps()


    def with_tcp_ip_auto_ip_init(self, value: Optional[TimeValue]) -> "Ipv4AutoIpPropsBuilder":
        """Set tcp_ip_auto_ip_init attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_ip_auto_ip_init = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "tcpIpAutoIpInit",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Ipv4AutoIpProps:
        """Build and return the Ipv4AutoIpProps instance with validation."""
        self._validate_instance()
        return self._obj