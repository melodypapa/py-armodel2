"""RoleBasedDataTypeAssignment AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)


class RoleBasedDataTypeAssignment(ARObject):
    """AUTOSAR RoleBasedDataTypeAssignment."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
        "used": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=any (ImplementationData),
        ),  # used
    }

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
