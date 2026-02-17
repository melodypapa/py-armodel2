"""LabeledList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 296)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.indent_sample import (
    IndentSample,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.labeled_item import (
    LabeledItem,
)


class LabeledList(Paginateable):
    """AUTOSAR LabeledList."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "indent_sample": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=IndentSample,
        ),  # indentSample
        "labeled_item_label": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="1",
            element_class=LabeledItem,
        ),  # labeledItemLabel
    }

    def __init__(self) -> None:
        """Initialize LabeledList."""
        super().__init__()
        self.indent_sample: Optional[IndentSample] = None
        self.labeled_item_label: LabeledItem = None


class LabeledListBuilder:
    """Builder for LabeledList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LabeledList = LabeledList()

    def build(self) -> LabeledList:
        """Build and return LabeledList object.

        Returns:
            LabeledList instance
        """
        # TODO: Add validation
        return self._obj
