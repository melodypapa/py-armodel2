"""LPlainText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 349)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_LanguageDataModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class LPlainText(ARObject):
    """AUTOSAR LPlainText."""

    def __init__(self) -> None:
        """Initialize LPlainText."""
        super().__init__()


class LPlainTextBuilder:
    """Builder for LPlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LPlainText = LPlainText()

    def build(self) -> LPlainText:
        """Build and return LPlainText object.

        Returns:
            LPlainText instance
        """
        # TODO: Add validation
        return self._obj
