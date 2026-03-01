"""ExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 159)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2025)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel2.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.memory_section_location import (
    MemorySectionLocation,
)
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ExecutionTime(Identifiable, ABC):
    """AUTOSAR ExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    exclusive_area_ref: Optional[ARRef]
    executable_entity_ref: Optional[ARRef]
    hardware: Optional[HardwareConfiguration]
    hw_element_ref: Optional[ARRef]
    included_library_refs: list[ARRef]
    memory_section_locations: list[MemorySectionLocation]
    software_context: Optional[SoftwareContext]
    _DESERIALIZE_DISPATCH = {
        "EXCLUSIVE-AREA-REF": lambda obj, elem: setattr(obj, "exclusive_area_ref", ARRef.deserialize(elem)),
        "EXECUTABLE-ENTITY-REF": ("_POLYMORPHIC", "executable_entity_ref", ["BswModuleEntity", "RunnableEntity"]),
        "HARDWARE": lambda obj, elem: setattr(obj, "hardware", SerializationHelper.deserialize_by_tag(elem, "HardwareConfiguration")),
        "HW-ELEMENT-REF": lambda obj, elem: setattr(obj, "hw_element_ref", ARRef.deserialize(elem)),
        "INCLUDED-LIBRARY-REFS": lambda obj, elem: [obj.included_library_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
        "MEMORY-SECTION-LOCATIONS": lambda obj, elem: obj.memory_section_locations.append(SerializationHelper.deserialize_by_tag(elem, "MemorySectionLocation")),
        "SOFTWARE-CONTEXT": lambda obj, elem: setattr(obj, "software_context", SerializationHelper.deserialize_by_tag(elem, "SoftwareContext")),
    }


    def __init__(self) -> None:
        """Initialize ExecutionTime."""
        super().__init__()
        self.exclusive_area_ref: Optional[ARRef] = None
        self.executable_entity_ref: Optional[ARRef] = None
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element_ref: Optional[ARRef] = None
        self.included_library_refs: list[ARRef] = []
        self.memory_section_locations: list[MemorySectionLocation] = []
        self.software_context: Optional[SoftwareContext] = None

    def serialize(self) -> ET.Element:
        """Serialize ExecutionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ExecutionTime, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize exclusive_area_ref
        if self.exclusive_area_ref is not None:
            serialized = SerializationHelper.serialize_item(self.exclusive_area_ref, "ExclusiveArea")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXCLUSIVE-AREA-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize executable_entity_ref
        if self.executable_entity_ref is not None:
            serialized = SerializationHelper.serialize_item(self.executable_entity_ref, "ExecutableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXECUTABLE-ENTITY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hardware
        if self.hardware is not None:
            serialized = SerializationHelper.serialize_item(self.hardware, "HardwareConfiguration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HARDWARE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize hw_element_ref
        if self.hw_element_ref is not None:
            serialized = SerializationHelper.serialize_item(self.hw_element_ref, "HwElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("HW-ELEMENT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize included_library_refs (list to container "INCLUDED-LIBRARY-REFS")
        if self.included_library_refs:
            wrapper = ET.Element("INCLUDED-LIBRARY-REFS")
            for item in self.included_library_refs:
                serialized = SerializationHelper.serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    child_elem = ET.Element("INCLUDED-LIBRARY-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize memory_section_locations (list to container "MEMORY-SECTION-LOCATIONS")
        if self.memory_section_locations:
            wrapper = ET.Element("MEMORY-SECTION-LOCATIONS")
            for item in self.memory_section_locations:
                serialized = SerializationHelper.serialize_item(item, "MemorySectionLocation")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize software_context
        if self.software_context is not None:
            serialized = SerializationHelper.serialize_item(self.software_context, "SoftwareContext")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SOFTWARE-CONTEXT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionTime":
        """Deserialize XML element to ExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutionTime object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ExecutionTime, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "EXCLUSIVE-AREA-REF":
                setattr(obj, "exclusive_area_ref", ARRef.deserialize(child))
            elif tag == "EXECUTABLE-ENTITY-REF":
                setattr(obj, "executable_entity_ref", ARRef.deserialize(child))
            elif tag == "HARDWARE":
                setattr(obj, "hardware", SerializationHelper.deserialize_by_tag(child, "HardwareConfiguration"))
            elif tag == "HW-ELEMENT-REF":
                setattr(obj, "hw_element_ref", ARRef.deserialize(child))
            elif tag == "INCLUDED-LIBRARY-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.included_library_refs.append(ARRef.deserialize(item_elem))
            elif tag == "MEMORY-SECTION-LOCATIONS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.memory_section_locations.append(SerializationHelper.deserialize_by_tag(item_elem, "MemorySectionLocation"))
            elif tag == "SOFTWARE-CONTEXT":
                setattr(obj, "software_context", SerializationHelper.deserialize_by_tag(child, "SoftwareContext"))

        return obj



class ExecutionTimeBuilder(IdentifiableBuilder):
    """Builder for ExecutionTime with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ExecutionTime = ExecutionTime()


    def with_exclusive_area(self, value: Optional[ExclusiveArea]) -> "ExecutionTimeBuilder":
        """Set exclusive_area attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.exclusive_area = value
        return self

    def with_executable_entity(self, value: Optional[ExecutableEntity]) -> "ExecutionTimeBuilder":
        """Set executable_entity attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.executable_entity = value
        return self

    def with_hardware(self, value: Optional[HardwareConfiguration]) -> "ExecutionTimeBuilder":
        """Set hardware attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.hardware = value
        return self

    def with_hw_element(self, value: Optional[HwElement]) -> "ExecutionTimeBuilder":
        """Set hw_element attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.hw_element = value
        return self

    def with_included_libraries(self, items: list[DependencyOnArtifact]) -> "ExecutionTimeBuilder":
        """Set included_libraries list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.included_libraries = list(items) if items else []
        return self

    def with_memory_section_locations(self, items: list[MemorySectionLocation]) -> "ExecutionTimeBuilder":
        """Set memory_section_locations list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.memory_section_locations = list(items) if items else []
        return self

    def with_software_context(self, value: Optional[SoftwareContext]) -> "ExecutionTimeBuilder":
        """Set software_context attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.software_context = value
        return self


    def add_included_library(self, item: DependencyOnArtifact) -> "ExecutionTimeBuilder":
        """Add a single item to included_libraries list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.included_libraries.append(item)
        return self

    def clear_included_libraries(self) -> "ExecutionTimeBuilder":
        """Clear all items from included_libraries list.

        Returns:
            self for method chaining
        """
        self._obj.included_libraries = []
        return self

    def add_memory_section_location(self, item: MemorySectionLocation) -> "ExecutionTimeBuilder":
        """Add a single item to memory_section_locations list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.memory_section_locations.append(item)
        return self

    def clear_memory_section_locations(self) -> "ExecutionTimeBuilder":
        """Clear all items from memory_section_locations list.

        Returns:
            self for method chaining
        """
        self._obj.memory_section_locations = []
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


    @abstractmethod
    def build(self) -> ExecutionTime:
        """Build and return the ExecutionTime instance (abstract)."""
        raise NotImplementedError