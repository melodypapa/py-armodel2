"""MultiLanguageParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 290)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import (
    LParagraph,
)


class MultiLanguageParagraph(Paginateable):
    """AUTOSAR MultiLanguageParagraph."""

    def __init__(self) -> None:
        """Initialize MultiLanguageParagraph."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.l1: LParagraph = None


class MultiLanguageParagraphBuilder:
    """Builder for MultiLanguageParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguageParagraph = MultiLanguageParagraph()

    def build(self) -> MultiLanguageParagraph:
        """Build and return MultiLanguageParagraph object.

        Returns:
            MultiLanguageParagraph instance
        """
        # TODO: Add validation
        return self._obj
