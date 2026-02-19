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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    executions: list[RptExecutionContext]
    mc_datas: list[RoleBasedMcDataAssignment]
    rpt_event_id: Optional[PositiveInteger]
    rpt_executable_entity: Optional[RptExecutableEntity]
    rpt_impl_policy: Optional[RptImplPolicy]
    rpt_service_points: list[RptServicePoint]
    def __init__(self) -> None:
        """Initialize RptExecutableEntityEvent."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rpt_event_id: Optional[PositiveInteger] = None
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_service_points: list[RptServicePoint] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntityEvent":
        """Deserialize XML element to RptExecutableEntityEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptExecutableEntityEvent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse executions (list)
        obj.executions = []
        for child in ARObject._find_all_child_elements(element, "EXECUTIONS"):
            executions_value = ARObject._deserialize_by_tag(child, "RptExecutionContext")
            obj.executions.append(executions_value)

        # Parse mc_datas (list)
        obj.mc_datas = []
        for child in ARObject._find_all_child_elements(element, "MC-DATAS"):
            mc_datas_value = ARObject._deserialize_by_tag(child, "RoleBasedMcDataAssignment")
            obj.mc_datas.append(mc_datas_value)

        # Parse rpt_event_id
        child = ARObject._find_child_element(element, "RPT-EVENT-ID")
        if child is not None:
            rpt_event_id_value = child.text
            obj.rpt_event_id = rpt_event_id_value

        # Parse rpt_executable_entity
        child = ARObject._find_child_element(element, "RPT-EXECUTABLE-ENTITY")
        if child is not None:
            rpt_executable_entity_value = ARObject._deserialize_by_tag(child, "RptExecutableEntity")
            obj.rpt_executable_entity = rpt_executable_entity_value

        # Parse rpt_impl_policy
        child = ARObject._find_child_element(element, "RPT-IMPL-POLICY")
        if child is not None:
            rpt_impl_policy_value = ARObject._deserialize_by_tag(child, "RptImplPolicy")
            obj.rpt_impl_policy = rpt_impl_policy_value

        # Parse rpt_service_points (list)
        obj.rpt_service_points = []
        for child in ARObject._find_all_child_elements(element, "RPT-SERVICE-POINTS"):
            rpt_service_points_value = ARObject._deserialize_by_tag(child, "RptServicePoint")
            obj.rpt_service_points.append(rpt_service_points_value)

        return obj



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
