"""CpSwClusterToDiagEventMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 272)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_CpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticEvent.diagnostic_event import (
    DiagnosticEvent,
)


class CpSwClusterToDiagEventMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterToDiagEventMapping."""

    def __init__(self) -> None:
        """Initialize CpSwClusterToDiagEventMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.diagnostic_event: Optional[DiagnosticEvent] = None


class CpSwClusterToDiagEventMappingBuilder:
    """Builder for CpSwClusterToDiagEventMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSwClusterToDiagEventMapping = CpSwClusterToDiagEventMapping()

    def build(self) -> CpSwClusterToDiagEventMapping:
        """Build and return CpSwClusterToDiagEventMapping object.

        Returns:
            CpSwClusterToDiagEventMapping instance
        """
        # TODO: Add validation
        return self._obj
