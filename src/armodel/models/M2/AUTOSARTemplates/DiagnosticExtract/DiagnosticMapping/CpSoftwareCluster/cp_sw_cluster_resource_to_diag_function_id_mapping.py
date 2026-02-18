"""CpSwClusterResourceToDiagFunctionIdMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 275)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_CpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)


class CpSwClusterResourceToDiagFunctionIdMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterResourceToDiagFunctionIdMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cp_software_cluster: Optional[CpSoftwareCluster]
    function: Optional[Any]
    def __init__(self) -> None:
        """Initialize CpSwClusterResourceToDiagFunctionIdMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.function: Optional[Any] = None


class CpSwClusterResourceToDiagFunctionIdMappingBuilder:
    """Builder for CpSwClusterResourceToDiagFunctionIdMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSwClusterResourceToDiagFunctionIdMapping = CpSwClusterResourceToDiagFunctionIdMapping()

    def build(self) -> CpSwClusterResourceToDiagFunctionIdMapping:
        """Build and return CpSwClusterResourceToDiagFunctionIdMapping object.

        Returns:
            CpSwClusterResourceToDiagFunctionIdMapping instance
        """
        # TODO: Add validation
        return self._obj
