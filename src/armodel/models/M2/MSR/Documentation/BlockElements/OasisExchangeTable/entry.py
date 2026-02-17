"""Entry AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 336)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_OasisExchangeTable.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    AlignEnum,
    ValignEnum,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.MSR.Documentation.BlockElements.OasisExchangeTable import (
    TableSeparatorString,
)
from armodel.models.M2.MSR.Documentation.BlockElements.documentation_block import (
    DocumentationBlock,
)


class Entry(ARObject):
    """AUTOSAR Entry."""

    align: Optional[AlignEnum]
    bgcolor: String
    colname: Optional[String]
    colsep: Optional[TableSeparatorString]
    entry_contents: DocumentationBlock
    morerows: Optional[String]
    nameend: Optional[String]
    namest: Optional[String]
    rotate: Optional[String]
    rowsep: Optional[TableSeparatorString]
    spanname: Optional[String]
    valign: Optional[ValignEnum]
    def __init__(self) -> None:
        """Initialize Entry."""
        super().__init__()
        self.align: Optional[AlignEnum] = None
        self.bgcolor: String = None
        self.colname: Optional[String] = None
        self.colsep: Optional[TableSeparatorString] = None
        self.entry_contents: DocumentationBlock = None
        self.morerows: Optional[String] = None
        self.nameend: Optional[String] = None
        self.namest: Optional[String] = None
        self.rotate: Optional[String] = None
        self.rowsep: Optional[TableSeparatorString] = None
        self.spanname: Optional[String] = None
        self.valign: Optional[ValignEnum] = None


class EntryBuilder:
    """Builder for Entry."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Entry = Entry()

    def build(self) -> Entry:
        """Build and return Entry object.

        Returns:
            Entry instance
        """
        # TODO: Add validation
        return self._obj
