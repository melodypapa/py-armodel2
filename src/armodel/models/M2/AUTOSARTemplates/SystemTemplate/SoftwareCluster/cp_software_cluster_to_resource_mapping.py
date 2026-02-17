"""CpSoftwareClusterToResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 907)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_SoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSoftwareClusterToResourceMapping(Identifiable):
    """AUTOSAR CpSoftwareClusterToResourceMapping."""

    provider: Optional[CpSoftwareCluster]
    requesters: list[CpSoftwareCluster]
    service: Optional[CpSoftwareCluster]
    def __init__(self) -> None:
        """Initialize CpSoftwareClusterToResourceMapping."""
        super().__init__()
        self.provider: Optional[CpSoftwareCluster] = None
        self.requesters: list[CpSoftwareCluster] = []
        self.service: Optional[CpSoftwareCluster] = None


class CpSoftwareClusterToResourceMappingBuilder:
    """Builder for CpSoftwareClusterToResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSoftwareClusterToResourceMapping = CpSoftwareClusterToResourceMapping()

    def build(self) -> CpSoftwareClusterToResourceMapping:
        """Build and return CpSoftwareClusterToResourceMapping object.

        Returns:
            CpSoftwareClusterToResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
