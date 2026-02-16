"""ExecutionTime AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("exclusive_area", None, False, False, ExclusiveArea),  # exclusiveArea
        ("executable_entity", None, False, False, ExecutableEntity),  # executableEntity
        ("hardware", None, False, False, HardwareConfiguration),  # hardware
        ("hw_element", None, False, False, HwElement),  # hwElement
        ("included_libraries", None, False, True, DependencyOnArtifact),  # includedLibraries
        ("memory_section_locations", None, False, True, MemorySectionLocation),  # memorySectionLocations
        ("software_context", None, False, False, SoftwareContext),  # softwareContext
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ExecutionTime to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExecutionTime":
        """Create ExecutionTime from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ExecutionTime instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ExecutionTime since parent returns ARObject
        return cast("ExecutionTime", obj)


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
