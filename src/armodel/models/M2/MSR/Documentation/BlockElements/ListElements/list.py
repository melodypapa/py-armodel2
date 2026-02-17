"""List AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 295)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_ListElements.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.ListElements import (
    ListEnum,
)

if TYPE_CHECKING:
    from armodel.models.M2.MSR.Documentation.BlockElements.ListElements.item import (
        Item,
    )



class List(Paginateable):
    """AUTOSAR List."""

    item: Item
    type: Optional[ListEnum]
    def __init__(self) -> None:
        """Initialize List."""
        super().__init__()
        self.item: Item = None
        self.type: Optional[ListEnum] = None


class ListBuilder:
    """Builder for List."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: List = List()

    def build(self) -> List:
        """Build and return List object.

        Returns:
            List instance
        """
        # TODO: Add validation
        return self._obj
