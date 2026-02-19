"""ModeTransition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 43)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 630)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ModeDeclaration.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeTransition(Identifiable):
    """AUTOSAR ModeTransition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    entered_mode: Optional[ModeDeclaration]
    exited_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeTransition."""
        super().__init__()
        self.entered_mode: Optional[ModeDeclaration] = None
        self.exited_mode: Optional[ModeDeclaration] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeTransition":
        """Deserialize XML element to ModeTransition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeTransition object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeTransition, cls).deserialize(element)

        # Parse entered_mode
        child = ARObject._find_child_element(element, "ENTERED-MODE")
        if child is not None:
            entered_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.entered_mode = entered_mode_value

        # Parse exited_mode
        child = ARObject._find_child_element(element, "EXITED-MODE")
        if child is not None:
            exited_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.exited_mode = exited_mode_value

        return obj



class ModeTransitionBuilder:
    """Builder for ModeTransition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeTransition = ModeTransition()

    def build(self) -> ModeTransition:
        """Build and return ModeTransition object.

        Returns:
            ModeTransition instance
        """
        # TODO: Add validation
        return self._obj
