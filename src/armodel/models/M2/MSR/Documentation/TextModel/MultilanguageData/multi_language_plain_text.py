"""MultiLanguagePlainText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 349)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_MultilanguageData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization.decorators import l_prefix

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.LanguageDataModel.l_plain_text import (
    LPlainText,
)


class MultiLanguagePlainText(ARObject):
    """AUTOSAR MultiLanguagePlainText."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _l10: list[LPlainText]
    def __init__(self) -> None:
        """Initialize MultiLanguagePlainText."""
        super().__init__()
        self._l10: list[LPlainText] = []
    @property
    @l_prefix("L-10")
    def l10(self) -> list[LPlainText]:
        """Get l10 with language-specific wrapper."""
        return self._l10

    @l10.setter
    def l10(self, value: list[LPlainText]) -> None:
        """Set l10 with language-specific wrapper."""
        self._l10 = value




class MultiLanguagePlainTextBuilder:
    """Builder for MultiLanguagePlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MultiLanguagePlainText = MultiLanguagePlainText()

    def build(self) -> MultiLanguagePlainText:
        """Build and return MultiLanguagePlainText object.

        Returns:
            MultiLanguagePlainText instance
        """
        # TODO: Add validation
        return self._obj
