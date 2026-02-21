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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
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



class ResourceConsumptionBuilder:
    """Builder for ResourceConsumption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ResourceConsumption = ResourceConsumption()

    def build(self) -> ResourceConsumption:
        """Build and return ResourceConsumption object.

        Returns:
            ResourceConsumption instance
        """
        # TODO: Add validation
        return self._obj
