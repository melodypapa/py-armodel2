"""ExecutionTime AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 159)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2025)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_ExecutionTime.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
from abc import ABC, abstractmethod


class ExecutionTime(Identifiable, ABC):
    """AUTOSAR ExecutionTime."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    exclusive_area: Optional[ExclusiveArea]
    executable_entity: Optional[ExecutableEntity]
    hardware: Optional[HardwareConfiguration]
    hw_element: Optional[HwElement]
    included_librarie_refs: list[ARRef]
    memory_section_locations: list[MemorySectionLocation]
    software_context: Optional[SoftwareContext]
    def __init__(self) -> None:
        """Initialize ExecutionTime."""
        super().__init__()
        self.exclusive_area: Optional[ExclusiveArea] = None
        self.executable_entity: Optional[ExecutableEntity] = None
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element: Optional[HwElement] = None
        self.included_librarie_refs: list[ARRef] = []
        self.memory_section_locations: list[MemorySectionLocation] = []
        self.software_context: Optional[SoftwareContext] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionTime":
        """Deserialize XML element to ExecutionTime object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExecutionTime object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse exclusive_area
        child = ARObject._find_child_element(element, "EXCLUSIVE-AREA")
        if child is not None:
            exclusive_area_value = ARObject._deserialize_by_tag(child, "ExclusiveArea")
            obj.exclusive_area = exclusive_area_value

        # Parse executable_entity
        child = ARObject._find_child_element(element, "EXECUTABLE-ENTITY")
        if child is not None:
            executable_entity_value = ARObject._deserialize_by_tag(child, "ExecutableEntity")
            obj.executable_entity = executable_entity_value

        # Parse hardware
        child = ARObject._find_child_element(element, "HARDWARE")
        if child is not None:
            hardware_value = ARObject._deserialize_by_tag(child, "HardwareConfiguration")
            obj.hardware = hardware_value

        # Parse hw_element
        child = ARObject._find_child_element(element, "HW-ELEMENT")
        if child is not None:
            hw_element_value = ARObject._deserialize_by_tag(child, "HwElement")
            obj.hw_element = hw_element_value

        # Parse included_librarie_refs (list)
        obj.included_librarie_refs = []
        for child in ARObject._find_all_child_elements(element, "INCLUDED-LIBRARIES"):
            included_librarie_refs_value = ARObject._deserialize_by_tag(child, "DependencyOnArtifact")
            obj.included_librarie_refs.append(included_librarie_refs_value)

        # Parse memory_section_locations (list)
        obj.memory_section_locations = []
        for child in ARObject._find_all_child_elements(element, "MEMORY-SECTION-LOCATIONS"):
            memory_section_locations_value = ARObject._deserialize_by_tag(child, "MemorySectionLocation")
            obj.memory_section_locations.append(memory_section_locations_value)

        # Parse software_context
        child = ARObject._find_child_element(element, "SOFTWARE-CONTEXT")
        if child is not None:
            software_context_value = ARObject._deserialize_by_tag(child, "SoftwareContext")
            obj.software_context = software_context_value

        return obj



class ExecutionTimeBuilder:
    """Builder for ExecutionTime."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExecutionTime = ExecutionTime()

    def build(self) -> ExecutionTime:
        """Build and return ExecutionTime object.

        Returns:
            ExecutionTime instance
        """
        # TODO: Add validation
        return self._obj
