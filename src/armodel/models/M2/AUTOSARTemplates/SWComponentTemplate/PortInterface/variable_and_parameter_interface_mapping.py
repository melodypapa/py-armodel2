"""VariableAndParameterInterfaceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 124)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2077)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import (
    PortInterfaceMapping,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface_mapping import PortInterfaceMappingBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_prototype_mapping import (
    DataPrototypeMapping,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class VariableAndParameterInterfaceMapping(PortInterfaceMapping):
    """AUTOSAR VariableAndParameterInterfaceMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    data_mapping_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize VariableAndParameterInterfaceMapping."""
        super().__init__()
        self.data_mapping_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize VariableAndParameterInterfaceMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(VariableAndParameterInterfaceMapping, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_mapping_refs (list to container "DATA-MAPPING-REFS")
        if self.data_mapping_refs:
            wrapper = ET.Element("DATA-MAPPING-REFS")
            for item in self.data_mapping_refs:
                serialized = SerializationHelper.serialize_item(item, "DataPrototypeMapping")
                if serialized is not None:
                    child_elem = ET.Element("DATA-MAPPING-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableAndParameterInterfaceMapping":
        """Deserialize XML element to VariableAndParameterInterfaceMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableAndParameterInterfaceMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(VariableAndParameterInterfaceMapping, cls).deserialize(element)

        # Parse data_mapping_refs (list from container "DATA-MAPPING-REFS")
        obj.data_mapping_refs = []
        container = SerializationHelper.find_child_element(element, "DATA-MAPPING-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_element_tag = SerializationHelper.strip_namespace(child.tag)
                if child_element_tag.endswith("-REF") or child_element_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.data_mapping_refs.append(child_value)

        return obj



class VariableAndParameterInterfaceMappingBuilder(PortInterfaceMappingBuilder):
    """Builder for VariableAndParameterInterfaceMapping with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: VariableAndParameterInterfaceMapping = VariableAndParameterInterfaceMapping()


    def with_data_mappings(self, items: list[DataPrototypeMapping]) -> "VariableAndParameterInterfaceMappingBuilder":
        """Set data_mappings list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.data_mappings = list(items) if items else []
        return self


    def add_data_mapping(self, item: DataPrototypeMapping) -> "VariableAndParameterInterfaceMappingBuilder":
        """Add a single item to data_mappings list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.data_mappings.append(item)
        return self

    def clear_data_mappings(self) -> "VariableAndParameterInterfaceMappingBuilder":
        """Clear all items from data_mappings list.

        Returns:
            self for method chaining
        """
        self._obj.data_mappings = []
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


    def build(self) -> VariableAndParameterInterfaceMapping:
        """Build and return the VariableAndParameterInterfaceMapping instance with validation."""
        self._validate_instance()
        pass
        return self._obj