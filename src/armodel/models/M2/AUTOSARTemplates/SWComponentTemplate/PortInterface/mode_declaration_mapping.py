"""ModeDeclarationMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

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


class ModeDeclarationMapping(Identifiable):
    """AUTOSAR ModeDeclarationMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    first_modes: list[ModeDeclaration]
    second_mode: Optional[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeDeclarationMapping."""
        super().__init__()
        self.first_modes: list[ModeDeclaration] = []
        self.second_mode: Optional[ModeDeclaration] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "ModeDeclarationMapping":
        """Deserialize XML element to ModeDeclarationMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ModeDeclarationMapping object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ModeDeclarationMapping, cls).deserialize(element)

        # Parse first_modes (list from container "FIRST-MODES")
        obj.first_modes = []
        container = ARObject._find_child_element(element, "FIRST-MODES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.first_modes.append(child_value)

        # Parse second_mode
        child = ARObject._find_child_element(element, "SECOND-MODE")
        if child is not None:
            second_mode_value = ARObject._deserialize_by_tag(child, "ModeDeclaration")
            obj.second_mode = second_mode_value

        return obj



class ModeDeclarationMappingBuilder:
    """Builder for ModeDeclarationMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationMapping = ModeDeclarationMapping()

    def build(self) -> ModeDeclarationMapping:
        """Build and return ModeDeclarationMapping object.

        Returns:
            ModeDeclarationMapping instance
        """
        # TODO: Add validation
        return self._obj
