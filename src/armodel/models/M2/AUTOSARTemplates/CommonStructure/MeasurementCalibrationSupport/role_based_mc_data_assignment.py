"""RoleBasedMcDataAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 329)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_MeasurementCalibrationSupport.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    executions: list[RptExecutionContext]
    mc_data_instances: list[McDataInstance]
    role: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize RoleBasedMcDataAssignment."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.mc_data_instances: list[McDataInstance] = []
        self.role: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize RoleBasedMcDataAssignment to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize executions (list to container "EXECUTIONS")
        if self.executions:
            wrapper = ET.Element("EXECUTIONS")
            for item in self.executions:
                serialized = ARObject._serialize_item(item, "RptExecutionContext")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize mc_data_instances (list to container "MC-DATA-INSTANCES")
        if self.mc_data_instances:
            wrapper = ET.Element("MC-DATA-INSTANCES")
            for item in self.mc_data_instances:
                serialized = ARObject._serialize_item(item, "McDataInstance")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize role
        if self.role is not None:
            serialized = ARObject._serialize_item(self.role, "Identifier")
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

        # Parse executions (list from container "EXECUTIONS")
        obj.executions = []
        container = ARObject._find_child_element(element, "EXECUTIONS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.executions.append(child_value)

        # Parse mc_data_instances (list from container "MC-DATA-INSTANCES")
        obj.mc_data_instances = []
        container = ARObject._find_child_element(element, "MC-DATA-INSTANCES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.mc_data_instances.append(child_value)

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
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
