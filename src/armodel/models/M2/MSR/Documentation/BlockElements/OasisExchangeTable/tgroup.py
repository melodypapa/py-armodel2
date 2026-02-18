"""Tgroup AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 334)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.colspec import (
    Colspec,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable.tbody import (
    Tbody,
)


class Tgroup(ARObject):
    """AUTOSAR Tgroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    align: Optional[AlignEnum]
    cols: Integer
    colsep: Optional[TableSeparatorString]
    colspecs: list[Colspec]
    rowsep: Optional[TableSeparatorString]
    tbody: Tbody
    tfoot: Optional[Tbody]
    thead: Optional[Tbody]
    def __init__(self) -> None:
        """Initialize Tgroup."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.cols: Integer = None
        self.colsep: Optional[TableSeparatorString] = None
        self.colspecs: list[Colspec] = []
        self.rowsep: Optional[TableSeparatorString] = None
        self.tbody: Tbody = None
        self.tfoot: Optional[Tbody] = None
        self.thead: Optional[Tbody] = None


class TgroupBuilder:
    """Builder for Tgroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Tgroup = Tgroup()

    def build(self) -> Tgroup:
        """Build and return Tgroup object.

        Returns:
            Tgroup instance
        """
        # TODO: Add validation
        return self._obj
