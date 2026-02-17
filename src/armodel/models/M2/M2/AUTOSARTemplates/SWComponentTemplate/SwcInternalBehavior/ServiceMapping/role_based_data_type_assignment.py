"""RoleBasedDataTypeAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 227)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 610)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)


class RoleBasedDataTypeAssignment(ARObject):
    """AUTOSAR RoleBasedDataTypeAssignment."""

    def __init__(self) -> None:
        """Initialize RoleBasedDataTypeAssignment."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.used: Optional[Any] = None


class RoleBasedDataTypeAssignmentBuilder:
    """Builder for RoleBasedDataTypeAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedDataTypeAssignment = RoleBasedDataTypeAssignment()

    def build(self) -> RoleBasedDataTypeAssignment:
        """Build and return RoleBasedDataTypeAssignment object.

        Returns:
            RoleBasedDataTypeAssignment instance
        """
        # TODO: Add validation
        return self._obj
