"""RptExecutableEntityEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 201)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport_RptSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    execution_refs: list[ARRef]
    mc_datas: list[RoleBasedMcDataAssignment]
    rpt_event_id: Optional[PositiveInteger]
    rpt_executable_entity: Optional[RptExecutableEntity]
    rpt_impl_policy: Optional[RptImplPolicy]
    rpt_service_point_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize RptExecutableEntityEvent."""
        super().__init__()
        self.execution_refs: list[ARRef] = []
        self.mc_datas: list[RoleBasedMcDataAssignment] = []
        self.rpt_event_id: Optional[PositiveInteger] = None
        self.rpt_executable_entity: Optional[RptExecutableEntity] = None
        self.rpt_impl_policy: Optional[RptImplPolicy] = None
        self.rpt_service_point_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize RptExecutableEntityEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RptExecutableEntityEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize execution_refs (list to container "EXECUTION-REFS")
        if self.execution_refs:
            wrapper = ET.Element("EXECUTION-REFS")
            for item in self.execution_refs:
                serialized = SerializationHelper.serialize_item(item, "RptExecutionContext")
                if serialized is not None:
                    child_elem = ET.Element("EXECUTION-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_datas (list to container "MC-DATAS")
        if self.mc_datas:
            wrapper = ET.Element("MC-DATAS")
            for item in self.mc_datas:
                serialized = SerializationHelper.serialize_item(item, "RoleBasedMcDataAssignment")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize rpt_event_id
        if self.rpt_event_id is not None:
            serialized = SerializationHelper.serialize_item(self.rpt_event_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("RPT-EVENT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

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

        # Serialize rpt_service_point_refs (list to container "RPT-SERVICE-POINT-REFS")
        if self.rpt_service_point_refs:
            wrapper = ET.Element("RPT-SERVICE-POINT-REFS")
            for item in self.rpt_service_point_refs:
                serialized = SerializationHelper.serialize_item(item, "RptServicePoint")
                if serialized is not None:
                    child_elem = ET.Element("RPT-SERVICE-POINT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RptExecutableEntityEvent":
        """Deserialize XML element to RptExecutableEntityEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RptExecutableEntityEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(RptExecutableEntityEvent, cls).deserialize(element)

        # Parse execution_refs (list from container "EXECUTION-REFS")
        obj.execution_refs = []
        container = SerializationHelper.find_child_element(element, "EXECUTION-REFS")
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
                    obj.execution_refs.append(child_value)

        # Parse mc_datas (list from container "MC-DATAS")
        obj.mc_datas = []
        container = SerializationHelper.find_child_element(element, "MC-DATAS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_datas.append(child_value)

        # Parse rpt_event_id
        child = SerializationHelper.find_child_element(element, "RPT-EVENT-ID")
        if child is not None:
            rpt_event_id_value = child.text
            obj.rpt_event_id = rpt_event_id_value

        # Parse rpt_executable_entity
        child = SerializationHelper.find_child_element(element, "RPT-EXECUTABLE-ENTITY")
        if child is not None:
            rpt_executable_entity_value = SerializationHelper.deserialize_by_tag(child, "RptExecutableEntity")
            obj.rpt_executable_entity = rpt_executable_entity_value

        # Parse rpt_impl_policy
        child = SerializationHelper.find_child_element(element, "RPT-IMPL-POLICY")
        if child is not None:
            rpt_impl_policy_value = SerializationHelper.deserialize_by_tag(child, "RptImplPolicy")
            obj.rpt_impl_policy = rpt_impl_policy_value

        # Parse rpt_service_point_refs (list from container "RPT-SERVICE-POINT-REFS")
        obj.rpt_service_point_refs = []
        container = SerializationHelper.find_child_element(element, "RPT-SERVICE-POINT-REFS")
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
                    obj.rpt_service_point_refs.append(child_value)

        return obj



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
