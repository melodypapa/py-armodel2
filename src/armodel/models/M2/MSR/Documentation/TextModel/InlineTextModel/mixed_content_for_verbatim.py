"""MixedContentForVerbatim AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 292)

JSON Source: docs/json/packages/M2_MSR_Documentation_TextModel_InlineTextModel.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.br import (
    Br,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.emphasis_text import (
    EmphasisText,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.tt import (
    Tt,
)
from armodel.models.M2.MSR.Documentation.TextModel.InlineTextElements.xref import (
    Xref,
)


class MixedContentForVerbatim(ARObject):
    """AUTOSAR MixedContentForVerbatim."""

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
    }

    def __init__(self) -> None:
        """Initialize MixedContentForVerbatim."""
        super().__init__()
        self.br: Br = None
        self.e: EmphasisText = None
        self.tt: Tt = None
        self.xref: Xref = None


class MixedContentForVerbatimBuilder:
    """Builder for MixedContentForVerbatim."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MixedContentForVerbatim = MixedContentForVerbatim()

    def build(self) -> MixedContentForVerbatim:
        """Build and return MixedContentForVerbatim object.

        Returns:
            MixedContentForVerbatim instance
        """
        # TODO: Add validation
        return self._obj
