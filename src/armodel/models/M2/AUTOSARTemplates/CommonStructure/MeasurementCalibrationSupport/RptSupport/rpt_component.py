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

    def serialize(self) -> ET.Element:
        """Serialize RptComponent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptComponent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize mc_datas (list to container "MC-DATAS")
        if self.mc_datas:
            wrapper = ET.Element("MC-DATAS")
            for item in self.mc_datas:
                serialized = ARObject._serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rp_impl_policy
        if self.rp_impl_policy is not None:
            serialized = ARObject._serialize_item(self.rp_impl_policy, "RptImplPolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RP-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_executable_entities (list to container "RPT-EXECUTABLE-ENTITIES")
        if self.rpt_executable_entities:
            wrapper = ET.Element("RPT-EXECUTABLE-ENTITIES")
            for item in self.rpt_executable_entities:
                serialized = ARObject._serialize_item(item, "RptExecutableEntity")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptComponent":
        """Deserialize XML element to RptComponent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptComponent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptComponent, cls).deserialize(element)

        # Parse mc_datas (list from container "MC-DATAS")
        obj.mc_datas = []
        container = ARObject._find_child_element(element, "MC-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_datas.append(child_value)

        # Parse rp_impl_policy
        child = ARObject._find_child_element(element, "RP-IMPL-POLICY")
        if child is not None:
            rp_impl_policy_value = ARObject._deserialize_by_tag(child, "RptImplPolicy")
            obj.rp_impl_policy = rp_impl_policy_value

        # Parse rpt_executable_entities (list from container "RPT-EXECUTABLE-ENTITIES")
        obj.rpt_executable_entities = []
        container = ARObject._find_child_element(element, "RPT-EXECUTABLE-ENTITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_executable_entities.append(child_value)

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
