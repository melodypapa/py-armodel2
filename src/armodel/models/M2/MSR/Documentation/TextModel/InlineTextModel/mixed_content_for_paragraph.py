"""MixedContentForParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 289)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements import (
    Superscript,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.br import (
    Br,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.index_entry import (
    IndexEntry,
)
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.sl_paragraph import (
    SlParagraph,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.std import (
    Std,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xdoc import (
    Xdoc,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xfile import (
    Xfile,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
    Xref,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref_target import (
    XrefTarget,
)


class MixedContentForParagraph(ARObject):
    """AUTOSAR MixedContentForParagraph."""

    br: Br
    e: EmphasisText
    ft: SlParagraph
    ie: IndexEntry
    std: Std
    sub: Superscript
    sup: Superscript
    trace: Traceable
    tt: Tt
    xdoc: Xdoc
    xfile: Xfile
    xref: Xref
    xref_target: XrefTarget
    def __init__(self) -> None:
        """Initialize MixedContentForParagraph."""
        super().__init__()
        self.br: Br = None
        self.e: EmphasisText = None
        self.ft: SlParagraph = None
        self.ie: IndexEntry = None
        self.std: Std = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.trace: Traceable = None
        self.tt: Tt = None
        self.xdoc: Xdoc = None
        self.xfile: Xfile = None
        self.xref: Xref = None
        self.xref_target: XrefTarget = None


class MixedContentForParagraphBuilder:
    """Builder for MixedContentForParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForParagraph = MixedContentForParagraph()

    def build(self) -> MixedContentForParagraph:
        """Build and return MixedContentForParagraph object.

        Returns:
            MixedContentForParagraph instance
        """
        # TODO: Add validation
        return self._obj
