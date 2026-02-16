"""RptContainer AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.RPTScenario.rpt_container import (
    RptContainer,
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("by_pass_points", None, False, True, AtpFeature),  # byPassPoints
        ("explicit_rpts", None, False, True, RptProfile),  # explicitRpts
        ("rpt_containers", None, False, True, RptContainer),  # rptContainers
        ("rpt_executable_entity", None, False, False, RptExecutableEntity),  # rptExecutableEntity
        ("rpt_hook", None, False, False, RptHook),  # rptHook
        ("rpt_impl_policy", None, False, False, RptImplPolicy),  # rptImplPolicy
        ("rpt_sw", None, False, False, RptSwPrototypingAccess),  # rptSw
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptContainer to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptContainer":
        """Create RptContainer from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptContainer instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptContainer since parent returns ARObject
        return cast("RptContainer", obj)


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
