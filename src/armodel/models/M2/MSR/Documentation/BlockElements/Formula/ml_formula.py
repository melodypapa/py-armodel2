"""MlFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 301)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 309)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_Formula.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.caption import (
    Caption,
)
from armodel.models.M2.MSR.Documentation.BlockElements.Figure.l_graphic import (
    LGraphic,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_plain_text import (
    MultiLanguagePlainText,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_verbatim import (
    MultiLanguageVerbatim,
)


class MlFormula(Paginateable):
    """AUTOSAR MlFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    formula_caption: Optional[Caption]
    generic_math: Optional[MultiLanguagePlainText]
    l_graphics: list[LGraphic]
    tex_math: Optional[MultiLanguagePlainText]
    verbatim: Optional[MultiLanguageVerbatim]
    def __init__(self) -> None:
        """Initialize MlFormula."""
        super().__init__()
        self.formula_caption: Optional[Caption] = None
        self.generic_math: Optional[MultiLanguagePlainText] = None
        self.l_graphics: list[LGraphic] = []
        self.tex_math: Optional[MultiLanguagePlainText] = None
        self.verbatim: Optional[MultiLanguageVerbatim] = None


class MlFormulaBuilder:
    """Builder for MlFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MlFormula = MlFormula()

    def build(self) -> MlFormula:
        """Build and return MlFormula object.

        Returns:
            MlFormula instance
        """
        # TODO: Add validation
        return self._obj
