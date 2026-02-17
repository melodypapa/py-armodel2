"""Row AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 336)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.Documentation.BlockElements.PaginationAndView.paginateable import (
    Paginateable,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    ValignEnum,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)


class Row(Paginateable):
    """AUTOSAR Row."""

    def __init__(self) -> None:
        """Initialize Row."""
        super().__init__()
        self.rowsep: Optional[TableSeparatorString] = None
        self.valign: Optional[ValignEnum] = None


class RowBuilder:
    """Builder for Row."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Row = Row()

    def build(self) -> Row:
        """Build and return Row object.

        Returns:
            Row instance
        """
        # TODO: Add validation
        return self._obj
