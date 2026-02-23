"""DhcpServerConfiguration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 131)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv4_dhcp_server_configuration import (
    Ipv4DhcpServerConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ipv6_dhcp_server_configuration import (
    Ipv6DhcpServerConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DhcpServerConfiguration(ARObject):
    """AUTOSAR DhcpServerConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ipv4_dhcp_server: Optional[Ipv4DhcpServerConfiguration]
    ipv6_dhcp_server: Optional[Ipv6DhcpServerConfiguration]
    def __init__(self) -> None:
        """Initialize DhcpServerConfiguration."""
        super().__init__()
        self.ipv4_dhcp_server: Optional[Ipv4DhcpServerConfiguration] = None
        self.ipv6_dhcp_server: Optional[Ipv6DhcpServerConfiguration] = None

    def serialize(self) -> ET.Element:
        """Serialize DhcpServerConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DhcpServerConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ipv4_dhcp_server
        if self.ipv4_dhcp_server is not None:
            serialized = SerializationHelper.serialize_item(self.ipv4_dhcp_server, "Ipv4DhcpServerConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-DHCP-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_dhcp_server
        if self.ipv6_dhcp_server is not None:
            serialized = SerializationHelper.serialize_item(self.ipv6_dhcp_server, "Ipv6DhcpServerConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-DHCP-SERVER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DhcpServerConfiguration":
        """Deserialize XML element to DhcpServerConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DhcpServerConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DhcpServerConfiguration, cls).deserialize(element)

        # Parse ipv4_dhcp_server
        child = SerializationHelper.find_child_element(element, "IPV4-DHCP-SERVER")
        if child is not None:
            ipv4_dhcp_server_value = SerializationHelper.deserialize_by_tag(child, "Ipv4DhcpServerConfiguration")
            obj.ipv4_dhcp_server = ipv4_dhcp_server_value

        # Parse ipv6_dhcp_server
        child = SerializationHelper.find_child_element(element, "IPV6-DHCP-SERVER")
        if child is not None:
            ipv6_dhcp_server_value = SerializationHelper.deserialize_by_tag(child, "Ipv6DhcpServerConfiguration")
            obj.ipv6_dhcp_server = ipv6_dhcp_server_value

        return obj



class DhcpServerConfigurationBuilder(BuilderBase):
    """Builder for DhcpServerConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DhcpServerConfiguration = DhcpServerConfiguration()


    def with_ipv4_dhcp_server(self, value: Optional[Ipv4DhcpServerConfiguration]) -> "DhcpServerConfigurationBuilder":
        """Set ipv4_dhcp_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv4_dhcp_server = value
        return self

    def with_ipv6_dhcp_server(self, value: Optional[Ipv6DhcpServerConfiguration]) -> "DhcpServerConfigurationBuilder":
        """Set ipv6_dhcp_server attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv6_dhcp_server = value
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


    def build(self) -> DhcpServerConfiguration:
        """Build and return the DhcpServerConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj