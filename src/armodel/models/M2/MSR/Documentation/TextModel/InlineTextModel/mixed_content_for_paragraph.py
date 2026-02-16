"""MixedContentForParagraph AUTOSAR element."""

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
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("br", None, False, False, Br),  # br
        ("e", None, False, False, EmphasisText),  # e
        ("ft", None, False, False, SlParagraph),  # ft
        ("ie", None, False, False, IndexEntry),  # ie
        ("std", None, False, False, Std),  # std
        ("sub", None, True, False, None),  # sub
        ("sup", None, True, False, None),  # sup
        ("trace", None, False, False, Traceable),  # trace
        ("tt", None, False, False, Tt),  # tt
        ("xdoc", None, False, False, Xdoc),  # xdoc
        ("xfile", None, False, False, Xfile),  # xfile
        ("xref", None, False, False, Xref),  # xref
        ("xref_target", None, False, False, XrefTarget),  # xrefTarget
    ]

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

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert MixedContentForParagraph to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "MixedContentForParagraph":
        """Create MixedContentForParagraph from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            MixedContentForParagraph instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to MixedContentForParagraph since parent returns ARObject
        return cast("MixedContentForParagraph", obj)


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
