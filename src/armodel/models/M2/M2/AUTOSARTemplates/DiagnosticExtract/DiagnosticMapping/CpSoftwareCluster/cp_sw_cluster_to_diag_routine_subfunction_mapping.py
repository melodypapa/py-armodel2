"""CpSwClusterToDiagRoutineSubfunctionMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 274)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_DiagnosticMapping_CpSoftwareCluster.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.diagnostic_mapping import (
    DiagnosticMapping,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.SoftwareCluster.cp_software_cluster import (
    CpSoftwareCluster,
)
from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.CommonDiagnostics.diagnostic_routine import (
    DiagnosticRoutine,
)


class CpSwClusterToDiagRoutineSubfunctionMapping(DiagnosticMapping):
    """AUTOSAR CpSwClusterToDiagRoutineSubfunctionMapping."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "cp_software_cluster": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=CpSoftwareCluster,
        ),  # cpSoftwareCluster
        "routine": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DiagnosticRoutine,
        ),  # routine
    }

    def __init__(self) -> None:
        """Initialize CpSwClusterToDiagRoutineSubfunctionMapping."""
        super().__init__()
        self.cp_software_cluster: Optional[CpSoftwareCluster] = None
        self.routine: Optional[DiagnosticRoutine] = None


class CpSwClusterToDiagRoutineSubfunctionMappingBuilder:
    """Builder for CpSwClusterToDiagRoutineSubfunctionMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CpSwClusterToDiagRoutineSubfunctionMapping = CpSwClusterToDiagRoutineSubfunctionMapping()

    def build(self) -> CpSwClusterToDiagRoutineSubfunctionMapping:
        """Build and return CpSwClusterToDiagRoutineSubfunctionMapping object.

        Returns:
            CpSwClusterToDiagRoutineSubfunctionMapping instance
        """
        # TODO: Add validation
        return self._obj
