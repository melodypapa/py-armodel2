"""RptExecutableEntityEvent AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "executions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptExecutionContext,
        ),  # executions
        "mc_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RoleBasedMcDataAssignment,
        ),  # mcDatas
        "rpt_event_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # rptEventId
        "rpt_executable_entity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptExecutableEntity,
        ),  # rptExecutableEntity
        "rpt_impl_policy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptImplPolicy,
        ),  # rptImplPolicy
        "rpt_service_points": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptServicePoint,
        ),  # rptServicePoints
    }

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
