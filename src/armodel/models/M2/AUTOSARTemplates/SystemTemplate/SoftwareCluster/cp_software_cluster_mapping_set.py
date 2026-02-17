"""CpSoftwareClusterMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 285)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.port_element_to_communication_resource_mapping import (
    PortElementToCommunicationResourceMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SWmapping.swc_to_application_partition_mapping import (
    SwcToApplicationPartitionMapping,
)


class CpSoftwareClusterMappingSet(ARElement):
    """AUTOSAR CpSoftwareClusterMappingSet."""

    port_element_tos: list[PortElementToCommunicationResourceMapping]
    resource_tos: list[CpSoftwareCluster]
    software_clusters: list[Any]
    swc_tos: list[SwcToApplicationPartitionMapping]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterMappingSet."""
        super().__init__()
        self.port_element_tos: list[PortElementToCommunicationResourceMapping] = []
        self.resource_tos: list[CpSoftwareCluster] = []
        self.software_clusters: list[Any] = []
        self.swc_tos: list[SwcToApplicationPartitionMapping] = []


class CpSoftwareClusterMappingSetBuilder:
    """Builder for CpSoftwareClusterMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterMappingSet = CpSoftwareClusterMappingSet()

    def build(self) -> CpSoftwareClusterMappingSet:
        """Build and return CpSoftwareClusterMappingSet object.

        Returns:
            CpSoftwareClusterMappingSet instance
        """
        # TODO: Add validation
        return self._obj
