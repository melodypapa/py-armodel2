"""MixedContentForLongName AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.index_entry import (
    IndexEntry,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)


class MixedContentForLongName(ARObject):
    """AUTOSAR MixedContentForLongName."""

    def __init__(self) -> None:
        """Initialize MixedContentForLongName."""
        super().__init__()
        self.e: EmphasisText = None
        self.ie: IndexEntry = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.tt: Tt = None


class MixedContentForLongNameBuilder:
    """Builder for MixedContentForLongName."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForLongName = MixedContentForLongName()

    def build(self) -> MixedContentForLongName:
        """Build and return MixedContentForLongName object.

        Returns:
            MixedContentForLongName instance
        """
        # TODO: Add validation
        return self._obj
