"""RoleBasedMcDataAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
        McDataInstance,
    )



class RoleBasedMcDataAssignment(ARObject):
    """AUTOSAR RoleBasedMcDataAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    execution_refs: list[ARRef]
    mc_data_instance_refs: list[ARRef]
    role: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize RoleBasedMcDataAssignment."""
        super().__init__()
        self.execution_refs: list[ARRef] = []
        self.mc_data_instance_refs: list[ARRef] = []
        self.role: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RoleBasedMcDataAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

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

        # Serialize mc_data_instance_refs (list to container "MC-DATA-INSTANCE-REFS")
        if self.mc_data_instance_refs:
            wrapper = ET.Element("MC-DATA-INSTANCE-REFS")
            for item in self.mc_data_instance_refs:
                serialized = SerializationHelper.serialize_item(item, "McDataInstance")
                if serialized is not None:
                    child_elem = ET.Element("MC-DATA-INSTANCE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize role
        if self.role is not None:
            serialized = SerializationHelper.serialize_item(self.role, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ROLE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedMcDataAssignment":
        """Deserialize XML element to RoleBasedMcDataAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedMcDataAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

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

        # Parse mc_data_instance_refs (list from container "MC-DATA-INSTANCE-REFS")
        obj.mc_data_instance_refs = []
        container = SerializationHelper.find_child_element(element, "MC-DATA-INSTANCE-REFS")
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
                    obj.mc_data_instance_refs.append(child_value)

        # Parse role
        child = SerializationHelper.find_child_element(element, "ROLE")
        if child is not None:
            role_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        return obj



class RoleBasedMcDataAssignmentBuilder:
    """Builder for RoleBasedMcDataAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedMcDataAssignment = RoleBasedMcDataAssignment()

    def build(self) -> RoleBasedMcDataAssignment:
        """Build and return RoleBasedMcDataAssignment object.

        Returns:
            RoleBasedMcDataAssignment instance
        """
        # TODO: Add validation
        return self._obj
