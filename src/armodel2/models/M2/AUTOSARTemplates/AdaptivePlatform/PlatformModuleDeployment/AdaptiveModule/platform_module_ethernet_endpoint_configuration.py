"""PlatformModuleEthernetEndpointConfiguration AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_SecurityExtractTemplate.pdf (page 65)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_AdaptivePlatform_PlatformModuleDeployment_AdaptiveModule.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Ip4AddressString,
    Ip6AddressString,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.ethernet_communication_connector import (
    EthernetCommunicationConnector,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PlatformModuleEthernetEndpointConfiguration(ARElement):
    """AUTOSAR PlatformModuleEthernetEndpointConfiguration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PLATFORM-MODULE-ETHERNET-ENDPOINT-CONFIGURATION"


    communication_connector_ref: Optional[ARRef]
    ipv4_multicast_ip_address: Optional[Ip4AddressString]
    ipv6_multicast_ip_address: Optional[Ip6AddressString]
    _DESERIALIZE_DISPATCH = {
        "COMMUNICATION-CONNECTOR-REF": lambda obj, elem: setattr(obj, "communication_connector_ref", ARRef.deserialize(elem)),
        "IPV4-MULTICAST-IP-ADDRESS": lambda obj, elem: setattr(obj, "ipv4_multicast_ip_address", SerializationHelper.deserialize_by_tag(elem, "Ip4AddressString")),
        "IPV6-MULTICAST-IP-ADDRESS": lambda obj, elem: setattr(obj, "ipv6_multicast_ip_address", SerializationHelper.deserialize_by_tag(elem, "Ip6AddressString")),
    }


    def __init__(self) -> None:
        """Initialize PlatformModuleEthernetEndpointConfiguration."""
        super().__init__()
        self.communication_connector_ref: Optional[ARRef] = None
        self.ipv4_multicast_ip_address: Optional[Ip4AddressString] = None
        self.ipv6_multicast_ip_address: Optional[Ip6AddressString] = None

    def serialize(self) -> ET.Element:
        """Serialize PlatformModuleEthernetEndpointConfiguration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PlatformModuleEthernetEndpointConfiguration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize communication_connector_ref
        if self.communication_connector_ref is not None:
            serialized = SerializationHelper.serialize_item(self.communication_connector_ref, "EthernetCommunicationConnector")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMMUNICATION-CONNECTOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv4_multicast_ip_address
        if self.ipv4_multicast_ip_address is not None:
            serialized = SerializationHelper.serialize_item(self.ipv4_multicast_ip_address, "Ip4AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV4-MULTICAST-IP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ipv6_multicast_ip_address
        if self.ipv6_multicast_ip_address is not None:
            serialized = SerializationHelper.serialize_item(self.ipv6_multicast_ip_address, "Ip6AddressString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IPV6-MULTICAST-IP-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PlatformModuleEthernetEndpointConfiguration":
        """Deserialize XML element to PlatformModuleEthernetEndpointConfiguration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PlatformModuleEthernetEndpointConfiguration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PlatformModuleEthernetEndpointConfiguration, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            child_tag = tag  # Alias for polymorphic type checking
            if tag == "COMMUNICATION-CONNECTOR-REF":
                setattr(obj, "communication_connector_ref", ARRef.deserialize(child))
            elif tag == "IPV4-MULTICAST-IP-ADDRESS":
                setattr(obj, "ipv4_multicast_ip_address", SerializationHelper.deserialize_by_tag(child, "Ip4AddressString"))
            elif tag == "IPV6-MULTICAST-IP-ADDRESS":
                setattr(obj, "ipv6_multicast_ip_address", SerializationHelper.deserialize_by_tag(child, "Ip6AddressString"))

        return obj



class PlatformModuleEthernetEndpointConfigurationBuilder(ARElementBuilder):
    """Builder for PlatformModuleEthernetEndpointConfiguration with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PlatformModuleEthernetEndpointConfiguration = PlatformModuleEthernetEndpointConfiguration()


    def with_communication_connector(self, value: Optional[EthernetCommunicationConnector]) -> "PlatformModuleEthernetEndpointConfigurationBuilder":
        """Set communication_connector attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.communication_connector = value
        return self

    def with_ipv4_multicast_ip_address(self, value: Optional[Ip4AddressString]) -> "PlatformModuleEthernetEndpointConfigurationBuilder":
        """Set ipv4_multicast_ip_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv4_multicast_ip_address = value
        return self

    def with_ipv6_multicast_ip_address(self, value: Optional[Ip6AddressString]) -> "PlatformModuleEthernetEndpointConfigurationBuilder":
        """Set ipv6_multicast_ip_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.ipv6_multicast_ip_address = value
        return self




    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from typing import get_type_hints
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

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


    def build(self) -> PlatformModuleEthernetEndpointConfiguration:
        """Build and return the PlatformModuleEthernetEndpointConfiguration instance with validation."""
        self._validate_instance()
        pass
        return self._obj