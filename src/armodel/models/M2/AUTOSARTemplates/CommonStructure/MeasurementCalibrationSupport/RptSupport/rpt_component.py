"""RptComponent AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("mc_datas", None, False, True, RoleBasedMcDataAssignment),  # mcDatas
        ("rp_impl_policy", None, False, False, RptImplPolicy),  # rpImplPolicy
        ("rpt_executable_entities", None, False, True, RptExecutableEntity),  # rptExecutableEntities
    ]

    def __init__(self) -> None:
        """Initialize RptComponent."""
        super().__init__()
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rp_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_executable_entities: list[RptExecutableEntity] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RptComponent to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptComponent":
        """Create RptComponent from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RptComponent instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RptComponent since parent returns ARObject
        return cast("RptComponent", obj)


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
