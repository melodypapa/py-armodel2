"""ViewMap AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2079)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 401)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_ViewMapSet.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class ViewMap(Identifiable):
    """AUTOSAR ViewMap."""

    first_elements: list[AtpFeature]
    role: Optional[Identifier]
    second_elements: list[AtpFeature]
    def __init__(self) -> None:
        """Initialize ViewMap."""
        super().__init__()
        self.first_elements: list[AtpFeature] = []
        self.role: Optional[Identifier] = None
        self.second_elements: list[AtpFeature] = []


class ViewMapBuilder:
    """Builder for ViewMap."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ViewMap = ViewMap()

    def build(self) -> ViewMap:
        """Build and return ViewMap object.

        Returns:
            ViewMap instance
        """
        # TODO: Add validation
        return self._obj
