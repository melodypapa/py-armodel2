"""EthTcpIpProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 153)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import ARElementBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.tcp_props import (
    TcpProps,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.udp_props import (
    UdpProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthTcpIpProps(ARElement):
    """AUTOSAR EthTcpIpProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    tcp_props: Optional[TcpProps]
    udp_props: Optional[UdpProps]
    def __init__(self) -> None:
        """Initialize EthTcpIpProps."""
        super().__init__()
        self.tcp_props: Optional[TcpProps] = None
        self.udp_props: Optional[UdpProps] = None

    def serialize(self) -> ET.Element:
        """Serialize EthTcpIpProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthTcpIpProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tcp_props
        if self.tcp_props is not None:
            serialized = SerializationHelper.serialize_item(self.tcp_props, "TcpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TCP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize udp_props
        if self.udp_props is not None:
            serialized = SerializationHelper.serialize_item(self.udp_props, "UdpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("UDP-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthTcpIpProps":
        """Deserialize XML element to EthTcpIpProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthTcpIpProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthTcpIpProps, cls).deserialize(element)

        # Parse tcp_props
        child = SerializationHelper.find_child_element(element, "TCP-PROPS")
        if child is not None:
            tcp_props_value = SerializationHelper.deserialize_by_tag(child, "TcpProps")
            obj.tcp_props = tcp_props_value

        # Parse udp_props
        child = SerializationHelper.find_child_element(element, "UDP-PROPS")
        if child is not None:
            udp_props_value = SerializationHelper.deserialize_by_tag(child, "UdpProps")
            obj.udp_props = udp_props_value

        return obj



class EthTcpIpPropsBuilder(ARElementBuilder):
    """Builder for EthTcpIpProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthTcpIpProps = EthTcpIpProps()


    def with_tcp_props(self, value: Optional[TcpProps]) -> "EthTcpIpPropsBuilder":
        """Set tcp_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.tcp_props = value
        return self

    def with_udp_props(self, value: Optional[UdpProps]) -> "EthTcpIpPropsBuilder":
        """Set udp_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.udp_props = value
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


    def build(self) -> EthTcpIpProps:
        """Build and return the EthTcpIpProps instance with validation."""
        self._validate_instance()
        pass
        return self._obj