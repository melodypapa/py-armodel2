"""RptComponent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "mc_datas": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RoleBasedMcDataAssignment,
        ),  # mcDatas
        "rp_impl_policy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptImplPolicy,
        ),  # rpImplPolicy
        "rpt_executable_entities": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptExecutableEntity,
        ),  # rptExecutableEntities
    }

    def __init__(self) -> None:
        """Initialize RptComponent."""
        super().__init__()
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rp_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_executable_entities: list[RptExecutableEntity] = []


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
