"""MixedContentForLongName AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 62)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
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

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "e": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=EmphasisText,
        ),  # e
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
        "tt": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=Tt,
        ),  # tt
    }

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
