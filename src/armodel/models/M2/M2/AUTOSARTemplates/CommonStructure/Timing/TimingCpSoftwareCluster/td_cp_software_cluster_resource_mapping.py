"""TDCpSoftwareClusterResourceMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 158)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingCpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.timing_description import (
    TimingDescription,
)


class TDCpSoftwareClusterResourceMapping(Identifiable):
    """AUTOSAR TDCpSoftwareClusterResourceMapping."""

    def __init__(self) -> None:
        """Initialize TDCpSoftwareClusterResourceMapping."""
        super().__init__()
        self.resource: Optional[CpSoftwareCluster] = None
        self.timing: Optional[TimingDescription] = None


class TDCpSoftwareClusterResourceMappingBuilder:
    """Builder for TDCpSoftwareClusterResourceMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDCpSoftwareClusterResourceMapping = TDCpSoftwareClusterResourceMapping()

    def build(self) -> TDCpSoftwareClusterResourceMapping:
        """Build and return TDCpSoftwareClusterResourceMapping object.

        Returns:
            TDCpSoftwareClusterResourceMapping instance
        """
        # TODO: Add validation
        return self._obj
