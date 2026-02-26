"""J1939NmNode AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 322)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 691)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import (
    NmNode,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.nm_node import NmNodeBuilder
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement import (
    J1939NmAddressConfigurationCapabilityEnum,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.NetworkManagement.j1939_node_name import (
    J1939NodeName,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class J1939NmNode(NmNode):
    """AUTOSAR J1939NmNode."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    address: Optional[J1939NmAddressConfigurationCapabilityEnum]
    node_name: Optional[J1939NodeName]
    def __init__(self) -> None:
        """Initialize J1939NmNode."""
        super().__init__()
        self.address: Optional[J1939NmAddressConfigurationCapabilityEnum] = None
        self.node_name: Optional[J1939NodeName] = None

    def serialize(self) -> ET.Element:
        """Serialize J1939NmNode to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(J1939NmNode, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize address
        if self.address is not None:
            serialized = SerializationHelper.serialize_item(self.address, "J1939NmAddressConfigurationCapabilityEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ADDRESS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize node_name
        if self.node_name is not None:
            serialized = SerializationHelper.serialize_item(self.node_name, "J1939NodeName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NODE-NAME")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "J1939NmNode":
        """Deserialize XML element to J1939NmNode object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized J1939NmNode object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(J1939NmNode, cls).deserialize(element)

        # Parse address
        child = SerializationHelper.find_child_element(element, "ADDRESS")
        if child is not None:
            address_value = J1939NmAddressConfigurationCapabilityEnum.deserialize(child)
            obj.address = address_value

        # Parse node_name
        child = SerializationHelper.find_child_element(element, "NODE-NAME")
        if child is not None:
            node_name_value = SerializationHelper.deserialize_by_tag(child, "J1939NodeName")
            obj.node_name = node_name_value

        return obj



class J1939NmNodeBuilder(NmNodeBuilder):
    """Builder for J1939NmNode with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: J1939NmNode = J1939NmNode()


    def with_address(self, value: Optional[J1939NmAddressConfigurationCapabilityEnum]) -> "J1939NmNodeBuilder":
        """Set address attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.address = value
        return self

    def with_node_name(self, value: Optional[J1939NodeName]) -> "J1939NmNodeBuilder":
        """Set node_name attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.node_name = value
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


    def build(self) -> J1939NmNode:
        """Build and return the J1939NmNode instance with validation."""
        self._validate_instance()
        pass
        return self._obj