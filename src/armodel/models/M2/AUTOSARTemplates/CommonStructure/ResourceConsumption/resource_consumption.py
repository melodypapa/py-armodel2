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
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ResourceConsumption":
        """Deserialize XML element to ResourceConsumption object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ResourceConsumption object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse access_count_set_refs (list)
        obj.access_count_set_refs = []
        for child in ARObject._find_all_child_elements(element, "ACCESS-COUNT-SETS"):
            access_count_set_refs_value = ARObject._deserialize_by_tag(child, "AccessCountSet")
            obj.access_count_set_refs.append(access_count_set_refs_value)

        # Parse execution_times (list)
        obj.execution_times = []
        for child in ARObject._find_all_child_elements(element, "EXECUTION-TIMES"):
            execution_times_value = ARObject._deserialize_by_tag(child, "ExecutionTime")
            obj.execution_times.append(execution_times_value)

        # Parse heap_usages (list)
        obj.heap_usages = []
        for child in ARObject._find_all_child_elements(element, "HEAP-USAGES"):
            heap_usages_value = ARObject._deserialize_by_tag(child, "HeapUsage")
            obj.heap_usages.append(heap_usages_value)

        # Parse memory_sections (list)
        obj.memory_sections = []
        for child in ARObject._find_all_child_elements(element, "MEMORY-SECTIONS"):
            memory_sections_value = ARObject._deserialize_by_tag(child, "MemorySection")
            obj.memory_sections.append(memory_sections_value)

        # Parse section_name_prefixes (list)
        obj.section_name_prefixes = []
        for child in ARObject._find_all_child_elements(element, "SECTION-NAME-PREFIXES"):
            section_name_prefixes_value = ARObject._deserialize_by_tag(child, "SectionNamePrefix")
            obj.section_name_prefixes.append(section_name_prefixes_value)

        # Parse stack_usages (list)
        obj.stack_usages = []
        for child in ARObject._find_all_child_elements(element, "STACK-USAGES"):
            stack_usages_value = ARObject._deserialize_by_tag(child, "StackUsage")
            obj.stack_usages.append(stack_usages_value)

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
