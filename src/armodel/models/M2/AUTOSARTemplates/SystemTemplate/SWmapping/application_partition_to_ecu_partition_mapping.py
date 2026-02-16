"""ApplicationPartitionToEcuPartitionMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.ecu_partition import (
    EcuPartition,
)


class ApplicationPartitionToEcuPartitionMapping(Identifiable):
    """AUTOSAR ApplicationPartitionToEcuPartitionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("applications", None, False, True, ApplicationPartition),  # applications
        ("ecu_partition", None, False, False, EcuPartition),  # ecuPartition
    ]

    def __init__(self) -> None:
        """Initialize ApplicationPartitionToEcuPartitionMapping."""
        super().__init__()
        self.applications: list[ApplicationPartition] = []
        self.ecu_partition: Optional[EcuPartition] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert ApplicationPartitionToEcuPartitionMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationPartitionToEcuPartitionMapping":
        """Create ApplicationPartitionToEcuPartitionMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ApplicationPartitionToEcuPartitionMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to ApplicationPartitionToEcuPartitionMapping since parent returns ARObject
        return cast("ApplicationPartitionToEcuPartitionMapping", obj)


class ApplicationPartitionToEcuPartitionMappingBuilder:
    """Builder for ApplicationPartitionToEcuPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationPartitionToEcuPartitionMapping = ApplicationPartitionToEcuPartitionMapping()

    def build(self) -> ApplicationPartitionToEcuPartitionMapping:
        """Build and return ApplicationPartitionToEcuPartitionMapping object.

        Returns:
            ApplicationPartitionToEcuPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
