"""TimingCpSoftwareCluster module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCpSoftwareCluster.td_cp_software_cluster_mapping_set import (
        TDCpSoftwareClusterMappingSet,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCpSoftwareCluster.td_cp_software_cluster_mapping import (
        TDCpSoftwareClusterMapping,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingCpSoftwareCluster.td_cp_software_cluster_resource_mapping import (
        TDCpSoftwareClusterResourceMapping,
    )

__all__ = [
    "TDCpSoftwareClusterMapping",
    "TDCpSoftwareClusterMappingSet",
    "TDCpSoftwareClusterResourceMapping",
]
