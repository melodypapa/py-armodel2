"""Ipv4Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_arp_props import (
    Ipv4ArpProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_auto_ip_props import (
    Ipv4AutoIpProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_fragmentation_props import (
    Ipv4FragmentationProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class Ipv4Props(ARObject):
    """AUTOSAR Ipv4Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "IPV4-PROPS"


    arp_props: Optional[Ipv4ArpProps]
    auto_ip_props: Optional[Ipv4AutoIpProps]
    fragmentation: Optional[Ipv4FragmentationProps]
    _DESERIALIZE_DISPATCH = {
        "ARP-PROPS": lambda obj, elem: setattr(obj, "arp_props", SerializationHelper.deserialize_by_tag(elem, "Ipv4ArpProps")),
        "AUTO-IP-PROPS": lambda obj, elem: setattr(obj, "auto_ip_props", SerializationHelper.deserialize_by_tag(elem, "Ipv4AutoIpProps")),
        "FRAGMENTATION": lambda obj, elem: setattr(obj, "fragmentation", SerializationHelper.deserialize_by_tag(elem, "Ipv4FragmentationProps")),
    }


    def __init__(self) -> None:
        """Initialize Ipv4Props."""
        super().__init__()
        self.arp_props: Optional[Ipv4ArpProps] = None
        self.auto_ip_props: Optional[Ipv4AutoIpProps] = None
        self.fragmentation: Optional[Ipv4FragmentationProps] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv4Props to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv4Props, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize arp_props
        if self.arp_props is not None:
            serialized = SerializationHelper.serialize_item(self.arp_props, "Ipv4ArpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ARP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize auto_ip_props
        if self.auto_ip_props is not None:
            serialized = SerializationHelper.serialize_item(self.auto_ip_props, "Ipv4AutoIpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTO-IP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fragmentation
        if self.fragmentation is not None:
            serialized = SerializationHelper.serialize_item(self.fragmentation, "Ipv4FragmentationProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FRAGMENTATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv4Props":
        """Deserialize XML element to Ipv4Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv4Props object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv4Props, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "ARP-PROPS":
                setattr(obj, "arp_props", SerializationHelper.deserialize_by_tag(child, "Ipv4ArpProps"))
            elif tag == "AUTO-IP-PROPS":
                setattr(obj, "auto_ip_props", SerializationHelper.deserialize_by_tag(child, "Ipv4AutoIpProps"))
            elif tag == "FRAGMENTATION":
                setattr(obj, "fragmentation", SerializationHelper.deserialize_by_tag(child, "Ipv4FragmentationProps"))

        return obj



class Ipv4PropsBuilder(BuilderBase):
    """Builder for Ipv4Props with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv4Props = Ipv4Props()


    def with_arp_props(self, value: Optional[Ipv4ArpProps]) -> "Ipv4PropsBuilder":
        """Set arp_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'arp_props' is required and cannot be None")
        self._obj.arp_props = value
        return self

    def with_auto_ip_props(self, value: Optional[Ipv4AutoIpProps]) -> "Ipv4PropsBuilder":
        """Set auto_ip_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'auto_ip_props' is required and cannot be None")
        self._obj.auto_ip_props = value
        return self

    def with_fragmentation(self, value: Optional[Ipv4FragmentationProps]) -> "Ipv4PropsBuilder":
        """Set fragmentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'fragmentation' is required and cannot be None")
        self._obj.fragmentation = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "arpProps",
        "autoIpProps",
        "fragmentation",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> Ipv4Props:
        """Build and return the Ipv4Props instance with validation."""
        self._validate_instance()
        return self._obj