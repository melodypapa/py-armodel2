"""ClientServerInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 128)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import PortInterfaceMappingBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_application_error_mapping import (
    ClientServerApplicationErrorMapping,
)
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.client_server_operation import (
    ClientServerOperation,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ClientServerInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR ClientServerInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    error_mappings: list[ClientServerApplicationErrorMapping]
    operations: list[ClientServerOperation]
    def __init__(self) -> None:
        """Initialize ClientServerInterfaceMapping."""
        super().__init__()
        self.error_mappings: list[ClientServerApplicationErrorMapping] = []
        self.operations: list[ClientServerOperation] = []

    def serialize(self) -> ET.Element:
        """Serialize ClientServerInterfaceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ClientServerInterfaceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize error_mappings (list to container "ERROR-MAPPINGS")
        if self.error_mappings:
            wrapper = ET.Element("ERROR-MAPPINGS")
            for item in self.error_mappings:
                serialized = SerializationHelper.serialize_item(item, "ClientServerApplicationErrorMapping")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize operations (list to container "OPERATIONS")
        if self.operations:
            wrapper = ET.Element("OPERATIONS")
            for item in self.operations:
                serialized = SerializationHelper.serialize_item(item, "ClientServerOperation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ClientServerInterfaceMapping":
        """Deserialize XML element to ClientServerInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ClientServerInterfaceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ClientServerInterfaceMapping, cls).deserialize(element)

        # Parse error_mappings (list from container "ERROR-MAPPINGS")
        obj.error_mappings = []
        container = SerializationHelper.find_child_element(element, "ERROR-MAPPINGS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.error_mappings.append(child_value)

        # Parse operations (list from container "OPERATIONS")
        obj.operations = []
        container = SerializationHelper.find_child_element(element, "OPERATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.operations.append(child_value)

        return obj



class ClientServerInterfaceMappingBuilder(PortInterfaceMappingBuilder):
    """Builder for ClientServerInterfaceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ClientServerInterfaceMapping = ClientServerInterfaceMapping()


    def with_error_mappings(self, items: list[ClientServerApplicationErrorMapping]) -> "ClientServerInterfaceMappingBuilder":
        """Set error_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.error_mappings = list(items) if items else []
        return self

    def with_operations(self, items: list[ClientServerOperation]) -> "ClientServerInterfaceMappingBuilder":
        """Set operations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.operations = list(items) if items else []
        return self


    def add_error_mapping(self, item: ClientServerApplicationErrorMapping) -> "ClientServerInterfaceMappingBuilder":
        """Add a single item to error_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.error_mappings.append(item)
        return self

    def clear_error_mappings(self) -> "ClientServerInterfaceMappingBuilder":
        """Clear all items from error_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.error_mappings = []
        return self

    def add_operation(self, item: ClientServerOperation) -> "ClientServerInterfaceMappingBuilder":
        """Add a single item to operations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.operations.append(item)
        return self

    def clear_operations(self) -> "ClientServerInterfaceMappingBuilder":
        """Clear all items from operations list.

        Returns:
            self for method chaining
        """
        self._obj.operations = []
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


    def build(self) -> ClientServerInterfaceMapping:
        """Build and return the ClientServerInterfaceMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj