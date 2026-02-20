"""MultiLanguageParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 290)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import l_prefix

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_paragraph import (
    LParagraph,
)


class MultiLanguageParagraph(Paginateable):
    """AUTOSAR MultiLanguageParagraph."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    help_entry: Optional[String]
    _l1: list[LParagraph]
    def __init__(self) -> None:
        """Initialize MultiLanguageParagraph."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self._l1: list[LParagraph] = []
    @property
    @l_prefix("L-1")
    def l1(self) -> LParagraph:
        """Get l1 with language-specific wrapper."""
        return self._l1

    @l1.setter
    def l1(self, value: LParagraph) -> None:
        """Set l1 with language-specific wrapper."""
        self._l1 = value




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
