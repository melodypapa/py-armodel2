"""DoIpConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 551)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DoIP.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.DoIP.do_ip_interface import (
    DoIpInterface,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.TransportProtocols.do_ip_logic_address import (
    DoIpLogicAddress,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class DoIpConfig(ARObject):
    """AUTOSAR DoIpConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    doip_interfaces: list[DoIpInterface]
    logic_address: Optional[DoIpLogicAddress]
    def __init__(self) -> None:
        """Initialize DoIpConfig."""
        super().__init__()
        self.doip_interfaces: list[DoIpInterface] = []
        self.logic_address: Optional[DoIpLogicAddress] = None

    def serialize(self) -> ET.Element:
        """Serialize DoIpConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DoIpConfig, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize doip_interfaces (list to container "DOIP-INTERFACES")
        if self.doip_interfaces:
            wrapper = ET.Element("DOIP-INTERFACES")
            for item in self.doip_interfaces:
                serialized = SerializationHelper.serialize_item(item, "DoIpInterface")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize logic_address
        if self.logic_address is not None:
            serialized = SerializationHelper.serialize_item(self.logic_address, "DoIpLogicAddress")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LOGIC-ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DoIpConfig":
        """Deserialize XML element to DoIpConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DoIpConfig object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DoIpConfig, cls).deserialize(element)

        # Parse doip_interfaces (list from container "DOIP-INTERFACES")
        obj.doip_interfaces = []
        container = SerializationHelper.find_child_element(element, "DOIP-INTERFACES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.doip_interfaces.append(child_value)

        # Parse logic_address
        child = SerializationHelper.find_child_element(element, "LOGIC-ADDRESS")
        if child is not None:
            logic_address_value = SerializationHelper.deserialize_by_tag(child, "DoIpLogicAddress")
            obj.logic_address = logic_address_value

        return obj



class DoIpConfigBuilder(BuilderBase):
    """Builder for DoIpConfig with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DoIpConfig = DoIpConfig()


    def with_doip_interfaces(self, items: list[DoIpInterface]) -> "DoIpConfigBuilder":
        """Set doip_interfaces list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.doip_interfaces = list(items) if items else []
        return self

    def with_logic_address(self, value: Optional[DoIpLogicAddress]) -> "DoIpConfigBuilder":
        """Set logic_address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.logic_address = value
        return self


    def add_doip_interface(self, item: DoIpInterface) -> "DoIpConfigBuilder":
        """Add a single item to doip_interfaces list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.doip_interfaces.append(item)
        return self

    def clear_doip_interfaces(self) -> "DoIpConfigBuilder":
        """Clear all items from doip_interfaces list.

        Returns:
            self for method chaining
        """
        self._obj.doip_interfaces = []
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


    def build(self) -> DoIpConfig:
        """Build and return the DoIpConfig instance with validation."""
        self._validate_instance()
        pass
        return self._obj