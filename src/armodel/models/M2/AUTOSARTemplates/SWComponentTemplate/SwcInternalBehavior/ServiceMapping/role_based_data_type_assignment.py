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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    role: Optional[Identifier]
    used: Optional[Any]
    def __init__(self) -> None:
        """Initialize RoleBasedDataTypeAssignment."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.used: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedDataTypeAssignment":
        """Deserialize XML element to RoleBasedDataTypeAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedDataTypeAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.role = role_value

        # Parse used
        child = ARObject._find_child_element(element, "USED")
        if child is not None:
            used_value = child.text
            obj.used = used_value

        return obj



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
