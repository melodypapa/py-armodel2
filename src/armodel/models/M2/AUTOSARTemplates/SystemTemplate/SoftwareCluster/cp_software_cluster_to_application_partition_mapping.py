"""CpSoftwareClusterToApplicationPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 287)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToApplicationPartitionMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    applications: list[ApplicationPartition]
    software_cluster: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToApplicationPartitionMapping."""
        super().__init__()
        self.applications: list[ApplicationPartition] = []
        self.software_cluster: Optional[CpSoftwareCluster] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "CpSoftwareClusterToApplicationPartitionMapping":
        """Deserialize XML element to CpSoftwareClusterToApplicationPartitionMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CpSoftwareClusterToApplicationPartitionMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse applications (list)
        obj.applications = []
        for child in ARObject._find_all_child_elements(element, "APPLICATIONS"):
            applications_value = ARObject._deserialize_by_tag(child, "ApplicationPartition")
            obj.applications.append(applications_value)

        # Parse software_cluster
        child = ARObject._find_child_element(element, "SOFTWARE-CLUSTER")
        if child is not None:
            software_cluster_value = ARObject._deserialize_by_tag(child, "CpSoftwareCluster")
            obj.software_cluster = software_cluster_value

        return obj



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
