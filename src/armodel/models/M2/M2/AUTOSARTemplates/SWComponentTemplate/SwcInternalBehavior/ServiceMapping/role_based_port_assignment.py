"""RoleBasedPortAssignment AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "port_prototype": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortPrototype,
        ),  # portPrototype
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
    }

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
