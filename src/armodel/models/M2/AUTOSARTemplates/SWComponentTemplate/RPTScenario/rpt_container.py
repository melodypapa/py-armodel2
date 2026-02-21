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
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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
    explicit_rpt_refs: list[ARRef]
    rpt_containers: list[RptContainer]
    rpt_executable_entity: Optional[RptExecutableEntity]
    rpt_hook: Optional[RptHook]
    rpt_impl_policy: Optional[RptImplPolicy]
    rpt_sw: Optional[RptSwPrototypingAccess]
    def __init__(self) -> None:
        """Initialize RptContainer."""
        super().__init__()
        self.by_pass_points: list[AtpFeature] = []
        self.explicit_rpt_refs: list[ARRef] = []
        self.rpt_containers: list[RptContainer] = []
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_hook: Optional[RptHook] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_sw: Optional[RptSwPrototypingAccess] = None

    def serialize(self) -> ET.Element:
        """Serialize RptContainer to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptContainer, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize by_pass_points (list to container "BY-PASS-POINTS")
        if self.by_pass_points:
            wrapper = ET.Element("BY-PASS-POINTS")
            for item in self.by_pass_points:
                serialized = SerializationHelper.serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize explicit_rpt_refs (list to container "EXPLICIT-RPT-REFS")
        if self.explicit_rpt_refs:
            wrapper = ET.Element("EXPLICIT-RPT-REFS")
            for item in self.explicit_rpt_refs:
                serialized = SerializationHelper.serialize_item(item, "RptProfile")
                if serialized is not None:
                    child_elem = ET.Element("EXPLICIT-RPT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_containers (list to container "RPT-CONTAINERS")
        if self.rpt_containers:
            wrapper = ET.Element("RPT-CONTAINERS")
            for item in self.rpt_containers:
                serialized = SerializationHelper.serialize_item(item, "RptContainer")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_executable_entity
        if self.rpt_executable_entity is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_executable_entity, "RptExecutableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-EXECUTABLE-ENTITY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_hook
        if self.rpt_hook is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_hook, "RptHook")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-HOOK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_impl_policy
        if self.rpt_impl_policy is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_impl_policy, "RptImplPolicy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-IMPL-POLICY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize rpt_sw
        if self.rpt_sw is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_sw, "RptSwPrototypingAccess")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-SW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptContainer":
        """Deserialize XML element to RptContainer object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptContainer object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptContainer, cls).deserialize(element)

        # Parse by_pass_points (list from container "BY-PASS-POINTS")
        obj.by_pass_points = []
        container = SerializationHelper.find_child_element(element, "BY-PASS-POINTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.by_pass_points.append(child_value)

        # Parse explicit_rpt_refs (list from container "EXPLICIT-RPT-REFS")
        obj.explicit_rpt_refs = []
        container = SerializationHelper.find_child_element(element, "EXPLICIT-RPT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.explicit_rpt_refs.append(child_value)

        # Parse rpt_containers (list from container "RPT-CONTAINERS")
        obj.rpt_containers = []
        container = SerializationHelper.find_child_element(element, "RPT-CONTAINERS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.rpt_containers.append(child_value)

        # Parse rpt_executable_entity
        child = SerializationHelper.find_child_element(element, "RPT-EXECUTABLE-ENTITY")
        if child is not None:
            rpt_executable_entity_value = SerializationHelper.deserialize_by_tag(child, "RptExecutableEntity")
            obj.rpt_executable_entity = rpt_executable_entity_value

        # Parse rpt_hook
        child = SerializationHelper.find_child_element(element, "RPT-HOOK")
        if child is not None:
            rpt_hook_value = SerializationHelper.deserialize_by_tag(child, "RptHook")
            obj.rpt_hook = rpt_hook_value

        # Parse rpt_impl_policy
        child = SerializationHelper.find_child_element(element, "RPT-IMPL-POLICY")
        if child is not None:
            rpt_impl_policy_value = SerializationHelper.deserialize_by_tag(child, "RptImplPolicy")
            obj.rpt_impl_policy = rpt_impl_policy_value

        # Parse rpt_sw
        child = SerializationHelper.find_child_element(element, "RPT-SW")
        if child is not None:
            rpt_sw_value = SerializationHelper.deserialize_by_tag(child, "RptSwPrototypingAccess")
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
