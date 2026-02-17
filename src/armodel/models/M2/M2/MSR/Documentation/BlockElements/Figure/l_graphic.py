"""LGraphic AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 307)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.language_specific import (
    LanguageSpecific,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.graphic import (
    Graphic,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.map import (
    Map,
)


class LGraphic(LanguageSpecific):
    """AUTOSAR LGraphic."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "graphic": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Graphic,
        ),  # graphic
        "map": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=Map,
        ),  # map
    }

    def __init__(self) -> None:
        """Initialize LGraphic."""
        super().__init__()
        self.graphic: Graphic = None
        self.map: Optional[Map] = None


class LGraphicBuilder:
    """Builder for LGraphic."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LGraphic = LGraphic()

    def build(self) -> LGraphic:
        """Build and return LGraphic object.

        Returns:
            LGraphic instance
        """
        # TODO: Add validation
        return self._obj
