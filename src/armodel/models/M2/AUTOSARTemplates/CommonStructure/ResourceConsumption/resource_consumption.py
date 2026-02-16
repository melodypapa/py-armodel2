"""ResourceConsumption AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("access_count_sets", None, False, True, AccessCountSet),  # accessCountSets
        ("execution_times", None, False, True, ExecutionTime),  # executionTimes
        ("heap_usages", None, False, True, HeapUsage),  # heapUsages
        ("memory_sections", None, False, True, MemorySection),  # memorySections
        ("section_name_prefixes", None, False, True, SectionNamePrefix),  # sectionNamePrefixes
        ("stack_usages", None, False, True, StackUsage),  # stackUsages
    ]

    def __init__(self) -> None:
        """Initialize ResourceConsumption."""
        super().__init__()
        self.access_count_sets: list[AccessCountSet] = []
        self.execution_times: list[ExecutionTime] = []
        self.heap_usages: list[HeapUsage] = []
        self.memory_sections: list[MemorySection] = []
        self.section_name_prefixes: list[SectionNamePrefix] = []
        self.stack_usages: list[StackUsage] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ResourceConsumption to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ResourceConsumption":
        """Create ResourceConsumption from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ResourceConsumption instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ResourceConsumption since parent returns ARObject
        return cast("ResourceConsumption", obj)


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
