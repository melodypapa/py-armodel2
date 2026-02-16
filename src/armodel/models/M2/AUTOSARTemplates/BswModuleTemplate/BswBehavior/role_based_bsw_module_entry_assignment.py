"""RoleBasedBswModuleEntryAssignment AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class RoleBasedBswModuleEntryAssignment(ARObject):
    """AUTOSAR RoleBasedBswModuleEntryAssignment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "assigned_entry": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswModuleEntry,
        ),  # assignedEntry
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
    }

    def __init__(self) -> None:
        """Initialize RoleBasedBswModuleEntryAssignment."""
        super().__init__()
        self.assigned_entry: Optional[BswModuleEntry] = None
        self.role: Optional[Identifier] = None


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
