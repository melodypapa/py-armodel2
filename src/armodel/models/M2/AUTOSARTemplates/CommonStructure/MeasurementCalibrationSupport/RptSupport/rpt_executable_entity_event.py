"""RptExecutableEntityEvent AUTOSAR element."""

from typing import Optional, cast
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("executions", None, False, True, RptExecutionContext),  # executions
        ("mc_datas", None, False, True, RoleBasedMcDataAssignment),  # mcDatas
        ("rpt_event_id", None, True, False, None),  # rptEventId
        ("rpt_executable_entity", None, False, False, RptExecutableEntity),  # rptExecutableEntity
        ("rpt_impl_policy", None, False, False, RptImplPolicy),  # rptImplPolicy
        ("rpt_service_points", None, False, True, RptServicePoint),  # rptServicePoints
    ]

    def __init__(self) -> None:
        """Initialize RptExecutableEntityEvent."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rpt_event_id: Optional[PositiveInteger] = None
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_service_points: list[RptServicePoint] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptExecutableEntityEvent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntityEvent":
        """Create RptExecutableEntityEvent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptExecutableEntityEvent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptExecutableEntityEvent since parent returns ARObject
        return cast("RptExecutableEntityEvent", obj)


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
