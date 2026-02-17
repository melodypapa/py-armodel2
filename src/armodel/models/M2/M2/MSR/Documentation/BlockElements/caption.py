"""Caption AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 432)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class Caption(MultilanguageReferrable):
    """AUTOSAR Caption."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "desc": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=MultiLanguageOverviewParagraph,
        ),  # desc
    }

    def __init__(self) -> None:
        """Initialize Caption."""
        super().__init__()
        self.desc: Optional[MultiLanguageOverviewParagraph] = None


class CaptionBuilder:
    """Builder for Caption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Caption = Caption()

    def build(self) -> Caption:
        """Build and return Caption object.

        Returns:
            Caption instance
        """
        # TODO: Add validation
        return self._obj
