"""RoleBasedMcDataAssignment AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "executions": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=RptExecutionContext,
        ),  # executions
        "mc_data_instances": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=McDataInstance,
        ),  # mcDataInstances
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
    }

    def __init__(self) -> None:
        """Initialize RoleBasedMcDataAssignment."""
        super().__init__()
        self.executions: list[RptExecutionContext] = []
        self.mc_data_instances: list[McDataInstance] = []
        self.role: Optional[Identifier] = None


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
