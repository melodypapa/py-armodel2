"""ExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 159)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2025)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import xml_element_name

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.exclusive_area import (
    ExclusiveArea,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.hardware_configuration import (
    HardwareConfiguration,
)
from armodel.models.M2.AUTOSARTemplates.EcuResourceTemplate.hw_element import (
    HwElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.memory_section_location import (
    MemorySectionLocation,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.software_context import (
    SoftwareContext,
)


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
    _included_librarie_refs: list[ARRef]
    memory_section_locations: list[MemorySectionLocation]
    software_context: Optional[SoftwareContext]
    def __init__(self) -> None:
        """Initialize ExecutionTime."""
        super().__init__()
        self.exclusive_area_ref: Optional[ARRef] = None
        self.executable_entity_ref: Optional[ARRef] = None
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element_ref: Optional[ARRef] = None
        self._included_librarie_refs: list[ARRef] = []
        self.memory_section_locations: list[MemorySectionLocation] = []
        self.software_context: Optional[SoftwareContext] = None
    @property
    @xml_element_name("INCLUDED-LIBRARYS")
    def included_librarie_refs(self) -> list[ARRef]:
        """Get included_librarie_refs with custom XML element name."""
        return self._included_librarie_refs

    @included_librarie_refs.setter
    def included_librarie_refs(self, value: list[ARRef]) -> None:
        """Set included_librarie_refs with custom XML element name."""
        self._included_librarie_refs = value


    def serialize(self) -> ET.Element:
        """Serialize ExecutionTime to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Serialize included_librarie_refs (list to container "INCLUDED-LIBRARYS")
        if self.included_librarie_refs:
            wrapper = ET.Element("INCLUDED-LIBRARYS")
            for item in self.included_librarie_refs:
                serialized = SerializationHelper.serialize_item(item, "DependencyOnArtifact")
                if serialized is not None:
                    child_elem = ET.Element("INCLUDED-LIBRARIE-REF")
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

        # Parse exclusive_area_ref
        child = SerializationHelper.find_child_element(element, "EXCLUSIVE-AREA-REF")
        if child is not None:
            exclusive_area_ref_value = ARRef.deserialize(child)
            obj.exclusive_area_ref = exclusive_area_ref_value

        # Parse executable_entity_ref
        child = SerializationHelper.find_child_element(element, "EXECUTABLE-ENTITY-REF")
        if child is not None:
            executable_entity_ref_value = ARRef.deserialize(child)
            obj.executable_entity_ref = executable_entity_ref_value

        # Parse hardware
        child = SerializationHelper.find_child_element(element, "HARDWARE")
        if child is not None:
            hardware_value = SerializationHelper.deserialize_by_tag(child, "HardwareConfiguration")
            obj.hardware = hardware_value

        # Parse hw_element_ref
        child = SerializationHelper.find_child_element(element, "HW-ELEMENT-REF")
        if child is not None:
            hw_element_ref_value = ARRef.deserialize(child)
            obj.hw_element_ref = hw_element_ref_value

        # Parse included_librarie_refs (list from container "INCLUDED-LIBRARYS")
        obj.included_librarie_refs = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-LIBRARYS")
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
                    obj.included_librarie_refs.append(child_value)

        # Parse memory_section_locations (list from container "MEMORY-SECTION-LOCATIONS")
        obj.memory_section_locations = []
        container = SerializationHelper.find_child_element(element, "MEMORY-SECTION-LOCATIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.memory_section_locations.append(child_value)

        # Parse software_context
        child = SerializationHelper.find_child_element(element, "SOFTWARE-CONTEXT")
        if child is not None:
            software_context_value = SerializationHelper.deserialize_by_tag(child, "SoftwareContext")
            obj.software_context = software_context_value

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


    def add_included_librarie(self, item: DependencyOnArtifact) -> "ExecutionTimeBuilder":
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


    @abstractmethod
    def build(self) -> ExecutionTime:
        """Build and return the ExecutionTime instance (abstract)."""
        raise NotImplementedError