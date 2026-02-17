"""RoleBasedMcDataAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
        McDataInstance,
    )



class RoleBasedMcDataAssignment(ARObject):
    """AUTOSAR RoleBasedMcDataAssignment."""

    def __init__(self) -> None:
        """Initialize RoleBasedMcDataAssignment."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.mc_data_instances: list[McDataInstance] = []
        self.role: Optional[Identifier] = None


class RoleBasedMcDataAssignmentBuilder:
    """Builder for RoleBasedMcDataAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedMcDataAssignment = RoleBasedMcDataAssignment()

    def build(self) -> RoleBasedMcDataAssignment:
        """Build and return RoleBasedMcDataAssignment object.

        Returns:
            RoleBasedMcDataAssignment instance
        """
        # TODO: Add validation
        return self._obj
