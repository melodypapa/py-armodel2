"""DataElements module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
        AutosarParameterRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
        AutosarVariableRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.parameter_access import (
        ParameterAccess,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access import (
        VariableAccess,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.ar_variable_in_implementation_data_instance_ref import (
        ArVariableInImplementationDataInstanceRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.ar_parameter_in_implementation_data_instance_ref import (
        ArParameterInImplementationDataInstanceRef,
    )

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.variable_access_scope_enum import (
    VariableAccessScopeEnum,
)

__all__ = [
    "ArParameterInImplementationDataInstanceRef",
    "ArVariableInImplementationDataInstanceRef",
    "AutosarParameterRef",
    "AutosarVariableRef",
    "ParameterAccess",
    "VariableAccess",
    "VariableAccessScopeEnum",
]
