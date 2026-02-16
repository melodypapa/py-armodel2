"""ExecutionTime AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
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


class ExecutionTime(Identifiable):
    """AUTOSAR ExecutionTime."""
    """Abstract base class - do not instantiate directly."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "exclusive_area": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExclusiveArea,
        ),  # exclusiveArea
        "executable_entity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=ExecutableEntity,
        ),  # executableEntity
        "hardware": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HardwareConfiguration,
        ),  # hardware
        "hw_element": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=HwElement,
        ),  # hwElement
        "included_libraries": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=DependencyOnArtifact,
        ),  # includedLibraries
        "memory_section_locations": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=MemorySectionLocation,
        ),  # memorySectionLocations
        "software_context": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SoftwareContext,
        ),  # softwareContext
    }

    def __init__(self) -> None:
        """Initialize ExecutionTime."""
        super().__init__()
        self.exclusive_area: Optional[ExclusiveArea] = None
        self.executable_entity: Optional[ExecutableEntity] = None
        self.hardware: Optional[HardwareConfiguration] = None
        self.hw_element: Optional[HwElement] = None
        self.included_libraries: list[DependencyOnArtifact] = []
        self.memory_section_locations: list[MemorySectionLocation] = []
        self.software_context: Optional[SoftwareContext] = None


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
