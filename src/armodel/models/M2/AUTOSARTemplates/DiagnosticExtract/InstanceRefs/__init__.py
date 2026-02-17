"""InstanceRefs module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.InstanceRefs.data_prototype_in_system_instance_ref import (
        DataPrototypeInSystemInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.InstanceRefs.swc_service_dependency_in_system_instance_ref import (
        SwcServiceDependencyInSystemInstanceRef,
    )
    from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.InstanceRefs.p_mode_in_system_instance_ref import (
        PModeInSystemInstanceRef,
    )

__all__ = [
    "DataPrototypeInSystemInstanceRef",
    "PModeInSystemInstanceRef",
    "SwcServiceDependencyInSystemInstanceRef",
]
