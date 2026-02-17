"""MixedContentForPlainText AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 349)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class MixedContentForPlainText(ARObject):
    """AUTOSAR MixedContentForPlainText."""

    def __init__(self) -> None:
        """Initialize MixedContentForPlainText."""
        super().__init__()


class MixedContentForPlainTextBuilder:
    """Builder for MixedContentForPlainText."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForPlainText = MixedContentForPlainText()

    def build(self) -> MixedContentForPlainText:
        """Build and return MixedContentForPlainText object.

        Returns:
            MixedContentForPlainText instance
        """
        # TODO: Add validation
        return self._obj
