"""RoleBasedDataTypeAssignment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)


class RoleBasedDataTypeAssignment(ARObject):
    """AUTOSAR RoleBasedDataTypeAssignment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("role", None, True, False, None),  # role
        ("used", None, False, False, any (ImplementationData)),  # used
    ]

    def __init__(self) -> None:
        """Initialize RoleBasedDataTypeAssignment."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.used: Optional[Any] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RoleBasedDataTypeAssignment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedDataTypeAssignment":
        """Create RoleBasedDataTypeAssignment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RoleBasedDataTypeAssignment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RoleBasedDataTypeAssignment since parent returns ARObject
        return cast("RoleBasedDataTypeAssignment", obj)


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
