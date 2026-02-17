"""CpSoftwareClusterServiceResource AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 904)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster_resource import (
    CpSoftwareClusterResource,
)
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class CpSoftwareClusterServiceResource(CpSoftwareClusterResource):
    """AUTOSAR CpSoftwareClusterServiceResource."""

    def __init__(self) -> None:
        """Initialize CpSoftwareClusterServiceResource."""
        super().__init__()
        self.resource_needses: list[EcucContainerValue] = []


class CpSoftwareClusterServiceResourceBuilder:
    """Builder for CpSoftwareClusterServiceResource."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterServiceResource = CpSoftwareClusterServiceResource()

    def build(self) -> CpSoftwareClusterServiceResource:
        """Build and return CpSoftwareClusterServiceResource object.

        Returns:
            CpSoftwareClusterServiceResource instance
        """
        # TODO: Add validation
        return self._obj
