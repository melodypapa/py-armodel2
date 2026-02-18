"""RoleBasedPortAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 329)
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 166)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 604)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2050)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ServiceMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class RoleBasedPortAssignment(ARObject):
    """AUTOSAR RoleBasedPortAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    port_prototype: Optional[PortPrototype]
    role: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize RoleBasedPortAssignment."""
        super().__init__()
        self.port_prototype: Optional[PortPrototype] = None
        self.role: Optional[Identifier] = None


class RoleBasedPortAssignmentBuilder:
    """Builder for RoleBasedPortAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedPortAssignment = RoleBasedPortAssignment()

    def build(self) -> RoleBasedPortAssignment:
        """Build and return RoleBasedPortAssignment object.

        Returns:
            RoleBasedPortAssignment instance
        """
        # TODO: Add validation
        return self._obj
