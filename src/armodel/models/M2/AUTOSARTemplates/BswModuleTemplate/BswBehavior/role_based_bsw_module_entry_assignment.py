"""RoleBasedBswModuleEntryAssignment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("assigned_entry", None, False, False, BswModuleEntry),  # assignedEntry
        ("role", None, True, False, None),  # role
    ]

    def __init__(self) -> None:
        """Initialize RoleBasedBswModuleEntryAssignment."""
        super().__init__()
        self.assigned_entry: Optional[BswModuleEntry] = None
        self.role: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RoleBasedBswModuleEntryAssignment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedBswModuleEntryAssignment":
        """Create RoleBasedBswModuleEntryAssignment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RoleBasedBswModuleEntryAssignment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RoleBasedBswModuleEntryAssignment since parent returns ARObject
        return cast("RoleBasedBswModuleEntryAssignment", obj)


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
