"""CpSoftwareCluster module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.CpSoftwareCluster.cp_sw_cluster_to_diag_event_mapping import (
        CpSwClusterToDiagEventMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.CpSoftwareCluster.cp_sw_cluster_resource_to_diag_data_elem_mapping import (
        CpSwClusterResourceToDiagDataElemMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.CpSoftwareCluster.cp_sw_cluster_to_diag_routine_subfunction_mapping import (
        CpSwClusterToDiagRoutineSubfunctionMapping,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.DiagnosticMapping.CpSoftwareCluster.cp_sw_cluster_resource_to_diag_function_id_mapping import (
        CpSwClusterResourceToDiagFunctionIdMapping,
    )

__all__ = [
    "CpSwClusterResourceToDiagDataElemMapping",
    "CpSwClusterResourceToDiagFunctionIdMapping",
    "CpSwClusterToDiagEventMapping",
    "CpSwClusterToDiagRoutineSubfunctionMapping",
]
