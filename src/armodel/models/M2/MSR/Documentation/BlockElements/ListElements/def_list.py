"""DefList AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 297)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.def_item import (
        DefItem,
    )



class DefList(Paginateable):
    """AUTOSAR DefList."""

    def_item: DefItem
    def __init__(self) -> None:
        """Initialize DefList."""
        super().__init__()
        self.def_item: DefItem = None


class DefListBuilder:
    """Builder for DefList."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DefList = DefList()

    def build(self) -> DefList:
        """Build and return DefList object.

        Returns:
            DefList instance
        """
        # TODO: Add validation
        return self._obj
