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
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.application_partition import (
    ApplicationPartition,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterToApplicationPartitionMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToApplicationPartitionMapping."""

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
