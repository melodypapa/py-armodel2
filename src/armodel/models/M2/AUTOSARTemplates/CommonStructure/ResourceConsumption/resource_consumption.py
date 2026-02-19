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
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ResourceConsumption, cls).deserialize(element)

        # Parse access_count_set_refs (list from container "ACCESS-COUNT-SETS")
        obj.access_count_set_refs = []
        container = ARObject._find_child_element(element, "ACCESS-COUNT-SETS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.access_count_set_refs.append(child_value)

        # Parse execution_times (list from container "EXECUTION-TIMES")
        obj.execution_times = []
        container = ARObject._find_child_element(element, "EXECUTION-TIMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.execution_times.append(child_value)

        # Parse heap_usages (list from container "HEAP-USAGES")
        obj.heap_usages = []
        container = ARObject._find_child_element(element, "HEAP-USAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.heap_usages.append(child_value)

        # Parse memory_sections (list from container "MEMORY-SECTIONS")
        obj.memory_sections = []
        container = ARObject._find_child_element(element, "MEMORY-SECTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.memory_sections.append(child_value)

        # Parse section_name_prefixes (list from container "SECTION-NAME-PREFIXES")
        obj.section_name_prefixes = []
        container = ARObject._find_child_element(element, "SECTION-NAME-PREFIXES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.section_name_prefixes.append(child_value)

        # Parse stack_usages (list from container "STACK-USAGES")
        obj.stack_usages = []
        container = ARObject._find_child_element(element, "STACK-USAGES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
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
