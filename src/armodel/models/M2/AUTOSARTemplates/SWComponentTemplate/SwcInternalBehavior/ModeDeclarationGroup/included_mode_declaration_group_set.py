"""IncludedModeDeclarationGroupSet AUTOSAR element."""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class IncludedModeDeclarationGroupSet(ARObject):
    """AUTOSAR IncludedModeDeclarationGroupSet."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
    }

    def __init__(self) -> None:
        """Initialize IncludedModeDeclarationGroupSet."""
        super().__init__()


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
