"""RoleBasedDataAssignment AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 226)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 607)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ServiceNeeds.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PerInstanceMemory.per_instance_memory import (
    PerInstanceMemory,
)


class RoleBasedDataAssignment(ARObject):
    """AUTOSAR RoleBasedDataAssignment."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    role: Optional[Identifier]
    used_data_ref: Optional[ARRef]
    used_parameter_ref: Optional[ARRef]
    used_pim: Optional[PerInstanceMemory]
    def __init__(self) -> None:
        """Initialize RoleBasedDataAssignment."""
        super().__init__()
        self.role: Optional[Identifier] = None
        self.used_data_ref: Optional[ARRef] = None
        self.used_parameter_ref: Optional[ARRef] = None
        self.used_pim: Optional[PerInstanceMemory] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "RoleBasedDataAssignment":
        """Deserialize XML element to RoleBasedDataAssignment object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RoleBasedDataAssignment object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse role
        child = ARObject._find_child_element(element, "ROLE")
        if child is not None:
            role_value = child.text
            obj.role = role_value

        # Parse used_data_ref
        child = ARObject._find_child_element(element, "USED-DATA")
        if child is not None:
            used_data_ref_value = ARObject._deserialize_by_tag(child, "AutosarVariableRef")
            obj.used_data_ref = used_data_ref_value

        # Parse used_parameter_ref
        child = ARObject._find_child_element(element, "USED-PARAMETER")
        if child is not None:
            used_parameter_ref_value = ARObject._deserialize_by_tag(child, "AutosarParameterRef")
            obj.used_parameter_ref = used_parameter_ref_value

        # Parse used_pim
        child = ARObject._find_child_element(element, "USED-PIM")
        if child is not None:
            used_pim_value = ARObject._deserialize_by_tag(child, "PerInstanceMemory")
            obj.used_pim = used_pim_value

        return obj



class RoleBasedDataAssignmentBuilder:
    """Builder for RoleBasedDataAssignment."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RoleBasedDataAssignment = RoleBasedDataAssignment()

    def build(self) -> RoleBasedDataAssignment:
        """Build and return RoleBasedDataAssignment object.

        Returns:
            RoleBasedDataAssignment instance
        """
        # TODO: Add validation
        return self._obj
