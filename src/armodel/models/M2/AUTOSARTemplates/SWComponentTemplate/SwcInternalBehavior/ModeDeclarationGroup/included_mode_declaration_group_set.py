"""IncludedModeDeclarationGroupSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 601)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_ModeDeclarationGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class IncludedModeDeclarationGroupSet(ARObject):
    """AUTOSAR IncludedModeDeclarationGroupSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    mode_refs: list[ARRef]
    prefix: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize IncludedModeDeclarationGroupSet."""
        super().__init__()
        self.mode_refs: list[ARRef] = []
        self.prefix: Optional[Identifier] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "IncludedModeDeclarationGroupSet":
        """Deserialize XML element to IncludedModeDeclarationGroupSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized IncludedModeDeclarationGroupSet object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse mode_refs (list)
        obj.mode_refs = []
        for child in ARObject._find_all_child_elements(element, "MODES"):
            mode_refs_value = ARObject._deserialize_by_tag(child, "ModeDeclarationGroup")
            obj.mode_refs.append(mode_refs_value)

        # Parse prefix
        child = ARObject._find_child_element(element, "PREFIX")
        if child is not None:
            prefix_value = child.text
            obj.prefix = prefix_value

        return obj



class IncludedModeDeclarationGroupSetBuilder:
    """Builder for IncludedModeDeclarationGroupSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: IncludedModeDeclarationGroupSet = IncludedModeDeclarationGroupSet()

    def build(self) -> IncludedModeDeclarationGroupSet:
        """Build and return IncludedModeDeclarationGroupSet object.

        Returns:
            IncludedModeDeclarationGroupSet instance
        """
        # TODO: Add validation
        return self._obj
