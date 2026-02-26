"""ECUCDescriptionTemplate module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_module_configuration_values import (
        EcucModuleConfigurationValues,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_value_collection import (
        EcucValueCollection,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_indexable_value import (
        EcucIndexableValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
        EcucContainerValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_parameter_value import (
        EcucParameterValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_textual_param_value import (
        EcucTextualParamValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_numerical_param_value import (
        EcucNumericalParamValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_add_info_param_value import (
        EcucAddInfoParamValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_abstract_reference_value import (
        EcucAbstractReferenceValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_reference_value import (
        EcucReferenceValue,
    )
    from armodel2.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_instance_reference_value import (
        EcucInstanceReferenceValue,
    )

__all__ = [
    "EcucAbstractReferenceValue",
    "EcucAddInfoParamValue",
    "EcucContainerValue",
    "EcucIndexableValue",
    "EcucInstanceReferenceValue",
    "EcucModuleConfigurationValues",
    "EcucNumericalParamValue",
    "EcucParameterValue",
    "EcucReferenceValue",
    "EcucTextualParamValue",
    "EcucValueCollection",
]
