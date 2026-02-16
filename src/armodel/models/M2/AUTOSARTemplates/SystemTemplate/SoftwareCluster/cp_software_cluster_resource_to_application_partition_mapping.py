"""CpSoftwareClusterResourceToApplicationPartitionMapping AUTOSAR element."""

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


class CpSoftwareClusterResourceToApplicationPartitionMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterResourceToApplicationPartitionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("application", None, False, False, ApplicationPartition),  # application
        ("resource", None, False, False, CpSoftwareCluster),  # resource
    ]

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResourceToApplicationPartitionMapping."""
        super().__init__()
        self.application: Optional[ApplicationPartition] = None
        self.resource: Optional[CpSoftwareCluster] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CpSoftwareClusterResourceToApplicationPartitionMapping to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterResourceToApplicationPartitionMapping":
        """Create CpSoftwareClusterResourceToApplicationPartitionMapping from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CpSoftwareClusterResourceToApplicationPartitionMapping instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CpSoftwareClusterResourceToApplicationPartitionMapping since parent returns ARObject
        return cast("CpSoftwareClusterResourceToApplicationPartitionMapping", obj)


class CpSoftwareClusterResourceToApplicationPartitionMappingBuilder:
    """Builder for CpSoftwareClusterResourceToApplicationPartitionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterResourceToApplicationPartitionMapping = CpSoftwareClusterResourceToApplicationPartitionMapping()

    def build(self) -> CpSoftwareClusterResourceToApplicationPartitionMapping:
        """Build and return CpSoftwareClusterResourceToApplicationPartitionMapping object.

        Returns:
            CpSoftwareClusterResourceToApplicationPartitionMapping instance
        """
        # TODO: Add validation
        return self._obj
