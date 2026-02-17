"""MultiLanguageVerbatim AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 291)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    FloatEnum,
    PgwideEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    String,
)
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_verbatim import (
    LVerbatim,
)


class MultiLanguageVerbatim(Paginateable):
    """AUTOSAR MultiLanguageVerbatim."""

    allow_break: Optional[NameToken]
    float: Optional[FloatEnum]
    help_entry: Optional[String]
    l5: LVerbatim
    pgwide: Optional[PgwideEnum]
    def __init__(self) -> None:
        """Initialize MultiLanguageVerbatim."""
        super().__init__()
        self.allow_break: Optional[NameToken] = None
        self.float: Optional[FloatEnum] = None
        self.help_entry: Optional[String] = None
        self.l5: LVerbatim = None
        self.pgwide: Optional[PgwideEnum] = None


class MultiLanguageVerbatimBuilder:
    """Builder for MultiLanguageVerbatim."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguageVerbatim = MultiLanguageVerbatim()

    def build(self) -> MultiLanguageVerbatim:
        """Build and return MultiLanguageVerbatim object.

        Returns:
            MultiLanguageVerbatim instance
        """
        # TODO: Add validation
        return self._obj
