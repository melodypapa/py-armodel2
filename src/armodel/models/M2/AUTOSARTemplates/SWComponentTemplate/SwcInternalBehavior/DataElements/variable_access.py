"""VariableAccess AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 351)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 567)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2077)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 256)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_DataElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.abstract_access_point import (
    AbstractAccessPoint,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements import (
    VariableAccessScopeEnum,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)


class VariableAccess(AbstractAccessPoint):
    """AUTOSAR VariableAccess."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    accessed_variable_ref: Optional[ARRef]
    scope: Optional[VariableAccessScopeEnum]
    def __init__(self) -> None:
        """Initialize VariableAccess."""
        super().__init__()
        self.accessed_variable_ref: Optional[ARRef] = None
        self.scope: Optional[VariableAccessScopeEnum] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "VariableAccess":
        """Deserialize XML element to VariableAccess object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized VariableAccess object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse accessed_variable_ref
        child = ARObject._find_child_element(element, "ACCESSED-VARIABLE")
        if child is not None:
            accessed_variable_ref_value = ARObject._deserialize_by_tag(child, "AutosarVariableRef")
            obj.accessed_variable_ref = accessed_variable_ref_value

        # Parse scope
        child = ARObject._find_child_element(element, "SCOPE")
        if child is not None:
            scope_value = child.text
            obj.scope = scope_value

        return obj



class VariableAccessBuilder:
    """Builder for VariableAccess."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: VariableAccess = VariableAccess()

    def build(self) -> VariableAccess:
        """Build and return VariableAccess object.

        Returns:
            VariableAccess instance
        """
        # TODO: Add validation
        return self._obj
