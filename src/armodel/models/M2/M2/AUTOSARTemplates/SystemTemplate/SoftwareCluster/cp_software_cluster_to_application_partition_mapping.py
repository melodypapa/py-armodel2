"""CpSoftwareClusterToApplicationPartitionMapping AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "applications": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=ApplicationPartition,
        ),  # applications
        "software_cluster": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # softwareCluster
    }

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToApplicationPartitionMapping."""
        super().__init__()
        self.applications: list[ApplicationPartition] = []
        self.software_cluster: Optional[CpSoftwareCluster] = None


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
