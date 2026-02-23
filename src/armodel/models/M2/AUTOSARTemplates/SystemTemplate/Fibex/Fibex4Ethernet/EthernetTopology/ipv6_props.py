"""Ipv6Props AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 147)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.dhcpv6_props import (
    Dhcpv6Props,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_fragmentation_props import (
    Ipv6FragmentationProps,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_ndp_props import (
    Ipv6NdpProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class Ipv6Props(ARObject):
    """AUTOSAR Ipv6Props."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dhcp_props: Optional[Dhcpv6Props]
    fragmentation: Optional[Ipv6FragmentationProps]
    ndp_props: Optional[Ipv6NdpProps]
    def __init__(self) -> None:
        """Initialize Ipv6Props."""
        super().__init__()
        self.dhcp_props: Optional[Dhcpv6Props] = None
        self.fragmentation: Optional[Ipv6FragmentationProps] = None
        self.ndp_props: Optional[Ipv6NdpProps] = None

    def serialize(self) -> ET.Element:
        """Serialize Ipv6Props to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(Ipv6Props, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dhcp_props
        if self.dhcp_props is not None:
            serialized = SerializationHelper.serialize_item(self.dhcp_props, "Dhcpv6Props")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DHCP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize fragmentation
        if self.fragmentation is not None:
            serialized = SerializationHelper.serialize_item(self.fragmentation, "Ipv6FragmentationProps")
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

        # Serialize ndp_props
        if self.ndp_props is not None:
            serialized = SerializationHelper.serialize_item(self.ndp_props, "Ipv6NdpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NDP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "Ipv6Props":
        """Deserialize XML element to Ipv6Props object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Ipv6Props object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Ipv6Props, cls).deserialize(element)

        # Parse dhcp_props
        child = SerializationHelper.find_child_element(element, "DHCP-PROPS")
        if child is not None:
            dhcp_props_value = SerializationHelper.deserialize_by_tag(child, "Dhcpv6Props")
            obj.dhcp_props = dhcp_props_value

        # Parse fragmentation
        child = SerializationHelper.find_child_element(element, "FRAGMENTATION")
        if child is not None:
            fragmentation_value = SerializationHelper.deserialize_by_tag(child, "Ipv6FragmentationProps")
            obj.fragmentation = fragmentation_value

        # Parse ndp_props
        child = SerializationHelper.find_child_element(element, "NDP-PROPS")
        if child is not None:
            ndp_props_value = SerializationHelper.deserialize_by_tag(child, "Ipv6NdpProps")
            obj.ndp_props = ndp_props_value

        return obj



class Ipv6PropsBuilder(BuilderBase):
    """Builder for Ipv6Props with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: Ipv6Props = Ipv6Props()


    def with_dhcp_props(self, value: Optional[Dhcpv6Props]) -> "Ipv6PropsBuilder":
        """Set dhcp_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.dhcp_props = value
        return self

    def with_fragmentation(self, value: Optional[Ipv6FragmentationProps]) -> "Ipv6PropsBuilder":
        """Set fragmentation attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.fragmentation = value
        return self

    def with_ndp_props(self, value: Optional[Ipv6NdpProps]) -> "Ipv6PropsBuilder":
        """Set ndp_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ndp_props = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # Get type hints for the class
        try:
            type_hints_dict = get_type_hints(type(self._obj))
        except Exception:
            # Cannot resolve type hints (e.g., forward references), skip validation
            return

        for attr_name, attr_type in type_hints_dict.items():
            if attr_name.startswith("_"):
                continue

            value = getattr(self._obj, attr_name)

            # Check required fields (not Optional)
            if value is None and not self._is_optional_type(attr_type):
                if mode == BuilderValidationMode.STRICT:
                    raise ValueError(
                        f"Required attribute '{attr_name}' is None"
                    )
                elif mode == BuilderValidationMode.LENIENT:
                    import warnings
                    warnings.warn(
                        f"Required attribute '{attr_name}' is None",
                        UserWarning
                    )

    @staticmethod
    def _is_optional_type(type_hint: Any) -> bool:
        """Check if a type hint is Optional.

        Args:
            type_hint: Type hint to check

        Returns:
            True if type is Optional, False otherwise
        """
        origin = getattr(type_hint, "__origin__", None)
        return origin is Union

    @staticmethod
    def _get_expected_type(type_hint: Any) -> type:
        """Extract expected type from type hint.

        Args:
            type_hint: Type hint to extract from

        Returns:
            Expected type
        """
        if isinstance(type_hint, str):
            return object
        origin = getattr(type_hint, "__origin__", None)
        if origin is Union:
            args = getattr(type_hint, "__args__", [])
            for arg in args:
                if arg is not type(None):
                    return arg
        elif origin is list:
            args = getattr(type_hint, "__args__", [object])
            return args[0] if args else object
        return type_hint if isinstance(type_hint, type) else object


    def build(self) -> Ipv6Props:
        """Build and return the Ipv6Props instance with validation."""
        self._validate_instance()
        pass
        return self._obj