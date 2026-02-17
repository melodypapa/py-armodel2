"""RoleBasedDataAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 226)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 607)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)


class RoleBasedDataAssignment(ARObject):
    """AUTOSAR RoleBasedDataAssignment."""

    role: Optional[Identifier]
    used_data: Optional[AutosarVariableRef]
    used_parameter: Optional[AutosarParameterRef]
    used_pim: Optional[PerInstanceMemory]
    def __init__(self) -> None:
        """Initialize RoleBasedDataAssignment."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.used_data: Optional[AutosarVariableRef] = None
        self.used_parameter: Optional[AutosarParameterRef] = None
        self.used_pim: Optional[PerInstanceMemory] = None


class RoleBasedDataAssignmentBuilder:
    """Builder for RoleBasedDataAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedDataAssignment = RoleBasedDataAssignment()

    def build(self) -> RoleBasedDataAssignment:
        """Build and return RoleBasedDataAssignment object.

        Returns:
            RoleBasedDataAssignment instance
        """
        # TODO: Add validation
        return self._obj
