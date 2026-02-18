"""ViewMapSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2079)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 401)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ViewMapSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.ViewMapSet.view_map import (
    ViewMap,
)


class ViewMapSet(ARElement):
    """AUTOSAR ViewMapSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    view_maps: list[ViewMap]
    def __init__(self) -> None:
        """Initialize ViewMapSet."""
        super().__init__()
        self.view_maps: list[ViewMap] = []


class ViewMapSetBuilder:
    """Builder for ViewMapSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ViewMapSet = ViewMapSet()

    def build(self) -> ViewMapSet:
        """Build and return ViewMapSet object.

        Returns:
            ViewMapSet instance
        """
        # TODO: Add validation
        return self._obj
