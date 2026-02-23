"""ResourceConsumption AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 137)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 260)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 238)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.builder_base import BuilderBase
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count_set import (
    AccessCountSet,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.ExecutionTime.execution_time import (
    ExecutionTime,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.HeapUsage.heap_usage import (
    HeapUsage,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.memory_section import (
    MemorySection,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.MemorySectionUsage.section_name_prefix import (
    SectionNamePrefix,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ResourceConsumption.StackUsage.stack_usage import (
    StackUsage,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class ResourceConsumption(Identifiable):
    """AUTOSAR ResourceConsumption."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access_count_set_refs: list[ARRef]
    execution_times: list[ExecutionTime]
    heap_usages: list[HeapUsage]
    memory_sections: list[MemorySection]
    section_name_prefixes: list[SectionNamePrefix]
    stack_usages: list[StackUsage]
    def __init__(self) -> None:
        """Initialize ResourceConsumption."""
        super().__init__()
        self.access_count_set_refs: list[ARRef] = []
        self.execution_times: list[ExecutionTime] = []
        self.heap_usages: list[HeapUsage] = []
        self.memory_sections: list[MemorySection] = []
        self.section_name_prefixes: list[SectionNamePrefix] = []
        self.stack_usages: list[StackUsage] = []

    def serialize(self) -> ET.Element:
        """Serialize ResourceConsumption to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ResourceConsumption, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_count_set_refs (list to container "ACCESS-COUNT-SET-REFS")
        if self.access_count_set_refs:
            wrapper = ET.Element("ACCESS-COUNT-SET-REFS")
            for item in self.access_count_set_refs:
                serialized = SerializationHelper.serialize_item(item, "AccessCountSet")
                if serialized is not None:
                    child_elem = ET.Element("ACCESS-COUNT-SET-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize execution_times (list to container "EXECUTION-TIMES")
        if self.execution_times:
            wrapper = ET.Element("EXECUTION-TIMES")
            for item in self.execution_times:
                serialized = SerializationHelper.serialize_item(item, "ExecutionTime")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize heap_usages (list to container "HEAP-USAGES")
        if self.heap_usages:
            wrapper = ET.Element("HEAP-USAGES")
            for item in self.heap_usages:
                serialized = SerializationHelper.serialize_item(item, "HeapUsage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize memory_sections (list to container "MEMORY-SECTIONS")
        if self.memory_sections:
            wrapper = ET.Element("MEMORY-SECTIONS")
            for item in self.memory_sections:
                serialized = SerializationHelper.serialize_item(item, "MemorySection")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize section_name_prefixes (list to container "SECTION-NAME-PREFIXES")
        if self.section_name_prefixes:
            wrapper = ET.Element("SECTION-NAME-PREFIXES")
            for item in self.section_name_prefixes:
                serialized = SerializationHelper.serialize_item(item, "SectionNamePrefix")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize stack_usages (list to container "STACK-USAGES")
        if self.stack_usages:
            wrapper = ET.Element("STACK-USAGES")
            for item in self.stack_usages:
                serialized = SerializationHelper.serialize_item(item, "StackUsage")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ResourceConsumption":
        """Deserialize XML element to ResourceConsumption object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ResourceConsumption object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ResourceConsumption, cls).deserialize(element)

        # Parse access_count_set_refs (list from container "ACCESS-COUNT-SET-REFS")
        obj.access_count_set_refs = []
        container = SerializationHelper.find_child_element(element, "ACCESS-COUNT-SET-REFS")
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
                    obj.access_count_set_refs.append(child_value)

        # Parse execution_times (list from container "EXECUTION-TIMES")
        obj.execution_times = []
        container = SerializationHelper.find_child_element(element, "EXECUTION-TIMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.execution_times.append(child_value)

        # Parse heap_usages (list from container "HEAP-USAGES")
        obj.heap_usages = []
        container = SerializationHelper.find_child_element(element, "HEAP-USAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.heap_usages.append(child_value)

        # Parse memory_sections (list from container "MEMORY-SECTIONS")
        obj.memory_sections = []
        container = SerializationHelper.find_child_element(element, "MEMORY-SECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.memory_sections.append(child_value)

        # Parse section_name_prefixes (list from container "SECTION-NAME-PREFIXES")
        obj.section_name_prefixes = []
        container = SerializationHelper.find_child_element(element, "SECTION-NAME-PREFIXES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.section_name_prefixes.append(child_value)

        # Parse stack_usages (list from container "STACK-USAGES")
        obj.stack_usages = []
        container = SerializationHelper.find_child_element(element, "STACK-USAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.stack_usages.append(child_value)

        return obj



class ResourceConsumptionBuilder(IdentifiableBuilder):
    """Builder for ResourceConsumption with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ResourceConsumption = ResourceConsumption()


    def with_access_count_sets(self, items: list[AccessCountSet]) -> "ResourceConsumptionBuilder":
        """Set access_count_sets list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.access_count_sets = list(items) if items else []
        return self

    def with_execution_times(self, items: list[ExecutionTime]) -> "ResourceConsumptionBuilder":
        """Set execution_times list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.execution_times = list(items) if items else []
        return self

    def with_heap_usages(self, items: list[HeapUsage]) -> "ResourceConsumptionBuilder":
        """Set heap_usages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.heap_usages = list(items) if items else []
        return self

    def with_memory_sections(self, items: list[MemorySection]) -> "ResourceConsumptionBuilder":
        """Set memory_sections list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.memory_sections = list(items) if items else []
        return self

    def with_section_name_prefixes(self, items: list[SectionNamePrefix]) -> "ResourceConsumptionBuilder":
        """Set section_name_prefixes list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.section_name_prefixes = list(items) if items else []
        return self

    def with_stack_usages(self, items: list[StackUsage]) -> "ResourceConsumptionBuilder":
        """Set stack_usages list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.stack_usages = list(items) if items else []
        return self


    def add_access_count_set(self, item: AccessCountSet) -> "ResourceConsumptionBuilder":
        """Add a single item to access_count_sets list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.access_count_sets.append(item)
        return self

    def clear_access_count_sets(self) -> "ResourceConsumptionBuilder":
        """Clear all items from access_count_sets list.

        Returns:
            self for method chaining
        """
        self._obj.access_count_sets = []
        return self

    def add_execution_time(self, item: ExecutionTime) -> "ResourceConsumptionBuilder":
        """Add a single item to execution_times list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.execution_times.append(item)
        return self

    def clear_execution_times(self) -> "ResourceConsumptionBuilder":
        """Clear all items from execution_times list.

        Returns:
            self for method chaining
        """
        self._obj.execution_times = []
        return self

    def add_heap_usage(self, item: HeapUsage) -> "ResourceConsumptionBuilder":
        """Add a single item to heap_usages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.heap_usages.append(item)
        return self

    def clear_heap_usages(self) -> "ResourceConsumptionBuilder":
        """Clear all items from heap_usages list.

        Returns:
            self for method chaining
        """
        self._obj.heap_usages = []
        return self

    def add_memory_section(self, item: MemorySection) -> "ResourceConsumptionBuilder":
        """Add a single item to memory_sections list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.memory_sections.append(item)
        return self

    def clear_memory_sections(self) -> "ResourceConsumptionBuilder":
        """Clear all items from memory_sections list.

        Returns:
            self for method chaining
        """
        self._obj.memory_sections = []
        return self

    def add_section_name_prefixe(self, item: SectionNamePrefix) -> "ResourceConsumptionBuilder":
        """Add a single item to section_name_prefixes list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.section_name_prefixes.append(item)
        return self

    def clear_section_name_prefixes(self) -> "ResourceConsumptionBuilder":
        """Clear all items from section_name_prefixes list.

        Returns:
            self for method chaining
        """
        self._obj.section_name_prefixes = []
        return self

    def add_stack_usage(self, item: StackUsage) -> "ResourceConsumptionBuilder":
        """Add a single item to stack_usages list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.stack_usages.append(item)
        return self

    def clear_stack_usages(self) -> "ResourceConsumptionBuilder":
        """Clear all items from stack_usages list.

        Returns:
            self for method chaining
        """
        self._obj.stack_usages = []
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


    def build(self) -> ResourceConsumption:
        """Build and return the ResourceConsumption instance with validation."""
        self._validate_instance()
        pass
        return self._obj