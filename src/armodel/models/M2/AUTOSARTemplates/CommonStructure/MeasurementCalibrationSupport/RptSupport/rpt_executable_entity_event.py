"""RptExecutableEntityEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_service_point import (
    RptServicePoint,
)


class RptExecutableEntityEvent(Identifiable):
    """AUTOSAR RptExecutableEntityEvent."""

    def __init__(self) -> None:
        """Initialize RptExecutableEntityEvent."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rpt_event_id: Optional[PositiveInteger] = None
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_service_points: list[RptServicePoint] = []


class RptExecutableEntityEventBuilder:
    """Builder for RptExecutableEntityEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptExecutableEntityEvent = RptExecutableEntityEvent()

    def build(self) -> RptExecutableEntityEvent:
        """Build and return RptExecutableEntityEvent object.

        Returns:
            RptExecutableEntityEvent instance
        """
        # TODO: Add validation
        return self._obj
