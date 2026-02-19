"""RptContainer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 847)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_executable_entity import (
    RptExecutableEntity,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_hook import (
    RptHook,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_impl_policy import (
    RptImplPolicy,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_profile import (
    RptProfile,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_sw_prototyping_access import (
    RptSwPrototypingAccess,
)


class RptContainer(Identifiable):
    """AUTOSAR RptContainer."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    by_pass_points: list[AtpFeature]
    explicit_rpts: list[RptProfile]
    rpt_containers: list[RptContainer]
    rpt_executable_entity: Optional[RptExecutableEntity]
    rpt_hook: Optional[RptHook]
    rpt_impl_policy: Optional[RptImplPolicy]
    rpt_sw: Optional[RptSwPrototypingAccess]
    def __init__(self) -> None:
        """Initialize RptContainer."""
        super().__init__()
        self.by_pass_points: list[AtpFeature] = []
        self.explicit_rpts: list[RptProfile] = []
        self.rpt_containers: list[RptContainer] = []
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_hook: Optional[RptHook] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_sw: Optional[RptSwPrototypingAccess] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptContainer":
        """Deserialize XML element to RptContainer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptContainer object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse by_pass_points (list)
        obj.by_pass_points = []
        for child in ARObject._find_all_child_elements(element, "BY-PASS-POINTS"):
            by_pass_points_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.by_pass_points.append(by_pass_points_value)

        # Parse explicit_rpts (list)
        obj.explicit_rpts = []
        for child in ARObject._find_all_child_elements(element, "EXPLICIT-RPTS"):
            explicit_rpts_value = ARObject._deserialize_by_tag(child, "RptProfile")
            obj.explicit_rpts.append(explicit_rpts_value)

        # Parse rpt_containers (list)
        obj.rpt_containers = []
        for child in ARObject._find_all_child_elements(element, "RPT-CONTAINERS"):
            rpt_containers_value = ARObject._deserialize_by_tag(child, "RptContainer")
            obj.rpt_containers.append(rpt_containers_value)

        # Parse rpt_executable_entity
        child = ARObject._find_child_element(element, "RPT-EXECUTABLE-ENTITY")
        if child is not None:
            rpt_executable_entity_value = ARObject._deserialize_by_tag(child, "RptExecutableEntity")
            obj.rpt_executable_entity = rpt_executable_entity_value

        # Parse rpt_hook
        child = ARObject._find_child_element(element, "RPT-HOOK")
        if child is not None:
            rpt_hook_value = ARObject._deserialize_by_tag(child, "RptHook")
            obj.rpt_hook = rpt_hook_value

        # Parse rpt_impl_policy
        child = ARObject._find_child_element(element, "RPT-IMPL-POLICY")
        if child is not None:
            rpt_impl_policy_value = ARObject._deserialize_by_tag(child, "RptImplPolicy")
            obj.rpt_impl_policy = rpt_impl_policy_value

        # Parse rpt_sw
        child = ARObject._find_child_element(element, "RPT-SW")
        if child is not None:
            rpt_sw_value = ARObject._deserialize_by_tag(child, "RptSwPrototypingAccess")
            obj.rpt_sw = rpt_sw_value

        return obj



class RptContainerBuilder:
    """Builder for RptContainer."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RptContainer = RptContainer()

    def build(self) -> RptContainer:
        """Build and return RptContainer object.

        Returns:
            RptContainer instance
        """
        # TODO: Add validation
        return self._obj
