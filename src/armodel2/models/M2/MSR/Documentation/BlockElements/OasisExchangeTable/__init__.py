"""OasisExchangeTable module."""

from __future__ import annotations
from typing import TYPE_CHECKING

from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table_separator_string import (
    TableSeparatorString,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.table import (
        Table,
    )
    from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.tgroup import (
        Tgroup,
    )
    from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.tbody import (
        Tbody,
    )
    from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.row import (
        Row,
    )
    from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.entry import (
        Entry,
    )
    from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.colspec import (
        Colspec,
    )

from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.float_enum import (
    FloatEnum,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.frame_enum import (
    FrameEnum,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.align_enum import (
    AlignEnum,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.valign_enum import (
    ValignEnum,
)
from armodel2.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.pgwide_enum import (
    PgwideEnum,
)

__all__ = [
    "AlignEnum",
    "Colspec",
    "Entry",
    "FloatEnum",
    "FrameEnum",
    "PgwideEnum",
    "Row",
    "Table",
    "TableSeparatorString",
    "Tbody",
    "Tgroup",
    "ValignEnum",
]
