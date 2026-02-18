"""Item AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 295)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
        DocumentationBlock,
    )



class Item(Paginateable):
    """AUTOSAR Item."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    item_contents: DocumentationBlock
    def __init__(self) -> None:
        """Initialize Item."""
        super().__init__()
        self.item_contents: DocumentationBlock = None


class ItemBuilder:
    """Builder for Item."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Item = Item()

    def build(self) -> Item:
        """Build and return Item object.

        Returns:
            Item instance
        """
        # TODO: Add validation
        return self._obj
