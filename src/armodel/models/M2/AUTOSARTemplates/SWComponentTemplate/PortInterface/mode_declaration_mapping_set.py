"""ModeDeclarationMappingSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 132)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)


class ModeDeclarationMappingSet(ARElement):
    """AUTOSAR ModeDeclarationMappingSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    modes: list[ModeDeclaration]
    def __init__(self) -> None:
        """Initialize ModeDeclarationMappingSet."""
        super().__init__()
        self.modes: list[ModeDeclaration] = []


class ModeDeclarationMappingSetBuilder:
    """Builder for ModeDeclarationMappingSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ModeDeclarationMappingSet = ModeDeclarationMappingSet()

    def build(self) -> ModeDeclarationMappingSet:
        """Build and return ModeDeclarationMappingSet object.

        Returns:
            ModeDeclarationMappingSet instance
        """
        # TODO: Add validation
        return self._obj
