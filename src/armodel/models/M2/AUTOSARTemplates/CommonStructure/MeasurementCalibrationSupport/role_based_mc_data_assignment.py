"""RoleBasedMcDataAssignment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.RptSupport.rpt_execution_context import (
    RptExecutionContext,
)


class RoleBasedMcDataAssignment(ARObject):
    """AUTOSAR RoleBasedMcDataAssignment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("executions", None, False, True, RptExecutionContext),  # executions
        ("mc_data_instances", None, False, True, McDataInstance),  # mcDataInstances
        ("role", None, True, False, None),  # role
    ]

    def __init__(self) -> None:
        """Initialize RoleBasedMcDataAssignment."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.mc_data_instances: list[McDataInstance] = []
        self.role: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RoleBasedMcDataAssignment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedMcDataAssignment":
        """Create RoleBasedMcDataAssignment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RoleBasedMcDataAssignment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RoleBasedMcDataAssignment since parent returns ARObject
        return cast("RoleBasedMcDataAssignment", obj)


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
