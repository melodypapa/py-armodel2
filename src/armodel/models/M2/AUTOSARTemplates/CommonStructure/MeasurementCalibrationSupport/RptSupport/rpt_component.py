"""RptComponent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.role_based_mc_data_assignment import (
    RoleBasedMcDataAssignment,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)


class RptComponent(Identifiable):
    """AUTOSAR RptComponent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mc_datas: list[RoleBasedMcDataAssignment]
    rp_impl_policy: Optional[RptImplPolicy]
    rpt_executable_entities: list[RptExecutableEntity]
    def __init__(self) -> None:
        """Initialize RptComponent."""
        super().__init__()
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rp_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_executable_entities: list[RptExecutableEntity] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptComponent":
        """Deserialize XML element to RptComponent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptComponent object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mc_datas (list)
        obj.mc_datas = []
        for child in ARObject._find_all_child_elements(element, "MC-DATAS"):
            mc_datas_value = ARObject._deserialize_by_tag(child, "RoleBasedMcDataAssignment")
            obj.mc_datas.append(mc_datas_value)

        # Parse rp_impl_policy
        child = ARObject._find_child_element(element, "RP-IMPL-POLICY")
        if child is not None:
            rp_impl_policy_value = ARObject._deserialize_by_tag(child, "RptImplPolicy")
            obj.rp_impl_policy = rp_impl_policy_value

        # Parse rpt_executable_entities (list)
        obj.rpt_executable_entities = []
        for child in ARObject._find_all_child_elements(element, "RPT-EXECUTABLE-ENTITIES"):
            rpt_executable_entities_value = ARObject._deserialize_by_tag(child, "RptExecutableEntity")
            obj.rpt_executable_entities.append(rpt_executable_entities_value)

        return obj



class RptComponentBuilder:
    """Builder for RptComponent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptComponent = RptComponent()

    def build(self) -> RptComponent:
        """Build and return RptComponent object.

        Returns:
            RptComponent instance
        """
        # TODO: Add validation
        return self._obj
