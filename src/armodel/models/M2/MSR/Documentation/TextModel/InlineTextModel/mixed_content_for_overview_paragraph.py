"""MixedContentForOverviewParagraph AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("br", None, False, False, Br),  # br
        ("e", None, False, False, EmphasisText),  # e
        ("ft", None, False, False, SlOverviewParagraph),  # ft
        ("ie", None, False, False, IndexEntry),  # ie
        ("sub", None, True, False, None),  # sub
        ("sup", None, True, False, None),  # sup
        ("trace", None, False, False, Traceable),  # trace
        ("tt", None, False, False, Tt),  # tt
        ("xref", None, False, False, Xref),  # xref
        ("xref_target", None, False, False, XrefTarget),  # xrefTarget
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MixedContentForOverviewParagraph to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForOverviewParagraph":
        """Create MixedContentForOverviewParagraph from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MixedContentForOverviewParagraph instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MixedContentForOverviewParagraph since parent returns ARObject
        return cast("MixedContentForOverviewParagraph", obj)


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
