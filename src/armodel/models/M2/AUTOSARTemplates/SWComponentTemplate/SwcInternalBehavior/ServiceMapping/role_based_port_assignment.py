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
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
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

    port_prototype_ref: Optional[ARRef]
    role: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize RoleBasedPortAssignment."""
        super().__init__()
        self.port_prototype_ref: Optional[ARRef] = None
        self.role: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedPortAssignment":
        """Deserialize XML element to RoleBasedPortAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedPortAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse port_prototype_ref
        child = ARObject._find_child_element(element, "PORT-PROTOTYPE")
        if child is not None:
            port_prototype_ref_value = ARObject._deserialize_by_tag(child, "PortPrototype")
            obj.port_prototype_ref = port_prototype_ref_value

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        return obj



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
