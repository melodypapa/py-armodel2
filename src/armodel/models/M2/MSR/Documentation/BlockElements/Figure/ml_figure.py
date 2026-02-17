"""MlFigure AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 307)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Figure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FrameEnum,
    PgwideEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.l_graphic import (
    LGraphic,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class MlFigure(Paginateable):
    """AUTOSAR MlFigure."""

    def __init__(self) -> None:
        """Initialize MlFigure."""
        super().__init__()
        self.figure_caption: Optional[Caption] = None
        self.frame: Optional[FrameEnum] = None
        self.help_entry: Optional[String] = None
        self.l_graphics: list[LGraphic] = []
        self.pgwide: Optional[PgwideEnum] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None


class MlFigureBuilder:
    """Builder for MlFigure."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MlFigure = MlFigure()

    def build(self) -> MlFigure:
        """Build and return MlFigure object.

        Returns:
            MlFigure instance
        """
        # TODO: Add validation
        return self._obj
