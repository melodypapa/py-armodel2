"""MixedContentForParagraph AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 289)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "br": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Br,
        ),  # br
        "e": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=EmphasisText,
        ),  # e
        "ft": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=SlParagraph,
        ),  # ft
        "ie": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=IndexEntry,
        ),  # ie
        "std": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Std,
        ),  # std
        "sub": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # sub
        "sup": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="1",
        ),  # sup
        "trace": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Traceable,
        ),  # trace
        "tt": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Tt,
        ),  # tt
        "xdoc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Xdoc,
        ),  # xdoc
        "xfile": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Xfile,
        ),  # xfile
        "xref": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Xref,
        ),  # xref
        "xref_target": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=XrefTarget,
        ),  # xrefTarget
    }

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
