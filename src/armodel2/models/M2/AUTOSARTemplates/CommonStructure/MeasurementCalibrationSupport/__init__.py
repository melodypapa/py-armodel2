"""MeasurementCalibrationSupport module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_support_data import (
        McSupportData,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
        McDataInstance,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_sw_emulation_method_support import (
        McSwEmulationMethodSupport,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_parameter_element_group import (
        McParameterElementGroup,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.implementation_element_in_parameter_instance_ref import (
        ImplementationElementInParameterInstanceRef,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_function import (
        McFunction,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_access_details import (
        McDataAccessDetails,
    )
    from armodel2.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
        RoleBasedMcDataAssignment,
    )

__all__ = [
    "ImplementationElementInParameterInstanceRef",
    "McDataAccessDetails",
    "McDataInstance",
    "McFunction",
    "McParameterElementGroup",
    "McSupportData",
    "McSwEmulationMethodSupport",
    "RoleBasedMcDataAssignment",
]
