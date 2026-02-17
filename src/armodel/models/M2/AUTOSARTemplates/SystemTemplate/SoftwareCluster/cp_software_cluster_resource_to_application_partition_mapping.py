"""CpSoftwareClusterResourceToApplicationPartitionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 284)

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


class CpSoftwareClusterResourceToApplicationPartitionMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterResourceToApplicationPartitionMapping."""

    application: Optional[ApplicationPartition]
    resource: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterResourceToApplicationPartitionMapping."""
        super().__init__()
        self.application: Optional[ApplicationPartition] = None
        self.resource: Optional[CpSoftwareCluster] = None


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
