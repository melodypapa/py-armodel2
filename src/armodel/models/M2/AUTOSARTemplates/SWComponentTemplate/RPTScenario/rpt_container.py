"""RptContainer AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 847)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_RPTScenario.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "by_pass_points": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=AtpFeature,
        ),  # byPassPoints
        "explicit_rpts": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptProfile,
        ),  # explicitRpts
        "rpt_containers": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptContainer,
        ),  # rptContainers
        "rpt_executable_entity": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptExecutableEntity,
        ),  # rptExecutableEntity
        "rpt_hook": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptHook,
        ),  # rptHook
        "rpt_impl_policy": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptImplPolicy,
        ),  # rptImplPolicy
        "rpt_sw": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RptSwPrototypingAccess,
        ),  # rptSw
    }

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
