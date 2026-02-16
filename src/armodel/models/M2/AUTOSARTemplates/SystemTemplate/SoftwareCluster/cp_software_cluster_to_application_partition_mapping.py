"""CpSoftwareClusterToApplicationPartitionMapping AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToApplicationPartitionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("applications", None, False, True, ApplicationPartition),  # applications
        ("software_cluster", None, False, False, CpSoftwareCluster),  # softwareCluster
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToApplicationPartitionMapping."""
        super().__init__()
        self.applications: list[ApplicationPartition] = []
        self.software_cluster: Optional[CpSoftwareCluster] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterToApplicationPartitionMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToApplicationPartitionMapping":
        """Create CpSoftwareClusterToApplicationPartitionMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterToApplicationPartitionMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterToApplicationPartitionMapping since parent returns ARObject
        return cast("CpSoftwareClusterToApplicationPartitionMapping", obj)


class CpSoftwareClusterToApplicationPartitionMappingBuilder:
    """Builder for CpSoftwareClusterToApplicationPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToApplicationPartitionMapping = CpSoftwareClusterToApplicationPartitionMapping()

    def build(self) -> CpSoftwareClusterToApplicationPartitionMapping:
        """Build and return CpSoftwareClusterToApplicationPartitionMapping object.

        Returns:
            CpSoftwareClusterToApplicationPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
