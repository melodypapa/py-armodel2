"""EthernetCommunicationConnector AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 117)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_EthernetTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import (
    CommunicationConnector,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.CoreTopology.communication_connector import CommunicationConnectorBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    PositiveInteger,
    TimeValue,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.EthernetTopology.eth_ip_props import (
    EthIpProps,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class EthernetCommunicationConnector(CommunicationConnector):
    """AUTOSAR EthernetCommunicationConnector."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "ETHERNET-COMMUNICATION-CONNECTOR"


    eth_ip_props_ref: Optional[ARRef]
    maximum: Optional[PositiveInteger]
    neighbor_cache: Optional[PositiveInteger]
    path_mtu: Optional[Boolean]
    path_mtu_timeout: Optional[TimeValue]
    _DESERIALIZE_DISPATCH = {
        "ETH-IP-PROPS-REF": lambda obj, elem: setattr(obj, "eth_ip_props_ref", ARRef.deserialize(elem)),
        "MAXIMUM": lambda obj, elem: setattr(obj, "maximum", elem.text),
        "NEIGHBOR-CACHE": lambda obj, elem: setattr(obj, "neighbor_cache", elem.text),
        "PATH-MTU": lambda obj, elem: setattr(obj, "path_mtu", elem.text),
        "PATH-MTU-TIMEOUT": lambda obj, elem: setattr(obj, "path_mtu_timeout", elem.text),
    }


    def __init__(self) -> None:
        """Initialize EthernetCommunicationConnector."""
        super().__init__()
        self.eth_ip_props_ref: Optional[ARRef] = None
        self.maximum: Optional[PositiveInteger] = None
        self.neighbor_cache: Optional[PositiveInteger] = None
        self.path_mtu: Optional[Boolean] = None
        self.path_mtu_timeout: Optional[TimeValue] = None

    def serialize(self) -> ET.Element:
        """Serialize EthernetCommunicationConnector to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EthernetCommunicationConnector, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize eth_ip_props_ref
        if self.eth_ip_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.eth_ip_props_ref, "EthIpProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ETH-IP-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize maximum
        if self.maximum is not None:
            serialized = SerializationHelper.serialize_item(self.maximum, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAXIMUM")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize neighbor_cache
        if self.neighbor_cache is not None:
            serialized = SerializationHelper.serialize_item(self.neighbor_cache, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NEIGHBOR-CACHE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize path_mtu
        if self.path_mtu is not None:
            serialized = SerializationHelper.serialize_item(self.path_mtu, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATH-MTU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize path_mtu_timeout
        if self.path_mtu_timeout is not None:
            serialized = SerializationHelper.serialize_item(self.path_mtu_timeout, "TimeValue")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PATH-MTU-TIMEOUT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EthernetCommunicationConnector":
        """Deserialize XML element to EthernetCommunicationConnector object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EthernetCommunicationConnector object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EthernetCommunicationConnector, cls).deserialize(element)

        # Parse eth_ip_props_ref
        child = SerializationHelper.find_child_element(element, "ETH-IP-PROPS-REF")
        if child is not None:
            eth_ip_props_ref_value = ARRef.deserialize(child)
            obj.eth_ip_props_ref = eth_ip_props_ref_value

        # Parse maximum
        child = SerializationHelper.find_child_element(element, "MAXIMUM")
        if child is not None:
            maximum_value = child.text
            obj.maximum = maximum_value

        # Parse neighbor_cache
        child = SerializationHelper.find_child_element(element, "NEIGHBOR-CACHE")
        if child is not None:
            neighbor_cache_value = child.text
            obj.neighbor_cache = neighbor_cache_value

        # Parse path_mtu
        child = SerializationHelper.find_child_element(element, "PATH-MTU")
        if child is not None:
            path_mtu_value = child.text
            obj.path_mtu = path_mtu_value

        # Parse path_mtu_timeout
        child = SerializationHelper.find_child_element(element, "PATH-MTU-TIMEOUT")
        if child is not None:
            path_mtu_timeout_value = child.text
            obj.path_mtu_timeout = path_mtu_timeout_value

        return obj



class EthernetCommunicationConnectorBuilder(CommunicationConnectorBuilder):
    """Builder for EthernetCommunicationConnector with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: EthernetCommunicationConnector = EthernetCommunicationConnector()


    def with_eth_ip_props(self, value: Optional[EthIpProps]) -> "EthernetCommunicationConnectorBuilder":
        """Set eth_ip_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.eth_ip_props = value
        return self

    def with_maximum(self, value: Optional[PositiveInteger]) -> "EthernetCommunicationConnectorBuilder":
        """Set maximum attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.maximum = value
        return self

    def with_neighbor_cache(self, value: Optional[PositiveInteger]) -> "EthernetCommunicationConnectorBuilder":
        """Set neighbor_cache attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.neighbor_cache = value
        return self

    def with_path_mtu(self, value: Optional[Boolean]) -> "EthernetCommunicationConnectorBuilder":
        """Set path_mtu attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.path_mtu = value
        return self

    def with_path_mtu_timeout(self, value: Optional[TimeValue]) -> "EthernetCommunicationConnectorBuilder":
        """Set path_mtu_timeout attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.path_mtu_timeout = value
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


    def build(self) -> EthernetCommunicationConnector:
        """Build and return the EthernetCommunicationConnector instance with validation."""
        self._validate_instance()
        pass
        return self._obj