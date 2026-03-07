"""EthIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 146)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_props import (
    Ipv4Props,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_props import (
    Ipv6Props,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthIpProps(ARElement):
    """AUTOSAR EthIpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETH-IP-PROPS"


    ipv4_props: Optional[Ipv4Props]
    ipv6_props: Optional[Ipv6Props]
    _DESERIALIZE_DISPATCH = {
        "IPV4-PROPS": lambda obj, elem: setattr(obj, "ipv4_props", SerializationHelper.deserialize_by_tag(elem, "Ipv4Props")),
        "IPV6-PROPS": lambda obj, elem: setattr(obj, "ipv6_props", SerializationHelper.deserialize_by_tag(elem, "Ipv6Props")),
    }


    def __init__(self) -> None:
        """Initialize EthIpProps."""
        super().__init__()
        self.ipv4_props: Optional[Ipv4Props] = None
        self.ipv6_props: Optional[Ipv6Props] = None

    def serialize(self) -> ET.Element:
        """Serialize EthIpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthIpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ipv4_props
        if self.ipv4_props is not None:
            serialized = SerializationHelper.serialize_item(self.ipv4_props, "Ipv4Props")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_props
        if self.ipv6_props is not None:
            serialized = SerializationHelper.serialize_item(self.ipv6_props, "Ipv6Props")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthIpProps":
        """Deserialize XML element to EthIpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthIpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthIpProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IPV4-PROPS":
                setattr(obj, "ipv4_props", SerializationHelper.deserialize_by_tag(child, "Ipv4Props"))
            elif tag == "IPV6-PROPS":
                setattr(obj, "ipv6_props", SerializationHelper.deserialize_by_tag(child, "Ipv6Props"))

        return obj



class EthIpPropsBuilder(ARElementBuilder):
    """Builder for EthIpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthIpProps = EthIpProps()


    def with_ipv4_props(self, value: Optional[Ipv4Props]) -> "EthIpPropsBuilder":
        """Set ipv4_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ipv4_props' is required and cannot be None")
        self._obj.ipv4_props = value
        return self

    def with_ipv6_props(self, value: Optional[Ipv6Props]) -> "EthIpPropsBuilder":
        """Set ipv6_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'ipv6_props' is required and cannot be None")
        self._obj.ipv6_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "ipv4Props",
        "ipv6Props",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> EthIpProps:
        """Build and return the EthIpProps instance with validation."""
        self._validate_instance()
        return self._obj