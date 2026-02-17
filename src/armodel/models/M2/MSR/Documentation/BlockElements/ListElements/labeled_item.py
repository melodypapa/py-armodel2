"""LabeledItem AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 296)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)
from armodel.models.M2.MSR.Documentation.TextModel.MultilanguageData.multi_language_overview_paragraph import (
    MultiLanguageOverviewParagraph,
)


class LabeledItem(Paginateable):
    """AUTOSAR LabeledItem."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "help_entry": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # helpEntry
        "item_contents": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=DocumentationBlock,
        ),  # itemContents
        "item_label": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=MultiLanguageOverviewParagraph,
        ),  # itemLabel
    }

    def __init__(self) -> None:
        """Initialize LabeledItem."""
        super().__init__()
        self.help_entry: Optional[String] = None
        self.item_contents: Optional[DocumentationBlock] = None
        self.item_label: MultiLanguageOverviewParagraph = None


class LabeledItemBuilder:
    """Builder for LabeledItem."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LabeledItem = LabeledItem()

    def build(self) -> LabeledItem:
        """Build and return LabeledItem object.

        Returns:
            LabeledItem instance
        """
        # TODO: Add validation
        return self._obj
