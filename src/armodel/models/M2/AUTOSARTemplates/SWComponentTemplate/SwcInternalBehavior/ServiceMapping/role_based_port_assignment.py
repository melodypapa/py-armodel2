"""RoleBasedPortAssignment AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)


class RoleBasedPortAssignment(ARObject):
    """AUTOSAR RoleBasedPortAssignment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("port_prototype", None, False, False, PortPrototype),  # portPrototype
        ("role", None, True, False, None),  # role
    ]

    def __init__(self) -> None:
        """Initialize RoleBasedPortAssignment."""
        super().__init__()
        self.port_prototype: Optional[PortPrototype] = None
        self.role: Optional[Identifier] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert RoleBasedPortAssignment to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedPortAssignment":
        """Create RoleBasedPortAssignment from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            RoleBasedPortAssignment instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to RoleBasedPortAssignment since parent returns ARObject
        return cast("RoleBasedPortAssignment", obj)


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
