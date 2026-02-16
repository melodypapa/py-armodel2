"""MixedContentForOverviewParagraph AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
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
from armodel.models.M2.MSR.Documentation.TextModel.SingleLanguageData.sl_overview_paragraph import (
    SlOverviewParagraph,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable import (
    Traceable,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
    Xref,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref_target import (
    XrefTarget,
)


class MixedContentForOverviewParagraph(ARObject):
    """AUTOSAR MixedContentForOverviewParagraph."""

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
            element_class=SlOverviewParagraph,
        ),  # ft
        "ie": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=IndexEntry,
        ),  # ie
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
        """Initialize MixedContentForOverviewParagraph."""
        super().__init__()
        self.br: Br = None
        self.e: EmphasisText = None
        self.ft: SlOverviewParagraph = None
        self.ie: IndexEntry = None
        self.sub: Superscript = None
        self.sup: Superscript = None
        self.trace: Traceable = None
        self.tt: Tt = None
        self.xref: Xref = None
        self.xref_target: XrefTarget = None


class MixedContentForOverviewParagraphBuilder:
    """Builder for MixedContentForOverviewParagraph."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForOverviewParagraph = MixedContentForOverviewParagraph()

    def build(self) -> MixedContentForOverviewParagraph:
        """Build and return MixedContentForOverviewParagraph object.

        Returns:
            MixedContentForOverviewParagraph instance
        """
        # TODO: Add validation
        return self._obj
