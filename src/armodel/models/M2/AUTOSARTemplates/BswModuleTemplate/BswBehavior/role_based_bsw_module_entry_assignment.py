"""RoleBasedBswModuleEntryAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 226)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class RoleBasedBswModuleEntryAssignment(ARObject):
    """AUTOSAR RoleBasedBswModuleEntryAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    assigned_entry: Optional[BswModuleEntry]
    role: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize RoleBasedBswModuleEntryAssignment."""
        super().__init__()
        self.assigned_entry: Optional[BswModuleEntry] = None
        self.role: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedBswModuleEntryAssignment":
        """Deserialize XML element to RoleBasedBswModuleEntryAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedBswModuleEntryAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse assigned_entry
        child = ARObject._find_child_element(element, "ASSIGNED-ENTRY")
        if child is not None:
            assigned_entry_value = ARObject._deserialize_by_tag(child, "BswModuleEntry")
            obj.assigned_entry = assigned_entry_value

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = child.text
            obj.role = role_value

        return obj



class RoleBasedBswModuleEntryAssignmentBuilder:
    """Builder for RoleBasedBswModuleEntryAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedBswModuleEntryAssignment = RoleBasedBswModuleEntryAssignment()

    def build(self) -> RoleBasedBswModuleEntryAssignment:
        """Build and return RoleBasedBswModuleEntryAssignment object.

        Returns:
            RoleBasedBswModuleEntryAssignment instance
        """
        # TODO: Add validation
        return self._obj
